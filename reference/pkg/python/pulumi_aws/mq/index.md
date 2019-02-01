<div class="section" id="module-pulumi_aws.mq">
<span id="mq"></span><h1>mq<a class="headerlink" href="#module-pulumi_aws.mq" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.mq.Broker">
<em class="property">class </em><code class="descclassname">pulumi_aws.mq.</code><code class="descname">Broker</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>apply_immediately=None</em>, <em>auto_minor_version_upgrade=None</em>, <em>broker_name=None</em>, <em>configuration=None</em>, <em>deployment_mode=None</em>, <em>engine_type=None</em>, <em>engine_version=None</em>, <em>host_instance_type=None</em>, <em>logs=None</em>, <em>maintenance_window_start_time=None</em>, <em>publicly_accessible=None</em>, <em>security_groups=None</em>, <em>subnet_ids=None</em>, <em>users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mq.Broker" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an MQ Broker Resource. This resources also manages users for the broker.</p>
<p>For more information on Amazon MQ, see [Amazon MQ documentation](<a class="reference external" href="https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html">https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html</a>).</p>
<p>Changes to an MQ Broker can occur when you change a
parameter, such as <cite>configuration</cite> or <cite>user</cite>, and are reflected in the next maintenance
window. Because of this, Terraform may report a difference in its planning
phase because a modification has not yet taken place. You can use the
<cite>apply_immediately</cite> flag to instruct the service to apply the change immediately
(see documentation below).</p>
<p>&gt; <strong>Note:</strong> using <cite>apply_immediately</cite> can result in a
brief downtime as the broker reboots.</p>
<p>&gt; <strong>Note:</strong> All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">https://www.terraform.io/docs/state/sensitive-data.html</a>).</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>apply_immediately</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether any broker modifications
are applied immediately, or during the next maintenance window. Default is <cite>false</cite>.</li>
<li><strong>auto_minor_version_upgrade</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions.</li>
<li><strong>broker_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the broker.</li>
<li><strong>configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration of the broker. See below.</li>
<li><strong>deployment_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The deployment mode of the broker. Supported: <cite>SINGLE_INSTANCE</cite> and <cite>ACTIVE_STANDBY_MULTI_AZ</cite>. Defaults to <cite>SINGLE_INSTANCE</cite>.</li>
<li><strong>engine_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of broker engine. Currently, Amazon MQ supports only <cite>ActiveMQ</cite>.</li>
<li><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the broker engine. Currently, Amazon MQ supports only <cite>5.15.0</cite> or <cite>5.15.6</cite>.</li>
<li><strong>host_instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The broker’s instance type. e.g. <cite>mq.t2.micro</cite> or <cite>mq.m4.large</cite></li>
<li><strong>logs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Logging configuration of the broker. See below.</li>
<li><strong>maintenance_window_start_time</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Maintenance window start time. See below.</li>
<li><strong>publicly_accessible</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable connections from applications outside of the VPC that hosts the broker’s subnets.</li>
<li><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of security group IDs assigned to the broker.</li>
<li><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of subnet IDs in which to launch the broker. A <cite>SINGLE_INSTANCE</cite> deployment requires one subnet. An <cite>ACTIVE_STANDBY_MULTI_AZ</cite> deployment requires two subnets.</li>
<li><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of all ActiveMQ usernames for the specified broker. See below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.apply_immediately">
<code class="descname">apply_immediately</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.apply_immediately" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether any broker modifications
are applied immediately, or during the next maintenance window. Default is <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the broker.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.auto_minor_version_upgrade">
<code class="descname">auto_minor_version_upgrade</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.auto_minor_version_upgrade" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.broker_name">
<code class="descname">broker_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.broker_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the broker.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.configuration">
<code class="descname">configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration of the broker. See below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.deployment_mode">
<code class="descname">deployment_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.deployment_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The deployment mode of the broker. Supported: <cite>SINGLE_INSTANCE</cite> and <cite>ACTIVE_STANDBY_MULTI_AZ</cite>. Defaults to <cite>SINGLE_INSTANCE</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.engine_type">
<code class="descname">engine_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.engine_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of broker engine. Currently, Amazon MQ supports only <cite>ActiveMQ</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.engine_version">
<code class="descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the broker engine. Currently, Amazon MQ supports only <cite>5.15.0</cite> or <cite>5.15.6</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.host_instance_type">
<code class="descname">host_instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.host_instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The broker’s instance type. e.g. <cite>mq.t2.micro</cite> or <cite>mq.m4.large</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.instances">
<code class="descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of information about allocated brokers (both active &amp; standby).
* <cite>instances.0.console_url</cite> - The URL of the broker’s [ActiveMQ Web Console](<a class="reference external" href="http://activemq.apache.org/web-console.html">http://activemq.apache.org/web-console.html</a>).
* <cite>instances.0.ip_address</cite> - The IP Address of the broker.
* <cite>instances.0.endpoints</cite> - The broker’s wire-level protocol endpoints in the following order &amp; format referenceable e.g. as <cite>instances.0.endpoints.0</cite> (SSL):
* <cite>ssl://broker-id.mq.us-west-2.amazonaws.com:61617</cite>
* <cite>amqp+ssl://broker-id.mq.us-west-2.amazonaws.com:5671</cite>
* <cite>stomp+ssl://broker-id.mq.us-west-2.amazonaws.com:61614</cite>
* <cite>mqtt+ssl://broker-id.mq.us-west-2.amazonaws.com:8883</cite>
* <cite>wss://broker-id.mq.us-west-2.amazonaws.com:61619</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.logs">
<code class="descname">logs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.logs" title="Permalink to this definition">¶</a></dt>
<dd><p>Logging configuration of the broker. See below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.maintenance_window_start_time">
<code class="descname">maintenance_window_start_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.maintenance_window_start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Maintenance window start time. See below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.publicly_accessible">
<code class="descname">publicly_accessible</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.publicly_accessible" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable connections from applications outside of the VPC that hosts the broker’s subnets.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.security_groups">
<code class="descname">security_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of security group IDs assigned to the broker.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.subnet_ids">
<code class="descname">subnet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of subnet IDs in which to launch the broker. A <cite>SINGLE_INSTANCE</cite> deployment requires one subnet. An <cite>ACTIVE_STANDBY_MULTI_AZ</cite> deployment requires two subnets.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.users">
<code class="descname">users</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.users" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of all ActiveMQ usernames for the specified broker. See below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.mq.Broker.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mq.Broker.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.mq.Broker.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mq.Broker.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.mq.Configuration">
<em class="property">class </em><code class="descclassname">pulumi_aws.mq.</code><code class="descname">Configuration</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>data=None</em>, <em>description=None</em>, <em>engine_type=None</em>, <em>engine_version=None</em>, <em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mq.Configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an MQ Configuration Resource.</p>
<p>For more information on Amazon MQ, see [Amazon MQ documentation](<a class="reference external" href="https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html">https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html</a>).</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The broker configuration in XML format.
See [official docs](<a class="reference external" href="https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-broker-configuration-parameters.html">https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-broker-configuration-parameters.html</a>)
for supported parameters and format of the XML.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the configuration.</li>
<li><strong>engine_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of broker engine.</li>
<li><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the broker engine.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the configuration</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.mq.Configuration.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Configuration.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Configuration.data">
<code class="descname">data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Configuration.data" title="Permalink to this definition">¶</a></dt>
<dd><p>The broker configuration in XML format.
See [official docs](<a class="reference external" href="https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-broker-configuration-parameters.html">https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-broker-configuration-parameters.html</a>)
for supported parameters and format of the XML.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Configuration.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Configuration.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Configuration.engine_type">
<code class="descname">engine_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Configuration.engine_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of broker engine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Configuration.engine_version">
<code class="descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Configuration.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the broker engine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Configuration.latest_revision">
<code class="descname">latest_revision</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Configuration.latest_revision" title="Permalink to this definition">¶</a></dt>
<dd><p>The latest revision of the configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Configuration.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Configuration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the configuration</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.mq.Configuration.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mq.Configuration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.mq.Configuration.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mq.Configuration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.mq.GetBrokerResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.mq.</code><code class="descname">GetBrokerResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>auto_minor_version_upgrade=None</em>, <em>broker_id=None</em>, <em>broker_name=None</em>, <em>configuration=None</em>, <em>deployment_mode=None</em>, <em>engine_type=None</em>, <em>engine_version=None</em>, <em>host_instance_type=None</em>, <em>instances=None</em>, <em>maintenance_window_start_time=None</em>, <em>publicly_accessible=None</em>, <em>security_groups=None</em>, <em>subnet_ids=None</em>, <em>users=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mq.GetBrokerResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBroker.</p>
<dl class="attribute">
<dt id="pulumi_aws.mq.GetBrokerResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.GetBrokerResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_aws.mq.get_broker">
<code class="descclassname">pulumi_aws.mq.</code><code class="descname">get_broker</code><span class="sig-paren">(</span><em>broker_id=None</em>, <em>broker_name=None</em>, <em>logs=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mq.get_broker" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a MQ Broker.</p>
</dd></dl>

</div>
