---
title: Module redis
title_tag: Module redis | Package pulumi_azure | Python SDK
linktitle: redis
notitle: true
---

<div class="section" id="redis">
<h1>redis<a class="headerlink" href="#redis" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.redis"></span><dl class="py class">
<dt id="pulumi_azure.redis.AwaitableGetCacheResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.redis.</code><code class="sig-name descname">AwaitableGetCacheResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_non_ssl_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minimum_tls_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">patch_schedules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary_access_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary_connection_string</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_static_ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redis_configurations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondary_access_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondary_connection_string</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shard_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sku_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zones</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.redis.AwaitableGetCacheResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azure.redis.Cache">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.redis.</code><code class="sig-name descname">Cache</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_non_ssl_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minimum_tls_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">patch_schedules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_static_ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redis_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shard_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sku_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.redis.Cache" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Redis Cache.</p>
<table class="docutils align-default">
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Redis Value</p></th>
<th class="head"><p>Basic</p></th>
<th class="head"><p>Standard</p></th>
<th class="head"><p>Premium</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>enable_authentication</p></td>
<td><p>true</p></td>
<td><p>true</p></td>
<td><p>true</p></td>
</tr>
<tr class="row-odd"><td><p>maxmemory_reserved</p></td>
<td><p>2</p></td>
<td><p>50</p></td>
<td><p>200</p></td>
</tr>
<tr class="row-even"><td><p>maxfragmentationmemory_reserved</p></td>
<td><p>2</p></td>
<td><p>50</p></td>
<td><p>200</p></td>
</tr>
<tr class="row-odd"><td><p>maxmemory_delta</p></td>
<td><p>2</p></td>
<td><p>50</p></td>
<td><p>200</p></td>
</tr>
<tr class="row-even"><td><p>maxmemory_policy</p></td>
<td><p>volatile-lru</p></td>
<td><p>volatile-lru</p></td>
<td><p>volatile-lru</p></td>
</tr>
</tbody>
</table>
<blockquote>
<div><p><strong>NOTE:</strong> The <code class="docutils literal notranslate"><span class="pre">maxmemory_reserved</span></code>, <code class="docutils literal notranslate"><span class="pre">maxmemory_delta</span></code> and <code class="docutils literal notranslate"><span class="pre">maxfragmentationmemory-reserved</span></code> settings are only available for Standard and Premium caches. More details are available in the Relevant Links section below._</p>
</div></blockquote>
<p>A <code class="docutils literal notranslate"><span class="pre">patch_schedule</span></code> block supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">day_of_week</span></code> (Required) the Weekday name - possible values include <code class="docutils literal notranslate"><span class="pre">Monday</span></code>, <code class="docutils literal notranslate"><span class="pre">Tuesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Wednesday</span></code> etc.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start_hour_utc</span></code> - (Optional) the Start Hour for maintenance in UTC - possible values range from <code class="docutils literal notranslate"><span class="pre">0</span> <span class="pre">-</span> <span class="pre">23</span></code>.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> The Patch Window lasts for <code class="docutils literal notranslate"><span class="pre">5</span></code> hours from the <code class="docutils literal notranslate"><span class="pre">start_hour_utc</span></code>.</p>
</div></blockquote>
<ul class="simple">
<li><p><a class="reference external" href="https://azure.microsoft.com/en-us/documentation/articles/cache-configure/#advanced-settings">Azure Redis Cache: SKU specific configuration limitations</a></p></li>
<li><p><a class="reference external" href="http://redis.io/topics/config">Redis: Available Configuration Settings</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the Redis cache to deploy. Valid values for a SKU <code class="docutils literal notranslate"><span class="pre">family</span></code> of C (Basic/Standard) are <code class="docutils literal notranslate"><span class="pre">0,</span> <span class="pre">1,</span> <span class="pre">2,</span> <span class="pre">3,</span> <span class="pre">4,</span> <span class="pre">5,</span> <span class="pre">6</span></code>, and for P (Premium) <code class="docutils literal notranslate"><span class="pre">family</span></code> are <code class="docutils literal notranslate"><span class="pre">1,</span> <span class="pre">2,</span> <span class="pre">3,</span> <span class="pre">4</span></code>.</p></li>
<li><p><strong>enable_non_ssl_port</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable the non-SSL port (6379) - disabled by default.</p></li>
<li><p><strong>family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU family/pricing group to use. Valid values are <code class="docutils literal notranslate"><span class="pre">C</span></code> (for Basic/Standard SKU family) and <code class="docutils literal notranslate"><span class="pre">P</span></code> (for <code class="docutils literal notranslate"><span class="pre">Premium</span></code>)</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the resource group.</p></li>
<li><p><strong>minimum_tls_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The minimum TLS version.  Defaults to <code class="docutils literal notranslate"><span class="pre">1.0</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Redis instance. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>patch_schedules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of <code class="docutils literal notranslate"><span class="pre">patch_schedule</span></code> blocks as defined below - only available for Premium SKU’s.</p></li>
<li><p><strong>private_static_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Static IP Address to assign to the Redis Cache when hosted inside the Virtual Network. Changing this forces a new resource to be created.</p></li>
<li><p><strong>redis_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">redis_configuration</span></code> as defined below - with some limitations by SKU - defaults/details are shown below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the Redis instance.</p></li>
<li><p><strong>shard_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <em>Only available when using the Premium SKU</em> The number of Shards to create on the Redis Cluster.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU of Redis to use. Possible values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <em>Only available when using the Premium SKU</em> The ID of the Subnet within which the Redis Cache should be deployed. This Subnet must only contain Azure Cache for Redis instances without any other type of resources. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A list of a single item of the Availability Zone which the Redis Cache should be allocated in.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>patch_schedules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dayOfWeek</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startHourUtc</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>redis_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aofBackupEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">aofStorageConnectionString0</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">aofStorageConnectionString1</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableAuthentication</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If set to <code class="docutils literal notranslate"><span class="pre">false</span></code>, the Redis instance will be accessible without authentication. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxclients</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Returns the max number of connected clients at the same time.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxfragmentationmemoryReserved</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Value in megabytes reserved to accommodate for memory fragmentation. Defaults are shown below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxmemoryDelta</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The max-memory delta for this Redis instance. Defaults are shown below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxmemoryPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How Redis will select what to remove when <code class="docutils literal notranslate"><span class="pre">maxmemory</span></code> is reached. Defaults are shown below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxmemoryReserved</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Value in megabytes reserved for non-cache usage e.g. failover. Defaults are shown below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notifyKeyspaceEvents</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Keyspace notifications allows clients to subscribe to Pub/Sub channels in order to receive events affecting the Redis data set in some way. <a class="reference external" href="https://redis.io/topics/notifications#configuration">Reference</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rdbBackupEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is Backup Enabled? Only supported on Premium SKU’s.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rdbBackupFrequency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Backup Frequency in Minutes. Only supported on Premium SKU’s. Possible values are: <code class="docutils literal notranslate"><span class="pre">15</span></code>, <code class="docutils literal notranslate"><span class="pre">30</span></code>, <code class="docutils literal notranslate"><span class="pre">60</span></code>, <code class="docutils literal notranslate"><span class="pre">360</span></code>, <code class="docutils literal notranslate"><span class="pre">720</span></code> and <code class="docutils literal notranslate"><span class="pre">1440</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rdbBackupMaxSnapshotCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of snapshots to create as a backup. Only supported for Premium SKU’s.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rdbStorageConnectionString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Connection String to the Storage Account. Only supported for Premium SKU’s. In the format: <code class="docutils literal notranslate"><span class="pre">DefaultEndpointsProtocol=https;BlobEndpoint=${azurerm_storage_account.example.primary_blob_endpoint};AccountName=${azurerm_storage_account.example.name};AccountKey=${azurerm_storage_account.example.primary_access_key}</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.redis.Cache.capacity">
<code class="sig-name descname">capacity</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the Redis cache to deploy. Valid values for a SKU <code class="docutils literal notranslate"><span class="pre">family</span></code> of C (Basic/Standard) are <code class="docutils literal notranslate"><span class="pre">0,</span> <span class="pre">1,</span> <span class="pre">2,</span> <span class="pre">3,</span> <span class="pre">4,</span> <span class="pre">5,</span> <span class="pre">6</span></code>, and for P (Premium) <code class="docutils literal notranslate"><span class="pre">family</span></code> are <code class="docutils literal notranslate"><span class="pre">1,</span> <span class="pre">2,</span> <span class="pre">3,</span> <span class="pre">4</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.Cache.enable_non_ssl_port">
<code class="sig-name descname">enable_non_ssl_port</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.enable_non_ssl_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable the non-SSL port (6379) - disabled by default.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.Cache.family">
<code class="sig-name descname">family</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.family" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU family/pricing group to use. Valid values are <code class="docutils literal notranslate"><span class="pre">C</span></code> (for Basic/Standard SKU family) and <code class="docutils literal notranslate"><span class="pre">P</span></code> (for <code class="docutils literal notranslate"><span class="pre">Premium</span></code>)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.Cache.hostname">
<code class="sig-name descname">hostname</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The Hostname of the Redis Instance</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.Cache.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the resource group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.Cache.minimum_tls_version">
<code class="sig-name descname">minimum_tls_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.minimum_tls_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum TLS version.  Defaults to <code class="docutils literal notranslate"><span class="pre">1.0</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.Cache.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Redis instance. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.Cache.patch_schedules">
<code class="sig-name descname">patch_schedules</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.patch_schedules" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of <code class="docutils literal notranslate"><span class="pre">patch_schedule</span></code> blocks as defined below - only available for Premium SKU’s.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dayOfWeek</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startHourUtc</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.Cache.port">
<code class="sig-name descname">port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The non-SSL Port of the Redis Instance</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.Cache.primary_access_key">
<code class="sig-name descname">primary_access_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.primary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Access Key for the Redis Instance</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.Cache.primary_connection_string">
<code class="sig-name descname">primary_connection_string</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary connection string of the Redis Instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.Cache.private_static_ip_address">
<code class="sig-name descname">private_static_ip_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.private_static_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The Static IP Address to assign to the Redis Cache when hosted inside the Virtual Network. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.Cache.redis_configuration">
<code class="sig-name descname">redis_configuration</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.redis_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">redis_configuration</span></code> as defined below - with some limitations by SKU - defaults/details are shown below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aofBackupEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">aofStorageConnectionString0</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">aofStorageConnectionString1</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableAuthentication</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If set to <code class="docutils literal notranslate"><span class="pre">false</span></code>, the Redis instance will be accessible without authentication. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxclients</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Returns the max number of connected clients at the same time.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxfragmentationmemoryReserved</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Value in megabytes reserved to accommodate for memory fragmentation. Defaults are shown below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxmemoryDelta</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The max-memory delta for this Redis instance. Defaults are shown below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxmemoryPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How Redis will select what to remove when <code class="docutils literal notranslate"><span class="pre">maxmemory</span></code> is reached. Defaults are shown below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxmemoryReserved</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Value in megabytes reserved for non-cache usage e.g. failover. Defaults are shown below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notifyKeyspaceEvents</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Keyspace notifications allows clients to subscribe to Pub/Sub channels in order to receive events affecting the Redis data set in some way. <a class="reference external" href="https://redis.io/topics/notifications#configuration">Reference</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rdbBackupEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is Backup Enabled? Only supported on Premium SKU’s.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rdbBackupFrequency</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Backup Frequency in Minutes. Only supported on Premium SKU’s. Possible values are: <code class="docutils literal notranslate"><span class="pre">15</span></code>, <code class="docutils literal notranslate"><span class="pre">30</span></code>, <code class="docutils literal notranslate"><span class="pre">60</span></code>, <code class="docutils literal notranslate"><span class="pre">360</span></code>, <code class="docutils literal notranslate"><span class="pre">720</span></code> and <code class="docutils literal notranslate"><span class="pre">1440</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rdbBackupMaxSnapshotCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of snapshots to create as a backup. Only supported for Premium SKU’s.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rdbStorageConnectionString</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Connection String to the Storage Account. Only supported for Premium SKU’s. In the format: <code class="docutils literal notranslate"><span class="pre">DefaultEndpointsProtocol=https;BlobEndpoint=${azurerm_storage_account.example.primary_blob_endpoint};AccountName=${azurerm_storage_account.example.name};AccountKey=${azurerm_storage_account.example.primary_access_key}</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.Cache.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the Redis instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.Cache.secondary_access_key">
<code class="sig-name descname">secondary_access_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.secondary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Access Key for the Redis Instance</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.Cache.secondary_connection_string">
<code class="sig-name descname">secondary_connection_string</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary connection string of the Redis Instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.Cache.shard_count">
<code class="sig-name descname">shard_count</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.shard_count" title="Permalink to this definition">¶</a></dt>
<dd><p><em>Only available when using the Premium SKU</em> The number of Shards to create on the Redis Cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.Cache.sku_name">
<code class="sig-name descname">sku_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU of Redis to use. Possible values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.Cache.ssl_port">
<code class="sig-name descname">ssl_port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.ssl_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSL Port of the Redis Instance</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.Cache.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p><em>Only available when using the Premium SKU</em> The ID of the Subnet within which the Redis Cache should be deployed. This Subnet must only contain Azure Cache for Redis instances without any other type of resources. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.Cache.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.Cache.zones">
<code class="sig-name descname">zones</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of a single item of the Availability Zone which the Redis Cache should be allocated in.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.redis.Cache.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_non_ssl_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minimum_tls_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">patch_schedules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary_access_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary_connection_string</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_static_ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redis_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondary_access_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondary_connection_string</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shard_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sku_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zones</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.redis.Cache.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cache resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the Redis cache to deploy. Valid values for a SKU <code class="docutils literal notranslate"><span class="pre">family</span></code> of C (Basic/Standard) are <code class="docutils literal notranslate"><span class="pre">0,</span> <span class="pre">1,</span> <span class="pre">2,</span> <span class="pre">3,</span> <span class="pre">4,</span> <span class="pre">5,</span> <span class="pre">6</span></code>, and for P (Premium) <code class="docutils literal notranslate"><span class="pre">family</span></code> are <code class="docutils literal notranslate"><span class="pre">1,</span> <span class="pre">2,</span> <span class="pre">3,</span> <span class="pre">4</span></code>.</p></li>
<li><p><strong>enable_non_ssl_port</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable the non-SSL port (6379) - disabled by default.</p></li>
<li><p><strong>family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU family/pricing group to use. Valid values are <code class="docutils literal notranslate"><span class="pre">C</span></code> (for Basic/Standard SKU family) and <code class="docutils literal notranslate"><span class="pre">P</span></code> (for <code class="docutils literal notranslate"><span class="pre">Premium</span></code>)</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Hostname of the Redis Instance</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the resource group.</p></li>
<li><p><strong>minimum_tls_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The minimum TLS version.  Defaults to <code class="docutils literal notranslate"><span class="pre">1.0</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Redis instance. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>patch_schedules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of <code class="docutils literal notranslate"><span class="pre">patch_schedule</span></code> blocks as defined below - only available for Premium SKU’s.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The non-SSL Port of the Redis Instance</p></li>
<li><p><strong>primary_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary Access Key for the Redis Instance</p></li>
<li><p><strong>primary_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The primary connection string of the Redis Instance.</p></li>
<li><p><strong>private_static_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Static IP Address to assign to the Redis Cache when hosted inside the Virtual Network. Changing this forces a new resource to be created.</p></li>
<li><p><strong>redis_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">redis_configuration</span></code> as defined below - with some limitations by SKU - defaults/details are shown below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the Redis instance.</p></li>
<li><p><strong>secondary_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Secondary Access Key for the Redis Instance</p></li>
<li><p><strong>secondary_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secondary connection string of the Redis Instance.</p></li>
<li><p><strong>shard_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <em>Only available when using the Premium SKU</em> The number of Shards to create on the Redis Cluster.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU of Redis to use. Possible values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>.</p></li>
<li><p><strong>ssl_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The SSL Port of the Redis Instance</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <em>Only available when using the Premium SKU</em> The ID of the Subnet within which the Redis Cache should be deployed. This Subnet must only contain Azure Cache for Redis instances without any other type of resources. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A list of a single item of the Availability Zone which the Redis Cache should be allocated in.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>patch_schedules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dayOfWeek</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startHourUtc</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>redis_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aofBackupEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">aofStorageConnectionString0</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">aofStorageConnectionString1</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableAuthentication</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If set to <code class="docutils literal notranslate"><span class="pre">false</span></code>, the Redis instance will be accessible without authentication. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxclients</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Returns the max number of connected clients at the same time.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxfragmentationmemoryReserved</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Value in megabytes reserved to accommodate for memory fragmentation. Defaults are shown below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxmemoryDelta</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The max-memory delta for this Redis instance. Defaults are shown below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxmemoryPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How Redis will select what to remove when <code class="docutils literal notranslate"><span class="pre">maxmemory</span></code> is reached. Defaults are shown below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxmemoryReserved</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Value in megabytes reserved for non-cache usage e.g. failover. Defaults are shown below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notifyKeyspaceEvents</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Keyspace notifications allows clients to subscribe to Pub/Sub channels in order to receive events affecting the Redis data set in some way. <a class="reference external" href="https://redis.io/topics/notifications#configuration">Reference</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rdbBackupEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is Backup Enabled? Only supported on Premium SKU’s.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rdbBackupFrequency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Backup Frequency in Minutes. Only supported on Premium SKU’s. Possible values are: <code class="docutils literal notranslate"><span class="pre">15</span></code>, <code class="docutils literal notranslate"><span class="pre">30</span></code>, <code class="docutils literal notranslate"><span class="pre">60</span></code>, <code class="docutils literal notranslate"><span class="pre">360</span></code>, <code class="docutils literal notranslate"><span class="pre">720</span></code> and <code class="docutils literal notranslate"><span class="pre">1440</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rdbBackupMaxSnapshotCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of snapshots to create as a backup. Only supported for Premium SKU’s.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rdbStorageConnectionString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Connection String to the Storage Account. Only supported for Premium SKU’s. In the format: <code class="docutils literal notranslate"><span class="pre">DefaultEndpointsProtocol=https;BlobEndpoint=${azurerm_storage_account.example.primary_blob_endpoint};AccountName=${azurerm_storage_account.example.name};AccountKey=${azurerm_storage_account.example.primary_access_key}</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.redis.Cache.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.redis.Cache.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.redis.Cache.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.redis.Cache.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.redis.FirewallRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.redis.</code><code class="sig-name descname">FirewallRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redis_cache_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.redis.FirewallRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Firewall Rule associated with a Redis Cache.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>end_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The highest IP address included in the range.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Firewall Rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>redis_cache_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Redis Cache. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which this Redis Cache exists.</p></li>
<li><p><strong>start_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The lowest IP address included in the range</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azure.redis.FirewallRule.end_ip">
<code class="sig-name descname">end_ip</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.FirewallRule.end_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The highest IP address included in the range.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.FirewallRule.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.FirewallRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Firewall Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.FirewallRule.redis_cache_name">
<code class="sig-name descname">redis_cache_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.FirewallRule.redis_cache_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Redis Cache. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.FirewallRule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.FirewallRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which this Redis Cache exists.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.FirewallRule.start_ip">
<code class="sig-name descname">start_ip</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.FirewallRule.start_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The lowest IP address included in the range</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.redis.FirewallRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redis_cache_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_ip</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.redis.FirewallRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FirewallRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>end_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The highest IP address included in the range.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Firewall Rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>redis_cache_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Redis Cache. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which this Redis Cache exists.</p></li>
<li><p><strong>start_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The lowest IP address included in the range</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.redis.FirewallRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.redis.FirewallRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.redis.FirewallRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.redis.FirewallRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.redis.GetCacheResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.redis.</code><code class="sig-name descname">GetCacheResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_non_ssl_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minimum_tls_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">patch_schedules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary_access_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary_connection_string</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_static_ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redis_configurations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondary_access_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondary_connection_string</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shard_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sku_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zones</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.redis.GetCacheResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCache.</p>
<dl class="py attribute">
<dt id="pulumi_azure.redis.GetCacheResult.capacity">
<code class="sig-name descname">capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.GetCacheResult.capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the Redis Cache deployed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.GetCacheResult.enable_non_ssl_port">
<code class="sig-name descname">enable_non_ssl_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.GetCacheResult.enable_non_ssl_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the SSL port is enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.GetCacheResult.family">
<code class="sig-name descname">family</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.GetCacheResult.family" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU family/pricing group used. Possible values are <code class="docutils literal notranslate"><span class="pre">C</span></code> (for Basic/Standard SKU family) and <code class="docutils literal notranslate"><span class="pre">P</span></code> (for <code class="docutils literal notranslate"><span class="pre">Premium</span></code>)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.GetCacheResult.hostname">
<code class="sig-name descname">hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.GetCacheResult.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The Hostname of the Redis Instance</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.GetCacheResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.GetCacheResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.GetCacheResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.GetCacheResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the Redis Cache.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.GetCacheResult.minimum_tls_version">
<code class="sig-name descname">minimum_tls_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.GetCacheResult.minimum_tls_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum TLS version.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.GetCacheResult.patch_schedules">
<code class="sig-name descname">patch_schedules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.GetCacheResult.patch_schedules" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of <code class="docutils literal notranslate"><span class="pre">patch_schedule</span></code> blocks as defined below - only available for Premium SKU’s.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.GetCacheResult.port">
<code class="sig-name descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.GetCacheResult.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The non-SSL Port of the Redis Instance</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.GetCacheResult.primary_access_key">
<code class="sig-name descname">primary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.GetCacheResult.primary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Access Key for the Redis Instance</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.GetCacheResult.primary_connection_string">
<code class="sig-name descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.GetCacheResult.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary connection string of the Redis Instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.GetCacheResult.redis_configurations">
<code class="sig-name descname">redis_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.GetCacheResult.redis_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">redis_configuration</span></code> block as defined below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.GetCacheResult.secondary_access_key">
<code class="sig-name descname">secondary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.GetCacheResult.secondary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Access Key for the Redis Instance</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.GetCacheResult.secondary_connection_string">
<code class="sig-name descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.GetCacheResult.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary connection string of the Redis Instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.GetCacheResult.sku_name">
<code class="sig-name descname">sku_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.GetCacheResult.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU of Redis used. Possible values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.redis.GetCacheResult.ssl_port">
<code class="sig-name descname">ssl_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.GetCacheResult.ssl_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSL Port of the Redis Instance</p>
</dd></dl>

</dd></dl>

<dl class="py function">
<dt id="pulumi_azure.redis.get_cache">
<code class="sig-prename descclassname">pulumi_azure.redis.</code><code class="sig-name descname">get_cache</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.redis.get_cache" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Redis Cache</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the Redis cache</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the resource group the Redis cache instance is located in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
