---
title: Module codedeploy
title_tag: Module codedeploy | Package pulumi_aws | Python SDK
linktitle: codedeploy
notitle: true
---

<div class="section" id="codedeploy">
<h1>codedeploy<a class="headerlink" href="#codedeploy" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.codedeploy"></span><dl class="class">
<dt id="pulumi_aws.codedeploy.Application">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.codedeploy.</code><code class="sig-name descname">Application</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">compute_platform=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">unique_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codedeploy.Application" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CodeDeploy application to be used as a basis for deployments</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>compute_platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The compute platform can either be <code class="docutils literal notranslate"><span class="pre">ECS</span></code>, <code class="docutils literal notranslate"><span class="pre">Lambda</span></code>, or <code class="docutils literal notranslate"><span class="pre">Server</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">Server</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the application.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.codedeploy.Application.compute_platform">
<code class="sig-name descname">compute_platform</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.Application.compute_platform" title="Permalink to this definition">¶</a></dt>
<dd><p>The compute platform can either be <code class="docutils literal notranslate"><span class="pre">ECS</span></code>, <code class="docutils literal notranslate"><span class="pre">Lambda</span></code>, or <code class="docutils literal notranslate"><span class="pre">Server</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">Server</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codedeploy.Application.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.Application.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the application.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.codedeploy.Application.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">compute_platform=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">unique_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codedeploy.Application.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Application resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>compute_platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The compute platform can either be <code class="docutils literal notranslate"><span class="pre">ECS</span></code>, <code class="docutils literal notranslate"><span class="pre">Lambda</span></code>, or <code class="docutils literal notranslate"><span class="pre">Server</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">Server</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the application.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.codedeploy.Application.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codedeploy.Application.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.codedeploy.Application.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codedeploy.Application.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.codedeploy.DeploymentConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.codedeploy.</code><code class="sig-name descname">DeploymentConfig</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">compute_platform=None</em>, <em class="sig-param">deployment_config_name=None</em>, <em class="sig-param">minimum_healthy_hosts=None</em>, <em class="sig-param">traffic_routing_config=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CodeDeploy deployment config for an application</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>compute_platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The compute platform can be <code class="docutils literal notranslate"><span class="pre">Server</span></code>, <code class="docutils literal notranslate"><span class="pre">Lambda</span></code>, or <code class="docutils literal notranslate"><span class="pre">ECS</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">Server</span></code>.</p></li>
<li><p><strong>deployment_config_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the deployment config.</p></li>
<li><p><strong>minimum_healthy_hosts</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A minimum_healthy_hosts block. Required for <code class="docutils literal notranslate"><span class="pre">Server</span></code> compute platform. Minimum Healthy Hosts are documented below.</p></li>
<li><p><strong>traffic_routing_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A traffic_routing_config block. Traffic Routing Config is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>minimum_healthy_hosts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type can either be <code class="docutils literal notranslate"><span class="pre">FLEET_PERCENT</span></code> or <code class="docutils literal notranslate"><span class="pre">HOST_COUNT</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The value when the type is <code class="docutils literal notranslate"><span class="pre">FLEET_PERCENT</span></code> represents the minimum number of healthy instances as
a percentage of the total number of instances in the deployment. If you specify FLEET_PERCENT, at the start of the
deployment, AWS CodeDeploy converts the percentage to the equivalent number of instance and rounds up fractional instances.
When the type is <code class="docutils literal notranslate"><span class="pre">HOST_COUNT</span></code>, the value represents the minimum number of healthy instances as an absolute value.</p></li>
</ul>
<p>The <strong>traffic_routing_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">timeBasedCanary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The time based canary configuration information. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">TimeBasedLinear</span></code>, use <code class="docutils literal notranslate"><span class="pre">time_based_linear</span></code> instead.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of minutes between the first and second traffic shifts of a <code class="docutils literal notranslate"><span class="pre">TimeBasedCanary</span></code> deployment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The percentage of traffic to shift in the first increment of a <code class="docutils literal notranslate"><span class="pre">TimeBasedCanary</span></code> deployment.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeBasedLinear</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The time based linear configuration information. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">TimeBasedCanary</span></code>, use <code class="docutils literal notranslate"><span class="pre">time_based_canary</span></code> instead.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of minutes between each incremental traffic shift of a <code class="docutils literal notranslate"><span class="pre">TimeBasedLinear</span></code> deployment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The percentage of traffic that is shifted at the start of each increment of a <code class="docutils literal notranslate"><span class="pre">TimeBasedLinear</span></code> deployment.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of traffic routing config. One of <code class="docutils literal notranslate"><span class="pre">TimeBasedCanary</span></code>, <code class="docutils literal notranslate"><span class="pre">TimeBasedLinear</span></code>, <code class="docutils literal notranslate"><span class="pre">AllAtOnce</span></code>.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentConfig.compute_platform">
<code class="sig-name descname">compute_platform</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentConfig.compute_platform" title="Permalink to this definition">¶</a></dt>
<dd><p>The compute platform can be <code class="docutils literal notranslate"><span class="pre">Server</span></code>, <code class="docutils literal notranslate"><span class="pre">Lambda</span></code>, or <code class="docutils literal notranslate"><span class="pre">ECS</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">Server</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentConfig.deployment_config_id">
<code class="sig-name descname">deployment_config_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentConfig.deployment_config_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS Assigned deployment config id</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentConfig.deployment_config_name">
<code class="sig-name descname">deployment_config_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentConfig.deployment_config_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the deployment config.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentConfig.minimum_healthy_hosts">
<code class="sig-name descname">minimum_healthy_hosts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentConfig.minimum_healthy_hosts" title="Permalink to this definition">¶</a></dt>
<dd><p>A minimum_healthy_hosts block. Required for <code class="docutils literal notranslate"><span class="pre">Server</span></code> compute platform. Minimum Healthy Hosts are documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type can either be <code class="docutils literal notranslate"><span class="pre">FLEET_PERCENT</span></code> or <code class="docutils literal notranslate"><span class="pre">HOST_COUNT</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The value when the type is <code class="docutils literal notranslate"><span class="pre">FLEET_PERCENT</span></code> represents the minimum number of healthy instances as
a percentage of the total number of instances in the deployment. If you specify FLEET_PERCENT, at the start of the
deployment, AWS CodeDeploy converts the percentage to the equivalent number of instance and rounds up fractional instances.
When the type is <code class="docutils literal notranslate"><span class="pre">HOST_COUNT</span></code>, the value represents the minimum number of healthy instances as an absolute value.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentConfig.traffic_routing_config">
<code class="sig-name descname">traffic_routing_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentConfig.traffic_routing_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A traffic_routing_config block. Traffic Routing Config is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">timeBasedCanary</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The time based canary configuration information. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">TimeBasedLinear</span></code>, use <code class="docutils literal notranslate"><span class="pre">time_based_linear</span></code> instead.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of minutes between the first and second traffic shifts of a <code class="docutils literal notranslate"><span class="pre">TimeBasedCanary</span></code> deployment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percentage</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The percentage of traffic to shift in the first increment of a <code class="docutils literal notranslate"><span class="pre">TimeBasedCanary</span></code> deployment.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeBasedLinear</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The time based linear configuration information. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">TimeBasedCanary</span></code>, use <code class="docutils literal notranslate"><span class="pre">time_based_canary</span></code> instead.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of minutes between each incremental traffic shift of a <code class="docutils literal notranslate"><span class="pre">TimeBasedLinear</span></code> deployment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percentage</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The percentage of traffic that is shifted at the start of each increment of a <code class="docutils literal notranslate"><span class="pre">TimeBasedLinear</span></code> deployment.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Type of traffic routing config. One of <code class="docutils literal notranslate"><span class="pre">TimeBasedCanary</span></code>, <code class="docutils literal notranslate"><span class="pre">TimeBasedLinear</span></code>, <code class="docutils literal notranslate"><span class="pre">AllAtOnce</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.codedeploy.DeploymentConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">compute_platform=None</em>, <em class="sig-param">deployment_config_id=None</em>, <em class="sig-param">deployment_config_name=None</em>, <em class="sig-param">minimum_healthy_hosts=None</em>, <em class="sig-param">traffic_routing_config=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DeploymentConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>compute_platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The compute platform can be <code class="docutils literal notranslate"><span class="pre">Server</span></code>, <code class="docutils literal notranslate"><span class="pre">Lambda</span></code>, or <code class="docutils literal notranslate"><span class="pre">ECS</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">Server</span></code>.</p></li>
<li><p><strong>deployment_config_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS Assigned deployment config id</p></li>
<li><p><strong>deployment_config_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the deployment config.</p></li>
<li><p><strong>minimum_healthy_hosts</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A minimum_healthy_hosts block. Required for <code class="docutils literal notranslate"><span class="pre">Server</span></code> compute platform. Minimum Healthy Hosts are documented below.</p></li>
<li><p><strong>traffic_routing_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A traffic_routing_config block. Traffic Routing Config is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>minimum_healthy_hosts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type can either be <code class="docutils literal notranslate"><span class="pre">FLEET_PERCENT</span></code> or <code class="docutils literal notranslate"><span class="pre">HOST_COUNT</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The value when the type is <code class="docutils literal notranslate"><span class="pre">FLEET_PERCENT</span></code> represents the minimum number of healthy instances as
a percentage of the total number of instances in the deployment. If you specify FLEET_PERCENT, at the start of the
deployment, AWS CodeDeploy converts the percentage to the equivalent number of instance and rounds up fractional instances.
When the type is <code class="docutils literal notranslate"><span class="pre">HOST_COUNT</span></code>, the value represents the minimum number of healthy instances as an absolute value.</p></li>
</ul>
<p>The <strong>traffic_routing_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">timeBasedCanary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The time based canary configuration information. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">TimeBasedLinear</span></code>, use <code class="docutils literal notranslate"><span class="pre">time_based_linear</span></code> instead.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of minutes between the first and second traffic shifts of a <code class="docutils literal notranslate"><span class="pre">TimeBasedCanary</span></code> deployment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The percentage of traffic to shift in the first increment of a <code class="docutils literal notranslate"><span class="pre">TimeBasedCanary</span></code> deployment.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeBasedLinear</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The time based linear configuration information. If <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">TimeBasedCanary</span></code>, use <code class="docutils literal notranslate"><span class="pre">time_based_canary</span></code> instead.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of minutes between each incremental traffic shift of a <code class="docutils literal notranslate"><span class="pre">TimeBasedLinear</span></code> deployment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The percentage of traffic that is shifted at the start of each increment of a <code class="docutils literal notranslate"><span class="pre">TimeBasedLinear</span></code> deployment.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of traffic routing config. One of <code class="docutils literal notranslate"><span class="pre">TimeBasedCanary</span></code>, <code class="docutils literal notranslate"><span class="pre">TimeBasedLinear</span></code>, <code class="docutils literal notranslate"><span class="pre">AllAtOnce</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.codedeploy.DeploymentConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.codedeploy.DeploymentConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.codedeploy.DeploymentGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.codedeploy.</code><code class="sig-name descname">DeploymentGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alarm_configuration=None</em>, <em class="sig-param">app_name=None</em>, <em class="sig-param">auto_rollback_configuration=None</em>, <em class="sig-param">autoscaling_groups=None</em>, <em class="sig-param">blue_green_deployment_config=None</em>, <em class="sig-param">deployment_config_name=None</em>, <em class="sig-param">deployment_group_name=None</em>, <em class="sig-param">deployment_style=None</em>, <em class="sig-param">ec2_tag_filters=None</em>, <em class="sig-param">ec2_tag_sets=None</em>, <em class="sig-param">ecs_service=None</em>, <em class="sig-param">load_balancer_info=None</em>, <em class="sig-param">on_premises_instance_tag_filters=None</em>, <em class="sig-param">service_role_arn=None</em>, <em class="sig-param">trigger_configurations=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CodeDeploy Deployment Group for a CodeDeploy Application</p>
<blockquote>
<div><p><strong>NOTE on blue/green deployments:</strong> When using <code class="docutils literal notranslate"><span class="pre">green_fleet_provisioning_option</span></code> with the <code class="docutils literal notranslate"><span class="pre">COPY_AUTO_SCALING_GROUP</span></code> action, CodeDeploy will create a new ASG with a different name. This ASG is <em>not</em> managed by this provider and will conflict with existing configuration and state. You may want to use a different approach to managing deployments that involve multiple ASG, such as <code class="docutils literal notranslate"><span class="pre">DISCOVER_EXISTING</span></code> with separate blue and green ASG.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alarm_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block of alarms associated with the deployment group (documented below).</p></li>
<li><p><strong>app_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the application.</p></li>
<li><p><strong>auto_rollback_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block of the automatic rollback configuration associated with the deployment group (documented below).</p></li>
<li><p><strong>autoscaling_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Autoscaling groups associated with the deployment group.</p></li>
<li><p><strong>blue_green_deployment_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block of the blue/green deployment options for a deployment group (documented below).</p></li>
<li><p><strong>deployment_config_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the group’s deployment config. The default is “CodeDeployDefault.OneAtATime”.</p></li>
<li><p><strong>deployment_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the deployment group.</p></li>
<li><p><strong>deployment_style</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block of the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer (documented below).</p></li>
<li><p><strong>ec2_tag_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Tag filters associated with the deployment group. See the AWS docs for details.</p></li>
<li><p><strong>ec2_tag_sets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configuration block(s) of Tag filters associated with the deployment group, which are also referred to as tag groups (documented below). See the AWS docs for details.</p></li>
<li><p><strong>ecs_service</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block(s) of the ECS services for a deployment group (documented below).</p></li>
<li><p><strong>load_balancer_info</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Single configuration block of the load balancer to use in a blue/green deployment (documented below).</p></li>
<li><p><strong>on_premises_instance_tag_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – On premise tag filters associated with the group. See the AWS docs for details.</p></li>
<li><p><strong>service_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service role ARN that allows deployments.</p></li>
<li><p><strong>trigger_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configuration block(s) of the triggers for the deployment group (documented below).</p></li>
</ul>
</dd>
</dl>
<p>The <strong>alarm_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alarms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of alarms configured for the deployment group. <em>A maximum of 10 alarms can be added to a deployment group</em>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether the alarm configuration is enabled. This option is useful when you want to temporarily deactivate alarm monitoring for a deployment group without having to add the same alarms again later.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ignorePollAlarmFailure</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from CloudWatch. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">true</span></code>: The deployment will proceed even if alarm status information can’t be retrieved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">false</span></code>: The deployment will stop if alarm status information can’t be retrieved.</p></li>
</ul>
</li>
</ul>
<p>The <strong>auto_rollback_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether a defined automatic rollback configuration is currently enabled for this Deployment Group. If you enable automatic rollback, you must specify at least one event type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">events</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The event type or types that trigger a rollback. Supported types are <code class="docutils literal notranslate"><span class="pre">DEPLOYMENT_FAILURE</span></code> and <code class="docutils literal notranslate"><span class="pre">DEPLOYMENT_STOP_ON_ALARM</span></code>.</p></li>
</ul>
<p>The <strong>blue_green_deployment_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deploymentReadyOption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment (documented below).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">actionOnTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When to reroute traffic from an original environment to a replacement environment in a blue/green deployment.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">CONTINUE_DEPLOYMENT</span></code>: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">STOP_DEPLOYMENT</span></code>: Do not register new instances with load balancer unless traffic is rerouted manually. If traffic is not rerouted manually before the end of the specified wait period, the deployment status is changed to Stopped.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitTimeInMinutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of minutes to wait before the status of a blue/green deployment changed to Stopped if rerouting is not started manually. Applies only to the <code class="docutils literal notranslate"><span class="pre">STOP_DEPLOYMENT</span></code> option for <code class="docutils literal notranslate"><span class="pre">action_on_timeout</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">greenFleetProvisioningOption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information about how instances are provisioned for a replacement environment in a blue/green deployment (documented below).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The method used to add instances to a replacement environment.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">DISCOVER_EXISTING</span></code>: Use instances that already exist or will be created manually.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">COPY_AUTO_SCALING_GROUP</span></code>: Use settings from a specified <strong>Auto Scaling</strong> group to define and create instances in a new Auto Scaling group. <em>Exactly one Auto Scaling group must be specified</em> when selecting <code class="docutils literal notranslate"><span class="pre">COPY_AUTO_SCALING_GROUP</span></code>. Use <code class="docutils literal notranslate"><span class="pre">autoscaling_groups</span></code> to specify the Auto Scaling group.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">terminateBlueInstancesOnDeploymentSuccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information about whether to terminate instances in the original fleet during a blue/green deployment (documented below).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The action to take on instances in the original environment after a successful blue/green deployment.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">TERMINATE</span></code>: Instances are terminated after a specified wait time.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">KEEP_ALIVE</span></code>: Instances are left running after they are deregistered from the load balancer and removed from the deployment group.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">terminationWaitTimeInMinutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.</p></li>
</ul>
</li>
</ul>
<p>The <strong>deployment_style</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deploymentOption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Indicates whether to route deployment traffic behind a load balancer. Valid Values are <code class="docutils literal notranslate"><span class="pre">WITH_TRAFFIC_CONTROL</span></code> or <code class="docutils literal notranslate"><span class="pre">WITHOUT_TRAFFIC_CONTROL</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">WITHOUT_TRAFFIC_CONTROL</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deploymentType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Indicates whether to run an in-place deployment or a blue/green deployment. Valid Values are <code class="docutils literal notranslate"><span class="pre">IN_PLACE</span></code> or <code class="docutils literal notranslate"><span class="pre">BLUE_GREEN</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">IN_PLACE</span></code>.</p></li>
</ul>
<p>The <strong>ec2_tag_filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The key of the tag filter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of the tag filter, either <code class="docutils literal notranslate"><span class="pre">KEY_ONLY</span></code>, <code class="docutils literal notranslate"><span class="pre">VALUE_ONLY</span></code>, or <code class="docutils literal notranslate"><span class="pre">KEY_AND_VALUE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the tag filter.</p></li>
</ul>
<p>The <strong>ec2_tag_sets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ec2_tag_filters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Tag filters associated with the deployment group. See the AWS docs for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The key of the tag filter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of the tag filter, either <code class="docutils literal notranslate"><span class="pre">KEY_ONLY</span></code>, <code class="docutils literal notranslate"><span class="pre">VALUE_ONLY</span></code>, or <code class="docutils literal notranslate"><span class="pre">KEY_AND_VALUE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the tag filter.</p></li>
</ul>
</li>
</ul>
<p>The <strong>ecs_service</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the ECS cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the ECS service.</p></li>
</ul>
<p>The <strong>load_balancer_info</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">elbInfos</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The Classic Elastic Load Balancer to use in a deployment. Conflicts with <code class="docutils literal notranslate"><span class="pre">target_group_info</span></code> and <code class="docutils literal notranslate"><span class="pre">target_group_pair_info</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the load balancer that will be used to route traffic from original instances to replacement instances in a blue/green deployment. For in-place deployments, the name of the load balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment completes.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetGroupInfos</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The (Application/Network Load Balancer) target group to use in a deployment. Conflicts with <code class="docutils literal notranslate"><span class="pre">elb_info</span></code> and <code class="docutils literal notranslate"><span class="pre">target_group_pair_info</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment completes.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetGroupPairInfo</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The (Application/Network Load Balancer) target group pair to use in a deployment. Conflicts with <code class="docutils literal notranslate"><span class="pre">elb_info</span></code> and <code class="docutils literal notranslate"><span class="pre">target_group_info</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">prodTrafficRoute</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block for the production traffic route (documented below).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">listenerArns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of Amazon Resource Names (ARNs) of the load balancer listeners.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Configuration blocks for a target group within a target group pair (documented below).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the target group.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">testTrafficRoute</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block for the test traffic route (documented below).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">listenerArns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of Amazon Resource Names (ARNs) of the load balancer listeners.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<p>The <strong>on_premises_instance_tag_filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The key of the tag filter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of the tag filter, either <code class="docutils literal notranslate"><span class="pre">KEY_ONLY</span></code>, <code class="docutils literal notranslate"><span class="pre">VALUE_ONLY</span></code>, or <code class="docutils literal notranslate"><span class="pre">KEY_AND_VALUE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the tag filter.</p></li>
</ul>
<p>The <strong>trigger_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">triggerEvents</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The event type or types for which notifications are triggered. Some values that are supported: <code class="docutils literal notranslate"><span class="pre">DeploymentStart</span></code>, <code class="docutils literal notranslate"><span class="pre">DeploymentSuccess</span></code>, <code class="docutils literal notranslate"><span class="pre">DeploymentFailure</span></code>, <code class="docutils literal notranslate"><span class="pre">DeploymentStop</span></code>, <code class="docutils literal notranslate"><span class="pre">DeploymentRollback</span></code>, <code class="docutils literal notranslate"><span class="pre">InstanceStart</span></code>, <code class="docutils literal notranslate"><span class="pre">InstanceSuccess</span></code>, <code class="docutils literal notranslate"><span class="pre">InstanceFailure</span></code>.  See <a class="reference external" href="http://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-sns-event-notifications-create-trigger.html">the CodeDeploy documentation</a> for all possible values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">triggerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the notification trigger.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">triggerTargetArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the SNS topic through which notifications are sent.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentGroup.alarm_configuration">
<code class="sig-name descname">alarm_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentGroup.alarm_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block of alarms associated with the deployment group (documented below).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alarms</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of alarms configured for the deployment group. <em>A maximum of 10 alarms can be added to a deployment group</em>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether the alarm configuration is enabled. This option is useful when you want to temporarily deactivate alarm monitoring for a deployment group without having to add the same alarms again later.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ignorePollAlarmFailure</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from CloudWatch. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">true</span></code>: The deployment will proceed even if alarm status information can’t be retrieved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">false</span></code>: The deployment will stop if alarm status information can’t be retrieved.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentGroup.app_name">
<code class="sig-name descname">app_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentGroup.app_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentGroup.auto_rollback_configuration">
<code class="sig-name descname">auto_rollback_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentGroup.auto_rollback_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block of the automatic rollback configuration associated with the deployment group (documented below).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether a defined automatic rollback configuration is currently enabled for this Deployment Group. If you enable automatic rollback, you must specify at least one event type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">events</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The event type or types that trigger a rollback. Supported types are <code class="docutils literal notranslate"><span class="pre">DEPLOYMENT_FAILURE</span></code> and <code class="docutils literal notranslate"><span class="pre">DEPLOYMENT_STOP_ON_ALARM</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentGroup.autoscaling_groups">
<code class="sig-name descname">autoscaling_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentGroup.autoscaling_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Autoscaling groups associated with the deployment group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentGroup.blue_green_deployment_config">
<code class="sig-name descname">blue_green_deployment_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentGroup.blue_green_deployment_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block of the blue/green deployment options for a deployment group (documented below).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deploymentReadyOption</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment (documented below).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">actionOnTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - When to reroute traffic from an original environment to a replacement environment in a blue/green deployment.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">CONTINUE_DEPLOYMENT</span></code>: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">STOP_DEPLOYMENT</span></code>: Do not register new instances with load balancer unless traffic is rerouted manually. If traffic is not rerouted manually before the end of the specified wait period, the deployment status is changed to Stopped.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitTimeInMinutes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of minutes to wait before the status of a blue/green deployment changed to Stopped if rerouting is not started manually. Applies only to the <code class="docutils literal notranslate"><span class="pre">STOP_DEPLOYMENT</span></code> option for <code class="docutils literal notranslate"><span class="pre">action_on_timeout</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">greenFleetProvisioningOption</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Information about how instances are provisioned for a replacement environment in a blue/green deployment (documented below).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The method used to add instances to a replacement environment.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">DISCOVER_EXISTING</span></code>: Use instances that already exist or will be created manually.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">COPY_AUTO_SCALING_GROUP</span></code>: Use settings from a specified <strong>Auto Scaling</strong> group to define and create instances in a new Auto Scaling group. <em>Exactly one Auto Scaling group must be specified</em> when selecting <code class="docutils literal notranslate"><span class="pre">COPY_AUTO_SCALING_GROUP</span></code>. Use <code class="docutils literal notranslate"><span class="pre">autoscaling_groups</span></code> to specify the Auto Scaling group.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">terminateBlueInstancesOnDeploymentSuccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Information about whether to terminate instances in the original fleet during a blue/green deployment (documented below).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The action to take on instances in the original environment after a successful blue/green deployment.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">TERMINATE</span></code>: Instances are terminated after a specified wait time.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">KEEP_ALIVE</span></code>: Instances are left running after they are deregistered from the load balancer and removed from the deployment group.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">terminationWaitTimeInMinutes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentGroup.deployment_config_name">
<code class="sig-name descname">deployment_config_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentGroup.deployment_config_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the group’s deployment config. The default is “CodeDeployDefault.OneAtATime”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentGroup.deployment_group_name">
<code class="sig-name descname">deployment_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentGroup.deployment_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the deployment group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentGroup.deployment_style">
<code class="sig-name descname">deployment_style</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentGroup.deployment_style" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block of the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer (documented below).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deploymentOption</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Indicates whether to route deployment traffic behind a load balancer. Valid Values are <code class="docutils literal notranslate"><span class="pre">WITH_TRAFFIC_CONTROL</span></code> or <code class="docutils literal notranslate"><span class="pre">WITHOUT_TRAFFIC_CONTROL</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">WITHOUT_TRAFFIC_CONTROL</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deploymentType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Indicates whether to run an in-place deployment or a blue/green deployment. Valid Values are <code class="docutils literal notranslate"><span class="pre">IN_PLACE</span></code> or <code class="docutils literal notranslate"><span class="pre">BLUE_GREEN</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">IN_PLACE</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentGroup.ec2_tag_filters">
<code class="sig-name descname">ec2_tag_filters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentGroup.ec2_tag_filters" title="Permalink to this definition">¶</a></dt>
<dd><p>Tag filters associated with the deployment group. See the AWS docs for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The key of the tag filter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of the tag filter, either <code class="docutils literal notranslate"><span class="pre">KEY_ONLY</span></code>, <code class="docutils literal notranslate"><span class="pre">VALUE_ONLY</span></code>, or <code class="docutils literal notranslate"><span class="pre">KEY_AND_VALUE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value of the tag filter.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentGroup.ec2_tag_sets">
<code class="sig-name descname">ec2_tag_sets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentGroup.ec2_tag_sets" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block(s) of Tag filters associated with the deployment group, which are also referred to as tag groups (documented below). See the AWS docs for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ec2_tag_filters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Tag filters associated with the deployment group. See the AWS docs for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The key of the tag filter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of the tag filter, either <code class="docutils literal notranslate"><span class="pre">KEY_ONLY</span></code>, <code class="docutils literal notranslate"><span class="pre">VALUE_ONLY</span></code>, or <code class="docutils literal notranslate"><span class="pre">KEY_AND_VALUE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value of the tag filter.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentGroup.ecs_service">
<code class="sig-name descname">ecs_service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentGroup.ecs_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block(s) of the ECS services for a deployment group (documented below).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the ECS cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the ECS service.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentGroup.load_balancer_info">
<code class="sig-name descname">load_balancer_info</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentGroup.load_balancer_info" title="Permalink to this definition">¶</a></dt>
<dd><p>Single configuration block of the load balancer to use in a blue/green deployment (documented below).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">elbInfos</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The Classic Elastic Load Balancer to use in a deployment. Conflicts with <code class="docutils literal notranslate"><span class="pre">target_group_info</span></code> and <code class="docutils literal notranslate"><span class="pre">target_group_pair_info</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the load balancer that will be used to route traffic from original instances to replacement instances in a blue/green deployment. For in-place deployments, the name of the load balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment completes.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetGroupInfos</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The (Application/Network Load Balancer) target group to use in a deployment. Conflicts with <code class="docutils literal notranslate"><span class="pre">elb_info</span></code> and <code class="docutils literal notranslate"><span class="pre">target_group_pair_info</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment completes.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetGroupPairInfo</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The (Application/Network Load Balancer) target group pair to use in a deployment. Conflicts with <code class="docutils literal notranslate"><span class="pre">elb_info</span></code> and <code class="docutils literal notranslate"><span class="pre">target_group_info</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">prodTrafficRoute</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Configuration block for the production traffic route (documented below).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">listenerArns</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of Amazon Resource Names (ARNs) of the load balancer listeners.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Configuration blocks for a target group within a target group pair (documented below).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the target group.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">testTrafficRoute</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Configuration block for the test traffic route (documented below).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">listenerArns</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of Amazon Resource Names (ARNs) of the load balancer listeners.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentGroup.on_premises_instance_tag_filters">
<code class="sig-name descname">on_premises_instance_tag_filters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentGroup.on_premises_instance_tag_filters" title="Permalink to this definition">¶</a></dt>
<dd><p>On premise tag filters associated with the group. See the AWS docs for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The key of the tag filter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of the tag filter, either <code class="docutils literal notranslate"><span class="pre">KEY_ONLY</span></code>, <code class="docutils literal notranslate"><span class="pre">VALUE_ONLY</span></code>, or <code class="docutils literal notranslate"><span class="pre">KEY_AND_VALUE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value of the tag filter.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentGroup.service_role_arn">
<code class="sig-name descname">service_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentGroup.service_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The service role ARN that allows deployments.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentGroup.trigger_configurations">
<code class="sig-name descname">trigger_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentGroup.trigger_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block(s) of the triggers for the deployment group (documented below).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">triggerEvents</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The event type or types for which notifications are triggered. Some values that are supported: <code class="docutils literal notranslate"><span class="pre">DeploymentStart</span></code>, <code class="docutils literal notranslate"><span class="pre">DeploymentSuccess</span></code>, <code class="docutils literal notranslate"><span class="pre">DeploymentFailure</span></code>, <code class="docutils literal notranslate"><span class="pre">DeploymentStop</span></code>, <code class="docutils literal notranslate"><span class="pre">DeploymentRollback</span></code>, <code class="docutils literal notranslate"><span class="pre">InstanceStart</span></code>, <code class="docutils literal notranslate"><span class="pre">InstanceSuccess</span></code>, <code class="docutils literal notranslate"><span class="pre">InstanceFailure</span></code>.  See <a class="reference external" href="http://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-sns-event-notifications-create-trigger.html">the CodeDeploy documentation</a> for all possible values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">triggerName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the notification trigger.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">triggerTargetArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the SNS topic through which notifications are sent.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.codedeploy.DeploymentGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alarm_configuration=None</em>, <em class="sig-param">app_name=None</em>, <em class="sig-param">auto_rollback_configuration=None</em>, <em class="sig-param">autoscaling_groups=None</em>, <em class="sig-param">blue_green_deployment_config=None</em>, <em class="sig-param">deployment_config_name=None</em>, <em class="sig-param">deployment_group_name=None</em>, <em class="sig-param">deployment_style=None</em>, <em class="sig-param">ec2_tag_filters=None</em>, <em class="sig-param">ec2_tag_sets=None</em>, <em class="sig-param">ecs_service=None</em>, <em class="sig-param">load_balancer_info=None</em>, <em class="sig-param">on_premises_instance_tag_filters=None</em>, <em class="sig-param">service_role_arn=None</em>, <em class="sig-param">trigger_configurations=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DeploymentGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alarm_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block of alarms associated with the deployment group (documented below).</p></li>
<li><p><strong>app_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the application.</p></li>
<li><p><strong>auto_rollback_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block of the automatic rollback configuration associated with the deployment group (documented below).</p></li>
<li><p><strong>autoscaling_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Autoscaling groups associated with the deployment group.</p></li>
<li><p><strong>blue_green_deployment_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block of the blue/green deployment options for a deployment group (documented below).</p></li>
<li><p><strong>deployment_config_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the group’s deployment config. The default is “CodeDeployDefault.OneAtATime”.</p></li>
<li><p><strong>deployment_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the deployment group.</p></li>
<li><p><strong>deployment_style</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block of the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer (documented below).</p></li>
<li><p><strong>ec2_tag_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Tag filters associated with the deployment group. See the AWS docs for details.</p></li>
<li><p><strong>ec2_tag_sets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configuration block(s) of Tag filters associated with the deployment group, which are also referred to as tag groups (documented below). See the AWS docs for details.</p></li>
<li><p><strong>ecs_service</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block(s) of the ECS services for a deployment group (documented below).</p></li>
<li><p><strong>load_balancer_info</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Single configuration block of the load balancer to use in a blue/green deployment (documented below).</p></li>
<li><p><strong>on_premises_instance_tag_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – On premise tag filters associated with the group. See the AWS docs for details.</p></li>
<li><p><strong>service_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service role ARN that allows deployments.</p></li>
<li><p><strong>trigger_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configuration block(s) of the triggers for the deployment group (documented below).</p></li>
</ul>
</dd>
</dl>
<p>The <strong>alarm_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alarms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of alarms configured for the deployment group. <em>A maximum of 10 alarms can be added to a deployment group</em>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether the alarm configuration is enabled. This option is useful when you want to temporarily deactivate alarm monitoring for a deployment group without having to add the same alarms again later.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ignorePollAlarmFailure</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from CloudWatch. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">true</span></code>: The deployment will proceed even if alarm status information can’t be retrieved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">false</span></code>: The deployment will stop if alarm status information can’t be retrieved.</p></li>
</ul>
</li>
</ul>
<p>The <strong>auto_rollback_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether a defined automatic rollback configuration is currently enabled for this Deployment Group. If you enable automatic rollback, you must specify at least one event type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">events</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The event type or types that trigger a rollback. Supported types are <code class="docutils literal notranslate"><span class="pre">DEPLOYMENT_FAILURE</span></code> and <code class="docutils literal notranslate"><span class="pre">DEPLOYMENT_STOP_ON_ALARM</span></code>.</p></li>
</ul>
<p>The <strong>blue_green_deployment_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deploymentReadyOption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment (documented below).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">actionOnTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When to reroute traffic from an original environment to a replacement environment in a blue/green deployment.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">CONTINUE_DEPLOYMENT</span></code>: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">STOP_DEPLOYMENT</span></code>: Do not register new instances with load balancer unless traffic is rerouted manually. If traffic is not rerouted manually before the end of the specified wait period, the deployment status is changed to Stopped.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitTimeInMinutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of minutes to wait before the status of a blue/green deployment changed to Stopped if rerouting is not started manually. Applies only to the <code class="docutils literal notranslate"><span class="pre">STOP_DEPLOYMENT</span></code> option for <code class="docutils literal notranslate"><span class="pre">action_on_timeout</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">greenFleetProvisioningOption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information about how instances are provisioned for a replacement environment in a blue/green deployment (documented below).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The method used to add instances to a replacement environment.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">DISCOVER_EXISTING</span></code>: Use instances that already exist or will be created manually.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">COPY_AUTO_SCALING_GROUP</span></code>: Use settings from a specified <strong>Auto Scaling</strong> group to define and create instances in a new Auto Scaling group. <em>Exactly one Auto Scaling group must be specified</em> when selecting <code class="docutils literal notranslate"><span class="pre">COPY_AUTO_SCALING_GROUP</span></code>. Use <code class="docutils literal notranslate"><span class="pre">autoscaling_groups</span></code> to specify the Auto Scaling group.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">terminateBlueInstancesOnDeploymentSuccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Information about whether to terminate instances in the original fleet during a blue/green deployment (documented below).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The action to take on instances in the original environment after a successful blue/green deployment.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">TERMINATE</span></code>: Instances are terminated after a specified wait time.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">KEEP_ALIVE</span></code>: Instances are left running after they are deregistered from the load balancer and removed from the deployment group.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">terminationWaitTimeInMinutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.</p></li>
</ul>
</li>
</ul>
<p>The <strong>deployment_style</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deploymentOption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Indicates whether to route deployment traffic behind a load balancer. Valid Values are <code class="docutils literal notranslate"><span class="pre">WITH_TRAFFIC_CONTROL</span></code> or <code class="docutils literal notranslate"><span class="pre">WITHOUT_TRAFFIC_CONTROL</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">WITHOUT_TRAFFIC_CONTROL</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deploymentType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Indicates whether to run an in-place deployment or a blue/green deployment. Valid Values are <code class="docutils literal notranslate"><span class="pre">IN_PLACE</span></code> or <code class="docutils literal notranslate"><span class="pre">BLUE_GREEN</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">IN_PLACE</span></code>.</p></li>
</ul>
<p>The <strong>ec2_tag_filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The key of the tag filter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of the tag filter, either <code class="docutils literal notranslate"><span class="pre">KEY_ONLY</span></code>, <code class="docutils literal notranslate"><span class="pre">VALUE_ONLY</span></code>, or <code class="docutils literal notranslate"><span class="pre">KEY_AND_VALUE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the tag filter.</p></li>
</ul>
<p>The <strong>ec2_tag_sets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ec2_tag_filters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Tag filters associated with the deployment group. See the AWS docs for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The key of the tag filter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of the tag filter, either <code class="docutils literal notranslate"><span class="pre">KEY_ONLY</span></code>, <code class="docutils literal notranslate"><span class="pre">VALUE_ONLY</span></code>, or <code class="docutils literal notranslate"><span class="pre">KEY_AND_VALUE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the tag filter.</p></li>
</ul>
</li>
</ul>
<p>The <strong>ecs_service</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the ECS cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the ECS service.</p></li>
</ul>
<p>The <strong>load_balancer_info</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">elbInfos</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The Classic Elastic Load Balancer to use in a deployment. Conflicts with <code class="docutils literal notranslate"><span class="pre">target_group_info</span></code> and <code class="docutils literal notranslate"><span class="pre">target_group_pair_info</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the load balancer that will be used to route traffic from original instances to replacement instances in a blue/green deployment. For in-place deployments, the name of the load balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment completes.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetGroupInfos</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The (Application/Network Load Balancer) target group to use in a deployment. Conflicts with <code class="docutils literal notranslate"><span class="pre">elb_info</span></code> and <code class="docutils literal notranslate"><span class="pre">target_group_pair_info</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment completes.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetGroupPairInfo</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The (Application/Network Load Balancer) target group pair to use in a deployment. Conflicts with <code class="docutils literal notranslate"><span class="pre">elb_info</span></code> and <code class="docutils literal notranslate"><span class="pre">target_group_info</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">prodTrafficRoute</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block for the production traffic route (documented below).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">listenerArns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of Amazon Resource Names (ARNs) of the load balancer listeners.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Configuration blocks for a target group within a target group pair (documented below).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the target group.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">testTrafficRoute</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block for the test traffic route (documented below).</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">listenerArns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of Amazon Resource Names (ARNs) of the load balancer listeners.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<p>The <strong>on_premises_instance_tag_filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The key of the tag filter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of the tag filter, either <code class="docutils literal notranslate"><span class="pre">KEY_ONLY</span></code>, <code class="docutils literal notranslate"><span class="pre">VALUE_ONLY</span></code>, or <code class="docutils literal notranslate"><span class="pre">KEY_AND_VALUE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the tag filter.</p></li>
</ul>
<p>The <strong>trigger_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">triggerEvents</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The event type or types for which notifications are triggered. Some values that are supported: <code class="docutils literal notranslate"><span class="pre">DeploymentStart</span></code>, <code class="docutils literal notranslate"><span class="pre">DeploymentSuccess</span></code>, <code class="docutils literal notranslate"><span class="pre">DeploymentFailure</span></code>, <code class="docutils literal notranslate"><span class="pre">DeploymentStop</span></code>, <code class="docutils literal notranslate"><span class="pre">DeploymentRollback</span></code>, <code class="docutils literal notranslate"><span class="pre">InstanceStart</span></code>, <code class="docutils literal notranslate"><span class="pre">InstanceSuccess</span></code>, <code class="docutils literal notranslate"><span class="pre">InstanceFailure</span></code>.  See <a class="reference external" href="http://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-sns-event-notifications-create-trigger.html">the CodeDeploy documentation</a> for all possible values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">triggerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the notification trigger.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">triggerTargetArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the SNS topic through which notifications are sent.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.codedeploy.DeploymentGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.codedeploy.DeploymentGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
