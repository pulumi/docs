---
title: Module gameservices
title_tag: Module gameservices | Package pulumi_gcp | Python SDK
linktitle: gameservices
notitle: true
---

<div class="section" id="gameservices">
<h1>gameservices<a class="headerlink" href="#gameservices" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.gameservices"></span><dl class="class">
<dt id="pulumi_gcp.gameservices.GameServerCluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.gameservices.</code><code class="sig-name descname">GameServerCluster</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_id=None</em>, <em class="sig-param">connection_info=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>A game server cluster resource.</p>
<p>To get more information about GameServerCluster, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/game-servers/docs/reference/rest/v1beta/projects.locations.realms.gameServerClusters">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/game-servers/docs">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/game_services_game_server_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/game_services_game_server_cluster.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required. The resource name of the game server cluster</p></li>
<li><p><strong>connection_info</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Game server cluster connection information. This information is used to manage game server clusters.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human readable description of the cluster.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The labels associated with this game server cluster. Each label is a key-value pair.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Location of the Cluster.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm id of the game server realm.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>connection_info</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">gkeClusterReference</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cluster</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.gameservices.GameServerCluster.cluster_id">
<code class="sig-name descname">cluster_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerCluster.cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Required. The resource name of the game server cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.GameServerCluster.connection_info">
<code class="sig-name descname">connection_info</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerCluster.connection_info" title="Permalink to this definition">¶</a></dt>
<dd><p>Game server cluster connection information. This information is used to manage game server clusters.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">gkeClusterReference</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cluster</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.GameServerCluster.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerCluster.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human readable description of the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.GameServerCluster.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerCluster.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>The labels associated with this game server cluster. Each label is a key-value pair.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.GameServerCluster.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerCluster.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Location of the Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.GameServerCluster.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerCluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource id of the game server cluster, eg:
‘projects/{project_id}/locations/{location}/realms/{realm_id}/gameServerClusters/{cluster_id}’. For example,
‘projects/my-project/locations/{location}/realms/zanzibar/gameServerClusters/my-onprem-cluster’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.GameServerCluster.realm_id">
<code class="sig-name descname">realm_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerCluster.realm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The realm id of the game server realm.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.gameservices.GameServerCluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_id=None</em>, <em class="sig-param">connection_info=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">realm_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerCluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GameServerCluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required. The resource name of the game server cluster</p></li>
<li><p><strong>connection_info</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Game server cluster connection information. This information is used to manage game server clusters.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human readable description of the cluster.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The labels associated with this game server cluster. Each label is a key-value pair.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Location of the Cluster.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource id of the game server cluster, eg:
‘projects/{project_id}/locations/{location}/realms/{realm_id}/gameServerClusters/{cluster_id}’. For example,
‘projects/my-project/locations/{location}/realms/zanzibar/gameServerClusters/my-onprem-cluster’.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm id of the game server realm.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>connection_info</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">gkeClusterReference</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cluster</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.gameservices.GameServerCluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.gameservices.GameServerCluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.gameservices.GameServerConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.gameservices.</code><code class="sig-name descname">GameServerConfig</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">config_id=None</em>, <em class="sig-param">deployment_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">fleet_configs=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">scaling_configs=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>A game server config resource. Configs are global and immutable.</p>
<p>To get more information about GameServerConfig, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/game-servers/docs/reference/rest/v1beta/projects.locations.gameServerDeployments.configs">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/game-servers/docs">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/game_services_game_server_config.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/game_services_game_server_config.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique id for the deployment config.</p></li>
<li><p><strong>deployment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique id for the deployment.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the game server config.</p></li>
<li><p><strong>fleet_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The fleet config contains list of fleet specs. In the Single Cloud, there will be only one.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The labels associated with this game server config. Each label is a key-value pair.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Location of the Deployment.</p></li>
<li><p><strong>scaling_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Optional. This contains the autoscaling settings.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>fleet_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fleetSpec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scaling_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fleetAutoscalerSpec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schedules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cronJobDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cronSpec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">selectors</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
</ul>
</li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.gameservices.GameServerConfig.config_id">
<code class="sig-name descname">config_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerConfig.config_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique id for the deployment config.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.GameServerConfig.deployment_id">
<code class="sig-name descname">deployment_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerConfig.deployment_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique id for the deployment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.GameServerConfig.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerConfig.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the game server config.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.GameServerConfig.fleet_configs">
<code class="sig-name descname">fleet_configs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerConfig.fleet_configs" title="Permalink to this definition">¶</a></dt>
<dd><p>The fleet config contains list of fleet specs. In the Single Cloud, there will be only one.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fleetSpec</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.GameServerConfig.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerConfig.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>The labels associated with this game server config. Each label is a key-value pair.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.GameServerConfig.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerConfig.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Location of the Deployment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.GameServerConfig.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerConfig.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of the game server config, in the form:
‘projects/{project_id}/locations/{location}/gameServerDeployments/{deployment_id}/configs/{config_id}’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.GameServerConfig.scaling_configs">
<code class="sig-name descname">scaling_configs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerConfig.scaling_configs" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional. This contains the autoscaling settings.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fleetAutoscalerSpec</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schedules</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cronJobDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cronSpec</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">selectors</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.gameservices.GameServerConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">config_id=None</em>, <em class="sig-param">deployment_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">fleet_configs=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">scaling_configs=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GameServerConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique id for the deployment config.</p></li>
<li><p><strong>deployment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique id for the deployment.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the game server config.</p></li>
<li><p><strong>fleet_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The fleet config contains list of fleet specs. In the Single Cloud, there will be only one.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The labels associated with this game server config. Each label is a key-value pair.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Location of the Deployment.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name of the game server config, in the form:
‘projects/{project_id}/locations/{location}/gameServerDeployments/{deployment_id}/configs/{config_id}’.</p></li>
<li><p><strong>scaling_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Optional. This contains the autoscaling settings.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>fleet_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fleetSpec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scaling_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fleetAutoscalerSpec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schedules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cronJobDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cronSpec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">selectors</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.gameservices.GameServerConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.gameservices.GameServerConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.gameservices.GameServerDeployment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.gameservices.</code><code class="sig-name descname">GameServerDeployment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">deployment_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerDeployment" title="Permalink to this definition">¶</a></dt>
<dd><p>A game server deployment resource.</p>
<p>To get more information about GameServerDeployment, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/game-servers/docs/reference/rest/v1beta/projects.locations.gameServerDeployments">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/game-servers/docs">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/game_services_game_server_deployment.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/game_services_game_server_deployment.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>deployment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique id for the deployment.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human readable description of the game server deployment.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The labels associated with this game server deployment. Each label is a key-value pair.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Location of the Deployment.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.gameservices.GameServerDeployment.deployment_id">
<code class="sig-name descname">deployment_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerDeployment.deployment_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique id for the deployment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.GameServerDeployment.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerDeployment.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human readable description of the game server deployment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.GameServerDeployment.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerDeployment.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>The labels associated with this game server deployment. Each label is a key-value pair.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.GameServerDeployment.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerDeployment.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Location of the Deployment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.GameServerDeployment.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerDeployment.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource id of the game server deployment, eg:
‘projects/{project_id}/locations/{location}/gameServerDeployments/{deployment_id}’. For example,
‘projects/my-project/locations/{location}/gameServerDeployments/my-deployment’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.GameServerDeployment.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerDeployment.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.gameservices.GameServerDeployment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">deployment_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerDeployment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GameServerDeployment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>deployment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique id for the deployment.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human readable description of the game server deployment.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The labels associated with this game server deployment. Each label is a key-value pair.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Location of the Deployment.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource id of the game server deployment, eg:
‘projects/{project_id}/locations/{location}/gameServerDeployments/{deployment_id}’. For example,
‘projects/my-project/locations/{location}/gameServerDeployments/my-deployment’.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.gameservices.GameServerDeployment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerDeployment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.gameservices.GameServerDeployment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerDeployment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.gameservices.GameServerDeploymentRollout">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.gameservices.</code><code class="sig-name descname">GameServerDeploymentRollout</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">default_game_server_config=None</em>, <em class="sig-param">deployment_id=None</em>, <em class="sig-param">game_server_config_overrides=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerDeploymentRollout" title="Permalink to this definition">¶</a></dt>
<dd><p>This represents the rollout state. This is part of the game server
deployment.</p>
<p>To get more information about GameServerDeploymentRollout, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/game-servers/docs/reference/rest/v1beta/GameServerDeploymentRollout">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/game-servers/docs">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/game_services_game_server_deployment_rollout.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/game_services_game_server_deployment_rollout.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_game_server_config</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This field points to the game server config that is applied by default to all realms and clusters. For example,
‘projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config’.</p></li>
<li><p><strong>deployment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The deployment to rollout the new config to. Only 1 rollout must be associated with each deployment.</p></li>
<li><p><strong>game_server_config_overrides</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The game_server_config_overrides contains the per game server config overrides. The overrides are processed in the order
they are listed. As soon as a match is found for a cluster, the rest of the list is not processed.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>game_server_config_overrides</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">configVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">realmsSelector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">realms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.gameservices.GameServerDeploymentRollout.default_game_server_config">
<code class="sig-name descname">default_game_server_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerDeploymentRollout.default_game_server_config" title="Permalink to this definition">¶</a></dt>
<dd><p>This field points to the game server config that is applied by default to all realms and clusters. For example,
‘projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.GameServerDeploymentRollout.deployment_id">
<code class="sig-name descname">deployment_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerDeploymentRollout.deployment_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The deployment to rollout the new config to. Only 1 rollout must be associated with each deployment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.GameServerDeploymentRollout.game_server_config_overrides">
<code class="sig-name descname">game_server_config_overrides</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerDeploymentRollout.game_server_config_overrides" title="Permalink to this definition">¶</a></dt>
<dd><p>The game_server_config_overrides contains the per game server config overrides. The overrides are processed in the order
they are listed. As soon as a match is found for a cluster, the rest of the list is not processed.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">configVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">realmsSelector</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">realms</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.GameServerDeploymentRollout.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerDeploymentRollout.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource id of the game server deployment eg:
‘projects/my-project/locations/global/gameServerDeployments/my-deployment/rollout’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.GameServerDeploymentRollout.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerDeploymentRollout.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.gameservices.GameServerDeploymentRollout.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">default_game_server_config=None</em>, <em class="sig-param">deployment_id=None</em>, <em class="sig-param">game_server_config_overrides=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerDeploymentRollout.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GameServerDeploymentRollout resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_game_server_config</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This field points to the game server config that is applied by default to all realms and clusters. For example,
‘projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config’.</p></li>
<li><p><strong>deployment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The deployment to rollout the new config to. Only 1 rollout must be associated with each deployment.</p></li>
<li><p><strong>game_server_config_overrides</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The game_server_config_overrides contains the per game server config overrides. The overrides are processed in the order
they are listed. As soon as a match is found for a cluster, the rest of the list is not processed.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource id of the game server deployment eg:
‘projects/my-project/locations/global/gameServerDeployments/my-deployment/rollout’.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>game_server_config_overrides</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">configVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">realmsSelector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">realms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.gameservices.GameServerDeploymentRollout.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerDeploymentRollout.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.gameservices.GameServerDeploymentRollout.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.gameservices.GameServerDeploymentRollout.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.gameservices.Realm">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.gameservices.</code><code class="sig-name descname">Realm</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">time_zone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.gameservices.Realm" title="Permalink to this definition">¶</a></dt>
<dd><p>A Realm resource.</p>
<p>To get more information about Realm, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/game-servers/docs/reference/rest/v1beta/projects.locations.realms">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/game-servers/docs">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/game_services_realm.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/game_services_realm.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human readable description of the realm.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The labels associated with this realm. Each label is a key-value pair.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Location of the Realm.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – GCP region of the Realm.</p></li>
<li><p><strong>time_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required. Time zone where all realm-specific policies are evaluated. The value of this field must be from the IANA time
zone database: <a class="reference external" href="https://www.iana.org/time-zones">https://www.iana.org/time-zones</a>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.gameservices.Realm.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.Realm.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human readable description of the realm.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.Realm.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.Realm.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>ETag of the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.Realm.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.Realm.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>The labels associated with this realm. Each label is a key-value pair.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.Realm.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.Realm.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Location of the Realm.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.Realm.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.Realm.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource id of the realm, of the form: ‘projects/{project_id}/locations/{location}/realms/{realm_id}’. For example,
‘projects/my-project/locations/{location}/realms/my-realm’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.Realm.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.Realm.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.Realm.realm_id">
<code class="sig-name descname">realm_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.Realm.realm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>GCP region of the Realm.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.gameservices.Realm.time_zone">
<code class="sig-name descname">time_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.gameservices.Realm.time_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Required. Time zone where all realm-specific policies are evaluated. The value of this field must be from the IANA time
zone database: <a class="reference external" href="https://www.iana.org/time-zones">https://www.iana.org/time-zones</a>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.gameservices.Realm.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">time_zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.gameservices.Realm.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Realm resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human readable description of the realm.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ETag of the resource.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The labels associated with this realm. Each label is a key-value pair.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Location of the Realm.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource id of the realm, of the form: ‘projects/{project_id}/locations/{location}/realms/{realm_id}’. For example,
‘projects/my-project/locations/{location}/realms/my-realm’.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – GCP region of the Realm.</p></li>
<li><p><strong>time_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required. Time zone where all realm-specific policies are evaluated. The value of this field must be from the IANA time
zone database: <a class="reference external" href="https://www.iana.org/time-zones">https://www.iana.org/time-zones</a>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.gameservices.Realm.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.gameservices.Realm.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.gameservices.Realm.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.gameservices.Realm.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
