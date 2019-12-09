---
title: Module storage
title_tag: Module storage | Package pulumi_azure | Python SDK
linktitle: storage
notitle: true
---

<div class="section" id="storage">
<h1>storage<a class="headerlink" href="#storage" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.storage"></span><dl class="class">
<dt id="pulumi_azure.storage.Account">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.storage.</code><code class="sig-name descname">Account</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_tier=None</em>, <em class="sig-param">account_encryption_source=None</em>, <em class="sig-param">account_kind=None</em>, <em class="sig-param">account_replication_type=None</em>, <em class="sig-param">account_tier=None</em>, <em class="sig-param">account_type=None</em>, <em class="sig-param">custom_domain=None</em>, <em class="sig-param">enable_advanced_threat_protection=None</em>, <em class="sig-param">enable_blob_encryption=None</em>, <em class="sig-param">enable_file_encryption=None</em>, <em class="sig-param">enable_https_traffic_only=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">is_hns_enabled=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_rules=None</em>, <em class="sig-param">queue_properties=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Account" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Storage Account.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the access tier for <code class="docutils literal notranslate"><span class="pre">BlobStorage</span></code>, <code class="docutils literal notranslate"><span class="pre">FileStorage</span></code> and <code class="docutils literal notranslate"><span class="pre">StorageV2</span></code> accounts. Valid options are <code class="docutils literal notranslate"><span class="pre">Hot</span></code> and <code class="docutils literal notranslate"><span class="pre">Cool</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Hot</span></code>.</p></li>
<li><p><strong>account_encryption_source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Encryption Source for this Storage Account. Possible values are <code class="docutils literal notranslate"><span class="pre">Microsoft.Keyvault</span></code> and <code class="docutils literal notranslate"><span class="pre">Microsoft.Storage</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Microsoft.Storage</span></code>.</p></li>
<li><p><strong>account_kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the Kind of account. Valid options are <code class="docutils literal notranslate"><span class="pre">BlobStorage</span></code>, <code class="docutils literal notranslate"><span class="pre">BlockBlobStorage</span></code>, <code class="docutils literal notranslate"><span class="pre">FileStorage</span></code>, <code class="docutils literal notranslate"><span class="pre">Storage</span></code> and <code class="docutils literal notranslate"><span class="pre">StorageV2</span></code>. Changing this forces a new resource to be created. Defaults to <code class="docutils literal notranslate"><span class="pre">Storage</span></code>.</p></li>
<li><p><strong>account_replication_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the type of replication to use for this storage account. Valid options are <code class="docutils literal notranslate"><span class="pre">LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">GRS</span></code>, <code class="docutils literal notranslate"><span class="pre">RAGRS</span></code> and <code class="docutils literal notranslate"><span class="pre">ZRS</span></code>.</p></li>
<li><p><strong>account_tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the Tier to use for this storage account. Valid options are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. For <code class="docutils literal notranslate"><span class="pre">FileStorage</span></code> accounts only <code class="docutils literal notranslate"><span class="pre">Premium</span></code> is valid. Changing this forces a new resource to be created.</p></li>
<li><p><strong>custom_domain</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">custom_domain</span></code> block as documented below.</p></li>
<li><p><strong>enable_advanced_threat_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls if advanced threat protection is enabled, see <a class="reference external" href="https://docs.microsoft.com/en-us/azure/storage/common/storage-advanced-threat-protection">here</a> for more information. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enable_blob_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Boolean flag which controls if Encryption Services are enabled for Blob storage, see <a class="reference external" href="https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/">here</a> for more information. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</p></li>
<li><p><strong>enable_file_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Boolean flag which controls if Encryption Services are enabled for File storage, see <a class="reference external" href="https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/">here</a> for more information. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</p></li>
<li><p><strong>enable_https_traffic_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Boolean flag which forces HTTPS if enabled, see <a class="reference external" href="https://docs.microsoft.com/en-us/azure/storage/storage-require-secure-transfer/">here</a>
for more information.</p>
</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p></li>
<li><p><strong>is_hns_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is Hierarchical Namespace enabled? This can be used with Azure Data Lake Storage Gen 2 (<a class="reference external" href="https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-quickstart-create-account/">see here for more information</a>). Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the storage account. Changing this forces a new resource to be created. This must be unique across the entire Azure service, not just within the resource group.</p></li>
<li><p><strong>network_rules</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">network_rules</span></code> block as documented below.</p></li>
<li><p><strong>queue_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">queue_properties</span></code> block as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the storage account. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>custom_domain</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the storage account. Changing this forces a new resource to be created. This must be unique across the entire Azure service, not just within the resource group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useSubdomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Principal ID for the Service Principal associated with the Identity of this Storage Account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Tenant ID for the Service Principal associated with the Identity of this Storage Account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>network_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bypasses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipRules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualNetworkSubnetIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>queue_properties</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">corsRules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedOrigins</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">exposedHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAgeInSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">hourMetrics</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeApis</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionPolicyDays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">logging</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">delete</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">read</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionPolicyDays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">minuteMetrics</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeApis</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionPolicyDays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_account.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_account.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.storage.Account.access_tier">
<code class="sig-name descname">access_tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.access_tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the access tier for <code class="docutils literal notranslate"><span class="pre">BlobStorage</span></code>, <code class="docutils literal notranslate"><span class="pre">FileStorage</span></code> and <code class="docutils literal notranslate"><span class="pre">StorageV2</span></code> accounts. Valid options are <code class="docutils literal notranslate"><span class="pre">Hot</span></code> and <code class="docutils literal notranslate"><span class="pre">Cool</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Hot</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.account_encryption_source">
<code class="sig-name descname">account_encryption_source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.account_encryption_source" title="Permalink to this definition">¶</a></dt>
<dd><p>The Encryption Source for this Storage Account. Possible values are <code class="docutils literal notranslate"><span class="pre">Microsoft.Keyvault</span></code> and <code class="docutils literal notranslate"><span class="pre">Microsoft.Storage</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Microsoft.Storage</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.account_kind">
<code class="sig-name descname">account_kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.account_kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the Kind of account. Valid options are <code class="docutils literal notranslate"><span class="pre">BlobStorage</span></code>, <code class="docutils literal notranslate"><span class="pre">BlockBlobStorage</span></code>, <code class="docutils literal notranslate"><span class="pre">FileStorage</span></code>, <code class="docutils literal notranslate"><span class="pre">Storage</span></code> and <code class="docutils literal notranslate"><span class="pre">StorageV2</span></code>. Changing this forces a new resource to be created. Defaults to <code class="docutils literal notranslate"><span class="pre">Storage</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.account_replication_type">
<code class="sig-name descname">account_replication_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.account_replication_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the type of replication to use for this storage account. Valid options are <code class="docutils literal notranslate"><span class="pre">LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">GRS</span></code>, <code class="docutils literal notranslate"><span class="pre">RAGRS</span></code> and <code class="docutils literal notranslate"><span class="pre">ZRS</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.account_tier">
<code class="sig-name descname">account_tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.account_tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the Tier to use for this storage account. Valid options are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. For <code class="docutils literal notranslate"><span class="pre">FileStorage</span></code> accounts only <code class="docutils literal notranslate"><span class="pre">Premium</span></code> is valid. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.custom_domain">
<code class="sig-name descname">custom_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.custom_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">custom_domain</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the storage account. Changing this forces a new resource to be created. This must be unique across the entire Azure service, not just within the resource group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useSubdomain</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.enable_advanced_threat_protection">
<code class="sig-name descname">enable_advanced_threat_protection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.enable_advanced_threat_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls if advanced threat protection is enabled, see <a class="reference external" href="https://docs.microsoft.com/en-us/azure/storage/common/storage-advanced-threat-protection">here</a> for more information. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.enable_blob_encryption">
<code class="sig-name descname">enable_blob_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.enable_blob_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls if Encryption Services are enabled for Blob storage, see <a class="reference external" href="https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/">here</a> for more information. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.enable_file_encryption">
<code class="sig-name descname">enable_file_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.enable_file_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls if Encryption Services are enabled for File storage, see <a class="reference external" href="https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/">here</a> for more information. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.enable_https_traffic_only">
<code class="sig-name descname">enable_https_traffic_only</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.enable_https_traffic_only" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which forces HTTPS if enabled, see <a class="reference external" href="https://docs.microsoft.com/en-us/azure/storage/storage-require-secure-transfer/">here</a>
for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.identity">
<code class="sig-name descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Principal ID for the Service Principal associated with the Identity of this Storage Account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Tenant ID for the Service Principal associated with the Identity of this Storage Account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.is_hns_enabled">
<code class="sig-name descname">is_hns_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.is_hns_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is Hierarchical Namespace enabled? This can be used with Azure Data Lake Storage Gen 2 (<a class="reference external" href="https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-quickstart-create-account/">see here for more information</a>). Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the storage account. Changing this forces a new resource to be created. This must be unique across the entire Azure service, not just within the resource group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.network_rules">
<code class="sig-name descname">network_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.network_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">network_rules</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bypasses</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultAction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipRules</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualNetworkSubnetIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.primary_access_key">
<code class="sig-name descname">primary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.primary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary access key for the storage account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.primary_blob_connection_string">
<code class="sig-name descname">primary_blob_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.primary_blob_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string associated with the primary blob location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.primary_blob_endpoint">
<code class="sig-name descname">primary_blob_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.primary_blob_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for blob storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.primary_blob_host">
<code class="sig-name descname">primary_blob_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.primary_blob_host" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname with port if applicable for blob storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.primary_connection_string">
<code class="sig-name descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string associated with the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.primary_dfs_endpoint">
<code class="sig-name descname">primary_dfs_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.primary_dfs_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for DFS storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.primary_dfs_host">
<code class="sig-name descname">primary_dfs_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.primary_dfs_host" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname with port if applicable for DFS storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.primary_file_endpoint">
<code class="sig-name descname">primary_file_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.primary_file_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for file storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.primary_file_host">
<code class="sig-name descname">primary_file_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.primary_file_host" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname with port if applicable for file storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.primary_location">
<code class="sig-name descname">primary_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.primary_location" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary location of the storage account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.primary_queue_endpoint">
<code class="sig-name descname">primary_queue_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.primary_queue_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for queue storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.primary_queue_host">
<code class="sig-name descname">primary_queue_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.primary_queue_host" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname with port if applicable for queue storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.primary_table_endpoint">
<code class="sig-name descname">primary_table_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.primary_table_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for table storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.primary_table_host">
<code class="sig-name descname">primary_table_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.primary_table_host" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname with port if applicable for table storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.primary_web_endpoint">
<code class="sig-name descname">primary_web_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.primary_web_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for web storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.primary_web_host">
<code class="sig-name descname">primary_web_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.primary_web_host" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname with port if applicable for web storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.queue_properties">
<code class="sig-name descname">queue_properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.queue_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">queue_properties</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">corsRules</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedOrigins</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">exposedHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAgeInSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">hourMetrics</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeApis</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionPolicyDays</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">logging</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">delete</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">read</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionPolicyDays</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">minuteMetrics</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeApis</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionPolicyDays</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the storage account. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.secondary_access_key">
<code class="sig-name descname">secondary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.secondary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary access key for the storage account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.secondary_blob_connection_string">
<code class="sig-name descname">secondary_blob_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.secondary_blob_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string associated with the secondary blob location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.secondary_blob_endpoint">
<code class="sig-name descname">secondary_blob_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.secondary_blob_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for blob storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.secondary_blob_host">
<code class="sig-name descname">secondary_blob_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.secondary_blob_host" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname with port if applicable for blob storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.secondary_connection_string">
<code class="sig-name descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string associated with the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.secondary_dfs_endpoint">
<code class="sig-name descname">secondary_dfs_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.secondary_dfs_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for DFS storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.secondary_dfs_host">
<code class="sig-name descname">secondary_dfs_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.secondary_dfs_host" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname with port if applicable for DFS storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.secondary_file_endpoint">
<code class="sig-name descname">secondary_file_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.secondary_file_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for file storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.secondary_file_host">
<code class="sig-name descname">secondary_file_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.secondary_file_host" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname with port if applicable for file storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.secondary_location">
<code class="sig-name descname">secondary_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.secondary_location" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary location of the storage account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.secondary_queue_endpoint">
<code class="sig-name descname">secondary_queue_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.secondary_queue_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for queue storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.secondary_queue_host">
<code class="sig-name descname">secondary_queue_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.secondary_queue_host" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname with port if applicable for queue storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.secondary_table_endpoint">
<code class="sig-name descname">secondary_table_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.secondary_table_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for table storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.secondary_table_host">
<code class="sig-name descname">secondary_table_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.secondary_table_host" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname with port if applicable for table storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.secondary_web_endpoint">
<code class="sig-name descname">secondary_web_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.secondary_web_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for web storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.secondary_web_host">
<code class="sig-name descname">secondary_web_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.secondary_web_host" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname with port if applicable for web storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.Account.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_tier=None</em>, <em class="sig-param">account_encryption_source=None</em>, <em class="sig-param">account_kind=None</em>, <em class="sig-param">account_replication_type=None</em>, <em class="sig-param">account_tier=None</em>, <em class="sig-param">account_type=None</em>, <em class="sig-param">custom_domain=None</em>, <em class="sig-param">enable_advanced_threat_protection=None</em>, <em class="sig-param">enable_blob_encryption=None</em>, <em class="sig-param">enable_file_encryption=None</em>, <em class="sig-param">enable_https_traffic_only=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">is_hns_enabled=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_rules=None</em>, <em class="sig-param">primary_access_key=None</em>, <em class="sig-param">primary_blob_connection_string=None</em>, <em class="sig-param">primary_blob_endpoint=None</em>, <em class="sig-param">primary_blob_host=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_dfs_endpoint=None</em>, <em class="sig-param">primary_dfs_host=None</em>, <em class="sig-param">primary_file_endpoint=None</em>, <em class="sig-param">primary_file_host=None</em>, <em class="sig-param">primary_location=None</em>, <em class="sig-param">primary_queue_endpoint=None</em>, <em class="sig-param">primary_queue_host=None</em>, <em class="sig-param">primary_table_endpoint=None</em>, <em class="sig-param">primary_table_host=None</em>, <em class="sig-param">primary_web_endpoint=None</em>, <em class="sig-param">primary_web_host=None</em>, <em class="sig-param">queue_properties=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_access_key=None</em>, <em class="sig-param">secondary_blob_connection_string=None</em>, <em class="sig-param">secondary_blob_endpoint=None</em>, <em class="sig-param">secondary_blob_host=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_dfs_endpoint=None</em>, <em class="sig-param">secondary_dfs_host=None</em>, <em class="sig-param">secondary_file_endpoint=None</em>, <em class="sig-param">secondary_file_host=None</em>, <em class="sig-param">secondary_location=None</em>, <em class="sig-param">secondary_queue_endpoint=None</em>, <em class="sig-param">secondary_queue_host=None</em>, <em class="sig-param">secondary_table_endpoint=None</em>, <em class="sig-param">secondary_table_host=None</em>, <em class="sig-param">secondary_web_endpoint=None</em>, <em class="sig-param">secondary_web_host=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Account.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Account resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the access tier for <code class="docutils literal notranslate"><span class="pre">BlobStorage</span></code>, <code class="docutils literal notranslate"><span class="pre">FileStorage</span></code> and <code class="docutils literal notranslate"><span class="pre">StorageV2</span></code> accounts. Valid options are <code class="docutils literal notranslate"><span class="pre">Hot</span></code> and <code class="docutils literal notranslate"><span class="pre">Cool</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Hot</span></code>.</p></li>
<li><p><strong>account_encryption_source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Encryption Source for this Storage Account. Possible values are <code class="docutils literal notranslate"><span class="pre">Microsoft.Keyvault</span></code> and <code class="docutils literal notranslate"><span class="pre">Microsoft.Storage</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Microsoft.Storage</span></code>.</p></li>
<li><p><strong>account_kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the Kind of account. Valid options are <code class="docutils literal notranslate"><span class="pre">BlobStorage</span></code>, <code class="docutils literal notranslate"><span class="pre">BlockBlobStorage</span></code>, <code class="docutils literal notranslate"><span class="pre">FileStorage</span></code>, <code class="docutils literal notranslate"><span class="pre">Storage</span></code> and <code class="docutils literal notranslate"><span class="pre">StorageV2</span></code>. Changing this forces a new resource to be created. Defaults to <code class="docutils literal notranslate"><span class="pre">Storage</span></code>.</p></li>
<li><p><strong>account_replication_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the type of replication to use for this storage account. Valid options are <code class="docutils literal notranslate"><span class="pre">LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">GRS</span></code>, <code class="docutils literal notranslate"><span class="pre">RAGRS</span></code> and <code class="docutils literal notranslate"><span class="pre">ZRS</span></code>.</p></li>
<li><p><strong>account_tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the Tier to use for this storage account. Valid options are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. For <code class="docutils literal notranslate"><span class="pre">FileStorage</span></code> accounts only <code class="docutils literal notranslate"><span class="pre">Premium</span></code> is valid. Changing this forces a new resource to be created.</p></li>
<li><p><strong>custom_domain</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">custom_domain</span></code> block as documented below.</p></li>
<li><p><strong>enable_advanced_threat_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Boolean flag which controls if advanced threat protection is enabled, see <a class="reference external" href="https://docs.microsoft.com/en-us/azure/storage/common/storage-advanced-threat-protection">here</a> for more information. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</p></li>
<li><p><strong>enable_blob_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Boolean flag which controls if Encryption Services are enabled for Blob storage, see <a class="reference external" href="https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/">here</a> for more information. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</p></li>
<li><p><strong>enable_file_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Boolean flag which controls if Encryption Services are enabled for File storage, see <a class="reference external" href="https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/">here</a> for more information. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</p></li>
<li><p><strong>enable_https_traffic_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Boolean flag which forces HTTPS if enabled, see <a class="reference external" href="https://docs.microsoft.com/en-us/azure/storage/storage-require-secure-transfer/">here</a>
for more information.</p>
</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p></li>
<li><p><strong>is_hns_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Is Hierarchical Namespace enabled? This can be used with Azure Data Lake Storage Gen 2 (<a class="reference external" href="https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-quickstart-create-account/">see here for more information</a>). Changing this forces a new resource to be created.</p>
</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the storage account. Changing this forces a new resource to be created. This must be unique across the entire Azure service, not just within the resource group.</p></li>
<li><p><strong>network_rules</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">network_rules</span></code> block as documented below.</p></li>
<li><p><strong>primary_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The primary access key for the storage account.</p></li>
<li><p><strong>primary_blob_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connection string associated with the primary blob location.</p></li>
<li><p><strong>primary_blob_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint URL for blob storage in the primary location.</p></li>
<li><p><strong>primary_blob_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The hostname with port if applicable for blob storage in the primary location.</p></li>
<li><p><strong>primary_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connection string associated with the primary location.</p></li>
<li><p><strong>primary_dfs_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint URL for DFS storage in the primary location.</p></li>
<li><p><strong>primary_dfs_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The hostname with port if applicable for DFS storage in the primary location.</p></li>
<li><p><strong>primary_file_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint URL for file storage in the primary location.</p></li>
<li><p><strong>primary_file_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The hostname with port if applicable for file storage in the primary location.</p></li>
<li><p><strong>primary_location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The primary location of the storage account.</p></li>
<li><p><strong>primary_queue_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint URL for queue storage in the primary location.</p></li>
<li><p><strong>primary_queue_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The hostname with port if applicable for queue storage in the primary location.</p></li>
<li><p><strong>primary_table_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint URL for table storage in the primary location.</p></li>
<li><p><strong>primary_table_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The hostname with port if applicable for table storage in the primary location.</p></li>
<li><p><strong>primary_web_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint URL for web storage in the primary location.</p></li>
<li><p><strong>primary_web_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The hostname with port if applicable for web storage in the primary location.</p></li>
<li><p><strong>queue_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">queue_properties</span></code> block as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the storage account. Changing this forces a new resource to be created.</p></li>
<li><p><strong>secondary_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secondary access key for the storage account.</p></li>
<li><p><strong>secondary_blob_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connection string associated with the secondary blob location.</p></li>
<li><p><strong>secondary_blob_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint URL for blob storage in the secondary location.</p></li>
<li><p><strong>secondary_blob_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The hostname with port if applicable for blob storage in the secondary location.</p></li>
<li><p><strong>secondary_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connection string associated with the secondary location.</p></li>
<li><p><strong>secondary_dfs_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint URL for DFS storage in the secondary location.</p></li>
<li><p><strong>secondary_dfs_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The hostname with port if applicable for DFS storage in the secondary location.</p></li>
<li><p><strong>secondary_file_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint URL for file storage in the secondary location.</p></li>
<li><p><strong>secondary_file_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The hostname with port if applicable for file storage in the secondary location.</p></li>
<li><p><strong>secondary_location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secondary location of the storage account.</p></li>
<li><p><strong>secondary_queue_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint URL for queue storage in the secondary location.</p></li>
<li><p><strong>secondary_queue_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The hostname with port if applicable for queue storage in the secondary location.</p></li>
<li><p><strong>secondary_table_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint URL for table storage in the secondary location.</p></li>
<li><p><strong>secondary_table_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The hostname with port if applicable for table storage in the secondary location.</p></li>
<li><p><strong>secondary_web_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint URL for web storage in the secondary location.</p></li>
<li><p><strong>secondary_web_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The hostname with port if applicable for web storage in the secondary location.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>custom_domain</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the storage account. Changing this forces a new resource to be created. This must be unique across the entire Azure service, not just within the resource group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useSubdomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Principal ID for the Service Principal associated with the Identity of this Storage Account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Tenant ID for the Service Principal associated with the Identity of this Storage Account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>network_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bypasses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipRules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualNetworkSubnetIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>queue_properties</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">corsRules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedOrigins</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">exposedHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAgeInSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">hourMetrics</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeApis</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionPolicyDays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">logging</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">delete</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">read</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionPolicyDays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">minuteMetrics</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeApis</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionPolicyDays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_account.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_account.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.Account.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Account.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.Account.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Account.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.AwaitableGetAccountBlobContainerSASResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.storage.</code><code class="sig-name descname">AwaitableGetAccountBlobContainerSASResult</code><span class="sig-paren">(</span><em class="sig-param">cache_control=None</em>, <em class="sig-param">connection_string=None</em>, <em class="sig-param">container_name=None</em>, <em class="sig-param">content_disposition=None</em>, <em class="sig-param">content_encoding=None</em>, <em class="sig-param">content_language=None</em>, <em class="sig-param">content_type=None</em>, <em class="sig-param">expiry=None</em>, <em class="sig-param">https_only=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">permissions=None</em>, <em class="sig-param">sas=None</em>, <em class="sig-param">start=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.AwaitableGetAccountBlobContainerSASResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.storage.AwaitableGetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.storage.</code><code class="sig-name descname">AwaitableGetAccountResult</code><span class="sig-paren">(</span><em class="sig-param">access_tier=None</em>, <em class="sig-param">account_encryption_source=None</em>, <em class="sig-param">account_kind=None</em>, <em class="sig-param">account_replication_type=None</em>, <em class="sig-param">account_tier=None</em>, <em class="sig-param">custom_domain=None</em>, <em class="sig-param">enable_blob_encryption=None</em>, <em class="sig-param">enable_file_encryption=None</em>, <em class="sig-param">enable_https_traffic_only=None</em>, <em class="sig-param">is_hns_enabled=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">primary_access_key=None</em>, <em class="sig-param">primary_blob_connection_string=None</em>, <em class="sig-param">primary_blob_endpoint=None</em>, <em class="sig-param">primary_blob_host=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_dfs_endpoint=None</em>, <em class="sig-param">primary_dfs_host=None</em>, <em class="sig-param">primary_file_endpoint=None</em>, <em class="sig-param">primary_file_host=None</em>, <em class="sig-param">primary_location=None</em>, <em class="sig-param">primary_queue_endpoint=None</em>, <em class="sig-param">primary_queue_host=None</em>, <em class="sig-param">primary_table_endpoint=None</em>, <em class="sig-param">primary_table_host=None</em>, <em class="sig-param">primary_web_endpoint=None</em>, <em class="sig-param">primary_web_host=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_access_key=None</em>, <em class="sig-param">secondary_blob_connection_string=None</em>, <em class="sig-param">secondary_blob_endpoint=None</em>, <em class="sig-param">secondary_blob_host=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_dfs_endpoint=None</em>, <em class="sig-param">secondary_dfs_host=None</em>, <em class="sig-param">secondary_file_endpoint=None</em>, <em class="sig-param">secondary_file_host=None</em>, <em class="sig-param">secondary_location=None</em>, <em class="sig-param">secondary_queue_endpoint=None</em>, <em class="sig-param">secondary_queue_host=None</em>, <em class="sig-param">secondary_table_endpoint=None</em>, <em class="sig-param">secondary_table_host=None</em>, <em class="sig-param">secondary_web_endpoint=None</em>, <em class="sig-param">secondary_web_host=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.AwaitableGetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.storage.AwaitableGetAccountSASResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.storage.</code><code class="sig-name descname">AwaitableGetAccountSASResult</code><span class="sig-paren">(</span><em class="sig-param">connection_string=None</em>, <em class="sig-param">expiry=None</em>, <em class="sig-param">https_only=None</em>, <em class="sig-param">permissions=None</em>, <em class="sig-param">resource_types=None</em>, <em class="sig-param">sas=None</em>, <em class="sig-param">services=None</em>, <em class="sig-param">start=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.AwaitableGetAccountSASResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.storage.AwaitableGetPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.storage.</code><code class="sig-name descname">AwaitableGetPolicyResult</code><span class="sig-paren">(</span><em class="sig-param">rules=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.AwaitableGetPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.storage.Blob">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.storage.</code><code class="sig-name descname">Blob</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_tier=None</em>, <em class="sig-param">attempts=None</em>, <em class="sig-param">content_type=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parallelism=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">source=None</em>, <em class="sig-param">source_content=None</em>, <em class="sig-param">source_uri=None</em>, <em class="sig-param">storage_account_name=None</em>, <em class="sig-param">storage_container_name=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Blob" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Blob within a Storage Container.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The access tier of the storage blob. Possible values are <code class="docutils literal notranslate"><span class="pre">Archive</span></code>, <code class="docutils literal notranslate"><span class="pre">Cool</span></code> and <code class="docutils literal notranslate"><span class="pre">Hot</span></code>.</p></li>
<li><p><strong>attempts</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of attempts to make per page or block when uploading. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The content type of the storage blob. Cannot be defined if <code class="docutils literal notranslate"><span class="pre">source_uri</span></code> is defined. Defaults to <code class="docutils literal notranslate"><span class="pre">application/octet-stream</span></code>.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of custom blob metadata.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the storage blob. Must be unique within the storage container the blob is located.</p></li>
<li><p><strong>parallelism</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of workers per CPU core to run for concurrent uploads. Defaults to <code class="docutils literal notranslate"><span class="pre">8</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the storage container.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Used only for <code class="docutils literal notranslate"><span class="pre">page</span></code> blobs to specify the size in bytes of the blob to be created. Must be a multiple of 512. Defaults to 0.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An absolute path to a file on the local system. This field cannot be specified for Append blobs and cannot be specified if <code class="docutils literal notranslate"><span class="pre">source_content</span></code> or <code class="docutils literal notranslate"><span class="pre">source_uri</span></code> is specified.</p></li>
<li><p><strong>source_content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The content for this blob which should be defined inline. This field can only be specified for Block blobs and cannot be specified if <code class="docutils literal notranslate"><span class="pre">source</span></code> or <code class="docutils literal notranslate"><span class="pre">source_uri</span></code> is specified.</p></li>
<li><p><strong>source_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of an existing blob, or a file in the Azure File service, to use as the source contents
for the blob to be created. Changing this forces a new resource to be created. This field cannot be specified for Append blobs and cannot be specified if <code class="docutils literal notranslate"><span class="pre">source</span></code> or <code class="docutils literal notranslate"><span class="pre">source_content</span></code> is specified.</p></li>
<li><p><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the storage account in which to create the storage container.
Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_container_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the storage container in which this blob should be created.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the storage blob to be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Append</span></code>, <code class="docutils literal notranslate"><span class="pre">Block</span></code> or <code class="docutils literal notranslate"><span class="pre">Page</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_blob.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_blob.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.access_tier">
<code class="sig-name descname">access_tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.access_tier" title="Permalink to this definition">¶</a></dt>
<dd><p>The access tier of the storage blob. Possible values are <code class="docutils literal notranslate"><span class="pre">Archive</span></code>, <code class="docutils literal notranslate"><span class="pre">Cool</span></code> and <code class="docutils literal notranslate"><span class="pre">Hot</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.attempts">
<code class="sig-name descname">attempts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.attempts" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of attempts to make per page or block when uploading. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.content_type">
<code class="sig-name descname">content_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.content_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The content type of the storage blob. Cannot be defined if <code class="docutils literal notranslate"><span class="pre">source_uri</span></code> is defined. Defaults to <code class="docutils literal notranslate"><span class="pre">application/octet-stream</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of custom blob metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the storage blob. Must be unique within the storage container the blob is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.parallelism">
<code class="sig-name descname">parallelism</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.parallelism" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of workers per CPU core to run for concurrent uploads. Defaults to <code class="docutils literal notranslate"><span class="pre">8</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the storage container.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.size">
<code class="sig-name descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.size" title="Permalink to this definition">¶</a></dt>
<dd><p>Used only for <code class="docutils literal notranslate"><span class="pre">page</span></code> blobs to specify the size in bytes of the blob to be created. Must be a multiple of 512. Defaults to 0.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.source">
<code class="sig-name descname">source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.source" title="Permalink to this definition">¶</a></dt>
<dd><p>An absolute path to a file on the local system. This field cannot be specified for Append blobs and cannot be specified if <code class="docutils literal notranslate"><span class="pre">source_content</span></code> or <code class="docutils literal notranslate"><span class="pre">source_uri</span></code> is specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.source_content">
<code class="sig-name descname">source_content</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.source_content" title="Permalink to this definition">¶</a></dt>
<dd><p>The content for this blob which should be defined inline. This field can only be specified for Block blobs and cannot be specified if <code class="docutils literal notranslate"><span class="pre">source</span></code> or <code class="docutils literal notranslate"><span class="pre">source_uri</span></code> is specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.source_uri">
<code class="sig-name descname">source_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.source_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of an existing blob, or a file in the Azure File service, to use as the source contents
for the blob to be created. Changing this forces a new resource to be created. This field cannot be specified for Append blobs and cannot be specified if <code class="docutils literal notranslate"><span class="pre">source</span></code> or <code class="docutils literal notranslate"><span class="pre">source_content</span></code> is specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.storage_account_name">
<code class="sig-name descname">storage_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.storage_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the storage account in which to create the storage container.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.storage_container_name">
<code class="sig-name descname">storage_container_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.storage_container_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the storage container in which this blob should be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the storage blob to be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Append</span></code>, <code class="docutils literal notranslate"><span class="pre">Block</span></code> or <code class="docutils literal notranslate"><span class="pre">Page</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.url">
<code class="sig-name descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the blob</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.Blob.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_tier=None</em>, <em class="sig-param">attempts=None</em>, <em class="sig-param">content_type=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parallelism=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">source=None</em>, <em class="sig-param">source_content=None</em>, <em class="sig-param">source_uri=None</em>, <em class="sig-param">storage_account_name=None</em>, <em class="sig-param">storage_container_name=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">url=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Blob.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Blob resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The access tier of the storage blob. Possible values are <code class="docutils literal notranslate"><span class="pre">Archive</span></code>, <code class="docutils literal notranslate"><span class="pre">Cool</span></code> and <code class="docutils literal notranslate"><span class="pre">Hot</span></code>.</p></li>
<li><p><strong>attempts</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of attempts to make per page or block when uploading. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The content type of the storage blob. Cannot be defined if <code class="docutils literal notranslate"><span class="pre">source_uri</span></code> is defined. Defaults to <code class="docutils literal notranslate"><span class="pre">application/octet-stream</span></code>.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of custom blob metadata.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the storage blob. Must be unique within the storage container the blob is located.</p></li>
<li><p><strong>parallelism</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of workers per CPU core to run for concurrent uploads. Defaults to <code class="docutils literal notranslate"><span class="pre">8</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the storage container.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Used only for <code class="docutils literal notranslate"><span class="pre">page</span></code> blobs to specify the size in bytes of the blob to be created. Must be a multiple of 512. Defaults to 0.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An absolute path to a file on the local system. This field cannot be specified for Append blobs and cannot be specified if <code class="docutils literal notranslate"><span class="pre">source_content</span></code> or <code class="docutils literal notranslate"><span class="pre">source_uri</span></code> is specified.</p></li>
<li><p><strong>source_content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The content for this blob which should be defined inline. This field can only be specified for Block blobs and cannot be specified if <code class="docutils literal notranslate"><span class="pre">source</span></code> or <code class="docutils literal notranslate"><span class="pre">source_uri</span></code> is specified.</p></li>
<li><p><strong>source_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of an existing blob, or a file in the Azure File service, to use as the source contents
for the blob to be created. Changing this forces a new resource to be created. This field cannot be specified for Append blobs and cannot be specified if <code class="docutils literal notranslate"><span class="pre">source</span></code> or <code class="docutils literal notranslate"><span class="pre">source_content</span></code> is specified.</p></li>
<li><p><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the storage account in which to create the storage container.
Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_container_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the storage container in which this blob should be created.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the storage blob to be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Append</span></code>, <code class="docutils literal notranslate"><span class="pre">Block</span></code> or <code class="docutils literal notranslate"><span class="pre">Page</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the blob</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_blob.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_blob.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.Blob.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Blob.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.Blob.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Blob.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.Container">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.storage.</code><code class="sig-name descname">Container</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">container_access_type=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">storage_account_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Container" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Container within an Azure Storage Account.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>container_access_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Access Level configured for this Container. Possible values are <code class="docutils literal notranslate"><span class="pre">blob</span></code>, <code class="docutils literal notranslate"><span class="pre">container</span></code> or <code class="docutils literal notranslate"><span class="pre">private</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">private</span></code>.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of MetaData for this Container.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Container which should be created within the Storage Account.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the storage container. This field is no longer used and will be removed in 2.0.</p></li>
<li><p><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Storage Account where the Container should be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_container.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_container.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.storage.Container.container_access_type">
<code class="sig-name descname">container_access_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Container.container_access_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Access Level configured for this Container. Possible values are <code class="docutils literal notranslate"><span class="pre">blob</span></code>, <code class="docutils literal notranslate"><span class="pre">container</span></code> or <code class="docutils literal notranslate"><span class="pre">private</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">private</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Container.has_immutability_policy">
<code class="sig-name descname">has_immutability_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Container.has_immutability_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Is there an Immutability Policy configured on this Storage Container?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Container.has_legal_hold">
<code class="sig-name descname">has_legal_hold</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Container.has_legal_hold" title="Permalink to this definition">¶</a></dt>
<dd><p>Is there a Legal Hold configured on this Storage Container?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Container.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Container.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of MetaData for this Container.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Container.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Container.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Container which should be created within the Storage Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Container.properties">
<code class="sig-name descname">properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Container.properties" title="Permalink to this definition">¶</a></dt>
<dd><p>(<strong>Deprecated</strong>) Key-value definition of additional properties associated to the Storage Container</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Container.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Container.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the storage container. This field is no longer used and will be removed in 2.0.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Container.storage_account_name">
<code class="sig-name descname">storage_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Container.storage_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Storage Account where the Container should be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.Container.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">container_access_type=None</em>, <em class="sig-param">has_immutability_policy=None</em>, <em class="sig-param">has_legal_hold=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">properties=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">storage_account_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Container.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Container resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>container_access_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Access Level configured for this Container. Possible values are <code class="docutils literal notranslate"><span class="pre">blob</span></code>, <code class="docutils literal notranslate"><span class="pre">container</span></code> or <code class="docutils literal notranslate"><span class="pre">private</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">private</span></code>.</p></li>
<li><p><strong>has_immutability_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is there an Immutability Policy configured on this Storage Container?</p></li>
<li><p><strong>has_legal_hold</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is there a Legal Hold configured on this Storage Container?</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of MetaData for this Container.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Container which should be created within the Storage Account.</p></li>
<li><p><strong>properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – (<strong>Deprecated</strong>) Key-value definition of additional properties associated to the Storage Container</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the storage container. This field is no longer used and will be removed in 2.0.</p></li>
<li><p><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Storage Account where the Container should be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_container.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_container.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.Container.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Container.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.Container.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Container.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.DataLakeGen2Filesystem">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.storage.</code><code class="sig-name descname">DataLakeGen2Filesystem</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">properties=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.DataLakeGen2Filesystem" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Data Lake Gen2 File System within an Azure Storage Account.</p>
<blockquote>
<div><p><strong>NOTE:</strong> This Resource requires using Azure Active Directory to connect to Azure Storage, which in turn requires the <code class="docutils literal notranslate"><span class="pre">Storage</span></code> specific roles - which are not granted by default.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Data Lake Gen2 File System which should be created within the Storage Account. Must be unique within the storage account the queue is located. Changing this forces a new resource to be created.</p></li>
<li><p><strong>properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of Key to Base64-Encoded Values which should be assigned to this Data Lake Gen2 File System.</p></li>
<li><p><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the Storage Account in which the Data Lake Gen2 File System should exist. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_data_lake_gen2_filesystem.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_data_lake_gen2_filesystem.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.storage.DataLakeGen2Filesystem.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.DataLakeGen2Filesystem.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Data Lake Gen2 File System which should be created within the Storage Account. Must be unique within the storage account the queue is located. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.DataLakeGen2Filesystem.properties">
<code class="sig-name descname">properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.DataLakeGen2Filesystem.properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of Key to Base64-Encoded Values which should be assigned to this Data Lake Gen2 File System.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.DataLakeGen2Filesystem.storage_account_id">
<code class="sig-name descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.DataLakeGen2Filesystem.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of the Storage Account in which the Data Lake Gen2 File System should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.DataLakeGen2Filesystem.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">properties=None</em>, <em class="sig-param">storage_account_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.DataLakeGen2Filesystem.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DataLakeGen2Filesystem resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Data Lake Gen2 File System which should be created within the Storage Account. Must be unique within the storage account the queue is located. Changing this forces a new resource to be created.</p></li>
<li><p><strong>properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of Key to Base64-Encoded Values which should be assigned to this Data Lake Gen2 File System.</p></li>
<li><p><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the Storage Account in which the Data Lake Gen2 File System should exist. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_data_lake_gen2_filesystem.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_data_lake_gen2_filesystem.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.DataLakeGen2Filesystem.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.DataLakeGen2Filesystem.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.DataLakeGen2Filesystem.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.DataLakeGen2Filesystem.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.GetAccountBlobContainerSASResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.storage.</code><code class="sig-name descname">GetAccountBlobContainerSASResult</code><span class="sig-paren">(</span><em class="sig-param">cache_control=None</em>, <em class="sig-param">connection_string=None</em>, <em class="sig-param">container_name=None</em>, <em class="sig-param">content_disposition=None</em>, <em class="sig-param">content_encoding=None</em>, <em class="sig-param">content_language=None</em>, <em class="sig-param">content_type=None</em>, <em class="sig-param">expiry=None</em>, <em class="sig-param">https_only=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">permissions=None</em>, <em class="sig-param">sas=None</em>, <em class="sig-param">start=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.GetAccountBlobContainerSASResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccountBlobContainerSAS.</p>
<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountBlobContainerSASResult.sas">
<code class="sig-name descname">sas</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountBlobContainerSASResult.sas" title="Permalink to this definition">¶</a></dt>
<dd><p>The computed Blob Container Shared Access Signature (SAS).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountBlobContainerSASResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountBlobContainerSASResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.storage.GetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.storage.</code><code class="sig-name descname">GetAccountResult</code><span class="sig-paren">(</span><em class="sig-param">access_tier=None</em>, <em class="sig-param">account_encryption_source=None</em>, <em class="sig-param">account_kind=None</em>, <em class="sig-param">account_replication_type=None</em>, <em class="sig-param">account_tier=None</em>, <em class="sig-param">custom_domain=None</em>, <em class="sig-param">enable_blob_encryption=None</em>, <em class="sig-param">enable_file_encryption=None</em>, <em class="sig-param">enable_https_traffic_only=None</em>, <em class="sig-param">is_hns_enabled=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">primary_access_key=None</em>, <em class="sig-param">primary_blob_connection_string=None</em>, <em class="sig-param">primary_blob_endpoint=None</em>, <em class="sig-param">primary_blob_host=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_dfs_endpoint=None</em>, <em class="sig-param">primary_dfs_host=None</em>, <em class="sig-param">primary_file_endpoint=None</em>, <em class="sig-param">primary_file_host=None</em>, <em class="sig-param">primary_location=None</em>, <em class="sig-param">primary_queue_endpoint=None</em>, <em class="sig-param">primary_queue_host=None</em>, <em class="sig-param">primary_table_endpoint=None</em>, <em class="sig-param">primary_table_host=None</em>, <em class="sig-param">primary_web_endpoint=None</em>, <em class="sig-param">primary_web_host=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_access_key=None</em>, <em class="sig-param">secondary_blob_connection_string=None</em>, <em class="sig-param">secondary_blob_endpoint=None</em>, <em class="sig-param">secondary_blob_host=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_dfs_endpoint=None</em>, <em class="sig-param">secondary_dfs_host=None</em>, <em class="sig-param">secondary_file_endpoint=None</em>, <em class="sig-param">secondary_file_host=None</em>, <em class="sig-param">secondary_location=None</em>, <em class="sig-param">secondary_queue_endpoint=None</em>, <em class="sig-param">secondary_queue_host=None</em>, <em class="sig-param">secondary_table_endpoint=None</em>, <em class="sig-param">secondary_table_host=None</em>, <em class="sig-param">secondary_web_endpoint=None</em>, <em class="sig-param">secondary_web_host=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccount.</p>
<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.access_tier">
<code class="sig-name descname">access_tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.access_tier" title="Permalink to this definition">¶</a></dt>
<dd><p>The access tier for <code class="docutils literal notranslate"><span class="pre">BlobStorage</span></code> accounts.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.account_encryption_source">
<code class="sig-name descname">account_encryption_source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.account_encryption_source" title="Permalink to this definition">¶</a></dt>
<dd><p>The Encryption Source for this Storage Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.account_kind">
<code class="sig-name descname">account_kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.account_kind" title="Permalink to this definition">¶</a></dt>
<dd><p>The Kind of account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.account_replication_type">
<code class="sig-name descname">account_replication_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.account_replication_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of replication used for this storage account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.account_tier">
<code class="sig-name descname">account_tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.account_tier" title="Permalink to this definition">¶</a></dt>
<dd><p>The Tier of this storage account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.custom_domain">
<code class="sig-name descname">custom_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.custom_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">custom_domain</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.enable_blob_encryption">
<code class="sig-name descname">enable_blob_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.enable_blob_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>Are Encryption Services are enabled for Blob storage? See <a class="reference external" href="https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/">here</a>
for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.enable_file_encryption">
<code class="sig-name descname">enable_file_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.enable_file_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>Are Encryption Services are enabled for File storage? See <a class="reference external" href="https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/">here</a>
for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.enable_https_traffic_only">
<code class="sig-name descname">enable_https_traffic_only</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.enable_https_traffic_only" title="Permalink to this definition">¶</a></dt>
<dd><p>Is traffic only allowed via HTTPS? See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/storage/storage-require-secure-transfer/">here</a>
for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.is_hns_enabled">
<code class="sig-name descname">is_hns_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.is_hns_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is Hierarchical Namespace enabled?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the Storage Account exists</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Custom Domain Name used for the Storage Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.primary_access_key">
<code class="sig-name descname">primary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.primary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary access key for the Storage Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.primary_blob_connection_string">
<code class="sig-name descname">primary_blob_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.primary_blob_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string associated with the primary blob location</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.primary_blob_endpoint">
<code class="sig-name descname">primary_blob_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.primary_blob_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for blob storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.primary_blob_host">
<code class="sig-name descname">primary_blob_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.primary_blob_host" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname with port if applicable for blob storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.primary_connection_string">
<code class="sig-name descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string associated with the primary location</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.primary_dfs_endpoint">
<code class="sig-name descname">primary_dfs_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.primary_dfs_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for DFS storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.primary_dfs_host">
<code class="sig-name descname">primary_dfs_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.primary_dfs_host" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname with port if applicable for DFS storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.primary_file_endpoint">
<code class="sig-name descname">primary_file_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.primary_file_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for file storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.primary_file_host">
<code class="sig-name descname">primary_file_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.primary_file_host" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname with port if applicable for file storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.primary_location">
<code class="sig-name descname">primary_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.primary_location" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary location of the Storage Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.primary_queue_endpoint">
<code class="sig-name descname">primary_queue_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.primary_queue_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for queue storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.primary_queue_host">
<code class="sig-name descname">primary_queue_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.primary_queue_host" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname with port if applicable for queue storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.primary_table_endpoint">
<code class="sig-name descname">primary_table_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.primary_table_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for table storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.primary_table_host">
<code class="sig-name descname">primary_table_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.primary_table_host" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname with port if applicable for table storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.primary_web_endpoint">
<code class="sig-name descname">primary_web_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.primary_web_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for web storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.primary_web_host">
<code class="sig-name descname">primary_web_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.primary_web_host" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname with port if applicable for web storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.secondary_access_key">
<code class="sig-name descname">secondary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.secondary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary access key for the Storage Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.secondary_blob_connection_string">
<code class="sig-name descname">secondary_blob_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.secondary_blob_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string associated with the secondary blob location</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.secondary_blob_endpoint">
<code class="sig-name descname">secondary_blob_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.secondary_blob_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for blob storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.secondary_blob_host">
<code class="sig-name descname">secondary_blob_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.secondary_blob_host" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname with port if applicable for blob storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.secondary_connection_string">
<code class="sig-name descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string associated with the secondary location</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.secondary_dfs_endpoint">
<code class="sig-name descname">secondary_dfs_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.secondary_dfs_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for DFS storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.secondary_dfs_host">
<code class="sig-name descname">secondary_dfs_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.secondary_dfs_host" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname with port if applicable for DFS storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.secondary_file_endpoint">
<code class="sig-name descname">secondary_file_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.secondary_file_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for file storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.secondary_file_host">
<code class="sig-name descname">secondary_file_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.secondary_file_host" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname with port if applicable for file storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.secondary_location">
<code class="sig-name descname">secondary_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.secondary_location" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary location of the Storage Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.secondary_queue_endpoint">
<code class="sig-name descname">secondary_queue_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.secondary_queue_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for queue storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.secondary_queue_host">
<code class="sig-name descname">secondary_queue_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.secondary_queue_host" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname with port if applicable for queue storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.secondary_table_endpoint">
<code class="sig-name descname">secondary_table_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.secondary_table_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for table storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.secondary_table_host">
<code class="sig-name descname">secondary_table_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.secondary_table_host" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname with port if applicable for table storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.secondary_web_endpoint">
<code class="sig-name descname">secondary_web_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.secondary_web_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for web storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.secondary_web_host">
<code class="sig-name descname">secondary_web_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.secondary_web_host" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname with port if applicable for web storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.storage.GetAccountSASResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.storage.</code><code class="sig-name descname">GetAccountSASResult</code><span class="sig-paren">(</span><em class="sig-param">connection_string=None</em>, <em class="sig-param">expiry=None</em>, <em class="sig-param">https_only=None</em>, <em class="sig-param">permissions=None</em>, <em class="sig-param">resource_types=None</em>, <em class="sig-param">sas=None</em>, <em class="sig-param">services=None</em>, <em class="sig-param">start=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.GetAccountSASResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccountSAS.</p>
<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountSASResult.sas">
<code class="sig-name descname">sas</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountSASResult.sas" title="Permalink to this definition">¶</a></dt>
<dd><p>The computed Account Shared Access Signature (SAS).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountSASResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountSASResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.storage.GetPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.storage.</code><code class="sig-name descname">GetPolicyResult</code><span class="sig-paren">(</span><em class="sig-param">rules=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.GetPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPolicy.</p>
<dl class="attribute">
<dt id="pulumi_azure.storage.GetPolicyResult.rules">
<code class="sig-name descname">rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetPolicyResult.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">rule</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetPolicyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.storage.ManagementPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.storage.</code><code class="sig-name descname">ManagementPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">rules=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.ManagementPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Storage Account Management Policy.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">rule</span></code> block as documented below.</p></li>
<li><p><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the id of the storage account to apply the management policy to.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An <code class="docutils literal notranslate"><span class="pre">actions</span></code> block as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">baseBlob</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">base_blob</span></code> block as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">deleteAfterDaysSinceModificationGreaterThan</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The age in days after last modification to delete the blob. Must be at least 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tierToArchiveAfterDaysSinceModificationGreaterThan</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The age in days after last modification to tier blobs to archive storage. Supports blob currently at Hot or Cool tier. Must be at least 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tierToCoolAfterDaysSinceModificationGreaterThan</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The age in days after last modification to tier blobs to cool storage. Supports blob currently at Hot tier. Must be at least 0.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">snapshot</span></code> block as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">deleteAfterDaysSinceCreationGreaterThan</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The age in days after create to delete the snaphot. Must be at least 0.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean to specify whether the rule is enabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">filter</span></code> block as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">blobTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - An array of predefined values. Only <code class="docutils literal notranslate"><span class="pre">blockBlob</span></code> is supported.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefixMatches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - An array of strings for prefixes to be matched.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A rule name can contain any combination of alpha numeric characters. Rule name is case-sensitive. It must be unique within a policy.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_management_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_management_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.storage.ManagementPolicy.rules">
<code class="sig-name descname">rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.ManagementPolicy.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">rule</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actions</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - An <code class="docutils literal notranslate"><span class="pre">actions</span></code> block as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">baseBlob</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">base_blob</span></code> block as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">deleteAfterDaysSinceModificationGreaterThan</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The age in days after last modification to delete the blob. Must be at least 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tierToArchiveAfterDaysSinceModificationGreaterThan</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The age in days after last modification to tier blobs to archive storage. Supports blob currently at Hot or Cool tier. Must be at least 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tierToCoolAfterDaysSinceModificationGreaterThan</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The age in days after last modification to tier blobs to cool storage. Supports blob currently at Hot tier. Must be at least 0.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">snapshot</span></code> block as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">deleteAfterDaysSinceCreationGreaterThan</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The age in days after create to delete the snaphot. Must be at least 0.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean to specify whether the rule is enabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filters</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">filter</span></code> block as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">blobTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - An array of predefined values. Only <code class="docutils literal notranslate"><span class="pre">blockBlob</span></code> is supported.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefixMatches</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - An array of strings for prefixes to be matched.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A rule name can contain any combination of alpha numeric characters. Rule name is case-sensitive. It must be unique within a policy.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.ManagementPolicy.storage_account_id">
<code class="sig-name descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.ManagementPolicy.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the id of the storage account to apply the management policy to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.ManagementPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">rules=None</em>, <em class="sig-param">storage_account_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.ManagementPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ManagementPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">rule</span></code> block as documented below.</p></li>
<li><p><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the id of the storage account to apply the management policy to.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An <code class="docutils literal notranslate"><span class="pre">actions</span></code> block as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">baseBlob</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">base_blob</span></code> block as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">deleteAfterDaysSinceModificationGreaterThan</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The age in days after last modification to delete the blob. Must be at least 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tierToArchiveAfterDaysSinceModificationGreaterThan</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The age in days after last modification to tier blobs to archive storage. Supports blob currently at Hot or Cool tier. Must be at least 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tierToCoolAfterDaysSinceModificationGreaterThan</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The age in days after last modification to tier blobs to cool storage. Supports blob currently at Hot tier. Must be at least 0.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">snapshot</span></code> block as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">deleteAfterDaysSinceCreationGreaterThan</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The age in days after create to delete the snaphot. Must be at least 0.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean to specify whether the rule is enabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">filter</span></code> block as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">blobTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - An array of predefined values. Only <code class="docutils literal notranslate"><span class="pre">blockBlob</span></code> is supported.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefixMatches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - An array of strings for prefixes to be matched.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A rule name can contain any combination of alpha numeric characters. Rule name is case-sensitive. It must be unique within a policy.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_management_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_management_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.ManagementPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.ManagementPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.ManagementPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.ManagementPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.Queue">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.storage.</code><code class="sig-name descname">Queue</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">storage_account_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Queue" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Queue within an Azure Storage Account.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of MetaData which should be assigned to this Storage Queue.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Queue which should be created within the Storage Account. Must be unique within the storage account the queue is located.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the storage queue.</p></li>
<li><p><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Storage Account in which the Storage Queue should exist. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_queue.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_queue.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.storage.Queue.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Queue.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of MetaData which should be assigned to this Storage Queue.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Queue.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Queue.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Queue which should be created within the Storage Account. Must be unique within the storage account the queue is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Queue.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Queue.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the storage queue.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Queue.storage_account_name">
<code class="sig-name descname">storage_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Queue.storage_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Storage Account in which the Storage Queue should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.Queue.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">storage_account_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Queue.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Queue resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of MetaData which should be assigned to this Storage Queue.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Queue which should be created within the Storage Account. Must be unique within the storage account the queue is located.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the storage queue.</p></li>
<li><p><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Storage Account in which the Storage Queue should exist. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_queue.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_queue.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.Queue.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Queue.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.Queue.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Queue.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.Share">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.storage.</code><code class="sig-name descname">Share</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acls=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">quota=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">storage_account_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Share" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a File Share within Azure Storage.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">acl</span></code> blocks as defined below.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of MetaData for this File Share.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the share. Must be unique within the storage account where the share is located.</p></li>
<li><p><strong>quota</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum size of the share, in gigabytes. For Standard storage accounts, this must be greater than 0 and less than 5120 GB (5 TB). For Premium FileStorage storage accounts, this must be greater than 100 GB and less than 102400 GB (100 TB). Default is 5120.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the share. Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the storage account in which to create the share.
Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>acls</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">access_policies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">expiry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">permissions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the File Share.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_share.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_share.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.storage.Share.acls">
<code class="sig-name descname">acls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Share.acls" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">acl</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">access_policies</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">expiry</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">permissions</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the File Share.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Share.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Share.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of MetaData for this File Share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Share.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Share.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the share. Must be unique within the storage account where the share is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Share.quota">
<code class="sig-name descname">quota</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Share.quota" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum size of the share, in gigabytes. For Standard storage accounts, this must be greater than 0 and less than 5120 GB (5 TB). For Premium FileStorage storage accounts, this must be greater than 100 GB and less than 102400 GB (100 TB). Default is 5120.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Share.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Share.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the share. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Share.storage_account_name">
<code class="sig-name descname">storage_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Share.storage_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the storage account in which to create the share.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Share.url">
<code class="sig-name descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Share.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the File Share</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.Share.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acls=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">quota=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">storage_account_name=None</em>, <em class="sig-param">url=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Share.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Share resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">acl</span></code> blocks as defined below.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of MetaData for this File Share.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the share. Must be unique within the storage account where the share is located.</p></li>
<li><p><strong>quota</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum size of the share, in gigabytes. For Standard storage accounts, this must be greater than 0 and less than 5120 GB (5 TB). For Premium FileStorage storage accounts, this must be greater than 100 GB and less than 102400 GB (100 TB). Default is 5120.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the share. Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the storage account in which to create the share.
Changing this forces a new resource to be created.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the File Share</p></li>
</ul>
</dd>
</dl>
<p>The <strong>acls</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">access_policies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">expiry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">permissions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the File Share.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_share.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_share.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.Share.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Share.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.Share.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Share.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.ShareDirectory">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.storage.</code><code class="sig-name descname">ShareDirectory</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">share_name=None</em>, <em class="sig-param">storage_account_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.ShareDirectory" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Directory within an Azure Storage File Share.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of metadata to assign to this Directory.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name (or path) of the Directory that should be created within this File Share. Changing this forces a new resource to be created.</p></li>
<li><p><strong>share_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the File Share where this Directory should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Storage Account within which the File Share is located. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_share_directory.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_share_directory.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.storage.ShareDirectory.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.ShareDirectory.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of metadata to assign to this Directory.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.ShareDirectory.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.ShareDirectory.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name (or path) of the Directory that should be created within this File Share. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.ShareDirectory.share_name">
<code class="sig-name descname">share_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.ShareDirectory.share_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the File Share where this Directory should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.ShareDirectory.storage_account_name">
<code class="sig-name descname">storage_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.ShareDirectory.storage_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Storage Account within which the File Share is located. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.ShareDirectory.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">share_name=None</em>, <em class="sig-param">storage_account_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.ShareDirectory.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ShareDirectory resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of metadata to assign to this Directory.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name (or path) of the Directory that should be created within this File Share. Changing this forces a new resource to be created.</p></li>
<li><p><strong>share_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the File Share where this Directory should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Storage Account within which the File Share is located. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_share_directory.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_share_directory.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.ShareDirectory.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.ShareDirectory.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.ShareDirectory.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.ShareDirectory.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.Table">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.storage.</code><code class="sig-name descname">Table</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acls=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">storage_account_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Table" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Table within an Azure Storage Account.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">acl</span></code> blocks as defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the storage table. Must be unique within the storage account the table is located.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the storage table.</p></li>
<li><p><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the storage account in which to create the storage table.
Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>acls</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">access_policies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">expiry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">permissions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Table within the Storage Account.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_table.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_table.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.storage.Table.acls">
<code class="sig-name descname">acls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Table.acls" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">acl</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">access_policies</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">expiry</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">permissions</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Table within the Storage Account.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Table.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Table.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the storage table. Must be unique within the storage account the table is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Table.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Table.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the storage table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Table.storage_account_name">
<code class="sig-name descname">storage_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Table.storage_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the storage account in which to create the storage table.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.Table.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acls=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">storage_account_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Table.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Table resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">acl</span></code> blocks as defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the storage table. Must be unique within the storage account the table is located.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the storage table.</p></li>
<li><p><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the storage account in which to create the storage table.
Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>acls</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">access_policies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">expiry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">permissions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Table within the Storage Account.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_table.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_table.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.Table.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Table.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.Table.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Table.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.TableEntity">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.storage.</code><code class="sig-name descname">TableEntity</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">entity=None</em>, <em class="sig-param">partition_key=None</em>, <em class="sig-param">row_key=None</em>, <em class="sig-param">storage_account_name=None</em>, <em class="sig-param">table_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.TableEntity" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Entity within a Table in an Azure Storage Account.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>entity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of key/value pairs that describe the entity to be inserted/merged in to the storage table.</p></li>
<li><p><strong>partition_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key for the partition where the entity will be inserted/merged. Changing this forces a new resource.</p></li>
<li><p><strong>row_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key for the row where the entity will be inserted/merged. Changing this forces a new resource.</p></li>
<li><p><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the storage account in which to create the storage table entity.
Changing this forces a new resource to be created.</p></li>
<li><p><strong>table_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the storage table in which to create the storage table entity. 
Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_table_entity.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_table_entity.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.storage.TableEntity.entity">
<code class="sig-name descname">entity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.TableEntity.entity" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of key/value pairs that describe the entity to be inserted/merged in to the storage table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.TableEntity.partition_key">
<code class="sig-name descname">partition_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.TableEntity.partition_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The key for the partition where the entity will be inserted/merged. Changing this forces a new resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.TableEntity.row_key">
<code class="sig-name descname">row_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.TableEntity.row_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The key for the row where the entity will be inserted/merged. Changing this forces a new resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.TableEntity.storage_account_name">
<code class="sig-name descname">storage_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.TableEntity.storage_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the storage account in which to create the storage table entity.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.TableEntity.table_name">
<code class="sig-name descname">table_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.TableEntity.table_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the storage table in which to create the storage table entity. 
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.TableEntity.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">entity=None</em>, <em class="sig-param">partition_key=None</em>, <em class="sig-param">row_key=None</em>, <em class="sig-param">storage_account_name=None</em>, <em class="sig-param">table_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.TableEntity.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TableEntity resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>entity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of key/value pairs that describe the entity to be inserted/merged in to the storage table.</p></li>
<li><p><strong>partition_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key for the partition where the entity will be inserted/merged. Changing this forces a new resource.</p></li>
<li><p><strong>row_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key for the row where the entity will be inserted/merged. Changing this forces a new resource.</p></li>
<li><p><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the storage account in which to create the storage table entity.
Changing this forces a new resource to be created.</p></li>
<li><p><strong>table_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the storage table in which to create the storage table entity. 
Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_table_entity.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/storage_table_entity.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.TableEntity.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.TableEntity.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.TableEntity.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.TableEntity.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.ZipBlob">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.storage.</code><code class="sig-name descname">ZipBlob</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_tier=None</em>, <em class="sig-param">attempts=None</em>, <em class="sig-param">content_type=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parallelism=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">content=None</em>, <em class="sig-param">source_content=None</em>, <em class="sig-param">source_uri=None</em>, <em class="sig-param">storage_account_name=None</em>, <em class="sig-param">storage_container_name=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.ZipBlob" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ZipBlob resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_azure.storage.ZipBlob.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_tier=None</em>, <em class="sig-param">attempts=None</em>, <em class="sig-param">content_type=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parallelism=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">content=None</em>, <em class="sig-param">source_content=None</em>, <em class="sig-param">source_uri=None</em>, <em class="sig-param">storage_account_name=None</em>, <em class="sig-param">storage_container_name=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">url=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.ZipBlob.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ZipBlob resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.ZipBlob.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.ZipBlob.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.ZipBlob.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.ZipBlob.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.get_account">
<code class="sig-prename descclassname">pulumi_azure.storage.</code><code class="sig-name descname">get_account</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.get_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Storage Account.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Storage Account</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the resource group the Storage Account is located in.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/storage_account.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/storage_account.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.storage.get_account_blob_container_sas">
<code class="sig-prename descclassname">pulumi_azure.storage.</code><code class="sig-name descname">get_account_blob_container_sas</code><span class="sig-paren">(</span><em class="sig-param">cache_control=None</em>, <em class="sig-param">connection_string=None</em>, <em class="sig-param">container_name=None</em>, <em class="sig-param">content_disposition=None</em>, <em class="sig-param">content_encoding=None</em>, <em class="sig-param">content_language=None</em>, <em class="sig-param">content_type=None</em>, <em class="sig-param">expiry=None</em>, <em class="sig-param">https_only=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">permissions=None</em>, <em class="sig-param">start=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.get_account_blob_container_sas" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to obtain a Shared Access Signature (SAS Token) for an existing Storage Account Blob Container.</p>
<p>Shared access signatures allow fine-grained, ephemeral access control to various aspects of an Azure Storage Account Blob Container.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cache_control</strong> (<em>str</em>) – The <code class="docutils literal notranslate"><span class="pre">Cache-Control</span></code> response header that is sent when this SAS token is used.</p></li>
<li><p><strong>container_name</strong> (<em>str</em>) – Name of the container.</p></li>
<li><p><strong>content_disposition</strong> (<em>str</em>) – The <code class="docutils literal notranslate"><span class="pre">Content-Disposition</span></code> response header that is sent when this SAS token is used.</p></li>
<li><p><strong>content_encoding</strong> (<em>str</em>) – The <code class="docutils literal notranslate"><span class="pre">Content-Encoding</span></code> response header that is sent when this SAS token is used.</p></li>
<li><p><strong>content_language</strong> (<em>str</em>) – The <code class="docutils literal notranslate"><span class="pre">Content-Language</span></code> response header that is sent when this SAS token is used.</p></li>
<li><p><strong>content_type</strong> (<em>str</em>) – The <code class="docutils literal notranslate"><span class="pre">Content-Type</span></code> response header that is sent when this SAS token is used.</p></li>
<li><p><strong>expiry</strong> (<em>str</em>) – The expiration time and date of this SAS. Must be a valid ISO-8601 format time/date string.</p></li>
<li><p><strong>https_only</strong> (<em>bool</em>) – Only permit <code class="docutils literal notranslate"><span class="pre">https</span></code> access. If <code class="docutils literal notranslate"><span class="pre">false</span></code>, both <code class="docutils literal notranslate"><span class="pre">http</span></code> and <code class="docutils literal notranslate"><span class="pre">https</span></code> are permitted. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>ip_address</strong> (<em>str</em>) – Single ipv4 address or range (connected with a dash) of ipv4 addresses.</p></li>
<li><p><strong>permissions</strong> (<em>dict</em>) – A <code class="docutils literal notranslate"><span class="pre">permissions</span></code> block as defined below.</p></li>
<li><p><strong>start</strong> (<em>str</em>) – The starting time and date of validity of this SAS. Must be a valid ISO-8601 format time/date string.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>permissions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">add</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">create</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">delete</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">list</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">read</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/storage_account_blob_container_sas.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/storage_account_blob_container_sas.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.storage.get_account_sas">
<code class="sig-prename descclassname">pulumi_azure.storage.</code><code class="sig-name descname">get_account_sas</code><span class="sig-paren">(</span><em class="sig-param">connection_string=None</em>, <em class="sig-param">expiry=None</em>, <em class="sig-param">https_only=None</em>, <em class="sig-param">permissions=None</em>, <em class="sig-param">resource_types=None</em>, <em class="sig-param">services=None</em>, <em class="sig-param">start=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.get_account_sas" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to obtain a Shared Access Signature (SAS Token) for an existing Storage Account.</p>
<p>Shared access signatures allow fine-grained, ephemeral access control to various aspects of an Azure Storage Account.</p>
<p>Note that this is an <a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/storageservices/constructing-an-account-sas">Account SAS</a>
and <em>not</em> a <a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/storageservices/constructing-a-service-sas">Service SAS</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>connection_string</strong> (<em>str</em>) – The connection string for the storage account to which this SAS applies. Typically directly from the <code class="docutils literal notranslate"><span class="pre">primary_connection_string</span></code> attribute of a <code class="docutils literal notranslate"><span class="pre">storage.Account</span></code> resource.</p></li>
<li><p><strong>expiry</strong> (<em>str</em>) – The expiration time and date of this SAS. Must be a valid ISO-8601 format time/date string.</p></li>
<li><p><strong>https_only</strong> (<em>bool</em>) – Only permit <code class="docutils literal notranslate"><span class="pre">https</span></code> access. If <code class="docutils literal notranslate"><span class="pre">false</span></code>, both <code class="docutils literal notranslate"><span class="pre">http</span></code> and <code class="docutils literal notranslate"><span class="pre">https</span></code> are permitted. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>permissions</strong> (<em>dict</em>) – A <code class="docutils literal notranslate"><span class="pre">permissions</span></code> block as defined below.</p></li>
<li><p><strong>resource_types</strong> (<em>dict</em>) – A <code class="docutils literal notranslate"><span class="pre">resource_types</span></code> block as defined below.</p></li>
<li><p><strong>services</strong> (<em>dict</em>) – A <code class="docutils literal notranslate"><span class="pre">services</span></code> block as defined below.</p></li>
<li><p><strong>start</strong> (<em>str</em>) – The starting time and date of validity of this SAS. Must be a valid ISO-8601 format time/date string.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>permissions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">add</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">create</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">delete</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">list</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">process</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">read</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">update</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
<p>The <strong>resource_types</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">container</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">object</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
<p>The <strong>services</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">blob</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">file</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queue</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/storage_account_sas.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/storage_account_sas.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.storage.get_policy">
<code class="sig-prename descclassname">pulumi_azure.storage.</code><code class="sig-name descname">get_policy</code><span class="sig-paren">(</span><em class="sig-param">storage_account_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.get_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Storage Management Policy.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>storage_account_id</strong> (<em>str</em>) – Specifies the id of the storage account to retrieve the management policy for.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/storage_management_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/storage_management_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
