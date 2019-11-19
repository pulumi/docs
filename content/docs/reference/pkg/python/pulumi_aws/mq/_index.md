---
title: Module mq
linktitle: mq
notitle: true
---

<div class="section" id="mq">
<h1>mq<a class="headerlink" href="#mq" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.mq"></span><dl class="class">
<dt id="pulumi_aws.mq.AwaitableGetBrokerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.mq.</code><code class="sig-name descname">AwaitableGetBrokerResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">auto_minor_version_upgrade=None</em>, <em class="sig-param">broker_id=None</em>, <em class="sig-param">broker_name=None</em>, <em class="sig-param">configuration=None</em>, <em class="sig-param">deployment_mode=None</em>, <em class="sig-param">encryption_options=None</em>, <em class="sig-param">engine_type=None</em>, <em class="sig-param">engine_version=None</em>, <em class="sig-param">host_instance_type=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">logs=None</em>, <em class="sig-param">maintenance_window_start_time=None</em>, <em class="sig-param">publicly_accessible=None</em>, <em class="sig-param">security_groups=None</em>, <em class="sig-param">subnet_ids=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">users=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mq.AwaitableGetBrokerResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.mq.Broker">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.mq.</code><code class="sig-name descname">Broker</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">apply_immediately=None</em>, <em class="sig-param">auto_minor_version_upgrade=None</em>, <em class="sig-param">broker_name=None</em>, <em class="sig-param">configuration=None</em>, <em class="sig-param">deployment_mode=None</em>, <em class="sig-param">encryption_options=None</em>, <em class="sig-param">engine_type=None</em>, <em class="sig-param">engine_version=None</em>, <em class="sig-param">host_instance_type=None</em>, <em class="sig-param">logs=None</em>, <em class="sig-param">maintenance_window_start_time=None</em>, <em class="sig-param">publicly_accessible=None</em>, <em class="sig-param">security_groups=None</em>, <em class="sig-param">subnet_ids=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">users=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mq.Broker" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an MQ Broker Resource. This resources also manages users for the broker.</p>
<p>For more information on Amazon MQ, see <a class="reference external" href="https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html">Amazon MQ documentation</a>.</p>
<p>Changes to an MQ Broker can occur when you change a
parameter, such as <code class="docutils literal notranslate"><span class="pre">configuration</span></code> or <code class="docutils literal notranslate"><span class="pre">user</span></code>, and are reflected in the next maintenance
window. Because of this, this provider may report a difference in its planning
phase because a modification has not yet taken place. You can use the
<code class="docutils literal notranslate"><span class="pre">apply_immediately</span></code> flag to instruct the service to apply the change immediately
(see documentation below).</p>
<blockquote>
<div><p><strong>Note:</strong> using <code class="docutils literal notranslate"><span class="pre">apply_immediately</span></code> can result in a
brief downtime as the broker reboots.</p>
<p><strong>Note:</strong> All arguments including the username and password will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>apply_immediately</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether any broker modifications
are applied immediately, or during the next maintenance window. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>auto_minor_version_upgrade</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions.</p></li>
<li><p><strong>broker_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the broker.</p></li>
<li><p><strong>configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration of the broker. See below.</p></li>
<li><p><strong>deployment_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The deployment mode of the broker. Supported: <code class="docutils literal notranslate"><span class="pre">SINGLE_INSTANCE</span></code> and <code class="docutils literal notranslate"><span class="pre">ACTIVE_STANDBY_MULTI_AZ</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">SINGLE_INSTANCE</span></code>.</p></li>
<li><p><strong>encryption_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block containing encryption options. See below.</p></li>
<li><p><strong>engine_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of broker engine. Currently, Amazon MQ supports only <code class="docutils literal notranslate"><span class="pre">ActiveMQ</span></code>.</p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the broker engine. See the <a class="reference external" href="https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html">AmazonMQ Broker Engine docs</a> for supported versions.</p></li>
<li><p><strong>host_instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The broker’s instance type. e.g. <code class="docutils literal notranslate"><span class="pre">mq.t2.micro</span></code> or <code class="docutils literal notranslate"><span class="pre">mq.m4.large</span></code></p></li>
<li><p><strong>logs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Logging configuration of the broker. See below.</p></li>
<li><p><strong>maintenance_window_start_time</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Maintenance window start time. See below.</p></li>
<li><p><strong>publicly_accessible</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable connections from applications outside of the VPC that hosts the broker’s subnets.</p></li>
<li><p><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of security group IDs assigned to the broker.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of subnet IDs in which to launch the broker. A <code class="docutils literal notranslate"><span class="pre">SINGLE_INSTANCE</span></code> deployment requires one subnet. An <code class="docutils literal notranslate"><span class="pre">ACTIVE_STANDBY_MULTI_AZ</span></code> deployment requires two subnets.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of all ActiveMQ usernames for the specified broker. See below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Configuration ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revision</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Revision of the Configuration.</p></li>
</ul>
<p>The <strong>encryption_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amazon Resource Name (ARN) of Key Management Service (KMS) Customer Master Key (CMK) to use for encryption at rest. Requires setting <code class="docutils literal notranslate"><span class="pre">use_aws_owned_key</span></code> to <code class="docutils literal notranslate"><span class="pre">false</span></code>. To perform drift detection when AWS managed CMKs or customer managed CMKs are in use, this value must be configured.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useAwsOwnedKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean to enable an AWS owned Key Management Service (KMS) Customer Master Key (CMK) that is not in your account. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Setting to <code class="docutils literal notranslate"><span class="pre">false</span></code> without configuring <code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code> will create an AWS managed Customer Master Key (CMK) aliased to <code class="docutils literal notranslate"><span class="pre">aws/mq</span></code> in your account.</p></li>
</ul>
<p>The <strong>logs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">audit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables audit logging. User management action made using JMX or the ActiveMQ Web Console is logged. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">general</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables general logging via CloudWatch. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>maintenance_window_start_time</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dayOfWeek</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The day of the week. e.g. <code class="docutils literal notranslate"><span class="pre">MONDAY</span></code>, <code class="docutils literal notranslate"><span class="pre">TUESDAY</span></code>, or <code class="docutils literal notranslate"><span class="pre">WEDNESDAY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeOfDay</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The time, in 24-hour format. e.g. <code class="docutils literal notranslate"><span class="pre">02:00</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeZone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The time zone, UTC by default, in either the Country/City format, or the UTC offset format. e.g. <code class="docutils literal notranslate"><span class="pre">CET</span></code></p></li>
</ul>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consoleAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to enable access to the <a class="reference external" href="http://activemq.apache.org/web-console.html">ActiveMQ Web Console</a> for the user.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The list of groups (20 maximum) to which the ActiveMQ user belongs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password of the user. It must be 12 to 250 characters long, at least 4 unique characters, and must not contain commas.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username of the user.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/mq_broker.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/mq_broker.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.apply_immediately">
<code class="sig-name descname">apply_immediately</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.apply_immediately" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether any broker modifications
are applied immediately, or during the next maintenance window. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the broker.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.auto_minor_version_upgrade">
<code class="sig-name descname">auto_minor_version_upgrade</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.auto_minor_version_upgrade" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.broker_name">
<code class="sig-name descname">broker_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.broker_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the broker.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.configuration">
<code class="sig-name descname">configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration of the broker. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Configuration ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revision</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Revision of the Configuration.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.deployment_mode">
<code class="sig-name descname">deployment_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.deployment_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The deployment mode of the broker. Supported: <code class="docutils literal notranslate"><span class="pre">SINGLE_INSTANCE</span></code> and <code class="docutils literal notranslate"><span class="pre">ACTIVE_STANDBY_MULTI_AZ</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">SINGLE_INSTANCE</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.encryption_options">
<code class="sig-name descname">encryption_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.encryption_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block containing encryption options. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Amazon Resource Name (ARN) of Key Management Service (KMS) Customer Master Key (CMK) to use for encryption at rest. Requires setting <code class="docutils literal notranslate"><span class="pre">use_aws_owned_key</span></code> to <code class="docutils literal notranslate"><span class="pre">false</span></code>. To perform drift detection when AWS managed CMKs or customer managed CMKs are in use, this value must be configured.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useAwsOwnedKey</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean to enable an AWS owned Key Management Service (KMS) Customer Master Key (CMK) that is not in your account. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Setting to <code class="docutils literal notranslate"><span class="pre">false</span></code> without configuring <code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code> will create an AWS managed Customer Master Key (CMK) aliased to <code class="docutils literal notranslate"><span class="pre">aws/mq</span></code> in your account.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.engine_type">
<code class="sig-name descname">engine_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.engine_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of broker engine. Currently, Amazon MQ supports only <code class="docutils literal notranslate"><span class="pre">ActiveMQ</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.engine_version">
<code class="sig-name descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the broker engine. See the <a class="reference external" href="https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html">AmazonMQ Broker Engine docs</a> for supported versions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.host_instance_type">
<code class="sig-name descname">host_instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.host_instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The broker’s instance type. e.g. <code class="docutils literal notranslate"><span class="pre">mq.t2.micro</span></code> or <code class="docutils literal notranslate"><span class="pre">mq.m4.large</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.instances">
<code class="sig-name descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of information about allocated brokers (both active &amp; standby).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instances.0.console_url</span></code> - The URL of the broker’s <a class="reference external" href="http://activemq.apache.org/web-console.html">ActiveMQ Web Console</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instances.0.ip_address</span></code> - The IP Address of the broker.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instances.0.endpoints</span></code> - The broker’s wire-level protocol endpoints in the following order &amp; format referenceable e.g. as <code class="docutils literal notranslate"><span class="pre">instances.0.endpoints.0</span></code> (SSL):</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssl://broker-id.mq.us-west-2.amazonaws.com:61617</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">amqp+ssl://broker-id.mq.us-west-2.amazonaws.com:5671</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stomp+ssl://broker-id.mq.us-west-2.amazonaws.com:61614</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mqtt+ssl://broker-id.mq.us-west-2.amazonaws.com:8883</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">wss://broker-id.mq.us-west-2.amazonaws.com:61619</span></code></p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">consoleUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endpoints</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.logs">
<code class="sig-name descname">logs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.logs" title="Permalink to this definition">¶</a></dt>
<dd><p>Logging configuration of the broker. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">audit</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables audit logging. User management action made using JMX or the ActiveMQ Web Console is logged. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">general</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables general logging via CloudWatch. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.maintenance_window_start_time">
<code class="sig-name descname">maintenance_window_start_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.maintenance_window_start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Maintenance window start time. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dayOfWeek</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The day of the week. e.g. <code class="docutils literal notranslate"><span class="pre">MONDAY</span></code>, <code class="docutils literal notranslate"><span class="pre">TUESDAY</span></code>, or <code class="docutils literal notranslate"><span class="pre">WEDNESDAY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeOfDay</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The time, in 24-hour format. e.g. <code class="docutils literal notranslate"><span class="pre">02:00</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeZone</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The time zone, UTC by default, in either the Country/City format, or the UTC offset format. e.g. <code class="docutils literal notranslate"><span class="pre">CET</span></code></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.publicly_accessible">
<code class="sig-name descname">publicly_accessible</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.publicly_accessible" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable connections from applications outside of the VPC that hosts the broker’s subnets.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.security_groups">
<code class="sig-name descname">security_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of security group IDs assigned to the broker.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.subnet_ids">
<code class="sig-name descname">subnet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of subnet IDs in which to launch the broker. A <code class="docutils literal notranslate"><span class="pre">SINGLE_INSTANCE</span></code> deployment requires one subnet. An <code class="docutils literal notranslate"><span class="pre">ACTIVE_STANDBY_MULTI_AZ</span></code> deployment requires two subnets.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Broker.users">
<code class="sig-name descname">users</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Broker.users" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of all ActiveMQ usernames for the specified broker. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consoleAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to enable access to the <a class="reference external" href="http://activemq.apache.org/web-console.html">ActiveMQ Web Console</a> for the user.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The list of groups (20 maximum) to which the ActiveMQ user belongs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password of the user. It must be 12 to 250 characters long, at least 4 unique characters, and must not contain commas.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username of the user.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.mq.Broker.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">apply_immediately=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">auto_minor_version_upgrade=None</em>, <em class="sig-param">broker_name=None</em>, <em class="sig-param">configuration=None</em>, <em class="sig-param">deployment_mode=None</em>, <em class="sig-param">encryption_options=None</em>, <em class="sig-param">engine_type=None</em>, <em class="sig-param">engine_version=None</em>, <em class="sig-param">host_instance_type=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">logs=None</em>, <em class="sig-param">maintenance_window_start_time=None</em>, <em class="sig-param">publicly_accessible=None</em>, <em class="sig-param">security_groups=None</em>, <em class="sig-param">subnet_ids=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mq.Broker.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Broker resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>apply_immediately</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether any broker modifications
are applied immediately, or during the next maintenance window. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the broker.</p></li>
<li><p><strong>auto_minor_version_upgrade</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions.</p></li>
<li><p><strong>broker_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the broker.</p></li>
<li><p><strong>configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration of the broker. See below.</p></li>
<li><p><strong>deployment_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The deployment mode of the broker. Supported: <code class="docutils literal notranslate"><span class="pre">SINGLE_INSTANCE</span></code> and <code class="docutils literal notranslate"><span class="pre">ACTIVE_STANDBY_MULTI_AZ</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">SINGLE_INSTANCE</span></code>.</p></li>
<li><p><strong>encryption_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block containing encryption options. See below.</p></li>
<li><p><strong>engine_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of broker engine. Currently, Amazon MQ supports only <code class="docutils literal notranslate"><span class="pre">ActiveMQ</span></code>.</p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The version of the broker engine. See the <a class="reference external" href="https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html">AmazonMQ Broker Engine docs</a> for supported versions.</p>
</p></li>
<li><p><strong>host_instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The broker’s instance type. e.g. <code class="docutils literal notranslate"><span class="pre">mq.t2.micro</span></code> or <code class="docutils literal notranslate"><span class="pre">mq.m4.large</span></code></p></li>
<li><p><strong>instances</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of information about allocated brokers (both active &amp; standby).</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `instances.0.console_url` - The URL of the broker&#39;s [ActiveMQ Web Console](http://activemq.apache.org/web-console.html).
* `instances.0.ip_address` - The IP Address of the broker.
* `instances.0.endpoints` - The broker&#39;s wire-level protocol endpoints in the following order &amp; format referenceable e.g. as `instances.0.endpoints.0` (SSL):
* `ssl://broker-id.mq.us-west-2.amazonaws.com:61617`
* `amqp+ssl://broker-id.mq.us-west-2.amazonaws.com:5671`
* `stomp+ssl://broker-id.mq.us-west-2.amazonaws.com:61614`
* `mqtt+ssl://broker-id.mq.us-west-2.amazonaws.com:8883`
* `wss://broker-id.mq.us-west-2.amazonaws.com:61619`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>logs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Logging configuration of the broker. See below.</p></li>
<li><p><strong>maintenance_window_start_time</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Maintenance window start time. See below.</p></li>
<li><p><strong>publicly_accessible</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable connections from applications outside of the VPC that hosts the broker’s subnets.</p></li>
<li><p><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of security group IDs assigned to the broker.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of subnet IDs in which to launch the broker. A <code class="docutils literal notranslate"><span class="pre">SINGLE_INSTANCE</span></code> deployment requires one subnet. An <code class="docutils literal notranslate"><span class="pre">ACTIVE_STANDBY_MULTI_AZ</span></code> deployment requires two subnets.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of all ActiveMQ usernames for the specified broker. See below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Configuration ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revision</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Revision of the Configuration.</p></li>
</ul>
<p>The <strong>encryption_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amazon Resource Name (ARN) of Key Management Service (KMS) Customer Master Key (CMK) to use for encryption at rest. Requires setting <code class="docutils literal notranslate"><span class="pre">use_aws_owned_key</span></code> to <code class="docutils literal notranslate"><span class="pre">false</span></code>. To perform drift detection when AWS managed CMKs or customer managed CMKs are in use, this value must be configured.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useAwsOwnedKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean to enable an AWS owned Key Management Service (KMS) Customer Master Key (CMK) that is not in your account. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Setting to <code class="docutils literal notranslate"><span class="pre">false</span></code> without configuring <code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code> will create an AWS managed Customer Master Key (CMK) aliased to <code class="docutils literal notranslate"><span class="pre">aws/mq</span></code> in your account.</p></li>
</ul>
<p>The <strong>instances</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consoleUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endpoints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>logs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">audit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables audit logging. User management action made using JMX or the ActiveMQ Web Console is logged. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">general</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables general logging via CloudWatch. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>maintenance_window_start_time</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dayOfWeek</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The day of the week. e.g. <code class="docutils literal notranslate"><span class="pre">MONDAY</span></code>, <code class="docutils literal notranslate"><span class="pre">TUESDAY</span></code>, or <code class="docutils literal notranslate"><span class="pre">WEDNESDAY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeOfDay</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The time, in 24-hour format. e.g. <code class="docutils literal notranslate"><span class="pre">02:00</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeZone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The time zone, UTC by default, in either the Country/City format, or the UTC offset format. e.g. <code class="docutils literal notranslate"><span class="pre">CET</span></code></p></li>
</ul>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consoleAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to enable access to the <a class="reference external" href="http://activemq.apache.org/web-console.html">ActiveMQ Web Console</a> for the user.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The list of groups (20 maximum) to which the ActiveMQ user belongs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password of the user. It must be 12 to 250 characters long, at least 4 unique characters, and must not contain commas.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username of the user.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/mq_broker.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/mq_broker.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.mq.Broker.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mq.Broker.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.mq.Broker.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mq.Broker.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.mq.Configuration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.mq.</code><code class="sig-name descname">Configuration</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">data=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">engine_type=None</em>, <em class="sig-param">engine_version=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mq.Configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an MQ Configuration Resource.</p>
<p>For more information on Amazon MQ, see <a class="reference external" href="https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html">Amazon MQ documentation</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The broker configuration in XML format.
See <a class="reference external" href="https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-broker-configuration-parameters.html">official docs</a>
for supported parameters and format of the XML.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the configuration.</p></li>
<li><p><strong>engine_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of broker engine.</p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the broker engine.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the configuration</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/mq_configuration.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/mq_configuration.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.mq.Configuration.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Configuration.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Configuration.data">
<code class="sig-name descname">data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Configuration.data" title="Permalink to this definition">¶</a></dt>
<dd><p>The broker configuration in XML format.
See <a class="reference external" href="https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-broker-configuration-parameters.html">official docs</a>
for supported parameters and format of the XML.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Configuration.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Configuration.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Configuration.engine_type">
<code class="sig-name descname">engine_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Configuration.engine_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of broker engine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Configuration.engine_version">
<code class="sig-name descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Configuration.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the broker engine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Configuration.latest_revision">
<code class="sig-name descname">latest_revision</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Configuration.latest_revision" title="Permalink to this definition">¶</a></dt>
<dd><p>The latest revision of the configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Configuration.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Configuration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the configuration</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mq.Configuration.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.Configuration.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.mq.Configuration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">data=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">engine_type=None</em>, <em class="sig-param">engine_version=None</em>, <em class="sig-param">latest_revision=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mq.Configuration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Configuration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the configuration.</p></li>
<li><p><strong>data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The broker configuration in XML format.
See <a class="reference external" href="https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-broker-configuration-parameters.html">official docs</a>
for supported parameters and format of the XML.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the configuration.</p></li>
<li><p><strong>engine_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of broker engine.</p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the broker engine.</p></li>
<li><p><strong>latest_revision</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The latest revision of the configuration.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the configuration</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/mq_configuration.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/mq_configuration.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.mq.Configuration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mq.Configuration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.mq.Configuration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mq.Configuration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.mq.GetBrokerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.mq.</code><code class="sig-name descname">GetBrokerResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">auto_minor_version_upgrade=None</em>, <em class="sig-param">broker_id=None</em>, <em class="sig-param">broker_name=None</em>, <em class="sig-param">configuration=None</em>, <em class="sig-param">deployment_mode=None</em>, <em class="sig-param">encryption_options=None</em>, <em class="sig-param">engine_type=None</em>, <em class="sig-param">engine_version=None</em>, <em class="sig-param">host_instance_type=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">logs=None</em>, <em class="sig-param">maintenance_window_start_time=None</em>, <em class="sig-param">publicly_accessible=None</em>, <em class="sig-param">security_groups=None</em>, <em class="sig-param">subnet_ids=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">users=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mq.GetBrokerResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBroker.</p>
<dl class="attribute">
<dt id="pulumi_aws.mq.GetBrokerResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mq.GetBrokerResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_aws.mq.get_broker">
<code class="sig-prename descclassname">pulumi_aws.mq.</code><code class="sig-name descname">get_broker</code><span class="sig-paren">(</span><em class="sig-param">broker_id=None</em>, <em class="sig-param">broker_name=None</em>, <em class="sig-param">logs=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mq.get_broker" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a MQ Broker.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>broker_id</strong> (<em>str</em>) – The unique id of the mq broker.</p></li>
<li><p><strong>broker_name</strong> (<em>str</em>) – The unique name of the mq broker.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>logs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">audit</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">general</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/mq_broker.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/mq_broker.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
