---
title: Module redis
title_tag: Module redis | Package pulumi_gcp | Python SDK
linktitle: redis
notitle: true
---

<div class="section" id="redis">
<h1>redis<a class="headerlink" href="#redis" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.redis"></span><dl class="class">
<dt id="pulumi_gcp.redis.Instance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.redis.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alternative_location_id=None</em>, <em class="sig-param">authorized_network=None</em>, <em class="sig-param">connect_mode=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">location_id=None</em>, <em class="sig-param">memory_size_gb=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">redis_configs=None</em>, <em class="sig-param">redis_version=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">reserved_ip_range=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.redis.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>A Google Cloud Redis instance.</p>
<p>To get more information about Instance, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/memorystore/docs/redis/reference/rest/">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/memorystore/docs/redis/">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alternative_location_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Only applicable to STANDARD_HA tier which protects the instance against zonal failures by provisioning it across two
zones. If provided, it must be a different zone from the one provided in [locationId].</p></li>
<li><p><strong>authorized_network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full name of the Google Compute Engine network to which the instance is connected. If left unspecified, the default
network will be used.</p></li>
<li><p><strong>connect_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connection mode of the Redis instance. Can be either ‘DIRECT_PEERING’ or ‘PRIVATE_SERVICE_ACCESS’. The default
connect mode if not provided is ‘DIRECT_PEERING’.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An arbitrary and optional user-provided name for the instance.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Resource labels to represent user provided metadata.</p></li>
<li><p><strong>location_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone where the instance will be provisioned. If not provided, the service will choose a zone for the instance. For
STANDARD_HA tier, instances will be created across two zones for protection against zonal failures. If
[alternativeLocationId] is also provided, it must be different from [locationId].</p></li>
<li><p><strong>memory_size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Redis memory size in GiB.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the instance or a fully qualified identifier for the instance.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>redis_configs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Redis configuration parameters, according to <a class="reference external" href="http://redis.io/topics/config">http://redis.io/topics/config</a>. Please check Memorystore documentation for
the list of supported parameters:
<a class="reference external" href="https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs">https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs</a></p></li>
<li><p><strong>redis_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of Redis software. If not provided, latest supported version will be used. Currently, the supported values
are: - REDIS_4_0 for Redis 4.0 compatibility - REDIS_3_2 for Redis 3.2 compatibility</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Redis region of the instance.</p></li>
<li><p><strong>reserved_ip_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CIDR range of internal addresses that are reserved for this instance. If not provided, the service will choose an
unused /29 block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be unique and non-overlapping with existing
subnets in an authorized network.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service tier of the instance. Must be one of these values: - BASIC: standalone instance - STANDARD_HA: highly
available primary/replica instances</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.redis.Instance.alternative_location_id">
<code class="sig-name descname">alternative_location_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.redis.Instance.alternative_location_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Only applicable to STANDARD_HA tier which protects the instance against zonal failures by provisioning it across two
zones. If provided, it must be a different zone from the one provided in [locationId].</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.redis.Instance.authorized_network">
<code class="sig-name descname">authorized_network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.redis.Instance.authorized_network" title="Permalink to this definition">¶</a></dt>
<dd><p>The full name of the Google Compute Engine network to which the instance is connected. If left unspecified, the default
network will be used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.redis.Instance.connect_mode">
<code class="sig-name descname">connect_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.redis.Instance.connect_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection mode of the Redis instance. Can be either ‘DIRECT_PEERING’ or ‘PRIVATE_SERVICE_ACCESS’. The default
connect mode if not provided is ‘DIRECT_PEERING’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.redis.Instance.create_time">
<code class="sig-name descname">create_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.redis.Instance.create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time the instance was created in RFC3339 UTC “Zulu” format, accurate to nanoseconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.redis.Instance.current_location_id">
<code class="sig-name descname">current_location_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.redis.Instance.current_location_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The current zone where the Redis endpoint is placed. For Basic Tier instances, this will always be the same as the
[locationId] provided by the user at creation time. For Standard Tier instances, this can be either [locationId] or
[alternativeLocationId] and can change after a failover event.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.redis.Instance.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.redis.Instance.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>An arbitrary and optional user-provided name for the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.redis.Instance.host">
<code class="sig-name descname">host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.redis.Instance.host" title="Permalink to this definition">¶</a></dt>
<dd><p>Hostname or IP address of the exposed Redis endpoint used by clients to connect to the service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.redis.Instance.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.redis.Instance.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource labels to represent user provided metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.redis.Instance.location_id">
<code class="sig-name descname">location_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.redis.Instance.location_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone where the instance will be provisioned. If not provided, the service will choose a zone for the instance. For
STANDARD_HA tier, instances will be created across two zones for protection against zonal failures. If
[alternativeLocationId] is also provided, it must be different from [locationId].</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.redis.Instance.memory_size_gb">
<code class="sig-name descname">memory_size_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.redis.Instance.memory_size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>Redis memory size in GiB.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.redis.Instance.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.redis.Instance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the instance or a fully qualified identifier for the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.redis.Instance.port">
<code class="sig-name descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.redis.Instance.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port number of the exposed Redis endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.redis.Instance.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.redis.Instance.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.redis.Instance.redis_configs">
<code class="sig-name descname">redis_configs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.redis.Instance.redis_configs" title="Permalink to this definition">¶</a></dt>
<dd><p>Redis configuration parameters, according to <a class="reference external" href="http://redis.io/topics/config">http://redis.io/topics/config</a>. Please check Memorystore documentation for
the list of supported parameters:
<a class="reference external" href="https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs">https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.redis.Instance.redis_version">
<code class="sig-name descname">redis_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.redis.Instance.redis_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of Redis software. If not provided, latest supported version will be used. Currently, the supported values
are: - REDIS_4_0 for Redis 4.0 compatibility - REDIS_3_2 for Redis 3.2 compatibility</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.redis.Instance.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.redis.Instance.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Redis region of the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.redis.Instance.reserved_ip_range">
<code class="sig-name descname">reserved_ip_range</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.redis.Instance.reserved_ip_range" title="Permalink to this definition">¶</a></dt>
<dd><p>The CIDR range of internal addresses that are reserved for this instance. If not provided, the service will choose an
unused /29 block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be unique and non-overlapping with existing
subnets in an authorized network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.redis.Instance.tier">
<code class="sig-name descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.redis.Instance.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>The service tier of the instance. Must be one of these values: - BASIC: standalone instance - STANDARD_HA: highly
available primary/replica instances</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.redis.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alternative_location_id=None</em>, <em class="sig-param">authorized_network=None</em>, <em class="sig-param">connect_mode=None</em>, <em class="sig-param">create_time=None</em>, <em class="sig-param">current_location_id=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">host=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">location_id=None</em>, <em class="sig-param">memory_size_gb=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">redis_configs=None</em>, <em class="sig-param">redis_version=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">reserved_ip_range=None</em>, <em class="sig-param">tier=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.redis.Instance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alternative_location_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Only applicable to STANDARD_HA tier which protects the instance against zonal failures by provisioning it across two
zones. If provided, it must be a different zone from the one provided in [locationId].</p></li>
<li><p><strong>authorized_network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full name of the Google Compute Engine network to which the instance is connected. If left unspecified, the default
network will be used.</p></li>
<li><p><strong>connect_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connection mode of the Redis instance. Can be either ‘DIRECT_PEERING’ or ‘PRIVATE_SERVICE_ACCESS’. The default
connect mode if not provided is ‘DIRECT_PEERING’.</p></li>
<li><p><strong>create_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time the instance was created in RFC3339 UTC “Zulu” format, accurate to nanoseconds.</p></li>
<li><p><strong>current_location_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The current zone where the Redis endpoint is placed. For Basic Tier instances, this will always be the same as the
[locationId] provided by the user at creation time. For Standard Tier instances, this can be either [locationId] or
[alternativeLocationId] and can change after a failover event.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An arbitrary and optional user-provided name for the instance.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Hostname or IP address of the exposed Redis endpoint used by clients to connect to the service.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Resource labels to represent user provided metadata.</p></li>
<li><p><strong>location_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone where the instance will be provisioned. If not provided, the service will choose a zone for the instance. For
STANDARD_HA tier, instances will be created across two zones for protection against zonal failures. If
[alternativeLocationId] is also provided, it must be different from [locationId].</p></li>
<li><p><strong>memory_size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Redis memory size in GiB.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the instance or a fully qualified identifier for the instance.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port number of the exposed Redis endpoint.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>redis_configs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Redis configuration parameters, according to <a class="reference external" href="http://redis.io/topics/config">http://redis.io/topics/config</a>. Please check Memorystore documentation for
the list of supported parameters:
<a class="reference external" href="https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs">https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs</a></p></li>
<li><p><strong>redis_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of Redis software. If not provided, latest supported version will be used. Currently, the supported values
are: - REDIS_4_0 for Redis 4.0 compatibility - REDIS_3_2 for Redis 3.2 compatibility</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Redis region of the instance.</p></li>
<li><p><strong>reserved_ip_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CIDR range of internal addresses that are reserved for this instance. If not provided, the service will choose an
unused /29 block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be unique and non-overlapping with existing
subnets in an authorized network.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service tier of the instance. Must be one of these values: - BASIC: standalone instance - STANDARD_HA: highly
available primary/replica instances</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.redis.Instance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.redis.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.redis.Instance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.redis.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
