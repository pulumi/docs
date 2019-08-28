---
title: Module codedeploy
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codedeploy_app.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codedeploy_app.html.markdown</a>.</p>
</div></blockquote>
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
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] compute_platform: The compute platform can either be <code class="docutils literal notranslate"><span class="pre">ECS</span></code>, <code class="docutils literal notranslate"><span class="pre">Lambda</span></code>, or <code class="docutils literal notranslate"><span class="pre">Server</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">Server</span></code>.
:param pulumi.Input[str] name: The name of the application.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codedeploy_app.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codedeploy_app.html.markdown</a>.</p>
</div></blockquote>
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
<li><p><strong>minimum_healthy_hosts</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A minimum_healthy_hosts block. Minimum Healthy Hosts are documented below.</p></li>
<li><p><strong>traffic_routing_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A traffic_routing_config block. Traffic Routing Config is documented below.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codedeploy_deployment_config.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codedeploy_deployment_config.html.markdown</a>.</p>
</div></blockquote>
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
<dd><p>A minimum_healthy_hosts block. Minimum Healthy Hosts are documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentConfig.traffic_routing_config">
<code class="sig-name descname">traffic_routing_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentConfig.traffic_routing_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A traffic_routing_config block. Traffic Routing Config is documented below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.codedeploy.DeploymentConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">compute_platform=None</em>, <em class="sig-param">deployment_config_id=None</em>, <em class="sig-param">deployment_config_name=None</em>, <em class="sig-param">minimum_healthy_hosts=None</em>, <em class="sig-param">traffic_routing_config=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DeploymentConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] compute_platform: The compute platform can be <code class="docutils literal notranslate"><span class="pre">Server</span></code>, <code class="docutils literal notranslate"><span class="pre">Lambda</span></code>, or <code class="docutils literal notranslate"><span class="pre">ECS</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">Server</span></code>.
:param pulumi.Input[str] deployment_config_id: The AWS Assigned deployment config id
:param pulumi.Input[str] deployment_config_name: The name of the deployment config.
:param pulumi.Input[dict] minimum_healthy_hosts: A minimum_healthy_hosts block. Minimum Healthy Hosts are documented below.
:param pulumi.Input[dict] traffic_routing_config: A traffic_routing_config block. Traffic Routing Config is documented below.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codedeploy_deployment_config.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codedeploy_deployment_config.html.markdown</a>.</p>
</div></blockquote>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codedeploy_deployment_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codedeploy_deployment_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentGroup.alarm_configuration">
<code class="sig-name descname">alarm_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentGroup.alarm_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block of alarms associated with the deployment group (documented below).</p>
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
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentGroup.ec2_tag_filters">
<code class="sig-name descname">ec2_tag_filters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentGroup.ec2_tag_filters" title="Permalink to this definition">¶</a></dt>
<dd><p>Tag filters associated with the deployment group. See the AWS docs for details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentGroup.ec2_tag_sets">
<code class="sig-name descname">ec2_tag_sets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentGroup.ec2_tag_sets" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block(s) of Tag filters associated with the deployment group, which are also referred to as tag groups (documented below). See the AWS docs for details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentGroup.ecs_service">
<code class="sig-name descname">ecs_service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentGroup.ecs_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block(s) of the ECS services for a deployment group (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentGroup.load_balancer_info">
<code class="sig-name descname">load_balancer_info</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentGroup.load_balancer_info" title="Permalink to this definition">¶</a></dt>
<dd><p>Single configuration block of the load balancer to use in a blue/green deployment (documented below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codedeploy.DeploymentGroup.on_premises_instance_tag_filters">
<code class="sig-name descname">on_premises_instance_tag_filters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentGroup.on_premises_instance_tag_filters" title="Permalink to this definition">¶</a></dt>
<dd><p>On premise tag filters associated with the group. See the AWS docs for details.</p>
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
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.codedeploy.DeploymentGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alarm_configuration=None</em>, <em class="sig-param">app_name=None</em>, <em class="sig-param">auto_rollback_configuration=None</em>, <em class="sig-param">autoscaling_groups=None</em>, <em class="sig-param">blue_green_deployment_config=None</em>, <em class="sig-param">deployment_config_name=None</em>, <em class="sig-param">deployment_group_name=None</em>, <em class="sig-param">deployment_style=None</em>, <em class="sig-param">ec2_tag_filters=None</em>, <em class="sig-param">ec2_tag_sets=None</em>, <em class="sig-param">ecs_service=None</em>, <em class="sig-param">load_balancer_info=None</em>, <em class="sig-param">on_premises_instance_tag_filters=None</em>, <em class="sig-param">service_role_arn=None</em>, <em class="sig-param">trigger_configurations=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codedeploy.DeploymentGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DeploymentGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[dict] alarm_configuration: Configuration block of alarms associated with the deployment group (documented below).
:param pulumi.Input[str] app_name: The name of the application.
:param pulumi.Input[dict] auto_rollback_configuration: Configuration block of the automatic rollback configuration associated with the deployment group (documented below).
:param pulumi.Input[list] autoscaling_groups: Autoscaling groups associated with the deployment group.
:param pulumi.Input[dict] blue_green_deployment_config: Configuration block of the blue/green deployment options for a deployment group (documented below).
:param pulumi.Input[str] deployment_config_name: The name of the group’s deployment config. The default is “CodeDeployDefault.OneAtATime”.
:param pulumi.Input[str] deployment_group_name: The name of the deployment group.
:param pulumi.Input[dict] deployment_style: Configuration block of the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer (documented below).
:param pulumi.Input[list] ec2_tag_filters: Tag filters associated with the deployment group. See the AWS docs for details.
:param pulumi.Input[list] ec2_tag_sets: Configuration block(s) of Tag filters associated with the deployment group, which are also referred to as tag groups (documented below). See the AWS docs for details.
:param pulumi.Input[dict] ecs_service: Configuration block(s) of the ECS services for a deployment group (documented below).
:param pulumi.Input[dict] load_balancer_info: Single configuration block of the load balancer to use in a blue/green deployment (documented below).
:param pulumi.Input[list] on_premises_instance_tag_filters: On premise tag filters associated with the group. See the AWS docs for details.
:param pulumi.Input[str] service_role_arn: The service role ARN that allows deployments.
:param pulumi.Input[list] trigger_configurations: Configuration block(s) of the triggers for the deployment group (documented below).</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codedeploy_deployment_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codedeploy_deployment_group.html.markdown</a>.</p>
</div></blockquote>
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
