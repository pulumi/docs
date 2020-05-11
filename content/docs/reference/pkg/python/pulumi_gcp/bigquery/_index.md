---
title: Module bigquery
title_tag: Module bigquery | Package pulumi_gcp | Python SDK
linktitle: bigquery
notitle: true
---

<div class="section" id="bigquery">
<h1>bigquery<a class="headerlink" href="#bigquery" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.bigquery"></span><dl class="py class">
<dt id="pulumi_gcp.bigquery.AppProfile">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.bigquery.</code><code class="sig-name descname">AppProfile</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_profile_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_warnings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">multi_cluster_routing_use_any</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">single_cluster_routing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.AppProfile" title="Permalink to this definition">¶</a></dt>
<dd><p>App profile is a configuration object describing how Cloud Bigtable should treat traffic from a particular end user application.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_profile_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of the app profile in the form <code class="docutils literal notranslate"><span class="pre">[_a-zA-Z0-9][-_.a-zA-Z0-9]*</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Long form description of the use case for this app profile.</p></li>
<li><p><strong>ignore_warnings</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, ignore safety checks when deleting/updating the app profile.</p></li>
<li><p><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance to create the app profile within.</p></li>
<li><p><strong>multi_cluster_routing_use_any</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, read/write requests are routed to the nearest cluster in the instance, and will fail over to the nearest cluster that is available
in the event of transient errors or delays. Clusters in a region are considered equidistant. Choosing this option sacrifices read-your-writes
consistency to improve availability.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>single_cluster_routing</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Use a single-cluster routing policy.  Structure is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>single_cluster_routing</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowTransactionalWrites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If true, CheckAndMutateRow and ReadModifyWriteRow requests are allowed by this app profile.
It is unsafe to send these requests to the same table/row/column in multiple clusters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The cluster to which read/write requests should be routed.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.AppProfile.app_profile_id">
<code class="sig-name descname">app_profile_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.AppProfile.app_profile_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique name of the app profile in the form <code class="docutils literal notranslate"><span class="pre">[_a-zA-Z0-9][-_.a-zA-Z0-9]*</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.AppProfile.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.AppProfile.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Long form description of the use case for this app profile.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.AppProfile.ignore_warnings">
<code class="sig-name descname">ignore_warnings</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.AppProfile.ignore_warnings" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, ignore safety checks when deleting/updating the app profile.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.AppProfile.instance">
<code class="sig-name descname">instance</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.AppProfile.instance" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance to create the app profile within.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.AppProfile.multi_cluster_routing_use_any">
<code class="sig-name descname">multi_cluster_routing_use_any</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.AppProfile.multi_cluster_routing_use_any" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, read/write requests are routed to the nearest cluster in the instance, and will fail over to the nearest cluster that is available
in the event of transient errors or delays. Clusters in a region are considered equidistant. Choosing this option sacrifices read-your-writes
consistency to improve availability.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.AppProfile.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.AppProfile.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique name of the requested app profile. Values are of the form
‘projects/<span class="raw-html-m2r"><project></span>/instances/<span class="raw-html-m2r"><instance></span>/appProfiles/<span class="raw-html-m2r"><appProfileId></span>’.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.AppProfile.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.AppProfile.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.AppProfile.single_cluster_routing">
<code class="sig-name descname">single_cluster_routing</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.AppProfile.single_cluster_routing" title="Permalink to this definition">¶</a></dt>
<dd><p>Use a single-cluster routing policy.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowTransactionalWrites</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If true, CheckAndMutateRow and ReadModifyWriteRow requests are allowed by this app profile.
It is unsafe to send these requests to the same table/row/column in multiple clusters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The cluster to which read/write requests should be routed.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.bigquery.AppProfile.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_profile_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_warnings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">multi_cluster_routing_use_any</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">single_cluster_routing</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.AppProfile.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AppProfile resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_profile_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of the app profile in the form <code class="docutils literal notranslate"><span class="pre">[_a-zA-Z0-9][-_.a-zA-Z0-9]*</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Long form description of the use case for this app profile.</p></li>
<li><p><strong>ignore_warnings</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, ignore safety checks when deleting/updating the app profile.</p></li>
<li><p><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance to create the app profile within.</p></li>
<li><p><strong>multi_cluster_routing_use_any</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, read/write requests are routed to the nearest cluster in the instance, and will fail over to the nearest cluster that is available
in the event of transient errors or delays. Clusters in a region are considered equidistant. Choosing this option sacrifices read-your-writes
consistency to improve availability.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of the requested app profile. Values are of the form
‘projects/<span class="raw-html-m2r"><project></span>/instances/<span class="raw-html-m2r"><instance></span>/appProfiles/<span class="raw-html-m2r"><appProfileId></span>’.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>single_cluster_routing</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Use a single-cluster routing policy.  Structure is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>single_cluster_routing</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowTransactionalWrites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If true, CheckAndMutateRow and ReadModifyWriteRow requests are allowed by this app profile.
It is unsafe to send these requests to the same table/row/column in multiple clusters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The cluster to which read/write requests should be routed.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.bigquery.AppProfile.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.AppProfile.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigquery.AppProfile.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.AppProfile.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigquery.AwaitableGetDefaultServiceAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.bigquery.</code><code class="sig-name descname">AwaitableGetDefaultServiceAccountResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.AwaitableGetDefaultServiceAccountResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.bigquery.DataTransferConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.bigquery.</code><code class="sig-name descname">DataTransferConfig</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_refresh_window_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_source_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_dataset_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">params</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schedule</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.DataTransferConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a data transfer configuration. A transfer configuration
contains all metadata needed to perform a data transfer.</p>
<p>To get more information about Config, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/projects.locations.transferConfigs/create">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/bigquery/docs/reference/datatransfer/rest/">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data_refresh_window_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of days to look back to automatically refresh the data.
For example, if dataRefreshWindowDays = 10, then every day BigQuery
reingests data for [today-10, today-1], rather than ingesting data for
just [today-1]. Only valid if the data source supports the feature.
Set the value to 0 to use the default value.</p></li>
<li><p><strong>data_source_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data source id. Cannot be changed once the transfer config is created.</p></li>
<li><p><strong>destination_dataset_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The BigQuery target dataset id.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When set to true, no runs are scheduled for a given transfer.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user specified display name for the transfer config.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The geographic location where the transfer config should reside.
Examples: US, EU, asia-northeast1. The default value is US.</p></li>
<li><p><strong>params</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – These parameters are specific to each data source.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>schedule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Data transfer schedule. If the data source does not support a custom
schedule, this should be empty. If it is empty, the default value for
the data source will be used. The specified times are in UTC. Examples
of valid format: 1st,3rd monday of month 15:30, every wed,fri of jan,
jun 13:15, and first sunday of quarter 00:00. See more explanation
about the format here:
<a class="reference external" href="https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format">https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format</a>
NOTE: the granularity should be at least 8 hours, or less frequent.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.DataTransferConfig.data_refresh_window_days">
<code class="sig-name descname">data_refresh_window_days</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.DataTransferConfig.data_refresh_window_days" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of days to look back to automatically refresh the data.
For example, if dataRefreshWindowDays = 10, then every day BigQuery
reingests data for [today-10, today-1], rather than ingesting data for
just [today-1]. Only valid if the data source supports the feature.
Set the value to 0 to use the default value.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.DataTransferConfig.data_source_id">
<code class="sig-name descname">data_source_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.DataTransferConfig.data_source_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The data source id. Cannot be changed once the transfer config is created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.DataTransferConfig.destination_dataset_id">
<code class="sig-name descname">destination_dataset_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.DataTransferConfig.destination_dataset_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The BigQuery target dataset id.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.DataTransferConfig.disabled">
<code class="sig-name descname">disabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.DataTransferConfig.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>When set to true, no runs are scheduled for a given transfer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.DataTransferConfig.display_name">
<code class="sig-name descname">display_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.DataTransferConfig.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The user specified display name for the transfer config.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.DataTransferConfig.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.DataTransferConfig.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The geographic location where the transfer config should reside.
Examples: US, EU, asia-northeast1. The default value is US.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.DataTransferConfig.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.DataTransferConfig.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of the transfer config. Transfer config names have the form
projects/{projectId}/locations/{location}/transferConfigs/{configId}. Where configId is usually a uuid, but this is not
required. The name is ignored when creating a transfer config.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.DataTransferConfig.params">
<code class="sig-name descname">params</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.DataTransferConfig.params" title="Permalink to this definition">¶</a></dt>
<dd><p>These parameters are specific to each data source.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.DataTransferConfig.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.DataTransferConfig.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.DataTransferConfig.schedule">
<code class="sig-name descname">schedule</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.DataTransferConfig.schedule" title="Permalink to this definition">¶</a></dt>
<dd><p>Data transfer schedule. If the data source does not support a custom
schedule, this should be empty. If it is empty, the default value for
the data source will be used. The specified times are in UTC. Examples
of valid format: 1st,3rd monday of month 15:30, every wed,fri of jan,
jun 13:15, and first sunday of quarter 00:00. See more explanation
about the format here:
<a class="reference external" href="https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format">https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format</a>
NOTE: the granularity should be at least 8 hours, or less frequent.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.bigquery.DataTransferConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_refresh_window_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_source_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_dataset_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">params</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schedule</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.DataTransferConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DataTransferConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data_refresh_window_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of days to look back to automatically refresh the data.
For example, if dataRefreshWindowDays = 10, then every day BigQuery
reingests data for [today-10, today-1], rather than ingesting data for
just [today-1]. Only valid if the data source supports the feature.
Set the value to 0 to use the default value.</p></li>
<li><p><strong>data_source_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data source id. Cannot be changed once the transfer config is created.</p></li>
<li><p><strong>destination_dataset_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The BigQuery target dataset id.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When set to true, no runs are scheduled for a given transfer.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user specified display name for the transfer config.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The geographic location where the transfer config should reside.
Examples: US, EU, asia-northeast1. The default value is US.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name of the transfer config. Transfer config names have the form
projects/{projectId}/locations/{location}/transferConfigs/{configId}. Where configId is usually a uuid, but this is not
required. The name is ignored when creating a transfer config.</p></li>
<li><p><strong>params</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – These parameters are specific to each data source.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>schedule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Data transfer schedule. If the data source does not support a custom
schedule, this should be empty. If it is empty, the default value for
the data source will be used. The specified times are in UTC. Examples
of valid format: 1st,3rd monday of month 15:30, every wed,fri of jan,
jun 13:15, and first sunday of quarter 00:00. See more explanation
about the format here:
<a class="reference external" href="https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format">https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format</a>
NOTE: the granularity should be at least 8 hours, or less frequent.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.bigquery.DataTransferConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.DataTransferConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigquery.DataTransferConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.DataTransferConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigquery.Dataset">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.bigquery.</code><code class="sig-name descname">Dataset</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accesses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dataset_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_encryption_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_partition_expiration_ms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_table_expiration_ms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_contents_on_destroy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">friendly_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset" title="Permalink to this definition">¶</a></dt>
<dd><p>Datasets allow you to organize and control access to your tables.</p>
<p>To get more information about Dataset, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/bigquery/docs/datasets-intro">Datasets Intro</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accesses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of objects that define dataset access for one or more entities.  Structure is documented below.</p></li>
<li><p><strong>dataset_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the dataset containing this table.</p></li>
<li><p><strong>default_encryption_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The default encryption key for all tables in the dataset. Once this property is set,
all newly-created partitioned tables in the dataset will have encryption key set to
this value, unless table creation request (or query) overrides the key.  Structure is documented below.</p></li>
<li><p><strong>default_partition_expiration_ms</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default partition expiration for all partitioned tables in
the dataset, in milliseconds.</p></li>
<li><p><strong>default_table_expiration_ms</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default lifetime of all tables in the dataset, in milliseconds.
The minimum value is 3600000 milliseconds (one hour).</p></li>
<li><p><strong>delete_contents_on_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, delete all the tables in the
dataset when destroying the resource; otherwise,
destroying the resource will fail if tables are present.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user-friendly description of the dataset</p></li>
<li><p><strong>friendly_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A descriptive name for the dataset</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The labels associated with this dataset. You can use these to
organize and group your datasets</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The geographic location where the dataset should reside.
See <a class="reference external" href="https://cloud.google.com/bigquery/docs/dataset-locations">official docs</a>.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>accesses</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A domain to grant access to. Any users signed in with the
domain specified will be granted the specified access</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">group_by_email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An email address of a Google Group to grant access to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Describes the rights granted to the user specified by the other
member of the access object. Primitive, Predefined and custom
roles are supported. Predefined roles that have equivalent
primitive roles are swapped by the API to their Primitive
counterparts, and will show a diff post-create. See
<a class="reference external" href="https://cloud.google.com/bigquery/docs/access-control">official docs</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">special_group</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A special group to grant access to. Possible values include:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_by_email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An email address of a user to grant access to. For example:
<a class="reference external" href="mailto:fred&#37;&#52;&#48;example&#46;com">fred<span>&#64;</span>example<span>&#46;</span>com</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">view</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A view from a different dataset to grant access to. Queries
executed against that view will have read access to tables in
this dataset. The role field is not required when this field is
set. If that view is updated by any user, access to the view
needs to be granted again via an update operation.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the dataset containing this table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the project containing this table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the table. The ID must contain only letters (a-z,
A-Z), numbers (0-9), or underscores (_). The maximum length
is 1,024 characters.</p></li>
</ul>
</li>
</ul>
<p>The <strong>default_encryption_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Describes the Cloud KMS encryption key that will be used to protect destination
BigQuery table. The BigQuery Service Account associated with your project requires
access to this encryption key.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Dataset.accesses">
<code class="sig-name descname">accesses</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.accesses" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of objects that define dataset access for one or more entities.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A domain to grant access to. Any users signed in with the
domain specified will be granted the specified access</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">group_by_email</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An email address of a Google Group to grant access to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Describes the rights granted to the user specified by the other
member of the access object. Primitive, Predefined and custom
roles are supported. Predefined roles that have equivalent
primitive roles are swapped by the API to their Primitive
counterparts, and will show a diff post-create. See
<a class="reference external" href="https://cloud.google.com/bigquery/docs/access-control">official docs</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">special_group</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A special group to grant access to. Possible values include:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_by_email</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An email address of a user to grant access to. For example:
<a class="reference external" href="mailto:fred&#37;&#52;&#48;example&#46;com">fred<span>&#64;</span>example<span>&#46;</span>com</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">view</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A view from a different dataset to grant access to. Queries
executed against that view will have read access to tables in
this dataset. The role field is not required when this field is
set. If that view is updated by any user, access to the view
needs to be granted again via an update operation.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the dataset containing this table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the project containing this table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the table. The ID must contain only letters (a-z,
A-Z), numbers (0-9), or underscores (_). The maximum length
is 1,024 characters.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Dataset.creation_time">
<code class="sig-name descname">creation_time</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.creation_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when this dataset was created, in milliseconds since the epoch.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Dataset.dataset_id">
<code class="sig-name descname">dataset_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.dataset_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the dataset containing this table.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Dataset.default_encryption_configuration">
<code class="sig-name descname">default_encryption_configuration</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.default_encryption_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The default encryption key for all tables in the dataset. Once this property is set,
all newly-created partitioned tables in the dataset will have encryption key set to
this value, unless table creation request (or query) overrides the key.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Describes the Cloud KMS encryption key that will be used to protect destination
BigQuery table. The BigQuery Service Account associated with your project requires
access to this encryption key.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Dataset.default_partition_expiration_ms">
<code class="sig-name descname">default_partition_expiration_ms</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.default_partition_expiration_ms" title="Permalink to this definition">¶</a></dt>
<dd><p>The default partition expiration for all partitioned tables in
the dataset, in milliseconds.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Dataset.default_table_expiration_ms">
<code class="sig-name descname">default_table_expiration_ms</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.default_table_expiration_ms" title="Permalink to this definition">¶</a></dt>
<dd><p>The default lifetime of all tables in the dataset, in milliseconds.
The minimum value is 3600000 milliseconds (one hour).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Dataset.delete_contents_on_destroy">
<code class="sig-name descname">delete_contents_on_destroy</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.delete_contents_on_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, delete all the tables in the
dataset when destroying the resource; otherwise,
destroying the resource will fail if tables are present.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Dataset.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A user-friendly description of the dataset</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Dataset.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>A hash of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Dataset.friendly_name">
<code class="sig-name descname">friendly_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.friendly_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A descriptive name for the dataset</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Dataset.labels">
<code class="sig-name descname">labels</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>The labels associated with this dataset. You can use these to
organize and group your datasets</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Dataset.last_modified_time">
<code class="sig-name descname">last_modified_time</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.last_modified_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The date when this dataset or any of its tables was last modified, in milliseconds since the epoch.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Dataset.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The geographic location where the dataset should reside.
See <a class="reference external" href="https://cloud.google.com/bigquery/docs/dataset-locations">official docs</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Dataset.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Dataset.self_link">
<code class="sig-name descname">self_link</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.bigquery.Dataset.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accesses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creation_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dataset_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_encryption_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_partition_expiration_ms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_table_expiration_ms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_contents_on_destroy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">friendly_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_modified_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">self_link</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Dataset resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accesses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of objects that define dataset access for one or more entities.  Structure is documented below.</p></li>
<li><p><strong>creation_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time when this dataset was created, in milliseconds since the epoch.</p></li>
<li><p><strong>dataset_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the dataset containing this table.</p></li>
<li><p><strong>default_encryption_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The default encryption key for all tables in the dataset. Once this property is set,
all newly-created partitioned tables in the dataset will have encryption key set to
this value, unless table creation request (or query) overrides the key.  Structure is documented below.</p></li>
<li><p><strong>default_partition_expiration_ms</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default partition expiration for all partitioned tables in
the dataset, in milliseconds.</p></li>
<li><p><strong>default_table_expiration_ms</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default lifetime of all tables in the dataset, in milliseconds.
The minimum value is 3600000 milliseconds (one hour).</p></li>
<li><p><strong>delete_contents_on_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, delete all the tables in the
dataset when destroying the resource; otherwise,
destroying the resource will fail if tables are present.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user-friendly description of the dataset</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A hash of the resource.</p></li>
<li><p><strong>friendly_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A descriptive name for the dataset</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The labels associated with this dataset. You can use these to
organize and group your datasets</p></li>
<li><p><strong>last_modified_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The date when this dataset or any of its tables was last modified, in milliseconds since the epoch.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The geographic location where the dataset should reside.
See <a class="reference external" href="https://cloud.google.com/bigquery/docs/dataset-locations">official docs</a>.</p>
</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>accesses</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A domain to grant access to. Any users signed in with the
domain specified will be granted the specified access</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">group_by_email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An email address of a Google Group to grant access to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Describes the rights granted to the user specified by the other
member of the access object. Primitive, Predefined and custom
roles are supported. Predefined roles that have equivalent
primitive roles are swapped by the API to their Primitive
counterparts, and will show a diff post-create. See
<a class="reference external" href="https://cloud.google.com/bigquery/docs/access-control">official docs</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">special_group</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A special group to grant access to. Possible values include:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_by_email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An email address of a user to grant access to. For example:
<a class="reference external" href="mailto:fred&#37;&#52;&#48;example&#46;com">fred<span>&#64;</span>example<span>&#46;</span>com</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">view</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A view from a different dataset to grant access to. Queries
executed against that view will have read access to tables in
this dataset. The role field is not required when this field is
set. If that view is updated by any user, access to the view
needs to be granted again via an update operation.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the dataset containing this table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the project containing this table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the table. The ID must contain only letters (a-z,
A-Z), numbers (0-9), or underscores (_). The maximum length
is 1,024 characters.</p></li>
</ul>
</li>
</ul>
<p>The <strong>default_encryption_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Describes the Cloud KMS encryption key that will be used to protect destination
BigQuery table. The BigQuery Service Account associated with your project requires
access to this encryption key.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.bigquery.Dataset.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigquery.Dataset.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Dataset.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigquery.DatasetAccess">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.bigquery.</code><code class="sig-name descname">DatasetAccess</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dataset_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_by_email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iam_member</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">special_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_by_email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">view</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.DatasetAccess" title="Permalink to this definition">¶</a></dt>
<dd><p>Gives dataset access for a single entity. This resource is intended to be used in cases where
it is not possible to compile a full list of access blocks to include in a
<code class="docutils literal notranslate"><span class="pre">bigquery.Dataset</span></code> resource, to enable them to be added separately.</p>
<blockquote>
<div><p><strong>Note:</strong> If this resource is used alongside a <code class="docutils literal notranslate"><span class="pre">bigquery.Dataset</span></code> resource, the
dataset resource must either have no defined <code class="docutils literal notranslate"><span class="pre">access</span></code> blocks or a <code class="docutils literal notranslate"><span class="pre">lifecycle</span></code> block with
<code class="docutils literal notranslate"><span class="pre">ignore_changes</span> <span class="pre">=</span> <span class="pre">[access]</span></code> so they don’t fight over which accesses should be on the dataset.</p>
</div></blockquote>
<p>To get more information about DatasetAccess, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/bigquery/docs/dataset-access-controls">Controlling access to datasets</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dataset_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the dataset containing this table.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A domain to grant access to. Any users signed in with the
domain specified will be granted the specified access</p></li>
<li><p><strong>group_by_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An email address of a Google Group to grant access to.</p></li>
<li><p><strong>iam_member</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Some other type of member that appears in the IAM Policy but isn’t a user,
group, domain, or special group. For example: <code class="docutils literal notranslate"><span class="pre">allUsers</span></code></p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Describes the rights granted to the user specified by the other
member of the access object. Primitive, Predefined and custom
roles are supported. Predefined roles that have equivalent
primitive roles are swapped by the API to their Primitive
counterparts, and will show a diff post-create. See
<a class="reference external" href="https://cloud.google.com/bigquery/docs/access-control">official docs</a>.</p>
</p></li>
<li><p><strong>special_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A special group to grant access to. Possible values include:</p></li>
<li><p><strong>user_by_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An email address of a user to grant access to. For example:
<a class="reference external" href="mailto:fred&#37;&#52;&#48;example&#46;com">fred<span>&#64;</span>example<span>&#46;</span>com</a></p></li>
<li><p><strong>view</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A view from a different dataset to grant access to. Queries
executed against that view will have read access to tables in
this dataset. The role field is not required when this field is
set. If that view is updated by any user, access to the view
needs to be granted again via an update operation.  Structure is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>view</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the dataset containing this table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the project containing this table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the table. The ID must contain only letters (a-z,
A-Z), numbers (0-9), or underscores (_). The maximum length
is 1,024 characters.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.DatasetAccess.dataset_id">
<code class="sig-name descname">dataset_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.DatasetAccess.dataset_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the dataset containing this table.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.DatasetAccess.domain">
<code class="sig-name descname">domain</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.DatasetAccess.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>A domain to grant access to. Any users signed in with the
domain specified will be granted the specified access</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.DatasetAccess.group_by_email">
<code class="sig-name descname">group_by_email</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.DatasetAccess.group_by_email" title="Permalink to this definition">¶</a></dt>
<dd><p>An email address of a Google Group to grant access to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.DatasetAccess.iam_member">
<code class="sig-name descname">iam_member</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.DatasetAccess.iam_member" title="Permalink to this definition">¶</a></dt>
<dd><p>Some other type of member that appears in the IAM Policy but isn’t a user,
group, domain, or special group. For example: <code class="docutils literal notranslate"><span class="pre">allUsers</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.DatasetAccess.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.DatasetAccess.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.DatasetAccess.role">
<code class="sig-name descname">role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.DatasetAccess.role" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes the rights granted to the user specified by the other
member of the access object. Primitive, Predefined and custom
roles are supported. Predefined roles that have equivalent
primitive roles are swapped by the API to their Primitive
counterparts, and will show a diff post-create. See
<a class="reference external" href="https://cloud.google.com/bigquery/docs/access-control">official docs</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.DatasetAccess.special_group">
<code class="sig-name descname">special_group</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.DatasetAccess.special_group" title="Permalink to this definition">¶</a></dt>
<dd><p>A special group to grant access to. Possible values include:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.DatasetAccess.user_by_email">
<code class="sig-name descname">user_by_email</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.DatasetAccess.user_by_email" title="Permalink to this definition">¶</a></dt>
<dd><p>An email address of a user to grant access to. For example:
<a class="reference external" href="mailto:fred&#37;&#52;&#48;example&#46;com">fred<span>&#64;</span>example<span>&#46;</span>com</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.DatasetAccess.view">
<code class="sig-name descname">view</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.DatasetAccess.view" title="Permalink to this definition">¶</a></dt>
<dd><p>A view from a different dataset to grant access to. Queries
executed against that view will have read access to tables in
this dataset. The role field is not required when this field is
set. If that view is updated by any user, access to the view
needs to be granted again via an update operation.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the dataset containing this table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the project containing this table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the table. The ID must contain only letters (a-z,
A-Z), numbers (0-9), or underscores (_). The maximum length
is 1,024 characters.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.bigquery.DatasetAccess.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dataset_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_by_email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iam_member</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">special_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_by_email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">view</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.DatasetAccess.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DatasetAccess resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dataset_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the dataset containing this table.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A domain to grant access to. Any users signed in with the
domain specified will be granted the specified access</p></li>
<li><p><strong>group_by_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An email address of a Google Group to grant access to.</p></li>
<li><p><strong>iam_member</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Some other type of member that appears in the IAM Policy but isn’t a user,
group, domain, or special group. For example: <code class="docutils literal notranslate"><span class="pre">allUsers</span></code></p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Describes the rights granted to the user specified by the other
member of the access object. Primitive, Predefined and custom
roles are supported. Predefined roles that have equivalent
primitive roles are swapped by the API to their Primitive
counterparts, and will show a diff post-create. See
<a class="reference external" href="https://cloud.google.com/bigquery/docs/access-control">official docs</a>.</p>
</p></li>
<li><p><strong>special_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A special group to grant access to. Possible values include:</p></li>
<li><p><strong>user_by_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An email address of a user to grant access to. For example:
<a class="reference external" href="mailto:fred&#37;&#52;&#48;example&#46;com">fred<span>&#64;</span>example<span>&#46;</span>com</a></p></li>
<li><p><strong>view</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A view from a different dataset to grant access to. Queries
executed against that view will have read access to tables in
this dataset. The role field is not required when this field is
set. If that view is updated by any user, access to the view
needs to be granted again via an update operation.  Structure is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>view</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the dataset containing this table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the project containing this table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the table. The ID must contain only letters (a-z,
A-Z), numbers (0-9), or underscores (_). The maximum length
is 1,024 characters.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.bigquery.DatasetAccess.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.DatasetAccess.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigquery.DatasetAccess.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.DatasetAccess.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigquery.GetDefaultServiceAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.bigquery.</code><code class="sig-name descname">GetDefaultServiceAccountResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.GetDefaultServiceAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDefaultServiceAccount.</p>
<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.GetDefaultServiceAccountResult.email">
<code class="sig-name descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.GetDefaultServiceAccountResult.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address of the service account. This value is often used to refer to the service account
in order to grant IAM permissions.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.GetDefaultServiceAccountResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.GetDefaultServiceAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.bigquery.Job">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.bigquery.</code><code class="sig-name descname">Job</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">copy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extract</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">job_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">job_timeout_ms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Job" title="Permalink to this definition">¶</a></dt>
<dd><p>Jobs are actions that BigQuery runs on your behalf to load data, export data, query data, or copy data.
Once a BigQuery job is created, it cannot be changed or deleted.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>copy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Copies a table.  Structure is documented below.</p></li>
<li><p><strong>extract</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures an extract job.  Structure is documented below.</p></li>
<li><p><strong>job*id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The ID of the job. The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (<a href="#id13"><span class="problematic" id="id14">*</span></a>), or dashes (-). The maximum length is 1,024 characters.</p>
</p></li>
<li><p><strong>job_timeout_ms</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Job timeout in milliseconds. If this time limit is exceeded, BigQuery may attempt to terminate the job.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The labels associated with this job. You can use these to organize and group your jobs.</p></li>
<li><p><strong>load</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures a load job.  Structure is documented below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The geographic location of the job. The default value is US.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures a query job.  Structure is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>copy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">createDisposition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies whether the job is allowed to create new tables. The following values are supported:
CREATE_IF_NEEDED: If the table does not exist, BigQuery creates the table.
CREATE_NEVER: The table must already exist. If it does not, a ‘notFound’ error is returned in the job result.
The default value is CREATE_IF_NEEDED. Creation, truncation and append actions occur as one atomic update upon job completion</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationEncryptionConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Custom encryption configuration (e.g., Cloud KMS keys)  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table.
The BigQuery Service Account associated with your project requires access to this encryption key.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationTable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The destination table.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the dataset containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the project containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the table.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceTables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Source tables to copy.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the dataset containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the project containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the table.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">writeDisposition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the action that occurs if the destination table already exists. The following values are supported:
WRITE_TRUNCATE: If the table already exists, BigQuery overwrites the table data and uses the schema from the query result.
WRITE_APPEND: If the table already exists, BigQuery appends the data to the table.
WRITE_EMPTY: If the table already exists and contains data, a ‘duplicate’ error is returned in the job result.
The default value is WRITE_EMPTY. Each action is atomic and only occurs if BigQuery is able to complete the job successfully.
Creation, truncation and append actions occur as one atomic update upon job completion.</p></li>
</ul>
<p>The <strong>extract</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">compression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The compression type to use for exported files. Possible values include GZIP, DEFLATE, SNAPPY, and NONE.
The default value is NONE. DEFLATE and SNAPPY are only supported for Avro.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The exported file format. Possible values include CSV, NEWLINE_DELIMITED_JSON and AVRO for tables and SAVED_MODEL for models.
The default value for tables is CSV. Tables with nested or repeated fields cannot be exported as CSV.
The default value for models is SAVED_MODEL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of fully-qualified Google Cloud Storage URIs where the extracted table should be written.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When extracting data in CSV format, this defines the delimiter to use between fields in the exported data.
Default is ‘,’</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">printHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to print out a header row in the results. Default is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceModel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A reference to the model being exported.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the dataset containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">modelId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the project containing this model.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceTable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A reference to the table being exported.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the dataset containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the project containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the table.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">useAvroLogicalTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use logical types when extracting to AVRO format.</p></li>
</ul>
<p>The <strong>load</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowJaggedRows</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Accept rows that are missing trailing optional columns. The missing values are treated as nulls.
If false, records with missing trailing columns are treated as bad records, and if there are too many bad records,
an invalid error is returned in the job result. The default value is false. Only applicable to CSV, ignored for other formats.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowQuotedNewlines</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates if BigQuery should allow quoted data sections that contain newline characters in a CSV file.
The default value is false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autodetect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates if we should automatically infer the options and schema for CSV and JSON sources.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">createDisposition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies whether the job is allowed to create new tables. The following values are supported:
CREATE_IF_NEEDED: If the table does not exist, BigQuery creates the table.
CREATE_NEVER: The table must already exist. If it does not, a ‘notFound’ error is returned in the job result.
The default value is CREATE_IF_NEEDED. Creation, truncation and append actions occur as one atomic update upon job completion</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationEncryptionConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Custom encryption configuration (e.g., Cloud KMS keys)  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table.
The BigQuery Service Account associated with your project requires access to this encryption key.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationTable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The destination table.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the dataset containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the project containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the table.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The character encoding of the data. The supported values are UTF-8 or ISO-8859-1.
The default value is UTF-8. BigQuery decodes the data after the raw, binary data
has been split using the values of the quote and fieldDelimiter properties.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When extracting data in CSV format, this defines the delimiter to use between fields in the exported data.
Default is ‘,’</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ignoreUnknownValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates if BigQuery should allow extra values that are not represented in the table schema.
If true, the extra values are ignored. If false, records with extra columns are treated as bad records,
and if there are too many bad records, an invalid error is returned in the job result.
The default value is false. The sourceFormat property determines what BigQuery treats as an extra value:
CSV: Trailing columns
JSON: Named values that don’t match any column names</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxBadRecords</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of bad records that BigQuery can ignore when running the job. If the number of bad records exceeds this value,
an invalid error is returned in the job result. The default value is 0, which requires that all records are valid.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nullMarker</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies a string that represents a null value in a CSV file. The default value is the empty string. If you set this
property to a custom value, BigQuery throws an error if an
empty string is present for all data types except for STRING and BYTE. For STRING and BYTE columns, BigQuery interprets the empty string as
an empty value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectionFields</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - If sourceFormat is set to “DATASTORE_BACKUP”, indicates which entity properties to load into BigQuery from a Cloud Datastore backup.
Property names are case sensitive and must be top-level properties. If no properties are specified, BigQuery loads all properties.
If any named property isn’t found in the Cloud Datastore backup, an invalid error is returned in the job result.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">quote</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value that is used to quote data sections in a CSV file. BigQuery converts the string to ISO-8859-1 encoding,
and then uses the first byte of the encoded string to split the data in its raw, binary state.
The default value is a double-quote (‘”’). If your data does not contain quoted sections, set the property value to an empty string.
If your data contains quoted newline characters, you must also set the allowQuotedNewlines property to true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemaUpdateOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Allows the schema of the destination table to be updated as a side effect of the load job if a schema is autodetected or
supplied in the job configuration. Schema update options are supported in two cases: when writeDisposition is WRITE_APPEND;
when writeDisposition is WRITE_TRUNCATE and the destination table is a partition of a table, specified by partition decorators.
For normal tables, WRITE_TRUNCATE will always overwrite the schema. One or more of the following values are specified:
ALLOW_FIELD_ADDITION: allow adding a nullable field to the schema.
ALLOW_FIELD_RELAXATION: allow relaxing a required field in the original schema to nullable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">skipLeadingRows</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of rows at the top of a CSV file that BigQuery will skip when loading the data.
The default value is 0. This property is useful if you have header rows in the file that should be skipped.
When autodetect is on, the behavior is the following:
skipLeadingRows unspecified - Autodetect tries to detect headers in the first row. If they are not detected,
the row is read as data. Otherwise data is read starting from the second row.
skipLeadingRows is 0 - Instructs autodetect that there are no headers and data should be read starting from the first row.
skipLeadingRows = N &gt; 0 - Autodetect skips N-1 rows and tries to detect headers in row N. If headers are not detected,
row N is just skipped. Otherwise row N is used to extract column names for the detected schema.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The format of the data files. For CSV files, specify “CSV”. For datastore backups, specify “DATASTORE_BACKUP”.
For newline-delimited JSON, specify “NEWLINE_DELIMITED_JSON”. For Avro, specify “AVRO”. For parquet, specify “PARQUET”.
For orc, specify “ORC”. The default value is CSV.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The fully-qualified URIs that point to your data in Google Cloud.
For Google Cloud Storage URIs: Each URI can contain one ‘<em>’ wildcard character
and it must come after the ‘bucket’ name. Size limits related to load jobs apply
to external data sources. For Google Cloud Bigtable URIs: Exactly one URI can be
specified and it has be a fully specified and valid HTTPS URL for a Google Cloud Bigtable table.
For Google Cloud Datastore backups: Exactly one URI can be specified. Also, the ‘</em>’ wildcard character is not allowed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">time_partitioning</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Time-based partitioning specification for the destination table.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">expirationMs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Number of milliseconds for which to keep the storage for a partition. A wrapper is used here because 0 is an invalid value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">field</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If not set, the table is partitioned by pseudo column ‘_PARTITIONTIME’; if set, the table is partitioned by this field.
The field must be a top-level TIMESTAMP or DATE field. Its mode must be NULLABLE or REQUIRED.
A wrapper is used here because an empty string is an invalid value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The only type supported is DAY, which will generate one partition per day. Providing an empty string used to cause an error,
but in OnePlatform the field will be treated as unset.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">writeDisposition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the action that occurs if the destination table already exists. The following values are supported:
WRITE_TRUNCATE: If the table already exists, BigQuery overwrites the table data and uses the schema from the query result.
WRITE_APPEND: If the table already exists, BigQuery appends the data to the table.
WRITE_EMPTY: If the table already exists and contains data, a ‘duplicate’ error is returned in the job result.
The default value is WRITE_EMPTY. Each action is atomic and only occurs if BigQuery is able to complete the job successfully.
Creation, truncation and append actions occur as one atomic update upon job completion.</p></li>
</ul>
<p>The <strong>query</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowLargeResults</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If true and query uses legacy SQL dialect, allows the query to produce arbitrarily large result tables at a slight cost in performance.
Requires destinationTable to be set. For standard SQL queries, this flag is ignored and large results are always allowed.
However, you must still set destinationTable when result size exceeds the allowed maximum response size.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">createDisposition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies whether the job is allowed to create new tables. The following values are supported:
CREATE_IF_NEEDED: If the table does not exist, BigQuery creates the table.
CREATE_NEVER: The table must already exist. If it does not, a ‘notFound’ error is returned in the job result.
The default value is CREATE_IF_NEEDED. Creation, truncation and append actions occur as one atomic update upon job completion</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultDataset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies the default dataset to use for unqualified table names in the query. Note that this does not alter behavior of unqualified dataset names.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the dataset containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the project containing this model.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationEncryptionConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Custom encryption configuration (e.g., Cloud KMS keys)  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table.
The BigQuery Service Account associated with your project requires access to this encryption key.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationTable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The destination table.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the dataset containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the project containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the table.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">flattenResults</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If true and query uses legacy SQL dialect, flattens all nested and repeated fields in the query results.
allowLargeResults must be true if this is set to false. For standard SQL queries, this flag is ignored and results are never flattened.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximumBillingTier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Limits the billing tier for this job. Queries that have resource usage beyond this tier will fail (without incurring a charge).
If unspecified, this will be set to your project default.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximumBytesBilled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Limits the bytes billed for this job. Queries that will have bytes billed beyond this limit will fail (without incurring a charge).
If unspecified, this will be set to your project default.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Standard SQL only. Set to POSITIONAL to use positional (?) query parameters or to NAMED to use named (&#64;myparam) query parameters in this query.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies a priority for the query. Possible values include INTERACTIVE and BATCH. The default value is INTERACTIVE.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Configures a query job.  Structure is documented below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemaUpdateOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Allows the schema of the destination table to be updated as a side effect of the load job if a schema is autodetected or
supplied in the job configuration. Schema update options are supported in two cases: when writeDisposition is WRITE_APPEND;
when writeDisposition is WRITE_TRUNCATE and the destination table is a partition of a table, specified by partition decorators.
For normal tables, WRITE_TRUNCATE will always overwrite the schema. One or more of the following values are specified:
ALLOW_FIELD_ADDITION: allow adding a nullable field to the schema.
ALLOW_FIELD_RELAXATION: allow relaxing a required field in the original schema to nullable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scriptOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Options controlling the execution of scripts.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">keyResultStatement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Determines which statement in the script represents the “key result”,
used to populate the schema and query results of the script job. Default is LAST.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statementByteBudget</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Limit on the number of bytes billed per statement. Exceeding this budget results in an error.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statementTimeoutMs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Timeout period for each statement in a script.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">useLegacySql</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether to use BigQuery’s legacy SQL dialect for this query. The default value is true.
If set to false, the query will use BigQuery’s standard SQL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useQueryCache</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to look for the result in the query cache. The query cache is a best-effort cache that will be flushed whenever
tables in the query are modified. Moreover, the query cache is only available when a query does not have a destination table specified.
The default value is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userDefinedFunctionResources</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Describes user-defined function resources used in the query.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">inlineCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An inline resource that contains code for a user-defined function (UDF).
Providing a inline code resource is equivalent to providing a URI for a file containing the same code.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A code resource to load from a Google Cloud Storage URI (gs://bucket/path).</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">writeDisposition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the action that occurs if the destination table already exists. The following values are supported:
WRITE_TRUNCATE: If the table already exists, BigQuery overwrites the table data and uses the schema from the query result.
WRITE_APPEND: If the table already exists, BigQuery appends the data to the table.
WRITE_EMPTY: If the table already exists and contains data, a ‘duplicate’ error is returned in the job result.
The default value is WRITE_EMPTY. Each action is atomic and only occurs if BigQuery is able to complete the job successfully.
Creation, truncation and append actions occur as one atomic update upon job completion.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Job.copy">
<code class="sig-name descname">copy</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Job.copy" title="Permalink to this definition">¶</a></dt>
<dd><p>Copies a table.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">createDisposition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies whether the job is allowed to create new tables. The following values are supported:
CREATE_IF_NEEDED: If the table does not exist, BigQuery creates the table.
CREATE_NEVER: The table must already exist. If it does not, a ‘notFound’ error is returned in the job result.
The default value is CREATE_IF_NEEDED. Creation, truncation and append actions occur as one atomic update upon job completion</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationEncryptionConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Custom encryption configuration (e.g., Cloud KMS keys)  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table.
The BigQuery Service Account associated with your project requires access to this encryption key.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationTable</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The destination table.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the dataset containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the project containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the table.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceTables</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Source tables to copy.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the dataset containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the project containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the table.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">writeDisposition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the action that occurs if the destination table already exists. The following values are supported:
WRITE_TRUNCATE: If the table already exists, BigQuery overwrites the table data and uses the schema from the query result.
WRITE_APPEND: If the table already exists, BigQuery appends the data to the table.
WRITE_EMPTY: If the table already exists and contains data, a ‘duplicate’ error is returned in the job result.
The default value is WRITE_EMPTY. Each action is atomic and only occurs if BigQuery is able to complete the job successfully.
Creation, truncation and append actions occur as one atomic update upon job completion.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Job.extract">
<code class="sig-name descname">extract</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Job.extract" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures an extract job.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">compression</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The compression type to use for exported files. Possible values include GZIP, DEFLATE, SNAPPY, and NONE.
The default value is NONE. DEFLATE and SNAPPY are only supported for Avro.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The exported file format. Possible values include CSV, NEWLINE_DELIMITED_JSON and AVRO for tables and SAVED_MODEL for models.
The default value for tables is CSV. Tables with nested or repeated fields cannot be exported as CSV.
The default value for models is SAVED_MODEL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationUris</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of fully-qualified Google Cloud Storage URIs where the extracted table should be written.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - When extracting data in CSV format, this defines the delimiter to use between fields in the exported data.
Default is ‘,’</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">printHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to print out a header row in the results. Default is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceModel</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A reference to the model being exported.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the dataset containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">modelId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the project containing this model.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceTable</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A reference to the table being exported.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the dataset containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the project containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the table.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">useAvroLogicalTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to use logical types when extracting to AVRO format.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Job.job_id">
<code class="sig-name descname">job_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Job.job_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the job. The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). The maximum length is 1,024 characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Job.job_timeout_ms">
<code class="sig-name descname">job_timeout_ms</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Job.job_timeout_ms" title="Permalink to this definition">¶</a></dt>
<dd><p>Job timeout in milliseconds. If this time limit is exceeded, BigQuery may attempt to terminate the job.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Job.job_type">
<code class="sig-name descname">job_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Job.job_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the job.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Job.labels">
<code class="sig-name descname">labels</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Job.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>The labels associated with this job. You can use these to organize and group your jobs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Job.load">
<code class="sig-name descname">load</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Job.load" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures a load job.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowJaggedRows</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Accept rows that are missing trailing optional columns. The missing values are treated as nulls.
If false, records with missing trailing columns are treated as bad records, and if there are too many bad records,
an invalid error is returned in the job result. The default value is false. Only applicable to CSV, ignored for other formats.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowQuotedNewlines</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates if BigQuery should allow quoted data sections that contain newline characters in a CSV file.
The default value is false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autodetect</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates if we should automatically infer the options and schema for CSV and JSON sources.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">createDisposition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies whether the job is allowed to create new tables. The following values are supported:
CREATE_IF_NEEDED: If the table does not exist, BigQuery creates the table.
CREATE_NEVER: The table must already exist. If it does not, a ‘notFound’ error is returned in the job result.
The default value is CREATE_IF_NEEDED. Creation, truncation and append actions occur as one atomic update upon job completion</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationEncryptionConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Custom encryption configuration (e.g., Cloud KMS keys)  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table.
The BigQuery Service Account associated with your project requires access to this encryption key.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationTable</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The destination table.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the dataset containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the project containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the table.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The character encoding of the data. The supported values are UTF-8 or ISO-8859-1.
The default value is UTF-8. BigQuery decodes the data after the raw, binary data
has been split using the values of the quote and fieldDelimiter properties.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - When extracting data in CSV format, this defines the delimiter to use between fields in the exported data.
Default is ‘,’</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ignoreUnknownValues</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates if BigQuery should allow extra values that are not represented in the table schema.
If true, the extra values are ignored. If false, records with extra columns are treated as bad records,
and if there are too many bad records, an invalid error is returned in the job result.
The default value is false. The sourceFormat property determines what BigQuery treats as an extra value:
CSV: Trailing columns
JSON: Named values that don’t match any column names</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxBadRecords</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of bad records that BigQuery can ignore when running the job. If the number of bad records exceeds this value,
an invalid error is returned in the job result. The default value is 0, which requires that all records are valid.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nullMarker</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies a string that represents a null value in a CSV file. The default value is the empty string. If you set this
property to a custom value, BigQuery throws an error if an
empty string is present for all data types except for STRING and BYTE. For STRING and BYTE columns, BigQuery interprets the empty string as
an empty value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectionFields</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - If sourceFormat is set to “DATASTORE_BACKUP”, indicates which entity properties to load into BigQuery from a Cloud Datastore backup.
Property names are case sensitive and must be top-level properties. If no properties are specified, BigQuery loads all properties.
If any named property isn’t found in the Cloud Datastore backup, an invalid error is returned in the job result.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">quote</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value that is used to quote data sections in a CSV file. BigQuery converts the string to ISO-8859-1 encoding,
and then uses the first byte of the encoded string to split the data in its raw, binary state.
The default value is a double-quote (‘”’). If your data does not contain quoted sections, set the property value to an empty string.
If your data contains quoted newline characters, you must also set the allowQuotedNewlines property to true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemaUpdateOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Allows the schema of the destination table to be updated as a side effect of the load job if a schema is autodetected or
supplied in the job configuration. Schema update options are supported in two cases: when writeDisposition is WRITE_APPEND;
when writeDisposition is WRITE_TRUNCATE and the destination table is a partition of a table, specified by partition decorators.
For normal tables, WRITE_TRUNCATE will always overwrite the schema. One or more of the following values are specified:
ALLOW_FIELD_ADDITION: allow adding a nullable field to the schema.
ALLOW_FIELD_RELAXATION: allow relaxing a required field in the original schema to nullable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">skipLeadingRows</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of rows at the top of a CSV file that BigQuery will skip when loading the data.
The default value is 0. This property is useful if you have header rows in the file that should be skipped.
When autodetect is on, the behavior is the following:
skipLeadingRows unspecified - Autodetect tries to detect headers in the first row. If they are not detected,
the row is read as data. Otherwise data is read starting from the second row.
skipLeadingRows is 0 - Instructs autodetect that there are no headers and data should be read starting from the first row.
skipLeadingRows = N &gt; 0 - Autodetect skips N-1 rows and tries to detect headers in row N. If headers are not detected,
row N is just skipped. Otherwise row N is used to extract column names for the detected schema.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The format of the data files. For CSV files, specify “CSV”. For datastore backups, specify “DATASTORE_BACKUP”.
For newline-delimited JSON, specify “NEWLINE_DELIMITED_JSON”. For Avro, specify “AVRO”. For parquet, specify “PARQUET”.
For orc, specify “ORC”. The default value is CSV.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceUris</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The fully-qualified URIs that point to your data in Google Cloud.
For Google Cloud Storage URIs: Each URI can contain one ‘<em>’ wildcard character
and it must come after the ‘bucket’ name. Size limits related to load jobs apply
to external data sources. For Google Cloud Bigtable URIs: Exactly one URI can be
specified and it has be a fully specified and valid HTTPS URL for a Google Cloud Bigtable table.
For Google Cloud Datastore backups: Exactly one URI can be specified. Also, the ‘</em>’ wildcard character is not allowed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">time_partitioning</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Time-based partitioning specification for the destination table.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">expirationMs</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Number of milliseconds for which to keep the storage for a partition. A wrapper is used here because 0 is an invalid value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">field</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - If not set, the table is partitioned by pseudo column ‘_PARTITIONTIME’; if set, the table is partitioned by this field.
The field must be a top-level TIMESTAMP or DATE field. Its mode must be NULLABLE or REQUIRED.
A wrapper is used here because an empty string is an invalid value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The only type supported is DAY, which will generate one partition per day. Providing an empty string used to cause an error,
but in OnePlatform the field will be treated as unset.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">writeDisposition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the action that occurs if the destination table already exists. The following values are supported:
WRITE_TRUNCATE: If the table already exists, BigQuery overwrites the table data and uses the schema from the query result.
WRITE_APPEND: If the table already exists, BigQuery appends the data to the table.
WRITE_EMPTY: If the table already exists and contains data, a ‘duplicate’ error is returned in the job result.
The default value is WRITE_EMPTY. Each action is atomic and only occurs if BigQuery is able to complete the job successfully.
Creation, truncation and append actions occur as one atomic update upon job completion.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Job.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Job.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The geographic location of the job. The default value is US.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Job.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Job.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Job.query">
<code class="sig-name descname">query</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Job.query" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures a query job.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowLargeResults</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If true and query uses legacy SQL dialect, allows the query to produce arbitrarily large result tables at a slight cost in performance.
Requires destinationTable to be set. For standard SQL queries, this flag is ignored and large results are always allowed.
However, you must still set destinationTable when result size exceeds the allowed maximum response size.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">createDisposition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies whether the job is allowed to create new tables. The following values are supported:
CREATE_IF_NEEDED: If the table does not exist, BigQuery creates the table.
CREATE_NEVER: The table must already exist. If it does not, a ‘notFound’ error is returned in the job result.
The default value is CREATE_IF_NEEDED. Creation, truncation and append actions occur as one atomic update upon job completion</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultDataset</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Specifies the default dataset to use for unqualified table names in the query. Note that this does not alter behavior of unqualified dataset names.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the dataset containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the project containing this model.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationEncryptionConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Custom encryption configuration (e.g., Cloud KMS keys)  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table.
The BigQuery Service Account associated with your project requires access to this encryption key.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationTable</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The destination table.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the dataset containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the project containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the table.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">flattenResults</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If true and query uses legacy SQL dialect, flattens all nested and repeated fields in the query results.
allowLargeResults must be true if this is set to false. For standard SQL queries, this flag is ignored and results are never flattened.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximumBillingTier</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Limits the billing tier for this job. Queries that have resource usage beyond this tier will fail (without incurring a charge).
If unspecified, this will be set to your project default.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximumBytesBilled</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Limits the bytes billed for this job. Queries that will have bytes billed beyond this limit will fail (without incurring a charge).
If unspecified, this will be set to your project default.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Standard SQL only. Set to POSITIONAL to use positional (?) query parameters or to NAMED to use named (&#64;myparam) query parameters in this query.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies a priority for the query. Possible values include INTERACTIVE and BATCH. The default value is INTERACTIVE.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Configures a query job.  Structure is documented below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemaUpdateOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Allows the schema of the destination table to be updated as a side effect of the load job if a schema is autodetected or
supplied in the job configuration. Schema update options are supported in two cases: when writeDisposition is WRITE_APPEND;
when writeDisposition is WRITE_TRUNCATE and the destination table is a partition of a table, specified by partition decorators.
For normal tables, WRITE_TRUNCATE will always overwrite the schema. One or more of the following values are specified:
ALLOW_FIELD_ADDITION: allow adding a nullable field to the schema.
ALLOW_FIELD_RELAXATION: allow relaxing a required field in the original schema to nullable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scriptOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Options controlling the execution of scripts.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">keyResultStatement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Determines which statement in the script represents the “key result”,
used to populate the schema and query results of the script job. Default is LAST.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statementByteBudget</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Limit on the number of bytes billed per statement. Exceeding this budget results in an error.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statementTimeoutMs</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Timeout period for each statement in a script.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">useLegacySql</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether to use BigQuery’s legacy SQL dialect for this query. The default value is true.
If set to false, the query will use BigQuery’s standard SQL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useQueryCache</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to look for the result in the query cache. The query cache is a best-effort cache that will be flushed whenever
tables in the query are modified. Moreover, the query cache is only available when a query does not have a destination table specified.
The default value is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userDefinedFunctionResources</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Describes user-defined function resources used in the query.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">inlineCode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An inline resource that contains code for a user-defined function (UDF).
Providing a inline code resource is equivalent to providing a URI for a file containing the same code.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A code resource to load from a Google Cloud Storage URI (gs://bucket/path).</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">writeDisposition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the action that occurs if the destination table already exists. The following values are supported:
WRITE_TRUNCATE: If the table already exists, BigQuery overwrites the table data and uses the schema from the query result.
WRITE_APPEND: If the table already exists, BigQuery appends the data to the table.
WRITE_EMPTY: If the table already exists and contains data, a ‘duplicate’ error is returned in the job result.
The default value is WRITE_EMPTY. Each action is atomic and only occurs if BigQuery is able to complete the job successfully.
Creation, truncation and append actions occur as one atomic update upon job completion.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Job.user_email">
<code class="sig-name descname">user_email</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Job.user_email" title="Permalink to this definition">¶</a></dt>
<dd><p>Email address of the user who ran the job.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.bigquery.Job.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">copy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extract</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">job_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">job_timeout_ms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">job_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_email</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Job.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Job resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>copy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Copies a table.  Structure is documented below.</p></li>
<li><p><strong>extract</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures an extract job.  Structure is documented below.</p></li>
<li><p><strong>job*id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The ID of the job. The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (<a href="#id17"><span class="problematic" id="id18">*</span></a>), or dashes (-). The maximum length is 1,024 characters.</p>
</p></li>
<li><p><strong>job_timeout_ms</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Job timeout in milliseconds. If this time limit is exceeded, BigQuery may attempt to terminate the job.</p></li>
<li><p><strong>job_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the job.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The labels associated with this job. You can use these to organize and group your jobs.</p></li>
<li><p><strong>load</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures a load job.  Structure is documented below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The geographic location of the job. The default value is US.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures a query job.  Structure is documented below.</p></li>
<li><p><strong>user_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email address of the user who ran the job.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>copy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">createDisposition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies whether the job is allowed to create new tables. The following values are supported:
CREATE_IF_NEEDED: If the table does not exist, BigQuery creates the table.
CREATE_NEVER: The table must already exist. If it does not, a ‘notFound’ error is returned in the job result.
The default value is CREATE_IF_NEEDED. Creation, truncation and append actions occur as one atomic update upon job completion</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationEncryptionConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Custom encryption configuration (e.g., Cloud KMS keys)  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table.
The BigQuery Service Account associated with your project requires access to this encryption key.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationTable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The destination table.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the dataset containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the project containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the table.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceTables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Source tables to copy.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the dataset containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the project containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the table.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">writeDisposition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the action that occurs if the destination table already exists. The following values are supported:
WRITE_TRUNCATE: If the table already exists, BigQuery overwrites the table data and uses the schema from the query result.
WRITE_APPEND: If the table already exists, BigQuery appends the data to the table.
WRITE_EMPTY: If the table already exists and contains data, a ‘duplicate’ error is returned in the job result.
The default value is WRITE_EMPTY. Each action is atomic and only occurs if BigQuery is able to complete the job successfully.
Creation, truncation and append actions occur as one atomic update upon job completion.</p></li>
</ul>
<p>The <strong>extract</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">compression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The compression type to use for exported files. Possible values include GZIP, DEFLATE, SNAPPY, and NONE.
The default value is NONE. DEFLATE and SNAPPY are only supported for Avro.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The exported file format. Possible values include CSV, NEWLINE_DELIMITED_JSON and AVRO for tables and SAVED_MODEL for models.
The default value for tables is CSV. Tables with nested or repeated fields cannot be exported as CSV.
The default value for models is SAVED_MODEL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of fully-qualified Google Cloud Storage URIs where the extracted table should be written.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When extracting data in CSV format, this defines the delimiter to use between fields in the exported data.
Default is ‘,’</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">printHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to print out a header row in the results. Default is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceModel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A reference to the model being exported.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the dataset containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">modelId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the project containing this model.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceTable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A reference to the table being exported.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the dataset containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the project containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the table.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">useAvroLogicalTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use logical types when extracting to AVRO format.</p></li>
</ul>
<p>The <strong>load</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowJaggedRows</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Accept rows that are missing trailing optional columns. The missing values are treated as nulls.
If false, records with missing trailing columns are treated as bad records, and if there are too many bad records,
an invalid error is returned in the job result. The default value is false. Only applicable to CSV, ignored for other formats.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowQuotedNewlines</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates if BigQuery should allow quoted data sections that contain newline characters in a CSV file.
The default value is false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autodetect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates if we should automatically infer the options and schema for CSV and JSON sources.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">createDisposition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies whether the job is allowed to create new tables. The following values are supported:
CREATE_IF_NEEDED: If the table does not exist, BigQuery creates the table.
CREATE_NEVER: The table must already exist. If it does not, a ‘notFound’ error is returned in the job result.
The default value is CREATE_IF_NEEDED. Creation, truncation and append actions occur as one atomic update upon job completion</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationEncryptionConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Custom encryption configuration (e.g., Cloud KMS keys)  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table.
The BigQuery Service Account associated with your project requires access to this encryption key.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationTable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The destination table.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the dataset containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the project containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the table.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The character encoding of the data. The supported values are UTF-8 or ISO-8859-1.
The default value is UTF-8. BigQuery decodes the data after the raw, binary data
has been split using the values of the quote and fieldDelimiter properties.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When extracting data in CSV format, this defines the delimiter to use between fields in the exported data.
Default is ‘,’</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ignoreUnknownValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates if BigQuery should allow extra values that are not represented in the table schema.
If true, the extra values are ignored. If false, records with extra columns are treated as bad records,
and if there are too many bad records, an invalid error is returned in the job result.
The default value is false. The sourceFormat property determines what BigQuery treats as an extra value:
CSV: Trailing columns
JSON: Named values that don’t match any column names</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxBadRecords</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of bad records that BigQuery can ignore when running the job. If the number of bad records exceeds this value,
an invalid error is returned in the job result. The default value is 0, which requires that all records are valid.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nullMarker</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies a string that represents a null value in a CSV file. The default value is the empty string. If you set this
property to a custom value, BigQuery throws an error if an
empty string is present for all data types except for STRING and BYTE. For STRING and BYTE columns, BigQuery interprets the empty string as
an empty value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectionFields</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - If sourceFormat is set to “DATASTORE_BACKUP”, indicates which entity properties to load into BigQuery from a Cloud Datastore backup.
Property names are case sensitive and must be top-level properties. If no properties are specified, BigQuery loads all properties.
If any named property isn’t found in the Cloud Datastore backup, an invalid error is returned in the job result.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">quote</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value that is used to quote data sections in a CSV file. BigQuery converts the string to ISO-8859-1 encoding,
and then uses the first byte of the encoded string to split the data in its raw, binary state.
The default value is a double-quote (‘”’). If your data does not contain quoted sections, set the property value to an empty string.
If your data contains quoted newline characters, you must also set the allowQuotedNewlines property to true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemaUpdateOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Allows the schema of the destination table to be updated as a side effect of the load job if a schema is autodetected or
supplied in the job configuration. Schema update options are supported in two cases: when writeDisposition is WRITE_APPEND;
when writeDisposition is WRITE_TRUNCATE and the destination table is a partition of a table, specified by partition decorators.
For normal tables, WRITE_TRUNCATE will always overwrite the schema. One or more of the following values are specified:
ALLOW_FIELD_ADDITION: allow adding a nullable field to the schema.
ALLOW_FIELD_RELAXATION: allow relaxing a required field in the original schema to nullable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">skipLeadingRows</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of rows at the top of a CSV file that BigQuery will skip when loading the data.
The default value is 0. This property is useful if you have header rows in the file that should be skipped.
When autodetect is on, the behavior is the following:
skipLeadingRows unspecified - Autodetect tries to detect headers in the first row. If they are not detected,
the row is read as data. Otherwise data is read starting from the second row.
skipLeadingRows is 0 - Instructs autodetect that there are no headers and data should be read starting from the first row.
skipLeadingRows = N &gt; 0 - Autodetect skips N-1 rows and tries to detect headers in row N. If headers are not detected,
row N is just skipped. Otherwise row N is used to extract column names for the detected schema.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The format of the data files. For CSV files, specify “CSV”. For datastore backups, specify “DATASTORE_BACKUP”.
For newline-delimited JSON, specify “NEWLINE_DELIMITED_JSON”. For Avro, specify “AVRO”. For parquet, specify “PARQUET”.
For orc, specify “ORC”. The default value is CSV.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The fully-qualified URIs that point to your data in Google Cloud.
For Google Cloud Storage URIs: Each URI can contain one ‘<em>’ wildcard character
and it must come after the ‘bucket’ name. Size limits related to load jobs apply
to external data sources. For Google Cloud Bigtable URIs: Exactly one URI can be
specified and it has be a fully specified and valid HTTPS URL for a Google Cloud Bigtable table.
For Google Cloud Datastore backups: Exactly one URI can be specified. Also, the ‘</em>’ wildcard character is not allowed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">time_partitioning</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Time-based partitioning specification for the destination table.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">expirationMs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Number of milliseconds for which to keep the storage for a partition. A wrapper is used here because 0 is an invalid value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">field</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If not set, the table is partitioned by pseudo column ‘_PARTITIONTIME’; if set, the table is partitioned by this field.
The field must be a top-level TIMESTAMP or DATE field. Its mode must be NULLABLE or REQUIRED.
A wrapper is used here because an empty string is an invalid value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The only type supported is DAY, which will generate one partition per day. Providing an empty string used to cause an error,
but in OnePlatform the field will be treated as unset.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">writeDisposition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the action that occurs if the destination table already exists. The following values are supported:
WRITE_TRUNCATE: If the table already exists, BigQuery overwrites the table data and uses the schema from the query result.
WRITE_APPEND: If the table already exists, BigQuery appends the data to the table.
WRITE_EMPTY: If the table already exists and contains data, a ‘duplicate’ error is returned in the job result.
The default value is WRITE_EMPTY. Each action is atomic and only occurs if BigQuery is able to complete the job successfully.
Creation, truncation and append actions occur as one atomic update upon job completion.</p></li>
</ul>
<p>The <strong>query</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowLargeResults</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If true and query uses legacy SQL dialect, allows the query to produce arbitrarily large result tables at a slight cost in performance.
Requires destinationTable to be set. For standard SQL queries, this flag is ignored and large results are always allowed.
However, you must still set destinationTable when result size exceeds the allowed maximum response size.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">createDisposition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies whether the job is allowed to create new tables. The following values are supported:
CREATE_IF_NEEDED: If the table does not exist, BigQuery creates the table.
CREATE_NEVER: The table must already exist. If it does not, a ‘notFound’ error is returned in the job result.
The default value is CREATE_IF_NEEDED. Creation, truncation and append actions occur as one atomic update upon job completion</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultDataset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies the default dataset to use for unqualified table names in the query. Note that this does not alter behavior of unqualified dataset names.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the dataset containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the project containing this model.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationEncryptionConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Custom encryption configuration (e.g., Cloud KMS keys)  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table.
The BigQuery Service Account associated with your project requires access to this encryption key.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationTable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The destination table.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the dataset containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the project containing this model.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the table.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">flattenResults</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If true and query uses legacy SQL dialect, flattens all nested and repeated fields in the query results.
allowLargeResults must be true if this is set to false. For standard SQL queries, this flag is ignored and results are never flattened.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximumBillingTier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Limits the billing tier for this job. Queries that have resource usage beyond this tier will fail (without incurring a charge).
If unspecified, this will be set to your project default.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximumBytesBilled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Limits the bytes billed for this job. Queries that will have bytes billed beyond this limit will fail (without incurring a charge).
If unspecified, this will be set to your project default.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Standard SQL only. Set to POSITIONAL to use positional (?) query parameters or to NAMED to use named (&#64;myparam) query parameters in this query.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies a priority for the query. Possible values include INTERACTIVE and BATCH. The default value is INTERACTIVE.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Configures a query job.  Structure is documented below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemaUpdateOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Allows the schema of the destination table to be updated as a side effect of the load job if a schema is autodetected or
supplied in the job configuration. Schema update options are supported in two cases: when writeDisposition is WRITE_APPEND;
when writeDisposition is WRITE_TRUNCATE and the destination table is a partition of a table, specified by partition decorators.
For normal tables, WRITE_TRUNCATE will always overwrite the schema. One or more of the following values are specified:
ALLOW_FIELD_ADDITION: allow adding a nullable field to the schema.
ALLOW_FIELD_RELAXATION: allow relaxing a required field in the original schema to nullable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scriptOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Options controlling the execution of scripts.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">keyResultStatement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Determines which statement in the script represents the “key result”,
used to populate the schema and query results of the script job. Default is LAST.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statementByteBudget</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Limit on the number of bytes billed per statement. Exceeding this budget results in an error.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statementTimeoutMs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Timeout period for each statement in a script.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">useLegacySql</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether to use BigQuery’s legacy SQL dialect for this query. The default value is true.
If set to false, the query will use BigQuery’s standard SQL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useQueryCache</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to look for the result in the query cache. The query cache is a best-effort cache that will be flushed whenever
tables in the query are modified. Moreover, the query cache is only available when a query does not have a destination table specified.
The default value is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userDefinedFunctionResources</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Describes user-defined function resources used in the query.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">inlineCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An inline resource that contains code for a user-defined function (UDF).
Providing a inline code resource is equivalent to providing a URI for a file containing the same code.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A code resource to load from a Google Cloud Storage URI (gs://bucket/path).</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">writeDisposition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the action that occurs if the destination table already exists. The following values are supported:
WRITE_TRUNCATE: If the table already exists, BigQuery overwrites the table data and uses the schema from the query result.
WRITE_APPEND: If the table already exists, BigQuery appends the data to the table.
WRITE_EMPTY: If the table already exists and contains data, a ‘duplicate’ error is returned in the job result.
The default value is WRITE_EMPTY. Each action is atomic and only occurs if BigQuery is able to complete the job successfully.
Creation, truncation and append actions occur as one atomic update upon job completion.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.bigquery.Job.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Job.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigquery.Job.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Job.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigquery.Reservation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.bigquery.</code><code class="sig-name descname">Reservation</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_idle_slots</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slot_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Reservation" title="Permalink to this definition">¶</a></dt>
<dd><p>A reservation is a mechanism used to guarantee BigQuery slots to users.</p>
<p>To get more information about Reservation, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/bigquery/docs/reference/reservations/rest/v1beta1/projects.locations.reservations/create">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/bigquery/docs/reservations-intro">Introduction to Reservations</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ignore_idle_slots</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If false, any query using this reservation will use idle slots from other reservations within
the same admin project. If true, a query using this reservation will execute with the slot
capacity specified above at most.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The geographic location where the transfer config should reside.
Examples: US, EU, asia-northeast1. The default value is US.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the reservation. This field must only contain alphanumeric characters or dash.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>slot_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum slots available to this reservation. A slot is a unit of computational power in BigQuery, and serves as the
unit of parallelism. Queries using this reservation might use more slots during runtime if ignoreIdleSlots is set to false.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Reservation.ignore_idle_slots">
<code class="sig-name descname">ignore_idle_slots</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Reservation.ignore_idle_slots" title="Permalink to this definition">¶</a></dt>
<dd><p>If false, any query using this reservation will use idle slots from other reservations within
the same admin project. If true, a query using this reservation will execute with the slot
capacity specified above at most.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Reservation.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Reservation.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The geographic location where the transfer config should reside.
Examples: US, EU, asia-northeast1. The default value is US.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Reservation.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Reservation.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the reservation. This field must only contain alphanumeric characters or dash.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Reservation.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Reservation.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Reservation.slot_capacity">
<code class="sig-name descname">slot_capacity</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Reservation.slot_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>Minimum slots available to this reservation. A slot is a unit of computational power in BigQuery, and serves as the
unit of parallelism. Queries using this reservation might use more slots during runtime if ignoreIdleSlots is set to false.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.bigquery.Reservation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_idle_slots</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slot_capacity</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Reservation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Reservation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ignore_idle_slots</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If false, any query using this reservation will use idle slots from other reservations within
the same admin project. If true, a query using this reservation will execute with the slot
capacity specified above at most.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The geographic location where the transfer config should reside.
Examples: US, EU, asia-northeast1. The default value is US.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the reservation. This field must only contain alphanumeric characters or dash.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>slot_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum slots available to this reservation. A slot is a unit of computational power in BigQuery, and serves as the
unit of parallelism. Queries using this reservation might use more slots during runtime if ignoreIdleSlots is set to false.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.bigquery.Reservation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Reservation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigquery.Reservation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Reservation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigquery.Table">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.bigquery.</code><code class="sig-name descname">Table</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">clusterings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dataset_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiration_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_data_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">friendly_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">range_partitioning</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">table_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_partitioning</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">view</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Table" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a table resource in a dataset for Google BigQuery. For more information see
<a class="reference external" href="https://cloud.google.com/bigquery/docs/">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/bigquery/docs/reference/rest/v2/tables">API</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>clusterings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies column names to use for data clustering.
Up to four top-level columns are allowed, and should be specified in
descending priority order.</p></li>
<li><p><strong>dataset_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The dataset ID to create the table in.
Changing this forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The field description.</p></li>
<li><p><strong>encryption_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies how the table should be encrypted.
If left blank, the table will be encrypted with a Google-managed key; that process
is transparent to the user.  Structure is documented below.</p></li>
<li><p><strong>expiration_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time when this table expires, in
milliseconds since the epoch. If not present, the table will persist
indefinitely. Expired tables will be deleted and their storage
reclaimed.</p></li>
<li><p><strong>external_data_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Describes the data format,
location, and other properties of a table stored outside of BigQuery.
By defining these properties, the data source can then be queried as
if it were a standard BigQuery table. Structure is documented below.</p></li>
<li><p><strong>friendly_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A descriptive name for the table.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of labels to assign to the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>range_partitioning</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – If specified, configures range-based
partitioning for this table. Structure is documented below.</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON schema for the table. Schema is required
for CSV and JSON formats and is disallowed for Google Cloud
Bigtable, Cloud Datastore backups, and Avro formats when using
external tables. For more information see the
<a class="reference external" href="https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#resource">BigQuery API documentation</a>.
~&gt;<strong>NOTE</strong>: Because this field expects a JSON string, any changes to the
string will create a diff, even if the JSON itself hasn’t changed.
If the API returns a different value for the same schema, e.g. it
switched the order of values or replaced <code class="docutils literal notranslate"><span class="pre">STRUCT</span></code> field type with <code class="docutils literal notranslate"><span class="pre">RECORD</span></code>
field type, we currently cannot suppress the recurring diff this causes.
As a workaround, we recommend using the schema as returned by the API.</p></li>
<li><p><strong>table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique ID for the resource.
Changing this forces a new resource to be created.</p></li>
<li><p><strong>time_partitioning</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – If specified, configures time-based
partitioning for this table. Structure is documented below.</p></li>
<li><p><strong>view</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – If specified, configures this table as a view.
Structure is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>encryption_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The self link or full name of a key which should be used to
encrypt this table.  Note that the default bigquery service account will need to have
encrypt/decrypt permissions on this key - you may want to see the
<code class="docutils literal notranslate"><span class="pre">bigquery.getDefaultServiceAccount</span></code> datasource and the
<code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMBinding</span></code> resource.</p></li>
</ul>
<p>The <strong>external_data_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autodetect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - - Let BigQuery try to autodetect the schema
and format of the table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The compression type of the data source.
Valid values are “NONE” or “GZIP”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">csvOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Additional properties to set if
<code class="docutils literal notranslate"><span class="pre">source_format</span></code> is set to “CSV”. Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowJaggedRows</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates if BigQuery should accept rows
that are missing trailing optional columns.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowQuotedNewlines</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates if BigQuery should allow
quoted data sections that contain newline characters in a CSV file.
The default value is false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The character encoding of the data. The supported
values are UTF-8 or ISO-8859-1.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The separator for fields in a CSV file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">quote</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value that is used to quote data sections in a
CSV file. If your data does not contain quoted sections, set the
property value to an empty string. If your data contains quoted newline
characters, you must also set the <code class="docutils literal notranslate"><span class="pre">allow_quoted_newlines</span></code> property to true.
The API-side default is <code class="docutils literal notranslate"><span class="pre">&quot;</span></code>, specified in the provider escaped as <code class="docutils literal notranslate"><span class="pre">&quot;</span></code>. Due to
limitations with default values, this value is required to be
explicitly set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">skipLeadingRows</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of rows at the top of the sheet
that BigQuery will skip when reading the data. At least one of <code class="docutils literal notranslate"><span class="pre">range</span></code> or
<code class="docutils literal notranslate"><span class="pre">skip_leading_rows</span></code> must be set.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">googleSheetsOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Additional options if
<code class="docutils literal notranslate"><span class="pre">source_format</span></code> is set to “GOOGLE_SHEETS”. Structure is
documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">range</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Information required to partition based on ranges.
Structure is documented below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">skipLeadingRows</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of rows at the top of the sheet
that BigQuery will skip when reading the data. At least one of <code class="docutils literal notranslate"><span class="pre">range</span></code> or
<code class="docutils literal notranslate"><span class="pre">skip_leading_rows</span></code> must be set.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ignoreUnknownValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates if BigQuery should
allow extra values that are not represented in the table schema.
If true, the extra values are ignored. If false, records with
extra columns are treated as bad records, and if there are too
many bad records, an invalid error is returned in the job result.
The default value is false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxBadRecords</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of bad records that
BigQuery can ignore when reading data.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data format. Supported values are:
“CSV”, “GOOGLE_SHEETS”, “NEWLINE_DELIMITED_JSON”, “AVRO”, “PARQUET”,
and “DATSTORE_BACKUP”. To use “GOOGLE_SHEETS”
the <code class="docutils literal notranslate"><span class="pre">scopes</span></code> must include
“<a class="reference external" href="https://www.googleapis.com/auth/drive.readonly">https://www.googleapis.com/auth/drive.readonly</a>”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of the fully-qualified URIs that point to
your data in Google Cloud.</p></li>
</ul>
<p>The <strong>range_partitioning</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">field</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The field used to determine how to create a range-based
partition.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">range</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information required to partition based on ranges.
Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">end</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - End of the range partitioning, exclusive.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The width of each range within the partition.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Start of the range partitioning, inclusive.</p></li>
</ul>
</li>
</ul>
<p>The <strong>time_partitioning</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">expirationMs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of milliseconds for which to keep the
storage for a partition.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">field</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The field used to determine how to create a range-based
partition.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requirePartitionFilter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If set to true, queries over this table
require a partition filter that can be used for partition elimination to be
specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The only type supported is DAY, which will generate
one partition per day based on data loading time.</p></li>
</ul>
<p>The <strong>view</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A query that BigQuery executes when the view is referenced.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useLegacySql</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether to use BigQuery’s legacy SQL for this view.
The default value is true. If set to false, the view will use BigQuery’s standard SQL.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Table.clusterings">
<code class="sig-name descname">clusterings</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.clusterings" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies column names to use for data clustering.
Up to four top-level columns are allowed, and should be specified in
descending priority order.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Table.creation_time">
<code class="sig-name descname">creation_time</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.creation_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when this table was created, in milliseconds since the epoch.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Table.dataset_id">
<code class="sig-name descname">dataset_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.dataset_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The dataset ID to create the table in.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Table.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The field description.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Table.encryption_configuration">
<code class="sig-name descname">encryption_configuration</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.encryption_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies how the table should be encrypted.
If left blank, the table will be encrypted with a Google-managed key; that process
is transparent to the user.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The self link or full name of a key which should be used to
encrypt this table.  Note that the default bigquery service account will need to have
encrypt/decrypt permissions on this key - you may want to see the
<code class="docutils literal notranslate"><span class="pre">bigquery.getDefaultServiceAccount</span></code> datasource and the
<code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMBinding</span></code> resource.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Table.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>A hash of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Table.expiration_time">
<code class="sig-name descname">expiration_time</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.expiration_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when this table expires, in
milliseconds since the epoch. If not present, the table will persist
indefinitely. Expired tables will be deleted and their storage
reclaimed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Table.external_data_configuration">
<code class="sig-name descname">external_data_configuration</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.external_data_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes the data format,
location, and other properties of a table stored outside of BigQuery.
By defining these properties, the data source can then be queried as
if it were a standard BigQuery table. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autodetect</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - - Let BigQuery try to autodetect the schema
and format of the table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compression</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The compression type of the data source.
Valid values are “NONE” or “GZIP”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">csvOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Additional properties to set if
<code class="docutils literal notranslate"><span class="pre">source_format</span></code> is set to “CSV”. Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowJaggedRows</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates if BigQuery should accept rows
that are missing trailing optional columns.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowQuotedNewlines</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates if BigQuery should allow
quoted data sections that contain newline characters in a CSV file.
The default value is false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The character encoding of the data. The supported
values are UTF-8 or ISO-8859-1.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The separator for fields in a CSV file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">quote</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value that is used to quote data sections in a
CSV file. If your data does not contain quoted sections, set the
property value to an empty string. If your data contains quoted newline
characters, you must also set the <code class="docutils literal notranslate"><span class="pre">allow_quoted_newlines</span></code> property to true.
The API-side default is <code class="docutils literal notranslate"><span class="pre">&quot;</span></code>, specified in the provider escaped as <code class="docutils literal notranslate"><span class="pre">&quot;</span></code>. Due to
limitations with default values, this value is required to be
explicitly set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">skipLeadingRows</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of rows at the top of the sheet
that BigQuery will skip when reading the data. At least one of <code class="docutils literal notranslate"><span class="pre">range</span></code> or
<code class="docutils literal notranslate"><span class="pre">skip_leading_rows</span></code> must be set.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">googleSheetsOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Additional options if
<code class="docutils literal notranslate"><span class="pre">source_format</span></code> is set to “GOOGLE_SHEETS”. Structure is
documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">range</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Information required to partition based on ranges.
Structure is documented below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">skipLeadingRows</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of rows at the top of the sheet
that BigQuery will skip when reading the data. At least one of <code class="docutils literal notranslate"><span class="pre">range</span></code> or
<code class="docutils literal notranslate"><span class="pre">skip_leading_rows</span></code> must be set.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ignoreUnknownValues</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates if BigQuery should
allow extra values that are not represented in the table schema.
If true, the extra values are ignored. If false, records with
extra columns are treated as bad records, and if there are too
many bad records, an invalid error is returned in the job result.
The default value is false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxBadRecords</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of bad records that
BigQuery can ignore when reading data.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The data format. Supported values are:
“CSV”, “GOOGLE_SHEETS”, “NEWLINE_DELIMITED_JSON”, “AVRO”, “PARQUET”,
and “DATSTORE_BACKUP”. To use “GOOGLE_SHEETS”
the <code class="docutils literal notranslate"><span class="pre">scopes</span></code> must include
“<a class="reference external" href="https://www.googleapis.com/auth/drive.readonly">https://www.googleapis.com/auth/drive.readonly</a>”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceUris</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of the fully-qualified URIs that point to
your data in Google Cloud.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Table.friendly_name">
<code class="sig-name descname">friendly_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.friendly_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A descriptive name for the table.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Table.labels">
<code class="sig-name descname">labels</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of labels to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Table.last_modified_time">
<code class="sig-name descname">last_modified_time</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.last_modified_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when this table was last modified, in milliseconds since the epoch.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Table.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The geographic location where the table resides. This value is inherited from the dataset.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Table.num_bytes">
<code class="sig-name descname">num_bytes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.num_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of this table in bytes, excluding any data in the streaming buffer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Table.num_long_term_bytes">
<code class="sig-name descname">num_long_term_bytes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.num_long_term_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of bytes in the table that are considered “long-term storage”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Table.num_rows">
<code class="sig-name descname">num_rows</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.num_rows" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of rows of data in this table, excluding any data in the streaming buffer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Table.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Table.range_partitioning">
<code class="sig-name descname">range_partitioning</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.range_partitioning" title="Permalink to this definition">¶</a></dt>
<dd><p>If specified, configures range-based
partitioning for this table. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">field</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The field used to determine how to create a range-based
partition.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">range</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Information required to partition based on ranges.
Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">end</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - End of the range partitioning, exclusive.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The width of each range within the partition.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Start of the range partitioning, inclusive.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Table.schema">
<code class="sig-name descname">schema</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>A JSON schema for the table. Schema is required
for CSV and JSON formats and is disallowed for Google Cloud
Bigtable, Cloud Datastore backups, and Avro formats when using
external tables. For more information see the
<a class="reference external" href="https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#resource">BigQuery API documentation</a>.
~&gt;<strong>NOTE</strong>: Because this field expects a JSON string, any changes to the
string will create a diff, even if the JSON itself hasn’t changed.
If the API returns a different value for the same schema, e.g. it
switched the order of values or replaced <code class="docutils literal notranslate"><span class="pre">STRUCT</span></code> field type with <code class="docutils literal notranslate"><span class="pre">RECORD</span></code>
field type, we currently cannot suppress the recurring diff this causes.
As a workaround, we recommend using the schema as returned by the API.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Table.self_link">
<code class="sig-name descname">self_link</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Table.table_id">
<code class="sig-name descname">table_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique ID for the resource.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Table.time_partitioning">
<code class="sig-name descname">time_partitioning</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.time_partitioning" title="Permalink to this definition">¶</a></dt>
<dd><p>If specified, configures time-based
partitioning for this table. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">expirationMs</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of milliseconds for which to keep the
storage for a partition.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">field</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The field used to determine how to create a range-based
partition.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requirePartitionFilter</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If set to true, queries over this table
require a partition filter that can be used for partition elimination to be
specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The only type supported is DAY, which will generate
one partition per day based on data loading time.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Table.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The only type supported is DAY, which will generate
one partition per day based on data loading time.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.bigquery.Table.view">
<code class="sig-name descname">view</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.bigquery.Table.view" title="Permalink to this definition">¶</a></dt>
<dd><p>If specified, configures this table as a view.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A query that BigQuery executes when the view is referenced.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useLegacySql</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether to use BigQuery’s legacy SQL for this view.
The default value is true. If set to false, the view will use BigQuery’s standard SQL.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.bigquery.Table.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">clusterings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creation_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dataset_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiration_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_data_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">friendly_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_modified_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">num_bytes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">num_long_term_bytes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">num_rows</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">range_partitioning</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">self_link</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">table_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_partitioning</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">view</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Table.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Table resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>clusterings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies column names to use for data clustering.
Up to four top-level columns are allowed, and should be specified in
descending priority order.</p></li>
<li><p><strong>creation_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time when this table was created, in milliseconds since the epoch.</p></li>
<li><p><strong>dataset_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The dataset ID to create the table in.
Changing this forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The field description.</p></li>
<li><p><strong>encryption_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies how the table should be encrypted.
If left blank, the table will be encrypted with a Google-managed key; that process
is transparent to the user.  Structure is documented below.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A hash of the resource.</p></li>
<li><p><strong>expiration_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time when this table expires, in
milliseconds since the epoch. If not present, the table will persist
indefinitely. Expired tables will be deleted and their storage
reclaimed.</p></li>
<li><p><strong>external_data_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Describes the data format,
location, and other properties of a table stored outside of BigQuery.
By defining these properties, the data source can then be queried as
if it were a standard BigQuery table. Structure is documented below.</p></li>
<li><p><strong>friendly_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A descriptive name for the table.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of labels to assign to the resource.</p></li>
<li><p><strong>last_modified_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time when this table was last modified, in milliseconds since the epoch.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The geographic location where the table resides. This value is inherited from the dataset.</p></li>
<li><p><strong>num_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of this table in bytes, excluding any data in the streaming buffer.</p></li>
<li><p><strong>num_long_term_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of bytes in the table that are considered “long-term storage”.</p></li>
<li><p><strong>num_rows</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of rows of data in this table, excluding any data in the streaming buffer.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>range_partitioning</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – If specified, configures range-based
partitioning for this table. Structure is documented below.</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>A JSON schema for the table. Schema is required
for CSV and JSON formats and is disallowed for Google Cloud
Bigtable, Cloud Datastore backups, and Avro formats when using
external tables. For more information see the
<a class="reference external" href="https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#resource">BigQuery API documentation</a>.
~&gt;<strong>NOTE</strong>: Because this field expects a JSON string, any changes to the
string will create a diff, even if the JSON itself hasn’t changed.
If the API returns a different value for the same schema, e.g. it
switched the order of values or replaced <code class="docutils literal notranslate"><span class="pre">STRUCT</span></code> field type with <code class="docutils literal notranslate"><span class="pre">RECORD</span></code>
field type, we currently cannot suppress the recurring diff this causes.
As a workaround, we recommend using the schema as returned by the API.</p>
</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
<li><p><strong>table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique ID for the resource.
Changing this forces a new resource to be created.</p></li>
<li><p><strong>time_partitioning</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – If specified, configures time-based
partitioning for this table. Structure is documented below.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The only type supported is DAY, which will generate
one partition per day based on data loading time.</p></li>
<li><p><strong>view</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – If specified, configures this table as a view.
Structure is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>encryption_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The self link or full name of a key which should be used to
encrypt this table.  Note that the default bigquery service account will need to have
encrypt/decrypt permissions on this key - you may want to see the
<code class="docutils literal notranslate"><span class="pre">bigquery.getDefaultServiceAccount</span></code> datasource and the
<code class="docutils literal notranslate"><span class="pre">kms.CryptoKeyIAMBinding</span></code> resource.</p></li>
</ul>
<p>The <strong>external_data_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autodetect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - - Let BigQuery try to autodetect the schema
and format of the table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The compression type of the data source.
Valid values are “NONE” or “GZIP”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">csvOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Additional properties to set if
<code class="docutils literal notranslate"><span class="pre">source_format</span></code> is set to “CSV”. Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowJaggedRows</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates if BigQuery should accept rows
that are missing trailing optional columns.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowQuotedNewlines</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates if BigQuery should allow
quoted data sections that contain newline characters in a CSV file.
The default value is false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The character encoding of the data. The supported
values are UTF-8 or ISO-8859-1.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldDelimiter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The separator for fields in a CSV file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">quote</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value that is used to quote data sections in a
CSV file. If your data does not contain quoted sections, set the
property value to an empty string. If your data contains quoted newline
characters, you must also set the <code class="docutils literal notranslate"><span class="pre">allow_quoted_newlines</span></code> property to true.
The API-side default is <code class="docutils literal notranslate"><span class="pre">&quot;</span></code>, specified in the provider escaped as <code class="docutils literal notranslate"><span class="pre">&quot;</span></code>. Due to
limitations with default values, this value is required to be
explicitly set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">skipLeadingRows</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of rows at the top of the sheet
that BigQuery will skip when reading the data. At least one of <code class="docutils literal notranslate"><span class="pre">range</span></code> or
<code class="docutils literal notranslate"><span class="pre">skip_leading_rows</span></code> must be set.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">googleSheetsOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Additional options if
<code class="docutils literal notranslate"><span class="pre">source_format</span></code> is set to “GOOGLE_SHEETS”. Structure is
documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">range</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Information required to partition based on ranges.
Structure is documented below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">skipLeadingRows</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of rows at the top of the sheet
that BigQuery will skip when reading the data. At least one of <code class="docutils literal notranslate"><span class="pre">range</span></code> or
<code class="docutils literal notranslate"><span class="pre">skip_leading_rows</span></code> must be set.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ignoreUnknownValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates if BigQuery should
allow extra values that are not represented in the table schema.
If true, the extra values are ignored. If false, records with
extra columns are treated as bad records, and if there are too
many bad records, an invalid error is returned in the job result.
The default value is false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxBadRecords</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of bad records that
BigQuery can ignore when reading data.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data format. Supported values are:
“CSV”, “GOOGLE_SHEETS”, “NEWLINE_DELIMITED_JSON”, “AVRO”, “PARQUET”,
and “DATSTORE_BACKUP”. To use “GOOGLE_SHEETS”
the <code class="docutils literal notranslate"><span class="pre">scopes</span></code> must include
“<a class="reference external" href="https://www.googleapis.com/auth/drive.readonly">https://www.googleapis.com/auth/drive.readonly</a>”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of the fully-qualified URIs that point to
your data in Google Cloud.</p></li>
</ul>
<p>The <strong>range_partitioning</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">field</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The field used to determine how to create a range-based
partition.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">range</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information required to partition based on ranges.
Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">end</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - End of the range partitioning, exclusive.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The width of each range within the partition.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Start of the range partitioning, inclusive.</p></li>
</ul>
</li>
</ul>
<p>The <strong>time_partitioning</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">expirationMs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of milliseconds for which to keep the
storage for a partition.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">field</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The field used to determine how to create a range-based
partition.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requirePartitionFilter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If set to true, queries over this table
require a partition filter that can be used for partition elimination to be
specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The only type supported is DAY, which will generate
one partition per day based on data loading time.</p></li>
</ul>
<p>The <strong>view</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A query that BigQuery executes when the view is referenced.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useLegacySql</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether to use BigQuery’s legacy SQL for this view.
The default value is true. If set to false, the view will use BigQuery’s standard SQL.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.bigquery.Table.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Table.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigquery.Table.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.Table.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.bigquery.get_default_service_account">
<code class="sig-prename descclassname">pulumi_gcp.bigquery.</code><code class="sig-name descname">get_default_service_account</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.bigquery.get_default_service_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the email address of a project’s unique BigQuery service account.</p>
<p>Each Google Cloud project has a unique service account used by BigQuery. When using
BigQuery with <a class="reference external" href="https://cloud.google.com/bigquery/docs/customer-managed-encryption">customer-managed encryption keys</a>,
this account needs to be granted the
<code class="docutils literal notranslate"><span class="pre">cloudkms.cryptoKeyEncrypterDecrypter</span></code> IAM role on the customer-managed Cloud KMS key used to protect the data.</p>
<p>For more information see
<a class="reference external" href="https://cloud.google.com/bigquery/docs/reference/rest/v2/projects/getServiceAccount">the API reference</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>project</strong> (<em>str</em>) – The project the unique service account was created for. If it is not provided, the provider project is used.</p>
</dd>
</dl>
</dd></dl>

</div>
