<div class="section" id="module-pulumi_aws.opsworks">
<span id="opsworks"></span><h1>opsworks<a class="headerlink" href="#module-pulumi_aws.opsworks" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.opsworks.Application">
<em class="property">class </em><code class="descclassname">pulumi_aws.opsworks.</code><code class="descname">Application</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>app_sources=None</em>, <em>auto_bundle_on_deploy=None</em>, <em>aws_flow_ruby_settings=None</em>, <em>data_source_arn=None</em>, <em>data_source_database_name=None</em>, <em>data_source_type=None</em>, <em>description=None</em>, <em>document_root=None</em>, <em>domains=None</em>, <em>enable_ssl=None</em>, <em>environments=None</em>, <em>name=None</em>, <em>rails_env=None</em>, <em>short_name=None</em>, <em>ssl_configurations=None</em>, <em>stack_id=None</em>, <em>type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Application" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks application resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>app_sources</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – SCM configuration of the app as described below.</li>
<li><strong>auto_bundle_on_deploy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Run bundle install when deploying for application of type <cite>rails</cite>.</li>
<li><strong>aws_flow_ruby_settings</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify activity and workflow workers for your app using the aws-flow gem.</li>
<li><strong>data_source_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data source’s ARN.</li>
<li><strong>data_source_database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database name.</li>
<li><strong>data_source_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data source’s type one of <cite>AutoSelectOpsworksMysqlInstance</cite>, <cite>OpsworksMysqlInstance</cite>, or <cite>RdsDbInstance</cite>.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the app.</li>
<li><strong>document_root</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subfolder for the document root for application of type <cite>rails</cite>.</li>
<li><strong>domains</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of virtual host alias.</li>
<li><strong>enable_ssl</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable SSL for the app. This must be set in order to let <cite>ssl_configuration.private_key</cite>, <cite>ssl_configuration.certificate</cite> and <cite>ssl_configuration.chain</cite> take effect.</li>
<li><strong>environments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Object to define environment variables.  Object is described below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable name for the application.</li>
<li><strong>rails_env</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Rails environment for application of type <cite>rails</cite>.</li>
<li><strong>short_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short, machine-readable name for the application. This can only be defined on resource creation and ignored on resource update.</li>
<li><strong>ssl_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The SSL configuration of the app. Object is described below.</li>
<li><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the stack the application will belong to.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of source to use. For example, “archive”.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.app_sources">
<code class="descname">app_sources</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.app_sources" title="Permalink to this definition">¶</a></dt>
<dd><p>SCM configuration of the app as described below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.auto_bundle_on_deploy">
<code class="descname">auto_bundle_on_deploy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.auto_bundle_on_deploy" title="Permalink to this definition">¶</a></dt>
<dd><p>Run bundle install when deploying for application of type <cite>rails</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.aws_flow_ruby_settings">
<code class="descname">aws_flow_ruby_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.aws_flow_ruby_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify activity and workflow workers for your app using the aws-flow gem.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.data_source_arn">
<code class="descname">data_source_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.data_source_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The data source’s ARN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.data_source_database_name">
<code class="descname">data_source_database_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.data_source_database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The database name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.data_source_type">
<code class="descname">data_source_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.data_source_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The data source’s type one of <cite>AutoSelectOpsworksMysqlInstance</cite>, <cite>OpsworksMysqlInstance</cite>, or <cite>RdsDbInstance</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.document_root">
<code class="descname">document_root</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.document_root" title="Permalink to this definition">¶</a></dt>
<dd><p>Subfolder for the document root for application of type <cite>rails</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.domains">
<code class="descname">domains</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.domains" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of virtual host alias.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.enable_ssl">
<code class="descname">enable_ssl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.enable_ssl" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable SSL for the app. This must be set in order to let <cite>ssl_configuration.private_key</cite>, <cite>ssl_configuration.certificate</cite> and <cite>ssl_configuration.chain</cite> take effect.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.environments">
<code class="descname">environments</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.environments" title="Permalink to this definition">¶</a></dt>
<dd><p>Object to define environment variables.  Object is described below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.rails_env">
<code class="descname">rails_env</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.rails_env" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Rails environment for application of type <cite>rails</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.short_name">
<code class="descname">short_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.short_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A short, machine-readable name for the application. This can only be defined on resource creation and ignored on resource update.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.ssl_configurations">
<code class="descname">ssl_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.ssl_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSL configuration of the app. Object is described below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.stack_id">
<code class="descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the application will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Application.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Application.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of source to use. For example, “archive”.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.Application.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Application.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.Application.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Application.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.opsworks.CustomLayer">
<em class="property">class </em><code class="descclassname">pulumi_aws.opsworks.</code><code class="descname">CustomLayer</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>auto_assign_elastic_ips=None</em>, <em>auto_assign_public_ips=None</em>, <em>auto_healing=None</em>, <em>custom_configure_recipes=None</em>, <em>custom_deploy_recipes=None</em>, <em>custom_instance_profile_arn=None</em>, <em>custom_json=None</em>, <em>custom_security_group_ids=None</em>, <em>custom_setup_recipes=None</em>, <em>custom_shutdown_recipes=None</em>, <em>custom_undeploy_recipes=None</em>, <em>drain_elb_on_shutdown=None</em>, <em>ebs_volumes=None</em>, <em>elastic_load_balancer=None</em>, <em>install_updates_on_boot=None</em>, <em>instance_shutdown_timeout=None</em>, <em>name=None</em>, <em>short_name=None</em>, <em>stack_id=None</em>, <em>system_packages=None</em>, <em>use_ebs_optimized_instances=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks custom layer resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</li>
<li><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</li>
<li><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[list] custom_configure_recipes
:param pulumi.Input[list] custom_deploy_recipes
:param pulumi.Input[str] custom_instance_profile_arn: The ARN of an IAM profile that will be used for the layer’s instances.
:param pulumi.Input[str] custom_json: Custom JSON attributes to apply to the layer.
:param pulumi.Input[list] custom_security_group_ids: Ids for a set of security groups to apply to the layer’s instances.
:param pulumi.Input[list] custom_setup_recipes
:param pulumi.Input[list] custom_shutdown_recipes
:param pulumi.Input[list] custom_undeploy_recipes
:param pulumi.Input[bool] drain_elb_on_shutdown: Whether to enable Elastic Load Balancing connection draining.
:param pulumi.Input[list] ebs_volumes: <cite>ebs_volume</cite> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.
:param pulumi.Input[str] elastic_load_balancer: Name of an Elastic Load Balancer to attach to this layer
:param pulumi.Input[bool] install_updates_on_boot: Whether to install OS and package updates on each instance when it boots.
:param pulumi.Input[int] instance_shutdown_timeout: The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.
:param pulumi.Input[str] name: A human-readable name for the layer.
:param pulumi.Input[str] short_name: A short, machine-readable name for the layer, which will be used to identify it in the Chef node JSON.
:param pulumi.Input[str] stack_id: The id of the stack the layer will belong to.
:param pulumi.Input[list] system_packages: Names of a set of system packages to install on the layer’s instances.
:param pulumi.Input[bool] use_ebs_optimized_instances: Whether to use EBS-optimized instances.</p>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.auto_assign_elastic_ips">
<code class="descname">auto_assign_elastic_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.auto_assign_public_ips">
<code class="descname">auto_assign_public_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.auto_healing">
<code class="descname">auto_healing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.custom_instance_profile_arn">
<code class="descname">custom_instance_profile_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.custom_json">
<code class="descname">custom_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.custom_security_group_ids">
<code class="descname">custom_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.drain_elb_on_shutdown">
<code class="descname">drain_elb_on_shutdown</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.ebs_volumes">
<code class="descname">ebs_volumes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><cite>ebs_volume</cite> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.elastic_load_balancer">
<code class="descname">elastic_load_balancer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.install_updates_on_boot">
<code class="descname">install_updates_on_boot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.instance_shutdown_timeout">
<code class="descname">instance_shutdown_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.short_name">
<code class="descname">short_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.short_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A short, machine-readable name for the layer, which will be used to identify it in the Chef node JSON.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.stack_id">
<code class="descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.system_packages">
<code class="descname">system_packages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.CustomLayer.use_ebs_optimized_instances">
<code class="descname">use_ebs_optimized_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.CustomLayer.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.CustomLayer.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.CustomLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.opsworks.GangliaLayer">
<em class="property">class </em><code class="descclassname">pulumi_aws.opsworks.</code><code class="descname">GangliaLayer</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>auto_assign_elastic_ips=None</em>, <em>auto_assign_public_ips=None</em>, <em>auto_healing=None</em>, <em>custom_configure_recipes=None</em>, <em>custom_deploy_recipes=None</em>, <em>custom_instance_profile_arn=None</em>, <em>custom_json=None</em>, <em>custom_security_group_ids=None</em>, <em>custom_setup_recipes=None</em>, <em>custom_shutdown_recipes=None</em>, <em>custom_undeploy_recipes=None</em>, <em>drain_elb_on_shutdown=None</em>, <em>ebs_volumes=None</em>, <em>elastic_load_balancer=None</em>, <em>install_updates_on_boot=None</em>, <em>instance_shutdown_timeout=None</em>, <em>name=None</em>, <em>password=None</em>, <em>stack_id=None</em>, <em>system_packages=None</em>, <em>url=None</em>, <em>use_ebs_optimized_instances=None</em>, <em>username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks Ganglia layer resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</li>
<li><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</li>
<li><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[list] custom_configure_recipes
:param pulumi.Input[list] custom_deploy_recipes
:param pulumi.Input[str] custom_instance_profile_arn: The ARN of an IAM profile that will be used for the layer’s instances.
:param pulumi.Input[str] custom_json: Custom JSON attributes to apply to the layer.
:param pulumi.Input[list] custom_security_group_ids: Ids for a set of security groups to apply to the layer’s instances.
:param pulumi.Input[list] custom_setup_recipes
:param pulumi.Input[list] custom_shutdown_recipes
:param pulumi.Input[list] custom_undeploy_recipes
:param pulumi.Input[bool] drain_elb_on_shutdown: Whether to enable Elastic Load Balancing connection draining.
:param pulumi.Input[list] ebs_volumes: <cite>ebs_volume</cite> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.
:param pulumi.Input[str] elastic_load_balancer: Name of an Elastic Load Balancer to attach to this layer
:param pulumi.Input[bool] install_updates_on_boot: Whether to install OS and package updates on each instance when it boots.
:param pulumi.Input[int] instance_shutdown_timeout: The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.
:param pulumi.Input[str] name: A human-readable name for the layer.
:param pulumi.Input[str] password: The password to use for Ganglia.
:param pulumi.Input[str] stack_id: The id of the stack the layer will belong to.
:param pulumi.Input[list] system_packages: Names of a set of system packages to install on the layer’s instances.
:param pulumi.Input[str] url: The URL path to use for Ganglia. Defaults to “/ganglia”.
:param pulumi.Input[bool] use_ebs_optimized_instances: Whether to use EBS-optimized instances.
:param pulumi.Input[str] username: The username to use for Ganglia. Defaults to “opsworks”.</p>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.auto_assign_elastic_ips">
<code class="descname">auto_assign_elastic_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.auto_assign_public_ips">
<code class="descname">auto_assign_public_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.auto_healing">
<code class="descname">auto_healing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.custom_instance_profile_arn">
<code class="descname">custom_instance_profile_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.custom_json">
<code class="descname">custom_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.custom_security_group_ids">
<code class="descname">custom_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.drain_elb_on_shutdown">
<code class="descname">drain_elb_on_shutdown</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.ebs_volumes">
<code class="descname">ebs_volumes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><cite>ebs_volume</cite> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.elastic_load_balancer">
<code class="descname">elastic_load_balancer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.install_updates_on_boot">
<code class="descname">install_updates_on_boot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.instance_shutdown_timeout">
<code class="descname">instance_shutdown_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.password">
<code class="descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password to use for Ganglia.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.stack_id">
<code class="descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.system_packages">
<code class="descname">system_packages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.url">
<code class="descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL path to use for Ganglia. Defaults to “/ganglia”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.use_ebs_optimized_instances">
<code class="descname">use_ebs_optimized_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.GangliaLayer.username">
<code class="descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The username to use for Ganglia. Defaults to “opsworks”.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.GangliaLayer.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.GangliaLayer.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.GangliaLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.opsworks.HaproxyLayer">
<em class="property">class </em><code class="descclassname">pulumi_aws.opsworks.</code><code class="descname">HaproxyLayer</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>auto_assign_elastic_ips=None</em>, <em>auto_assign_public_ips=None</em>, <em>auto_healing=None</em>, <em>custom_configure_recipes=None</em>, <em>custom_deploy_recipes=None</em>, <em>custom_instance_profile_arn=None</em>, <em>custom_json=None</em>, <em>custom_security_group_ids=None</em>, <em>custom_setup_recipes=None</em>, <em>custom_shutdown_recipes=None</em>, <em>custom_undeploy_recipes=None</em>, <em>drain_elb_on_shutdown=None</em>, <em>ebs_volumes=None</em>, <em>elastic_load_balancer=None</em>, <em>healthcheck_method=None</em>, <em>healthcheck_url=None</em>, <em>install_updates_on_boot=None</em>, <em>instance_shutdown_timeout=None</em>, <em>name=None</em>, <em>stack_id=None</em>, <em>stats_enabled=None</em>, <em>stats_password=None</em>, <em>stats_url=None</em>, <em>stats_user=None</em>, <em>system_packages=None</em>, <em>use_ebs_optimized_instances=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks haproxy layer resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</li>
<li><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</li>
<li><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[list] custom_configure_recipes
:param pulumi.Input[list] custom_deploy_recipes
:param pulumi.Input[str] custom_instance_profile_arn: The ARN of an IAM profile that will be used for the layer’s instances.
:param pulumi.Input[str] custom_json: Custom JSON attributes to apply to the layer.
:param pulumi.Input[list] custom_security_group_ids: Ids for a set of security groups to apply to the layer’s instances.
:param pulumi.Input[list] custom_setup_recipes
:param pulumi.Input[list] custom_shutdown_recipes
:param pulumi.Input[list] custom_undeploy_recipes
:param pulumi.Input[bool] drain_elb_on_shutdown: Whether to enable Elastic Load Balancing connection draining.
:param pulumi.Input[list] ebs_volumes: <cite>ebs_volume</cite> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.
:param pulumi.Input[str] elastic_load_balancer: Name of an Elastic Load Balancer to attach to this layer
:param pulumi.Input[str] healthcheck_method: HTTP method to use for instance healthchecks. Defaults to “OPTIONS”.
:param pulumi.Input[str] healthcheck_url: URL path to use for instance healthchecks. Defaults to “/”.
:param pulumi.Input[bool] install_updates_on_boot: Whether to install OS and package updates on each instance when it boots.
:param pulumi.Input[int] instance_shutdown_timeout: The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.
:param pulumi.Input[str] name: A human-readable name for the layer.
:param pulumi.Input[str] stack_id: The id of the stack the layer will belong to.
:param pulumi.Input[bool] stats_enabled: Whether to enable HAProxy stats.
:param pulumi.Input[str] stats_password: The password to use for HAProxy stats.
:param pulumi.Input[str] stats_url: The HAProxy stats URL. Defaults to “/haproxy?stats”.
:param pulumi.Input[str] stats_user: The username for HAProxy stats. Defaults to “opsworks”.
:param pulumi.Input[list] system_packages: Names of a set of system packages to install on the layer’s instances.
:param pulumi.Input[bool] use_ebs_optimized_instances: Whether to use EBS-optimized instances.</p>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.auto_assign_elastic_ips">
<code class="descname">auto_assign_elastic_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.auto_assign_public_ips">
<code class="descname">auto_assign_public_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.auto_healing">
<code class="descname">auto_healing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.custom_instance_profile_arn">
<code class="descname">custom_instance_profile_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.custom_json">
<code class="descname">custom_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.custom_security_group_ids">
<code class="descname">custom_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.drain_elb_on_shutdown">
<code class="descname">drain_elb_on_shutdown</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.ebs_volumes">
<code class="descname">ebs_volumes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><cite>ebs_volume</cite> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.elastic_load_balancer">
<code class="descname">elastic_load_balancer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.healthcheck_method">
<code class="descname">healthcheck_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.healthcheck_method" title="Permalink to this definition">¶</a></dt>
<dd><p>HTTP method to use for instance healthchecks. Defaults to “OPTIONS”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.healthcheck_url">
<code class="descname">healthcheck_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.healthcheck_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL path to use for instance healthchecks. Defaults to “/”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.install_updates_on_boot">
<code class="descname">install_updates_on_boot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.instance_shutdown_timeout">
<code class="descname">instance_shutdown_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.stack_id">
<code class="descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.stats_enabled">
<code class="descname">stats_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.stats_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable HAProxy stats.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.stats_password">
<code class="descname">stats_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.stats_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password to use for HAProxy stats.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.stats_url">
<code class="descname">stats_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.stats_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The HAProxy stats URL. Defaults to “/haproxy?stats”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.stats_user">
<code class="descname">stats_user</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.stats_user" title="Permalink to this definition">¶</a></dt>
<dd><p>The username for HAProxy stats. Defaults to “opsworks”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.system_packages">
<code class="descname">system_packages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.HaproxyLayer.use_ebs_optimized_instances">
<code class="descname">use_ebs_optimized_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.HaproxyLayer.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.HaproxyLayer.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.HaproxyLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.opsworks.Instance">
<em class="property">class </em><code class="descclassname">pulumi_aws.opsworks.</code><code class="descname">Instance</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>agent_version=None</em>, <em>ami_id=None</em>, <em>architecture=None</em>, <em>auto_scaling_type=None</em>, <em>availability_zone=None</em>, <em>created_at=None</em>, <em>delete_ebs=None</em>, <em>delete_eip=None</em>, <em>ebs_block_devices=None</em>, <em>ebs_optimized=None</em>, <em>ecs_cluster_arn=None</em>, <em>elastic_ip=None</em>, <em>ephemeral_block_devices=None</em>, <em>hostname=None</em>, <em>infrastructure_class=None</em>, <em>install_updates_on_boot=None</em>, <em>instance_profile_arn=None</em>, <em>instance_type=None</em>, <em>last_service_error_id=None</em>, <em>layer_ids=None</em>, <em>os=None</em>, <em>platform=None</em>, <em>private_dns=None</em>, <em>private_ip=None</em>, <em>public_dns=None</em>, <em>public_ip=None</em>, <em>registered_by=None</em>, <em>reported_agent_version=None</em>, <em>reported_os_family=None</em>, <em>reported_os_name=None</em>, <em>reported_os_version=None</em>, <em>root_block_devices=None</em>, <em>root_device_type=None</em>, <em>root_device_volume_id=None</em>, <em>security_group_ids=None</em>, <em>ssh_host_dsa_key_fingerprint=None</em>, <em>ssh_host_rsa_key_fingerprint=None</em>, <em>ssh_key_name=None</em>, <em>stack_id=None</em>, <em>state=None</em>, <em>status=None</em>, <em>subnet_id=None</em>, <em>tenancy=None</em>, <em>virtualization_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks instance resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>agent_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS OpsWorks agent to install.  Defaults to <cite>“INHERIT”</cite>.</li>
<li><strong>ami_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AMI to use for the instance.  If an AMI is specified, <cite>os</cite> must be <cite>“Custom”</cite>.</li>
<li><strong>architecture</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Machine architecture for created instances.  Can be either <cite>“x86_64”</cite> (the default) or <cite>“i386”</cite></li>
<li><strong>auto_scaling_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates load-based or time-based instances.  If set, can be either: <cite>“load”</cite> or <cite>“timer”</cite>.</li>
<li><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the availability zone where instances will be created
by default.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] created_at
:param pulumi.Input[bool] delete_ebs
:param pulumi.Input[bool] delete_eip
:param pulumi.Input[list] ebs_block_devices: Additional EBS block devices to attach to the</p>
<blockquote>
<div>instance.  See Block Devices below for details.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>ebs_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the launched EC2 instance will be EBS-optimized.</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] ecs_cluster_arn
:param pulumi.Input[str] elastic_ip
:param pulumi.Input[list] ephemeral_block_devices: Customize Ephemeral (also known as</p>
<blockquote>
<div>“Instance Store”) volumes on the instance. See Block Devices below for details.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance’s host name.</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] infrastructure_class
:param pulumi.Input[bool] install_updates_on_boot: Controls where to install OS and package updates when the instance boots.  Defaults to <cite>true</cite>.
:param pulumi.Input[str] instance_profile_arn
:param pulumi.Input[str] instance_type: The type of instance to start
:param pulumi.Input[str] last_service_error_id
:param pulumi.Input[list] layer_ids: The ids of the layers the instance will belong to.
:param pulumi.Input[str] os: Name of operating system that will be installed.
:param pulumi.Input[str] platform
:param pulumi.Input[str] private_dns: The private DNS name assigned to the instance. Can only be</p>
<blockquote>
<div>used inside the Amazon EC2, and only available if you’ve enabled DNS hostnames
for your VPC</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>private_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private IP address assigned to the instance</li>
<li><strong>public_dns</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public DNS name assigned to the instance. For EC2-VPC, this
is only available if you’ve enabled DNS hostnames for your VPC</li>
<li><strong>public_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public IP address assigned to the instance, if applicable.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] registered_by
:param pulumi.Input[str] reported_agent_version
:param pulumi.Input[str] reported_os_family
:param pulumi.Input[str] reported_os_name
:param pulumi.Input[str] reported_os_version
:param pulumi.Input[list] root_block_devices: Customize details about the root block</p>
<blockquote>
<div>device of the instance. See Block Devices below for details.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>root_device_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the type of root device instances will have by default.  Can be either <cite>“ebs”</cite> or <cite>“instance-store”</cite></td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] root_device_volume_id
:param pulumi.Input[list] security_group_ids: The associated security groups.
:param pulumi.Input[str] ssh_host_dsa_key_fingerprint
:param pulumi.Input[str] ssh_host_rsa_key_fingerprint
:param pulumi.Input[str] ssh_key_name: Name of the SSH keypair that instances will have by default.
:param pulumi.Input[str] stack_id: The id of the stack the instance will belong to.
:param pulumi.Input[str] state: The desired state of the instance.  Can be either <cite>“running”</cite> or <cite>“stopped”</cite>.
:param pulumi.Input[str] status
:param pulumi.Input[str] subnet_id: Subnet ID to attach to
:param pulumi.Input[str] tenancy: Instance tenancy to use. Can be one of <cite>“default”</cite>, <cite>“dedicated”</cite> or <cite>“host”</cite>
:param pulumi.Input[str] virtualization_type: Keyword to choose what virtualization mode created instances</p>
<blockquote>
<div>will use. Can be either <cite>“paravirtual”</cite> or <cite>“hvm”</cite>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.agent_version">
<code class="descname">agent_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.agent_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS OpsWorks agent to install.  Defaults to <cite>“INHERIT”</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.ami_id">
<code class="descname">ami_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.ami_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AMI to use for the instance.  If an AMI is specified, <cite>os</cite> must be <cite>“Custom”</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.architecture">
<code class="descname">architecture</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.architecture" title="Permalink to this definition">¶</a></dt>
<dd><p>Machine architecture for created instances.  Can be either <cite>“x86_64”</cite> (the default) or <cite>“i386”</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.auto_scaling_type">
<code class="descname">auto_scaling_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.auto_scaling_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates load-based or time-based instances.  If set, can be either: <cite>“load”</cite> or <cite>“timer”</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the availability zone where instances will be created
by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.ebs_block_devices">
<code class="descname">ebs_block_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.ebs_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Additional EBS block devices to attach to the
instance.  See Block Devices below for details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.ebs_optimized">
<code class="descname">ebs_optimized</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.ebs_optimized" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the launched EC2 instance will be EBS-optimized.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.ec2_instance_id">
<code class="descname">ec2_instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.ec2_instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>EC2 instance ID</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.ephemeral_block_devices">
<code class="descname">ephemeral_block_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.ephemeral_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Customize Ephemeral (also known as
“Instance Store”) volumes on the instance. See Block Devices below for details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.hostname">
<code class="descname">hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance’s host name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.install_updates_on_boot">
<code class="descname">install_updates_on_boot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls where to install OS and package updates when the instance boots.  Defaults to <cite>true</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.instance_type">
<code class="descname">instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of instance to start</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.layer_ids">
<code class="descname">layer_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.layer_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The ids of the layers the instance will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.os">
<code class="descname">os</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.os" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of operating system that will be installed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.private_dns">
<code class="descname">private_dns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.private_dns" title="Permalink to this definition">¶</a></dt>
<dd><p>The private DNS name assigned to the instance. Can only be
used inside the Amazon EC2, and only available if you’ve enabled DNS hostnames
for your VPC</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.private_ip">
<code class="descname">private_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.private_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The private IP address assigned to the instance</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.public_dns">
<code class="descname">public_dns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.public_dns" title="Permalink to this definition">¶</a></dt>
<dd><p>The public DNS name assigned to the instance. For EC2-VPC, this
is only available if you’ve enabled DNS hostnames for your VPC</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.public_ip">
<code class="descname">public_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.public_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The public IP address assigned to the instance, if applicable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.root_block_devices">
<code class="descname">root_block_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.root_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Customize details about the root block
device of the instance. See Block Devices below for details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.root_device_type">
<code class="descname">root_device_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.root_device_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the type of root device instances will have by default.  Can be either <cite>“ebs”</cite> or <cite>“instance-store”</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.security_group_ids">
<code class="descname">security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The associated security groups.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.ssh_key_name">
<code class="descname">ssh_key_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.ssh_key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the SSH keypair that instances will have by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.stack_id">
<code class="descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the instance will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired state of the instance.  Can be either <cite>“running”</cite> or <cite>“stopped”</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.subnet_id">
<code class="descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Subnet ID to attach to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.tenancy">
<code class="descname">tenancy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.tenancy" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance tenancy to use. Can be one of <cite>“default”</cite>, <cite>“dedicated”</cite> or <cite>“host”</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Instance.virtualization_type">
<code class="descname">virtualization_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Instance.virtualization_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Keyword to choose what virtualization mode created instances
will use. Can be either <cite>“paravirtual”</cite> or <cite>“hvm”</cite>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.Instance.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.Instance.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.opsworks.JavaAppLayer">
<em class="property">class </em><code class="descclassname">pulumi_aws.opsworks.</code><code class="descname">JavaAppLayer</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>app_server=None</em>, <em>app_server_version=None</em>, <em>auto_assign_elastic_ips=None</em>, <em>auto_assign_public_ips=None</em>, <em>auto_healing=None</em>, <em>custom_configure_recipes=None</em>, <em>custom_deploy_recipes=None</em>, <em>custom_instance_profile_arn=None</em>, <em>custom_json=None</em>, <em>custom_security_group_ids=None</em>, <em>custom_setup_recipes=None</em>, <em>custom_shutdown_recipes=None</em>, <em>custom_undeploy_recipes=None</em>, <em>drain_elb_on_shutdown=None</em>, <em>ebs_volumes=None</em>, <em>elastic_load_balancer=None</em>, <em>install_updates_on_boot=None</em>, <em>instance_shutdown_timeout=None</em>, <em>jvm_options=None</em>, <em>jvm_type=None</em>, <em>jvm_version=None</em>, <em>name=None</em>, <em>stack_id=None</em>, <em>system_packages=None</em>, <em>use_ebs_optimized_instances=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks Java application layer resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>app_server</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Keyword for the application container to use. Defaults to “tomcat”.</li>
<li><strong>app_server_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of the selected application container to use. Defaults to “7”.</li>
<li><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</li>
<li><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</li>
<li><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[list] custom_configure_recipes
:param pulumi.Input[list] custom_deploy_recipes
:param pulumi.Input[str] custom_instance_profile_arn: The ARN of an IAM profile that will be used for the layer’s instances.
:param pulumi.Input[str] custom_json: Custom JSON attributes to apply to the layer.
:param pulumi.Input[list] custom_security_group_ids: Ids for a set of security groups to apply to the layer’s instances.
:param pulumi.Input[list] custom_setup_recipes
:param pulumi.Input[list] custom_shutdown_recipes
:param pulumi.Input[list] custom_undeploy_recipes
:param pulumi.Input[bool] drain_elb_on_shutdown: Whether to enable Elastic Load Balancing connection draining.
:param pulumi.Input[list] ebs_volumes: <cite>ebs_volume</cite> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.
:param pulumi.Input[str] elastic_load_balancer: Name of an Elastic Load Balancer to attach to this layer
:param pulumi.Input[bool] install_updates_on_boot: Whether to install OS and package updates on each instance when it boots.
:param pulumi.Input[int] instance_shutdown_timeout: The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.
:param pulumi.Input[str] jvm_options: Options to set for the JVM.
:param pulumi.Input[str] jvm_type: Keyword for the type of JVM to use. Defaults to <cite>openjdk</cite>.
:param pulumi.Input[str] jvm_version: Version of JVM to use. Defaults to “7”.
:param pulumi.Input[str] name: A human-readable name for the layer.
:param pulumi.Input[str] stack_id: The id of the stack the layer will belong to.
:param pulumi.Input[list] system_packages: Names of a set of system packages to install on the layer’s instances.
:param pulumi.Input[bool] use_ebs_optimized_instances: Whether to use EBS-optimized instances.</p>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.app_server">
<code class="descname">app_server</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.app_server" title="Permalink to this definition">¶</a></dt>
<dd><p>Keyword for the application container to use. Defaults to “tomcat”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.app_server_version">
<code class="descname">app_server_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.app_server_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of the selected application container to use. Defaults to “7”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.auto_assign_elastic_ips">
<code class="descname">auto_assign_elastic_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.auto_assign_public_ips">
<code class="descname">auto_assign_public_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.auto_healing">
<code class="descname">auto_healing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.custom_instance_profile_arn">
<code class="descname">custom_instance_profile_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.custom_json">
<code class="descname">custom_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.custom_security_group_ids">
<code class="descname">custom_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.drain_elb_on_shutdown">
<code class="descname">drain_elb_on_shutdown</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.ebs_volumes">
<code class="descname">ebs_volumes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><cite>ebs_volume</cite> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.elastic_load_balancer">
<code class="descname">elastic_load_balancer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.install_updates_on_boot">
<code class="descname">install_updates_on_boot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.instance_shutdown_timeout">
<code class="descname">instance_shutdown_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.jvm_options">
<code class="descname">jvm_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.jvm_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Options to set for the JVM.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.jvm_type">
<code class="descname">jvm_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.jvm_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Keyword for the type of JVM to use. Defaults to <cite>openjdk</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.jvm_version">
<code class="descname">jvm_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.jvm_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of JVM to use. Defaults to “7”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.stack_id">
<code class="descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.system_packages">
<code class="descname">system_packages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.JavaAppLayer.use_ebs_optimized_instances">
<code class="descname">use_ebs_optimized_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.JavaAppLayer.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.JavaAppLayer.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.JavaAppLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.opsworks.MemcachedLayer">
<em class="property">class </em><code class="descclassname">pulumi_aws.opsworks.</code><code class="descname">MemcachedLayer</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>allocated_memory=None</em>, <em>auto_assign_elastic_ips=None</em>, <em>auto_assign_public_ips=None</em>, <em>auto_healing=None</em>, <em>custom_configure_recipes=None</em>, <em>custom_deploy_recipes=None</em>, <em>custom_instance_profile_arn=None</em>, <em>custom_json=None</em>, <em>custom_security_group_ids=None</em>, <em>custom_setup_recipes=None</em>, <em>custom_shutdown_recipes=None</em>, <em>custom_undeploy_recipes=None</em>, <em>drain_elb_on_shutdown=None</em>, <em>ebs_volumes=None</em>, <em>elastic_load_balancer=None</em>, <em>install_updates_on_boot=None</em>, <em>instance_shutdown_timeout=None</em>, <em>name=None</em>, <em>stack_id=None</em>, <em>system_packages=None</em>, <em>use_ebs_optimized_instances=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks memcached layer resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>allocated_memory</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Amount of memory to allocate for the cache on each instance, in megabytes. Defaults to 512MB.</li>
<li><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</li>
<li><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</li>
<li><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[list] custom_configure_recipes
:param pulumi.Input[list] custom_deploy_recipes
:param pulumi.Input[str] custom_instance_profile_arn: The ARN of an IAM profile that will be used for the layer’s instances.
:param pulumi.Input[str] custom_json: Custom JSON attributes to apply to the layer.
:param pulumi.Input[list] custom_security_group_ids: Ids for a set of security groups to apply to the layer’s instances.
:param pulumi.Input[list] custom_setup_recipes
:param pulumi.Input[list] custom_shutdown_recipes
:param pulumi.Input[list] custom_undeploy_recipes
:param pulumi.Input[bool] drain_elb_on_shutdown: Whether to enable Elastic Load Balancing connection draining.
:param pulumi.Input[list] ebs_volumes: <cite>ebs_volume</cite> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.
:param pulumi.Input[str] elastic_load_balancer: Name of an Elastic Load Balancer to attach to this layer
:param pulumi.Input[bool] install_updates_on_boot: Whether to install OS and package updates on each instance when it boots.
:param pulumi.Input[int] instance_shutdown_timeout: The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.
:param pulumi.Input[str] name: A human-readable name for the layer.
:param pulumi.Input[str] stack_id: The id of the stack the layer will belong to.
:param pulumi.Input[list] system_packages: Names of a set of system packages to install on the layer’s instances.
:param pulumi.Input[bool] use_ebs_optimized_instances: Whether to use EBS-optimized instances.</p>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.allocated_memory">
<code class="descname">allocated_memory</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.allocated_memory" title="Permalink to this definition">¶</a></dt>
<dd><p>Amount of memory to allocate for the cache on each instance, in megabytes. Defaults to 512MB.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.auto_assign_elastic_ips">
<code class="descname">auto_assign_elastic_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.auto_assign_public_ips">
<code class="descname">auto_assign_public_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.auto_healing">
<code class="descname">auto_healing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.custom_instance_profile_arn">
<code class="descname">custom_instance_profile_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.custom_json">
<code class="descname">custom_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.custom_security_group_ids">
<code class="descname">custom_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.drain_elb_on_shutdown">
<code class="descname">drain_elb_on_shutdown</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.ebs_volumes">
<code class="descname">ebs_volumes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><cite>ebs_volume</cite> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.elastic_load_balancer">
<code class="descname">elastic_load_balancer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.install_updates_on_boot">
<code class="descname">install_updates_on_boot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.instance_shutdown_timeout">
<code class="descname">instance_shutdown_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.stack_id">
<code class="descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.system_packages">
<code class="descname">system_packages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MemcachedLayer.use_ebs_optimized_instances">
<code class="descname">use_ebs_optimized_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.MemcachedLayer.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.MemcachedLayer.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.MemcachedLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.opsworks.MysqlLayer">
<em class="property">class </em><code class="descclassname">pulumi_aws.opsworks.</code><code class="descname">MysqlLayer</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>auto_assign_elastic_ips=None</em>, <em>auto_assign_public_ips=None</em>, <em>auto_healing=None</em>, <em>custom_configure_recipes=None</em>, <em>custom_deploy_recipes=None</em>, <em>custom_instance_profile_arn=None</em>, <em>custom_json=None</em>, <em>custom_security_group_ids=None</em>, <em>custom_setup_recipes=None</em>, <em>custom_shutdown_recipes=None</em>, <em>custom_undeploy_recipes=None</em>, <em>drain_elb_on_shutdown=None</em>, <em>ebs_volumes=None</em>, <em>elastic_load_balancer=None</em>, <em>install_updates_on_boot=None</em>, <em>instance_shutdown_timeout=None</em>, <em>name=None</em>, <em>root_password=None</em>, <em>root_password_on_all_instances=None</em>, <em>stack_id=None</em>, <em>system_packages=None</em>, <em>use_ebs_optimized_instances=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks MySQL layer resource.</p>
<p>&gt; <strong>Note:</strong> All arguments including the root password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">https://www.terraform.io/docs/state/sensitive-data.html</a>).</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</li>
<li><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</li>
<li><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[list] custom_configure_recipes
:param pulumi.Input[list] custom_deploy_recipes
:param pulumi.Input[str] custom_instance_profile_arn: The ARN of an IAM profile that will be used for the layer’s instances.
:param pulumi.Input[str] custom_json: Custom JSON attributes to apply to the layer.
:param pulumi.Input[list] custom_security_group_ids: Ids for a set of security groups to apply to the layer’s instances.
:param pulumi.Input[list] custom_setup_recipes
:param pulumi.Input[list] custom_shutdown_recipes
:param pulumi.Input[list] custom_undeploy_recipes
:param pulumi.Input[bool] drain_elb_on_shutdown: Whether to enable Elastic Load Balancing connection draining.
:param pulumi.Input[list] ebs_volumes: <cite>ebs_volume</cite> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.
:param pulumi.Input[str] elastic_load_balancer: Name of an Elastic Load Balancer to attach to this layer
:param pulumi.Input[bool] install_updates_on_boot: Whether to install OS and package updates on each instance when it boots.
:param pulumi.Input[int] instance_shutdown_timeout: The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.
:param pulumi.Input[str] name: A human-readable name for the layer.
:param pulumi.Input[str] root_password: Root password to use for MySQL.
:param pulumi.Input[bool] root_password_on_all_instances: Whether to set the root user password to all instances in the stack so they can access the instances in this layer.
:param pulumi.Input[str] stack_id: The id of the stack the layer will belong to.
:param pulumi.Input[list] system_packages: Names of a set of system packages to install on the layer’s instances.
:param pulumi.Input[bool] use_ebs_optimized_instances: Whether to use EBS-optimized instances.</p>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.auto_assign_elastic_ips">
<code class="descname">auto_assign_elastic_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.auto_assign_public_ips">
<code class="descname">auto_assign_public_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.auto_healing">
<code class="descname">auto_healing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.custom_instance_profile_arn">
<code class="descname">custom_instance_profile_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.custom_json">
<code class="descname">custom_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.custom_security_group_ids">
<code class="descname">custom_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.drain_elb_on_shutdown">
<code class="descname">drain_elb_on_shutdown</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.ebs_volumes">
<code class="descname">ebs_volumes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><cite>ebs_volume</cite> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.elastic_load_balancer">
<code class="descname">elastic_load_balancer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.install_updates_on_boot">
<code class="descname">install_updates_on_boot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.instance_shutdown_timeout">
<code class="descname">instance_shutdown_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.root_password">
<code class="descname">root_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.root_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Root password to use for MySQL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.root_password_on_all_instances">
<code class="descname">root_password_on_all_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.root_password_on_all_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to set the root user password to all instances in the stack so they can access the instances in this layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.stack_id">
<code class="descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.system_packages">
<code class="descname">system_packages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.MysqlLayer.use_ebs_optimized_instances">
<code class="descname">use_ebs_optimized_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.MysqlLayer.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.MysqlLayer.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.MysqlLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.opsworks.NodejsAppLayer">
<em class="property">class </em><code class="descclassname">pulumi_aws.opsworks.</code><code class="descname">NodejsAppLayer</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>auto_assign_elastic_ips=None</em>, <em>auto_assign_public_ips=None</em>, <em>auto_healing=None</em>, <em>custom_configure_recipes=None</em>, <em>custom_deploy_recipes=None</em>, <em>custom_instance_profile_arn=None</em>, <em>custom_json=None</em>, <em>custom_security_group_ids=None</em>, <em>custom_setup_recipes=None</em>, <em>custom_shutdown_recipes=None</em>, <em>custom_undeploy_recipes=None</em>, <em>drain_elb_on_shutdown=None</em>, <em>ebs_volumes=None</em>, <em>elastic_load_balancer=None</em>, <em>install_updates_on_boot=None</em>, <em>instance_shutdown_timeout=None</em>, <em>name=None</em>, <em>nodejs_version=None</em>, <em>stack_id=None</em>, <em>system_packages=None</em>, <em>use_ebs_optimized_instances=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks NodeJS application layer resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</li>
<li><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</li>
<li><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[list] custom_configure_recipes
:param pulumi.Input[list] custom_deploy_recipes
:param pulumi.Input[str] custom_instance_profile_arn: The ARN of an IAM profile that will be used for the layer’s instances.
:param pulumi.Input[str] custom_json: Custom JSON attributes to apply to the layer.
:param pulumi.Input[list] custom_security_group_ids: Ids for a set of security groups to apply to the layer’s instances.
:param pulumi.Input[list] custom_setup_recipes
:param pulumi.Input[list] custom_shutdown_recipes
:param pulumi.Input[list] custom_undeploy_recipes
:param pulumi.Input[bool] drain_elb_on_shutdown: Whether to enable Elastic Load Balancing connection draining.
:param pulumi.Input[list] ebs_volumes: <cite>ebs_volume</cite> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.
:param pulumi.Input[str] elastic_load_balancer: Name of an Elastic Load Balancer to attach to this layer
:param pulumi.Input[bool] install_updates_on_boot: Whether to install OS and package updates on each instance when it boots.
:param pulumi.Input[int] instance_shutdown_timeout: The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.
:param pulumi.Input[str] name: A human-readable name for the layer.
:param pulumi.Input[str] nodejs_version: The version of NodeJS to use. Defaults to “0.10.38”.
:param pulumi.Input[str] stack_id: The id of the stack the layer will belong to.
:param pulumi.Input[list] system_packages: Names of a set of system packages to install on the layer’s instances.
:param pulumi.Input[bool] use_ebs_optimized_instances: Whether to use EBS-optimized instances.</p>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.auto_assign_elastic_ips">
<code class="descname">auto_assign_elastic_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.auto_assign_public_ips">
<code class="descname">auto_assign_public_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.auto_healing">
<code class="descname">auto_healing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.custom_instance_profile_arn">
<code class="descname">custom_instance_profile_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.custom_json">
<code class="descname">custom_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.custom_security_group_ids">
<code class="descname">custom_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.drain_elb_on_shutdown">
<code class="descname">drain_elb_on_shutdown</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.ebs_volumes">
<code class="descname">ebs_volumes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><cite>ebs_volume</cite> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.elastic_load_balancer">
<code class="descname">elastic_load_balancer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.install_updates_on_boot">
<code class="descname">install_updates_on_boot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.instance_shutdown_timeout">
<code class="descname">instance_shutdown_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.nodejs_version">
<code class="descname">nodejs_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.nodejs_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of NodeJS to use. Defaults to “0.10.38”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.stack_id">
<code class="descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.system_packages">
<code class="descname">system_packages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.use_ebs_optimized_instances">
<code class="descname">use_ebs_optimized_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.NodejsAppLayer.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.NodejsAppLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.opsworks.Permission">
<em class="property">class </em><code class="descclassname">pulumi_aws.opsworks.</code><code class="descname">Permission</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>allow_ssh=None</em>, <em>allow_sudo=None</em>, <em>level=None</em>, <em>stack_id=None</em>, <em>user_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Permission" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks permission resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>allow_ssh</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user is allowed to use SSH to communicate with the instance</li>
<li><strong>allow_sudo</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user is allowed to use sudo to elevate privileges</li>
<li><strong>level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The users permission level. Mus be one of <cite>deny</cite>, <cite>show</cite>, <cite>deploy</cite>, <cite>manage</cite>, <cite>iam_only</cite></li>
<li><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The stack to set the permissions for</li>
<li><strong>user_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s IAM ARN to set permissions for</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.Permission.allow_ssh">
<code class="descname">allow_ssh</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Permission.allow_ssh" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user is allowed to use SSH to communicate with the instance</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Permission.allow_sudo">
<code class="descname">allow_sudo</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Permission.allow_sudo" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user is allowed to use sudo to elevate privileges</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Permission.level">
<code class="descname">level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Permission.level" title="Permalink to this definition">¶</a></dt>
<dd><p>The users permission level. Mus be one of <cite>deny</cite>, <cite>show</cite>, <cite>deploy</cite>, <cite>manage</cite>, <cite>iam_only</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Permission.stack_id">
<code class="descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Permission.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The stack to set the permissions for</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Permission.user_arn">
<code class="descname">user_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Permission.user_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The user’s IAM ARN to set permissions for</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.Permission.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Permission.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.Permission.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Permission.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.opsworks.PhpAppLayer">
<em class="property">class </em><code class="descclassname">pulumi_aws.opsworks.</code><code class="descname">PhpAppLayer</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>auto_assign_elastic_ips=None</em>, <em>auto_assign_public_ips=None</em>, <em>auto_healing=None</em>, <em>custom_configure_recipes=None</em>, <em>custom_deploy_recipes=None</em>, <em>custom_instance_profile_arn=None</em>, <em>custom_json=None</em>, <em>custom_security_group_ids=None</em>, <em>custom_setup_recipes=None</em>, <em>custom_shutdown_recipes=None</em>, <em>custom_undeploy_recipes=None</em>, <em>drain_elb_on_shutdown=None</em>, <em>ebs_volumes=None</em>, <em>elastic_load_balancer=None</em>, <em>install_updates_on_boot=None</em>, <em>instance_shutdown_timeout=None</em>, <em>name=None</em>, <em>stack_id=None</em>, <em>system_packages=None</em>, <em>use_ebs_optimized_instances=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks PHP application layer resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</li>
<li><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</li>
<li><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[list] custom_configure_recipes
:param pulumi.Input[list] custom_deploy_recipes
:param pulumi.Input[str] custom_instance_profile_arn: The ARN of an IAM profile that will be used for the layer’s instances.
:param pulumi.Input[str] custom_json: Custom JSON attributes to apply to the layer.
:param pulumi.Input[list] custom_security_group_ids: Ids for a set of security groups to apply to the layer’s instances.
:param pulumi.Input[list] custom_setup_recipes
:param pulumi.Input[list] custom_shutdown_recipes
:param pulumi.Input[list] custom_undeploy_recipes
:param pulumi.Input[bool] drain_elb_on_shutdown: Whether to enable Elastic Load Balancing connection draining.
:param pulumi.Input[list] ebs_volumes: <cite>ebs_volume</cite> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.
:param pulumi.Input[str] elastic_load_balancer: Name of an Elastic Load Balancer to attach to this layer
:param pulumi.Input[bool] install_updates_on_boot: Whether to install OS and package updates on each instance when it boots.
:param pulumi.Input[int] instance_shutdown_timeout: The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.
:param pulumi.Input[str] name: A human-readable name for the layer.
:param pulumi.Input[str] stack_id: The id of the stack the layer will belong to.
:param pulumi.Input[list] system_packages: Names of a set of system packages to install on the layer’s instances.
:param pulumi.Input[bool] use_ebs_optimized_instances: Whether to use EBS-optimized instances.</p>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.auto_assign_elastic_ips">
<code class="descname">auto_assign_elastic_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.auto_assign_public_ips">
<code class="descname">auto_assign_public_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.auto_healing">
<code class="descname">auto_healing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.custom_instance_profile_arn">
<code class="descname">custom_instance_profile_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.custom_json">
<code class="descname">custom_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.custom_security_group_ids">
<code class="descname">custom_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.drain_elb_on_shutdown">
<code class="descname">drain_elb_on_shutdown</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.ebs_volumes">
<code class="descname">ebs_volumes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><cite>ebs_volume</cite> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.elastic_load_balancer">
<code class="descname">elastic_load_balancer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.install_updates_on_boot">
<code class="descname">install_updates_on_boot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.instance_shutdown_timeout">
<code class="descname">instance_shutdown_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.stack_id">
<code class="descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.system_packages">
<code class="descname">system_packages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.PhpAppLayer.use_ebs_optimized_instances">
<code class="descname">use_ebs_optimized_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.PhpAppLayer.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.PhpAppLayer.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.PhpAppLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.opsworks.RailsAppLayer">
<em class="property">class </em><code class="descclassname">pulumi_aws.opsworks.</code><code class="descname">RailsAppLayer</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>app_server=None</em>, <em>auto_assign_elastic_ips=None</em>, <em>auto_assign_public_ips=None</em>, <em>auto_healing=None</em>, <em>bundler_version=None</em>, <em>custom_configure_recipes=None</em>, <em>custom_deploy_recipes=None</em>, <em>custom_instance_profile_arn=None</em>, <em>custom_json=None</em>, <em>custom_security_group_ids=None</em>, <em>custom_setup_recipes=None</em>, <em>custom_shutdown_recipes=None</em>, <em>custom_undeploy_recipes=None</em>, <em>drain_elb_on_shutdown=None</em>, <em>ebs_volumes=None</em>, <em>elastic_load_balancer=None</em>, <em>install_updates_on_boot=None</em>, <em>instance_shutdown_timeout=None</em>, <em>manage_bundler=None</em>, <em>name=None</em>, <em>passenger_version=None</em>, <em>ruby_version=None</em>, <em>rubygems_version=None</em>, <em>stack_id=None</em>, <em>system_packages=None</em>, <em>use_ebs_optimized_instances=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks Ruby on Rails application layer resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>app_server</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Keyword for the app server to use. Defaults to “apache_passenger”.</li>
<li><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</li>
<li><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</li>
<li><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</li>
<li><strong>bundler_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When OpsWorks is managing Bundler, which version to use. Defaults to “1.5.3”.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[list] custom_configure_recipes
:param pulumi.Input[list] custom_deploy_recipes
:param pulumi.Input[str] custom_instance_profile_arn: The ARN of an IAM profile that will be used for the layer’s instances.
:param pulumi.Input[str] custom_json: Custom JSON attributes to apply to the layer.
:param pulumi.Input[list] custom_security_group_ids: Ids for a set of security groups to apply to the layer’s instances.
:param pulumi.Input[list] custom_setup_recipes
:param pulumi.Input[list] custom_shutdown_recipes
:param pulumi.Input[list] custom_undeploy_recipes
:param pulumi.Input[bool] drain_elb_on_shutdown: Whether to enable Elastic Load Balancing connection draining.
:param pulumi.Input[list] ebs_volumes: <cite>ebs_volume</cite> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.
:param pulumi.Input[str] elastic_load_balancer: Name of an Elastic Load Balancer to attach to this layer
:param pulumi.Input[bool] install_updates_on_boot: Whether to install OS and package updates on each instance when it boots.
:param pulumi.Input[int] instance_shutdown_timeout: The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.
:param pulumi.Input[bool] manage_bundler: Whether OpsWorks should manage bundler. On by default.
:param pulumi.Input[str] name: A human-readable name for the layer.
:param pulumi.Input[str] passenger_version: The version of Passenger to use. Defaults to “4.0.46”.
:param pulumi.Input[str] ruby_version: The version of Ruby to use. Defaults to “2.0.0”.
:param pulumi.Input[str] rubygems_version: The version of RubyGems to use. Defaults to “2.2.2”.
:param pulumi.Input[str] stack_id: The id of the stack the layer will belong to.
:param pulumi.Input[list] system_packages: Names of a set of system packages to install on the layer’s instances.
:param pulumi.Input[bool] use_ebs_optimized_instances: Whether to use EBS-optimized instances.</p>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.app_server">
<code class="descname">app_server</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.app_server" title="Permalink to this definition">¶</a></dt>
<dd><p>Keyword for the app server to use. Defaults to “apache_passenger”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.auto_assign_elastic_ips">
<code class="descname">auto_assign_elastic_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.auto_assign_public_ips">
<code class="descname">auto_assign_public_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.auto_healing">
<code class="descname">auto_healing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.bundler_version">
<code class="descname">bundler_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.bundler_version" title="Permalink to this definition">¶</a></dt>
<dd><p>When OpsWorks is managing Bundler, which version to use. Defaults to “1.5.3”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.custom_instance_profile_arn">
<code class="descname">custom_instance_profile_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.custom_json">
<code class="descname">custom_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.custom_security_group_ids">
<code class="descname">custom_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.drain_elb_on_shutdown">
<code class="descname">drain_elb_on_shutdown</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.ebs_volumes">
<code class="descname">ebs_volumes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><cite>ebs_volume</cite> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.elastic_load_balancer">
<code class="descname">elastic_load_balancer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.install_updates_on_boot">
<code class="descname">install_updates_on_boot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.instance_shutdown_timeout">
<code class="descname">instance_shutdown_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.manage_bundler">
<code class="descname">manage_bundler</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.manage_bundler" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether OpsWorks should manage bundler. On by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.passenger_version">
<code class="descname">passenger_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.passenger_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of Passenger to use. Defaults to “4.0.46”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.ruby_version">
<code class="descname">ruby_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.ruby_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of Ruby to use. Defaults to “2.0.0”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.rubygems_version">
<code class="descname">rubygems_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.rubygems_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of RubyGems to use. Defaults to “2.2.2”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.stack_id">
<code class="descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.system_packages">
<code class="descname">system_packages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RailsAppLayer.use_ebs_optimized_instances">
<code class="descname">use_ebs_optimized_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.RailsAppLayer.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.RailsAppLayer.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.RailsAppLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.opsworks.RdsDbInstance">
<em class="property">class </em><code class="descclassname">pulumi_aws.opsworks.</code><code class="descname">RdsDbInstance</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>db_password=None</em>, <em>db_user=None</em>, <em>rds_db_instance_arn=None</em>, <em>stack_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.RdsDbInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks RDS DB Instance resource.</p>
<p>&gt; <strong>Note:</strong> All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">https://www.terraform.io/docs/state/sensitive-data.html</a>).</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>db_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A db password</li>
<li><strong>db_user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A db username</li>
<li><strong>rds_db_instance_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The db instance to register for this stack. Changing this will force a new resource.</li>
<li><strong>stack_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The stack to register a db inatance for. Changing this will force a new resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.RdsDbInstance.db_password">
<code class="descname">db_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RdsDbInstance.db_password" title="Permalink to this definition">¶</a></dt>
<dd><p>A db password</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RdsDbInstance.db_user">
<code class="descname">db_user</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RdsDbInstance.db_user" title="Permalink to this definition">¶</a></dt>
<dd><p>A db username</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RdsDbInstance.rds_db_instance_arn">
<code class="descname">rds_db_instance_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RdsDbInstance.rds_db_instance_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The db instance to register for this stack. Changing this will force a new resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.RdsDbInstance.stack_id">
<code class="descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.RdsDbInstance.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The stack to register a db inatance for. Changing this will force a new resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.RdsDbInstance.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.RdsDbInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.RdsDbInstance.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.RdsDbInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.opsworks.Stack">
<em class="property">class </em><code class="descclassname">pulumi_aws.opsworks.</code><code class="descname">Stack</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>agent_version=None</em>, <em>berkshelf_version=None</em>, <em>color=None</em>, <em>configuration_manager_name=None</em>, <em>configuration_manager_version=None</em>, <em>custom_cookbooks_sources=None</em>, <em>custom_json=None</em>, <em>default_availability_zone=None</em>, <em>default_instance_profile_arn=None</em>, <em>default_os=None</em>, <em>default_root_device_type=None</em>, <em>default_ssh_key_name=None</em>, <em>default_subnet_id=None</em>, <em>hostname_theme=None</em>, <em>manage_berkshelf=None</em>, <em>name=None</em>, <em>region=None</em>, <em>service_role_arn=None</em>, <em>tags=None</em>, <em>use_custom_cookbooks=None</em>, <em>use_opsworks_security_groups=None</em>, <em>vpc_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Stack" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks stack resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>agent_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set to <cite>“LATEST”</cite>, OpsWorks will automatically install the latest version.</li>
<li><strong>berkshelf_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If <cite>manage_berkshelf</cite> is enabled, the version of Berkshelf to use.</li>
<li><strong>color</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Color to paint next to the stack’s resources in the OpsWorks console.</li>
<li><strong>configuration_manager_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the configuration manager to use. Defaults to “Chef”.</li>
<li><strong>configuration_manager_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of the configuration manager to use. Defaults to “11.4”.</li>
<li><strong>custom_cookbooks_sources</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – When <cite>use_custom_cookbooks</cite> is set, provide this sub-object as
described below.</li>
<li><strong>custom_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom JSON attributes to apply to the entire stack.</li>
<li><strong>default_availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the availability zone where instances will be created
by default. This is required unless you set <cite>vpc_id</cite>.</li>
<li><strong>default_instance_profile_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM Instance Profile that created instances
will have by default.</li>
<li><strong>default_os</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of OS that will be installed on instances by default.</li>
<li><strong>default_root_device_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the type of root device instances will have by default.</li>
<li><strong>default_ssh_key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the SSH keypair that instances will have by default.</li>
<li><strong>default_subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of the subnet in which instances will be created by default. Mandatory
if <cite>vpc_id</cite> is set, and forbidden if it isn’t.</li>
<li><strong>hostname_theme</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Keyword representing the naming scheme that will be used for instance hostnames
within this stack.</li>
<li><strong>manage_berkshelf</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value controlling whether Opsworks will run Berkshelf for this stack.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the stack.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the region where the stack will exist.</li>
<li><strong>service_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM role that the OpsWorks service will act as.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>use_custom_cookbooks</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value controlling whether the custom cookbook settings are
enabled.</li>
<li><strong>use_opsworks_security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value controlling whether the standard OpsWorks
security groups apply to created instances.</li>
<li><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the VPC that this stack belongs to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.agent_version">
<code class="descname">agent_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.agent_version" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to <cite>“LATEST”</cite>, OpsWorks will automatically install the latest version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.berkshelf_version">
<code class="descname">berkshelf_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.berkshelf_version" title="Permalink to this definition">¶</a></dt>
<dd><p>If <cite>manage_berkshelf</cite> is enabled, the version of Berkshelf to use.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.color">
<code class="descname">color</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.color" title="Permalink to this definition">¶</a></dt>
<dd><p>Color to paint next to the stack’s resources in the OpsWorks console.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.configuration_manager_name">
<code class="descname">configuration_manager_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.configuration_manager_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the configuration manager to use. Defaults to “Chef”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.configuration_manager_version">
<code class="descname">configuration_manager_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.configuration_manager_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of the configuration manager to use. Defaults to “11.4”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.custom_cookbooks_sources">
<code class="descname">custom_cookbooks_sources</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.custom_cookbooks_sources" title="Permalink to this definition">¶</a></dt>
<dd><p>When <cite>use_custom_cookbooks</cite> is set, provide this sub-object as
described below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.custom_json">
<code class="descname">custom_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.custom_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom JSON attributes to apply to the entire stack.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.default_availability_zone">
<code class="descname">default_availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.default_availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the availability zone where instances will be created
by default. This is required unless you set <cite>vpc_id</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.default_instance_profile_arn">
<code class="descname">default_instance_profile_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.default_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM Instance Profile that created instances
will have by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.default_os">
<code class="descname">default_os</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.default_os" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of OS that will be installed on instances by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.default_root_device_type">
<code class="descname">default_root_device_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.default_root_device_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the type of root device instances will have by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.default_ssh_key_name">
<code class="descname">default_ssh_key_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.default_ssh_key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the SSH keypair that instances will have by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.default_subnet_id">
<code class="descname">default_subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.default_subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Id of the subnet in which instances will be created by default. Mandatory
if <cite>vpc_id</cite> is set, and forbidden if it isn’t.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.hostname_theme">
<code class="descname">hostname_theme</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.hostname_theme" title="Permalink to this definition">¶</a></dt>
<dd><p>Keyword representing the naming scheme that will be used for instance hostnames
within this stack.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.manage_berkshelf">
<code class="descname">manage_berkshelf</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.manage_berkshelf" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean value controlling whether Opsworks will run Berkshelf for this stack.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the stack.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the region where the stack will exist.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.service_role_arn">
<code class="descname">service_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.service_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM role that the OpsWorks service will act as.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.use_custom_cookbooks">
<code class="descname">use_custom_cookbooks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.use_custom_cookbooks" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean value controlling whether the custom cookbook settings are
enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.use_opsworks_security_groups">
<code class="descname">use_opsworks_security_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.use_opsworks_security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean value controlling whether the standard OpsWorks
security groups apply to created instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.Stack.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.Stack.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the VPC that this stack belongs to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.Stack.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Stack.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.Stack.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.Stack.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.opsworks.StaticWebLayer">
<em class="property">class </em><code class="descclassname">pulumi_aws.opsworks.</code><code class="descname">StaticWebLayer</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>auto_assign_elastic_ips=None</em>, <em>auto_assign_public_ips=None</em>, <em>auto_healing=None</em>, <em>custom_configure_recipes=None</em>, <em>custom_deploy_recipes=None</em>, <em>custom_instance_profile_arn=None</em>, <em>custom_json=None</em>, <em>custom_security_group_ids=None</em>, <em>custom_setup_recipes=None</em>, <em>custom_shutdown_recipes=None</em>, <em>custom_undeploy_recipes=None</em>, <em>drain_elb_on_shutdown=None</em>, <em>ebs_volumes=None</em>, <em>elastic_load_balancer=None</em>, <em>install_updates_on_boot=None</em>, <em>instance_shutdown_timeout=None</em>, <em>name=None</em>, <em>stack_id=None</em>, <em>system_packages=None</em>, <em>use_ebs_optimized_instances=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks static web server layer resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>auto_assign_elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to automatically assign an elastic IP address to the layer’s instances.</li>
<li><strong>auto_assign_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</li>
<li><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable auto-healing for the layer.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[list] custom_configure_recipes
:param pulumi.Input[list] custom_deploy_recipes
:param pulumi.Input[str] custom_instance_profile_arn: The ARN of an IAM profile that will be used for the layer’s instances.
:param pulumi.Input[str] custom_json
:param pulumi.Input[list] custom_security_group_ids: Ids for a set of security groups to apply to the layer’s instances.
:param pulumi.Input[list] custom_setup_recipes
:param pulumi.Input[list] custom_shutdown_recipes
:param pulumi.Input[list] custom_undeploy_recipes
:param pulumi.Input[bool] drain_elb_on_shutdown: Whether to enable Elastic Load Balancing connection draining.
:param pulumi.Input[list] ebs_volumes: <cite>ebs_volume</cite> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.
:param pulumi.Input[str] elastic_load_balancer: Name of an Elastic Load Balancer to attach to this layer
:param pulumi.Input[bool] install_updates_on_boot: Whether to install OS and package updates on each instance when it boots.
:param pulumi.Input[int] instance_shutdown_timeout: The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.
:param pulumi.Input[str] name: A human-readable name for the layer.
:param pulumi.Input[str] stack_id: The id of the stack the layer will belong to.
:param pulumi.Input[list] system_packages: Names of a set of system packages to install on the layer’s instances.
:param pulumi.Input[bool] use_ebs_optimized_instances: Whether to use EBS-optimized instances.</p>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.auto_assign_elastic_ips">
<code class="descname">auto_assign_elastic_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.auto_assign_elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to automatically assign an elastic IP address to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.auto_assign_public_ips">
<code class="descname">auto_assign_public_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.auto_assign_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.auto_healing">
<code class="descname">auto_healing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable auto-healing for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.custom_instance_profile_arn">
<code class="descname">custom_instance_profile_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.custom_instance_profile_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM profile that will be used for the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.custom_security_group_ids">
<code class="descname">custom_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.custom_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids for a set of security groups to apply to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.drain_elb_on_shutdown">
<code class="descname">drain_elb_on_shutdown</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.drain_elb_on_shutdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Elastic Load Balancing connection draining.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.ebs_volumes">
<code class="descname">ebs_volumes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.ebs_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p><cite>ebs_volume</cite> blocks, as described below, will each create an EBS volume and connect it to the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.elastic_load_balancer">
<code class="descname">elastic_load_balancer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.elastic_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an Elastic Load Balancer to attach to this layer</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.install_updates_on_boot">
<code class="descname">install_updates_on_boot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.install_updates_on_boot" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to install OS and package updates on each instance when it boots.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.instance_shutdown_timeout">
<code class="descname">instance_shutdown_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.instance_shutdown_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable name for the layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.stack_id">
<code class="descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the stack the layer will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.system_packages">
<code class="descname">system_packages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.system_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Names of a set of system packages to install on the layer’s instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.StaticWebLayer.use_ebs_optimized_instances">
<code class="descname">use_ebs_optimized_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.use_ebs_optimized_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EBS-optimized instances.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.StaticWebLayer.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.StaticWebLayer.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.StaticWebLayer.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.opsworks.UserProfile">
<em class="property">class </em><code class="descclassname">pulumi_aws.opsworks.</code><code class="descname">UserProfile</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>allow_self_management=None</em>, <em>ssh_public_key=None</em>, <em>ssh_username=None</em>, <em>user_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.UserProfile" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an OpsWorks User Profile resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>allow_self_management</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether users can specify their own SSH public key through the My Settings page</li>
<li><strong>ssh_public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The users public key</li>
<li><strong>ssh_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ssh username, with witch this user wants to log in</li>
<li><strong>user_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s IAM ARN</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.opsworks.UserProfile.allow_self_management">
<code class="descname">allow_self_management</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.UserProfile.allow_self_management" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether users can specify their own SSH public key through the My Settings page</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.UserProfile.ssh_public_key">
<code class="descname">ssh_public_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.UserProfile.ssh_public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The users public key</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.UserProfile.ssh_username">
<code class="descname">ssh_username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.UserProfile.ssh_username" title="Permalink to this definition">¶</a></dt>
<dd><p>The ssh username, with witch this user wants to log in</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.opsworks.UserProfile.user_arn">
<code class="descname">user_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.opsworks.UserProfile.user_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The user’s IAM ARN</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.UserProfile.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.UserProfile.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.opsworks.UserProfile.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.opsworks.UserProfile.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

</div>
