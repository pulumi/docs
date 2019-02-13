<div class="section" id="module-pulumi_azure.redis">
<span id="redis"></span><h1>redis<a class="headerlink" href="#module-pulumi_azure.redis" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.redis.Cache">
<em class="property">class </em><code class="descclassname">pulumi_azure.redis.</code><code class="descname">Cache</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>capacity=None</em>, <em>enable_non_ssl_port=None</em>, <em>family=None</em>, <em>location=None</em>, <em>name=None</em>, <em>patch_schedules=None</em>, <em>private_static_ip_address=None</em>, <em>redis_configuration=None</em>, <em>resource_group_name=None</em>, <em>shard_count=None</em>, <em>sku_name=None</em>, <em>subnet_id=None</em>, <em>tags=None</em>, <em>zones=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.redis.Cache" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Redis Cache.</p>
<table border="1" class="docutils">
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Redis Value</th>
<th class="head">Basic</th>
<th class="head">Standard</th>
<th class="head">Premium</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td>maxmemory_reserved</td>
<td>2</td>
<td>50</td>
<td>200</td>
</tr>
<tr class="row-odd"><td>maxmemory_delta</td>
<td>2</td>
<td>50</td>
<td>200</td>
</tr>
<tr class="row-even"><td>maxmemory_policy</td>
<td>volatile-lru</td>
<td>volatile-lru</td>
<td>volatile-lru</td>
</tr>
</tbody>
</table>
<p>_<em>Important</em>: The <code class="docutils literal notranslate"><span class="pre">maxmemory_reserved</span></code> and <code class="docutils literal notranslate"><span class="pre">maxmemory_delta</span></code> settings are only available for Standard and Premium caches. More details are available in the Relevant Links section below._</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">patch_schedule</span></code> supports the following:</li>
<li><code class="docutils literal notranslate"><span class="pre">day_of_week</span></code> (Required) the Weekday name - possible values include <code class="docutils literal notranslate"><span class="pre">Monday</span></code>, <code class="docutils literal notranslate"><span class="pre">Tuesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Wednesday</span></code> etc.</li>
<li><code class="docutils literal notranslate"><span class="pre">start_hour_utc</span></code> - (Optional) the Start Hour for maintenance in UTC - possible values range from <code class="docutils literal notranslate"><span class="pre">0</span> <span class="pre">-</span> <span class="pre">23</span></code>.</li>
</ul>
<blockquote>
<div><strong>Note:</strong> The Patch Window lasts for <code class="docutils literal notranslate"><span class="pre">5</span></code> hours from the <code class="docutils literal notranslate"><span class="pre">start_hour_utc</span></code>.</div></blockquote>
<ul class="simple">
<li><a class="reference external" href="https://azure.microsoft.com/en-us/documentation/articles/cache-configure/#advanced-settings">Azure Redis Cache: SKU specific configuration limitations</a></li>
<li><a class="reference external" href="http://redis.io/topics/config">Redis: Available Configuration Settings</a></li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>capacity</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The size of the Redis cache to deploy. Valid values for a SKU <code class="docutils literal notranslate"><span class="pre">family</span></code> of C (Basic/Standard) are <code class="docutils literal notranslate"><span class="pre">0,</span> <span class="pre">1,</span> <span class="pre">2,</span> <span class="pre">3,</span> <span class="pre">4,</span> <span class="pre">5,</span> <span class="pre">6</span></code>, and for P (Premium) <code class="docutils literal notranslate"><span class="pre">family</span></code> are <code class="docutils literal notranslate"><span class="pre">1,</span> <span class="pre">2,</span> <span class="pre">3,</span> <span class="pre">4</span></code>.</li>
<li><strong>enable_non_ssl_port</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable the non-SSL port (6789) - disabled by default.</li>
<li><strong>family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU family to use. Valid values are <code class="docutils literal notranslate"><span class="pre">C</span></code> and <code class="docutils literal notranslate"><span class="pre">P</span></code>, where C = Basic/Standard, P = Premium.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the resource group.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Redis instance. Changing this forces a
new resource to be created.</li>
<li><strong>patch_schedules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of <code class="docutils literal notranslate"><span class="pre">patch_schedule</span></code> blocks as defined below - only available for Premium SKU’s.</li>
<li><strong>private_static_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Static IP Address to assign to the Redis Cache when hosted inside the Virtual Network. Changing this forces a new resource to be created.</li>
<li><strong>redis_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">redis_configuration</span></code> as defined below - with some limitations by SKU - defaults/details are shown below.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the Redis instance.</li>
<li><strong>shard_count</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – <em>Only available when using the Premium SKU</em> The number of Shards to create on the Redis Cluster.</li>
<li><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU of Redis to use - can be either Basic, Standard or Premium.</li>
<li><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Subnet within which the Redis Cache should be deployed. Changing this forces a new resource to be created.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A list of a single item of the Availability Zone which the Redis Cache should be allocated in.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.redis.Cache.capacity">
<code class="descname">capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the Redis cache to deploy. Valid values for a SKU <code class="docutils literal notranslate"><span class="pre">family</span></code> of C (Basic/Standard) are <code class="docutils literal notranslate"><span class="pre">0,</span> <span class="pre">1,</span> <span class="pre">2,</span> <span class="pre">3,</span> <span class="pre">4,</span> <span class="pre">5,</span> <span class="pre">6</span></code>, and for P (Premium) <code class="docutils literal notranslate"><span class="pre">family</span></code> are <code class="docutils literal notranslate"><span class="pre">1,</span> <span class="pre">2,</span> <span class="pre">3,</span> <span class="pre">4</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.redis.Cache.enable_non_ssl_port">
<code class="descname">enable_non_ssl_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.enable_non_ssl_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable the non-SSL port (6789) - disabled by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.redis.Cache.family">
<code class="descname">family</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.family" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU family to use. Valid values are <code class="docutils literal notranslate"><span class="pre">C</span></code> and <code class="docutils literal notranslate"><span class="pre">P</span></code>, where C = Basic/Standard, P = Premium.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.redis.Cache.hostname">
<code class="descname">hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The Hostname of the Redis Instance</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.redis.Cache.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the resource group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.redis.Cache.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Redis instance. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.redis.Cache.patch_schedules">
<code class="descname">patch_schedules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.patch_schedules" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of <code class="docutils literal notranslate"><span class="pre">patch_schedule</span></code> blocks as defined below - only available for Premium SKU’s.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.redis.Cache.port">
<code class="descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The non-SSL Port of the Redis Instance</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.redis.Cache.primary_access_key">
<code class="descname">primary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.primary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Access Key for the Redis Instance</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.redis.Cache.private_static_ip_address">
<code class="descname">private_static_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.private_static_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The Static IP Address to assign to the Redis Cache when hosted inside the Virtual Network. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.redis.Cache.redis_configuration">
<code class="descname">redis_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.redis_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">redis_configuration</span></code> as defined below - with some limitations by SKU - defaults/details are shown below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.redis.Cache.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the Redis instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.redis.Cache.secondary_access_key">
<code class="descname">secondary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.secondary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Access Key for the Redis Instance</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.redis.Cache.shard_count">
<code class="descname">shard_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.shard_count" title="Permalink to this definition">¶</a></dt>
<dd><p><em>Only available when using the Premium SKU</em> The number of Shards to create on the Redis Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.redis.Cache.sku_name">
<code class="descname">sku_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU of Redis to use - can be either Basic, Standard or Premium.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.redis.Cache.ssl_port">
<code class="descname">ssl_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.ssl_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSL Port of the Redis Instance</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.redis.Cache.subnet_id">
<code class="descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Subnet within which the Redis Cache should be deployed. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.redis.Cache.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.redis.Cache.zones">
<code class="descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.Cache.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of a single item of the Availability Zone which the Redis Cache should be allocated in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.redis.Cache.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.redis.Cache.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.redis.Cache.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.redis.Cache.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.redis.FirewallRule">
<em class="property">class </em><code class="descclassname">pulumi_azure.redis.</code><code class="descname">FirewallRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>end_ip=None</em>, <em>name=None</em>, <em>redis_cache_name=None</em>, <em>resource_group_name=None</em>, <em>start_ip=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.redis.FirewallRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Firewall Rule associated with a Redis Cache.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>end_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The highest IP address included in the range.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Firewall Rule. Changing this forces a new resource to be created.</li>
<li><strong>redis_cache_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Redis Cache. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which this Redis Cache exists.</li>
<li><strong>start_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The lowest IP address included in the range</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.redis.FirewallRule.end_ip">
<code class="descname">end_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.FirewallRule.end_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The highest IP address included in the range.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.redis.FirewallRule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.FirewallRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Firewall Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.redis.FirewallRule.redis_cache_name">
<code class="descname">redis_cache_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.FirewallRule.redis_cache_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Redis Cache. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.redis.FirewallRule.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.FirewallRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which this Redis Cache exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.redis.FirewallRule.start_ip">
<code class="descname">start_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.redis.FirewallRule.start_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The lowest IP address included in the range</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.redis.FirewallRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.redis.FirewallRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.redis.FirewallRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.redis.FirewallRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
