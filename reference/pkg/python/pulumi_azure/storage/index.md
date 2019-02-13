<div class="section" id="module-pulumi_azure.storage">
<span id="storage"></span><h1>storage<a class="headerlink" href="#module-pulumi_azure.storage" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.storage.Account">
<em class="property">class </em><code class="descclassname">pulumi_azure.storage.</code><code class="descname">Account</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>access_tier=None</em>, <em>account_encryption_source=None</em>, <em>account_kind=None</em>, <em>account_replication_type=None</em>, <em>account_tier=None</em>, <em>account_type=None</em>, <em>custom_domain=None</em>, <em>enable_blob_encryption=None</em>, <em>enable_file_encryption=None</em>, <em>enable_https_traffic_only=None</em>, <em>identity=None</em>, <em>location=None</em>, <em>name=None</em>, <em>network_rules=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Account" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage an Azure Storage Account.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>access_tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the access tier for <code class="docutils literal notranslate"><span class="pre">BlobStorage</span></code> and <code class="docutils literal notranslate"><span class="pre">StorageV2</span></code> accounts. Valid options are <code class="docutils literal notranslate"><span class="pre">Hot</span></code> and <code class="docutils literal notranslate"><span class="pre">Cool</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Hot</span></code>.</li>
<li><strong>account_encryption_source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Encryption Source for this Storage Account. Possible values are <code class="docutils literal notranslate"><span class="pre">Microsoft.Keyvault</span></code> and <code class="docutils literal notranslate"><span class="pre">Microsoft.Storage</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Microsoft.Storage</span></code>.</li>
<li><strong>account_kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the Kind of account. Valid options are <code class="docutils literal notranslate"><span class="pre">Storage</span></code>,
<code class="docutils literal notranslate"><span class="pre">StorageV2</span></code> and <code class="docutils literal notranslate"><span class="pre">BlobStorage</span></code>. Changing this forces a new resource to be created.
Defaults to <code class="docutils literal notranslate"><span class="pre">Storage</span></code>.</li>
<li><strong>account_replication_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the type of replication to use for this storage account. Valid options are <code class="docutils literal notranslate"><span class="pre">LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">GRS</span></code>, <code class="docutils literal notranslate"><span class="pre">RAGRS</span></code> and <code class="docutils literal notranslate"><span class="pre">ZRS</span></code>.</li>
<li><strong>account_tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the Tier to use for this storage account. Valid options are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] account_type
:param pulumi.Input[dict] custom_domain: A <code class="docutils literal notranslate"><span class="pre">custom_domain</span></code> block as documented below.
:param pulumi.Input[bool] enable_blob_encryption: Boolean flag which controls if Encryption Services are enabled for Blob storage, see <a class="reference external" href="https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/">here</a> for more information. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.
:param pulumi.Input[bool] enable_file_encryption: Boolean flag which controls if Encryption Services are enabled for File storage, see <a class="reference external" href="https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/">here</a> for more information. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.
:param pulumi.Input[bool] enable_https_traffic_only: Boolean flag which forces HTTPS if enabled, see <a class="reference external" href="https://docs.microsoft.com/en-us/azure/storage/storage-require-secure-transfer/">here</a></p>
<blockquote>
<div>for more information.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Managed Service Identity block as defined below.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the
resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Custom Domain Name to use for the Storage Account, which will be validated by Azure.</li>
<li><strong>network_rules</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">network_rules</span></code> block as documented below.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the storage account. Changing this forces a new resource to be created.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.storage.Account.access_tier">
<code class="descname">access_tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.access_tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the access tier for <code class="docutils literal notranslate"><span class="pre">BlobStorage</span></code> and <code class="docutils literal notranslate"><span class="pre">StorageV2</span></code> accounts. Valid options are <code class="docutils literal notranslate"><span class="pre">Hot</span></code> and <code class="docutils literal notranslate"><span class="pre">Cool</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Hot</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.account_encryption_source">
<code class="descname">account_encryption_source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.account_encryption_source" title="Permalink to this definition">¶</a></dt>
<dd><p>The Encryption Source for this Storage Account. Possible values are <code class="docutils literal notranslate"><span class="pre">Microsoft.Keyvault</span></code> and <code class="docutils literal notranslate"><span class="pre">Microsoft.Storage</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Microsoft.Storage</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.account_kind">
<code class="descname">account_kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.account_kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the Kind of account. Valid options are <code class="docutils literal notranslate"><span class="pre">Storage</span></code>,
<code class="docutils literal notranslate"><span class="pre">StorageV2</span></code> and <code class="docutils literal notranslate"><span class="pre">BlobStorage</span></code>. Changing this forces a new resource to be created.
Defaults to <code class="docutils literal notranslate"><span class="pre">Storage</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.account_replication_type">
<code class="descname">account_replication_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.account_replication_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the type of replication to use for this storage account. Valid options are <code class="docutils literal notranslate"><span class="pre">LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">GRS</span></code>, <code class="docutils literal notranslate"><span class="pre">RAGRS</span></code> and <code class="docutils literal notranslate"><span class="pre">ZRS</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.account_tier">
<code class="descname">account_tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.account_tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the Tier to use for this storage account. Valid options are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.custom_domain">
<code class="descname">custom_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.custom_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">custom_domain</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.enable_blob_encryption">
<code class="descname">enable_blob_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.enable_blob_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls if Encryption Services are enabled for Blob storage, see <a class="reference external" href="https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/">here</a> for more information. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.enable_file_encryption">
<code class="descname">enable_file_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.enable_file_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls if Encryption Services are enabled for File storage, see <a class="reference external" href="https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/">here</a> for more information. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.enable_https_traffic_only">
<code class="descname">enable_https_traffic_only</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.enable_https_traffic_only" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which forces HTTPS if enabled, see <a class="reference external" href="https://docs.microsoft.com/en-us/azure/storage/storage-require-secure-transfer/">here</a>
for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.identity">
<code class="descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>A Managed Service Identity block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the
resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Custom Domain Name to use for the Storage Account, which will be validated by Azure.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.network_rules">
<code class="descname">network_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.network_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">network_rules</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.primary_access_key">
<code class="descname">primary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.primary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary access key for the storage account</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.primary_blob_connection_string">
<code class="descname">primary_blob_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.primary_blob_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string associated with the primary blob location</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.primary_blob_endpoint">
<code class="descname">primary_blob_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.primary_blob_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for blob storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.primary_connection_string">
<code class="descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string associated with the primary location</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.primary_file_endpoint">
<code class="descname">primary_file_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.primary_file_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for file storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.primary_location">
<code class="descname">primary_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.primary_location" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary location of the storage account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.primary_queue_endpoint">
<code class="descname">primary_queue_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.primary_queue_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for queue storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.primary_table_endpoint">
<code class="descname">primary_table_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.primary_table_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for table storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the storage account. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.secondary_access_key">
<code class="descname">secondary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.secondary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary access key for the storage account</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.secondary_blob_connection_string">
<code class="descname">secondary_blob_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.secondary_blob_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string associated with the secondary blob location</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.secondary_blob_endpoint">
<code class="descname">secondary_blob_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.secondary_blob_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for blob storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.secondary_connection_string">
<code class="descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string associated with the secondary location</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.secondary_location">
<code class="descname">secondary_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.secondary_location" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary location of the storage account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.secondary_queue_endpoint">
<code class="descname">secondary_queue_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.secondary_queue_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for queue storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.secondary_table_endpoint">
<code class="descname">secondary_table_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.secondary_table_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for table storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Account.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Account.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.Account.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Account.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.Account.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Account.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.Blob">
<em class="property">class </em><code class="descclassname">pulumi_azure.storage.</code><code class="descname">Blob</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>attempts=None</em>, <em>content_type=None</em>, <em>name=None</em>, <em>parallelism=None</em>, <em>resource_group_name=None</em>, <em>size=None</em>, <em>source=None</em>, <em>source_uri=None</em>, <em>storage_account_name=None</em>, <em>storage_container_name=None</em>, <em>type=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Blob" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage an Azure Storage Blob.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>attempts</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of attempts to make per page or block when uploading. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</li>
<li><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The content type of the storage blob. Cannot be defined if <code class="docutils literal notranslate"><span class="pre">source_uri</span></code> is defined. Defaults to <code class="docutils literal notranslate"><span class="pre">application/octet-stream</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the storage blob. Must be unique within the storage container the blob is located.</li>
<li><strong>parallelism</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of workers per CPU core to run for concurrent uploads. Defaults to <code class="docutils literal notranslate"><span class="pre">8</span></code>.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the storage container. Changing this forces a new resource to be created.</li>
<li><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Used only for <code class="docutils literal notranslate"><span class="pre">page</span></code> blobs to specify the size in bytes of the blob to be created. Must be a multiple of 512. Defaults to 0.</li>
<li><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An absolute path to a file on the local system. Cannot be defined if <code class="docutils literal notranslate"><span class="pre">source_uri</span></code> is defined.</li>
<li><strong>source_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of an existing blob, or a file in the Azure File service, to use as the source contents
for the blob to be created. Changing this forces a new resource to be created. Cannot be defined if <code class="docutils literal notranslate"><span class="pre">source</span></code> is defined.</li>
<li><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the storage account in which to create the storage container.
Changing this forces a new resource to be created.</li>
<li><strong>storage_container_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the storage container in which this blob should be created.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the storage blob to be created. One of either <code class="docutils literal notranslate"><span class="pre">block</span></code> or <code class="docutils literal notranslate"><span class="pre">page</span></code>. When not copying from an existing blob,
this becomes required.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.attempts">
<code class="descname">attempts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.attempts" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of attempts to make per page or block when uploading. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.content_type">
<code class="descname">content_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.content_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The content type of the storage blob. Cannot be defined if <code class="docutils literal notranslate"><span class="pre">source_uri</span></code> is defined. Defaults to <code class="docutils literal notranslate"><span class="pre">application/octet-stream</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the storage blob. Must be unique within the storage container the blob is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.parallelism">
<code class="descname">parallelism</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.parallelism" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of workers per CPU core to run for concurrent uploads. Defaults to <code class="docutils literal notranslate"><span class="pre">8</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the storage container. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.size" title="Permalink to this definition">¶</a></dt>
<dd><p>Used only for <code class="docutils literal notranslate"><span class="pre">page</span></code> blobs to specify the size in bytes of the blob to be created. Must be a multiple of 512. Defaults to 0.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.source">
<code class="descname">source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.source" title="Permalink to this definition">¶</a></dt>
<dd><p>An absolute path to a file on the local system. Cannot be defined if <code class="docutils literal notranslate"><span class="pre">source_uri</span></code> is defined.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.source_uri">
<code class="descname">source_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.source_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of an existing blob, or a file in the Azure File service, to use as the source contents
for the blob to be created. Changing this forces a new resource to be created. Cannot be defined if <code class="docutils literal notranslate"><span class="pre">source</span></code> is defined.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.storage_account_name">
<code class="descname">storage_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.storage_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the storage account in which to create the storage container.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.storage_container_name">
<code class="descname">storage_container_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.storage_container_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the storage container in which this blob should be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the storage blob to be created. One of either <code class="docutils literal notranslate"><span class="pre">block</span></code> or <code class="docutils literal notranslate"><span class="pre">page</span></code>. When not copying from an existing blob,
this becomes required.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Blob.url">
<code class="descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Blob.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the blob</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.Blob.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Blob.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.Blob.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Blob.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.Container">
<em class="property">class </em><code class="descclassname">pulumi_azure.storage.</code><code class="descname">Container</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>container_access_type=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>storage_account_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Container" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage an Azure Storage Container.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>container_access_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ‘interface’ for access the container provides. Can be either <code class="docutils literal notranslate"><span class="pre">blob</span></code>, <code class="docutils literal notranslate"><span class="pre">container</span></code> or <code class="docutils literal notranslate"><span class="pre">private</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">private</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the storage container. Must be unique within the storage service the container is located.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the storage container. Changing this forces a new resource to be created.</li>
<li><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the storage account in which to create the storage container.
Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.storage.Container.container_access_type">
<code class="descname">container_access_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Container.container_access_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The ‘interface’ for access the container provides. Can be either <code class="docutils literal notranslate"><span class="pre">blob</span></code>, <code class="docutils literal notranslate"><span class="pre">container</span></code> or <code class="docutils literal notranslate"><span class="pre">private</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">private</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Container.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Container.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the storage container. Must be unique within the storage service the container is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Container.properties">
<code class="descname">properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Container.properties" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value definition of additional properties associated to the storage container</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Container.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Container.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the storage container. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Container.storage_account_name">
<code class="descname">storage_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Container.storage_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the storage account in which to create the storage container.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.Container.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Container.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.Container.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Container.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.GetAccountResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.storage.</code><code class="descname">GetAccountResult</code><span class="sig-paren">(</span><em>access_tier=None</em>, <em>account_encryption_source=None</em>, <em>account_kind=None</em>, <em>account_replication_type=None</em>, <em>account_tier=None</em>, <em>custom_domain=None</em>, <em>enable_blob_encryption=None</em>, <em>enable_file_encryption=None</em>, <em>enable_https_traffic_only=None</em>, <em>location=None</em>, <em>primary_access_key=None</em>, <em>primary_blob_connection_string=None</em>, <em>primary_blob_endpoint=None</em>, <em>primary_connection_string=None</em>, <em>primary_file_endpoint=None</em>, <em>primary_location=None</em>, <em>primary_queue_endpoint=None</em>, <em>primary_table_endpoint=None</em>, <em>secondary_access_key=None</em>, <em>secondary_blob_connection_string=None</em>, <em>secondary_blob_endpoint=None</em>, <em>secondary_connection_string=None</em>, <em>secondary_location=None</em>, <em>secondary_queue_endpoint=None</em>, <em>secondary_table_endpoint=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccount.</p>
<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.access_tier">
<code class="descname">access_tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.access_tier" title="Permalink to this definition">¶</a></dt>
<dd><p>The access tier for <code class="docutils literal notranslate"><span class="pre">BlobStorage</span></code> accounts.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.account_encryption_source">
<code class="descname">account_encryption_source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.account_encryption_source" title="Permalink to this definition">¶</a></dt>
<dd><p>The Encryption Source for this Storage Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.account_kind">
<code class="descname">account_kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.account_kind" title="Permalink to this definition">¶</a></dt>
<dd><p>The Kind of account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.account_replication_type">
<code class="descname">account_replication_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.account_replication_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of replication used for this storage account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.account_tier">
<code class="descname">account_tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.account_tier" title="Permalink to this definition">¶</a></dt>
<dd><p>The Tier of this storage account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.custom_domain">
<code class="descname">custom_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.custom_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">custom_domain</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.enable_blob_encryption">
<code class="descname">enable_blob_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.enable_blob_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>Are Encryption Services are enabled for Blob storage? See <a class="reference external" href="https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/">here</a>
for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.enable_file_encryption">
<code class="descname">enable_file_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.enable_file_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>Are Encryption Services are enabled for File storage? See <a class="reference external" href="https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/">here</a>
for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.enable_https_traffic_only">
<code class="descname">enable_https_traffic_only</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.enable_https_traffic_only" title="Permalink to this definition">¶</a></dt>
<dd><p>Is traffic only allowed via HTTPS? See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/storage/storage-require-secure-transfer/">here</a>
for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the Storage Account exists</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.primary_access_key">
<code class="descname">primary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.primary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary access key for the Storage Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.primary_blob_connection_string">
<code class="descname">primary_blob_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.primary_blob_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string associated with the primary blob location</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.primary_blob_endpoint">
<code class="descname">primary_blob_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.primary_blob_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for blob storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.primary_connection_string">
<code class="descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string associated with the primary location</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.primary_file_endpoint">
<code class="descname">primary_file_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.primary_file_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for file storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.primary_location">
<code class="descname">primary_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.primary_location" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary location of the Storage Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.primary_queue_endpoint">
<code class="descname">primary_queue_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.primary_queue_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for queue storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.primary_table_endpoint">
<code class="descname">primary_table_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.primary_table_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for table storage in the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.secondary_access_key">
<code class="descname">secondary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.secondary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary access key for the Storage Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.secondary_blob_connection_string">
<code class="descname">secondary_blob_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.secondary_blob_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string associated with the secondary blob location</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.secondary_blob_endpoint">
<code class="descname">secondary_blob_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.secondary_blob_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for blob storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.secondary_connection_string">
<code class="descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string associated with the secondary location</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.secondary_location">
<code class="descname">secondary_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.secondary_location" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary location of the Storage Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.secondary_queue_endpoint">
<code class="descname">secondary_queue_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.secondary_queue_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for queue storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.secondary_table_endpoint">
<code class="descname">secondary_table_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.secondary_table_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL for table storage in the secondary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.storage.GetAccountSASResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.storage.</code><code class="descname">GetAccountSASResult</code><span class="sig-paren">(</span><em>sas=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.GetAccountSASResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccountSAS.</p>
<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountSASResult.sas">
<code class="descname">sas</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountSASResult.sas" title="Permalink to this definition">¶</a></dt>
<dd><p>The computed Account Shared Access Signature (SAS).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.GetAccountSASResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.GetAccountSASResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.storage.Queue">
<em class="property">class </em><code class="descclassname">pulumi_azure.storage.</code><code class="descname">Queue</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>storage_account_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Queue" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage an Azure Storage Queue.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the storage queue. Must be unique within the storage account the queue is located.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the storage queue. Changing this forces a new resource to be created.</li>
<li><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the storage account in which to create the storage queue.
Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.storage.Queue.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Queue.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the storage queue. Must be unique within the storage account the queue is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Queue.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Queue.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the storage queue. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Queue.storage_account_name">
<code class="descname">storage_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Queue.storage_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the storage account in which to create the storage queue.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.Queue.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Queue.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.Queue.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Queue.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.Share">
<em class="property">class </em><code class="descclassname">pulumi_azure.storage.</code><code class="descname">Share</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>quota=None</em>, <em>resource_group_name=None</em>, <em>storage_account_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Share" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage an Azure Storage File Share.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the share. Must be unique within the storage account where the share is located.</li>
<li><strong>quota</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The maximum size of the share, in gigabytes. Must be greater than 0, and less than or equal to 5 TB (5120 GB). Default is 5120.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the share. Changing this forces a new resource to be created.</li>
<li><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the storage account in which to create the share.
Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.storage.Share.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Share.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the share. Must be unique within the storage account where the share is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Share.quota">
<code class="descname">quota</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Share.quota" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum size of the share, in gigabytes. Must be greater than 0, and less than or equal to 5 TB (5120 GB). Default is 5120.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Share.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Share.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the share. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Share.storage_account_name">
<code class="descname">storage_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Share.storage_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the storage account in which to create the share.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Share.url">
<code class="descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Share.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the share</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.Share.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Share.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.Share.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Share.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.Table">
<em class="property">class </em><code class="descclassname">pulumi_azure.storage.</code><code class="descname">Table</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>storage_account_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Table" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage an Azure Storage Table.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the storage table. Must be unique within the storage account the table is located.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the storage table. Changing this forces a new resource to be created.</li>
<li><strong>storage_account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the storage account in which to create the storage table.
Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.storage.Table.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Table.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the storage table. Must be unique within the storage account the table is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Table.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Table.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the storage table. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.storage.Table.storage_account_name">
<code class="descname">storage_account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.storage.Table.storage_account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the storage account in which to create the storage table.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.storage.Table.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Table.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.Table.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.Table.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.ZipBlob">
<em class="property">class </em><code class="descclassname">pulumi_azure.storage.</code><code class="descname">ZipBlob</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>attempts=None</em>, <em>content_type=None</em>, <em>name=None</em>, <em>parallelism=None</em>, <em>resource_group_name=None</em>, <em>size=None</em>, <em>content=None</em>, <em>source_uri=None</em>, <em>storage_account_name=None</em>, <em>storage_container_name=None</em>, <em>type=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.ZipBlob" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ZipBlob resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[int] attempts
:param pulumi.Input[str] content_type
:param pulumi.Input[str] name
:param pulumi.Input[int] parallelism
:param pulumi.Input[str] resource_group_name
:param pulumi.Input[int] size
:param pulumi.Input[pulumi.Archive] content
:param pulumi.Input[str] source_uri
:param pulumi.Input[str] storage_account_name
:param pulumi.Input[str] storage_container_name
:param pulumi.Input[str] type</p>
<dl class="method">
<dt id="pulumi_azure.storage.ZipBlob.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.ZipBlob.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.ZipBlob.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.ZipBlob.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.storage.get_account">
<code class="descclassname">pulumi_azure.storage.</code><code class="descname">get_account</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.get_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Storage Account.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.storage.get_account_sas">
<code class="descclassname">pulumi_azure.storage.</code><code class="descname">get_account_sas</code><span class="sig-paren">(</span><em>connection_string=None</em>, <em>expiry=None</em>, <em>https_only=None</em>, <em>permissions=None</em>, <em>resource_types=None</em>, <em>services=None</em>, <em>start=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.storage.get_account_sas" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to obtain a Shared Access Signature (SAS Token) for an existing Storage Account.</p>
<p>Shared access signatures allow fine-grained, ephemeral access control to various aspects of an Azure Storage Account.</p>
<p>Note that this is an <a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/storageservices/constructing-an-account-sas">Account SAS</a>
and <em>not</em> a <a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/storageservices/constructing-a-service-sas">Service SAS</a>.</p>
</dd></dl>

</div>
