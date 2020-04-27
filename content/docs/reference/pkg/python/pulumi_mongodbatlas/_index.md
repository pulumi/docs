---
title: Package pulumi_mongodbatlas
title_tag: Package pulumi_mongodbatlas | Python SDK
linktitle: pulumi_mongodbatlas
notitle: true
---

<div class="section" id="pulumi-mongodb-atlas">
<h1>Pulumi MongoDB Atlas<a class="headerlink" href="#pulumi-mongodb-atlas" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-mongodbatlas">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-mongodbatlas/issues">pulumi/pulumi-mongodbatlas repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-mongodbatlas/issues">terraform-providers/terraform-provider-mongodbatlas repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_mongodbatlas"></span><dl class="class">
<dt id="pulumi_mongodbatlas.AlertConfiguration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AlertConfiguration</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">event_type=None</em>, <em class="sig-param">matchers=None</em>, <em class="sig-param">metric_threshold=None</em>, <em class="sig-param">notifications=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AlertConfiguration" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.AlertConfiguration</span></code> provides an Alert Configuration resource to define the conditions that trigger an alert and the methods of notification within a MongoDB Atlas project.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – It is not required, but If the attribute is omitted, by default will be false, and the configuration would be disabled. You must set true to enable the configuration.</p></li>
<li><p><strong>event_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of event that will trigger an alert.
Alert type       Possible values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* Host
- `OUTSIDE_METRIC_THRESHOLD`
- `HOST_RESTARTED`
- `HOST_UPGRADED`
- `HOST_NOW_SECONDARY`
- `HOST_NOW_PRIMARY`
* Replica set
- `NO_PRIMARY`
- `TOO_MANY_ELECTIONS`
* Sharded cluster
- `CLUSTER_MONGOS_IS_MISSING`
- `User`
- `JOINED_GROUP`
- `REMOVED_FROM_GROUP`
- `USER_ROLES_CHANGED_AUDIT`
* Project
- `USERS_AWAITING_APPROVAL`
- `USERS_WITHOUT_MULTI_FACTOR_AUTH`
- `GROUP_CREATED`
* Team
- `JOINED_TEAM`
- `REMOVED_FROM_TEAM`
* Organization
- `INVITED_TO_ORG`
- `JOINED_ORG`
* Data Explorer
- `DATA_EXPLORER`
- `DATA_EXPLORER_CRUD`
* Billing
- `CREDIT_CARD_ABOUT_TO_EXPIRE`
- `CHARGE_SUCCEEDED`
- `INVOICE_CLOSED`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project where the alert configuration will create.</p>
</dd>
</dl>
<p>The <strong>matchers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fieldName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the field in the target object to match on.
Host alerts support these fields:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">TYPE_NAME</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HOSTNAME</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">PORT</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HOSTNAME_AND_PORT</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">REPLICA_SET_NAME</span></code>
Replica set alerts support these fields:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">REPLICA_SET_NAME</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">SHARD_NAME</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">CLUSTER_NAME</span></code>
Sharded cluster alerts support these fields:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">CLUSTER_NAME</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">SHARD_NAME</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Operator to apply when checking the current metric value against the threshold value.
Accepted values are:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">GREATER_THAN</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">LESS_THAN</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value to test with the specified operator. If <code class="docutils literal notranslate"><span class="pre">field_name</span></code> is set to TYPE_NAME, you can match on the following values:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">STANDALONE</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">CONFIG</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MONGOS</span></code></p></li>
</ul>
</li>
</ul>
<p>The <strong>metric_threshold</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">metric_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the metric to check.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - This must be set to AVERAGE. Atlas computes the current metric value as an average.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Operator to apply when checking the current metric value against the threshold value.
Accepted values are:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">GREATER_THAN</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">LESS_THAN</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Threshold value outside of which an alert will be triggered.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">units</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The units for the threshold value. Depends on the type of metric.
Accepted values are:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">RAW</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">BITS</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">BYTES</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">KILOBITS</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">KILOBYTES</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MEGABITS</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MEGABYTES</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GIGABITS</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GIGABYTES</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">TERABYTES</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">PETABYTES</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MILLISECONDS</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">SECONDS</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MINUTES</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HOURS</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">DAYS</span></code></p></li>
</ul>
</li>
</ul>
<p>The <strong>notifications</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">apiToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Slack API token. Required for the SLACK notifications type. If the token later becomes invalid, Atlas sends an email to the project owner and eventually removes the token.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">channelName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Slack channel name. Required for the SLACK notifications type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">datadogApiKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Datadog API Key. Found in the Datadog dashboard. Required for the DATADOG notifications type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">datadogRegion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Region that indicates which API URL to use. Accepted regions are: <code class="docutils literal notranslate"><span class="pre">US</span></code>, <code class="docutils literal notranslate"><span class="pre">EU</span></code>. The default Datadog region is US.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">delayMin</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of minutes to wait after an alert condition is detected before sending out the first notification.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Email address to which alert notifications are sent. Required for the EMAIL notifications type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Flag indicating if email notifications should be sent. Configurable for <code class="docutils literal notranslate"><span class="pre">ORG</span></code>, <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>, and <code class="docutils literal notranslate"><span class="pre">USER</span></code> notifications types.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">flowName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Flowdock flow name in lower-case letters. Required for the <code class="docutils literal notranslate"><span class="pre">FLOWDOCK</span></code> notifications type</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">flowdockApiToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Flowdock personal API token. Required for the <code class="docutils literal notranslate"><span class="pre">FLOWDOCK</span></code> notifications type. If the token later becomes invalid, Atlas sends an email to the project owner and eventually removes the token.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">intervalMin</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of minutes to wait between successive notifications for unacknowledged alerts that are not resolved. The minimum value is 5.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mobileNumber</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Mobile number to which alert notifications are sent. Required for the SMS notifications type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">opsGenieApiKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Opsgenie API Key. Required for the <code class="docutils literal notranslate"><span class="pre">OPS_GENIE</span></code> notifications type. If the key later becomes invalid, Atlas sends an email to the project owner and eventually removes the token.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">opsGenieRegion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Region that indicates which API URL to use. Accepted regions are: <code class="docutils literal notranslate"><span class="pre">US</span></code> ,<code class="docutils literal notranslate"><span class="pre">EU</span></code>. The default Opsgenie region is US.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">orgName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Flowdock organization name in lower-case letters. This is the name that appears after www.flowdock.com/app/ in the URL string. Required for the FLOWDOCK notifications type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">roles</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - PagerDuty service key. Required for the PAGER_DUTY notifications type. If the key later becomes invalid, Atlas sends an email to the project owner and eventually removes the key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Flag indicating if text message notifications should be sent. Configurable for <code class="docutils literal notranslate"><span class="pre">ORG</span></code>, <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>, and <code class="docutils literal notranslate"><span class="pre">USER</span></code> notifications types.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">team_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Unique identifier of a team.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">typeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of alert notification.
Accepted values are:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">DATADOG</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">EMAIL</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">FLOWDOCK</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP</span></code> (Project)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">OPS_GENIE</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ORG</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">PAGER_DUTY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">SLACK</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">SMS</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">TEAM</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">USER</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">VICTOR_OPS</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the Atlas user to which to send notifications. Only a user in the project that owns the alert configuration is allowed here. Required for the <code class="docutils literal notranslate"><span class="pre">USER</span></code> notifications type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">victorOpsApiKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - VictorOps API key. Required for the <code class="docutils literal notranslate"><span class="pre">VICTOR_OPS</span></code> notifications type. If the key later becomes invalid, Atlas sends an email to the project owner and eventually removes the key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">victorOpsRoutingKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - VictorOps routing key. Optional for the <code class="docutils literal notranslate"><span class="pre">VICTOR_OPS</span></code> notifications type. If the key later becomes invalid, Atlas sends an email to the project owner and eventually removes the key.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.AlertConfiguration.alert_configuration_id">
<code class="sig-name descname">alert_configuration_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.AlertConfiguration.alert_configuration_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier for the alert configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.AlertConfiguration.created">
<code class="sig-name descname">created</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.AlertConfiguration.created" title="Permalink to this definition">¶</a></dt>
<dd><p>Timestamp in ISO 8601 date and time format in UTC when this alert configuration was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.AlertConfiguration.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.AlertConfiguration.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>It is not required, but If the attribute is omitted, by default will be false, and the configuration would be disabled. You must set true to enable the configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.AlertConfiguration.event_type">
<code class="sig-name descname">event_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.AlertConfiguration.event_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of event that will trigger an alert.
Alert type  Possible values:</p>
<ul class="simple">
<li><p>Host</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">OUTSIDE_METRIC_THRESHOLD</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HOST_RESTARTED</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HOST_UPGRADED</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HOST_NOW_SECONDARY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HOST_NOW_PRIMARY</span></code></p></li>
<li><p>Replica set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">NO_PRIMARY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">TOO_MANY_ELECTIONS</span></code></p></li>
<li><p>Sharded cluster</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">CLUSTER_MONGOS_IS_MISSING</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">User</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">JOINED_GROUP</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">REMOVED_FROM_GROUP</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">USER_ROLES_CHANGED_AUDIT</span></code></p></li>
<li><p>Project</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">USERS_AWAITING_APPROVAL</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">USERS_WITHOUT_MULTI_FACTOR_AUTH</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP_CREATED</span></code></p></li>
<li><p>Team</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">JOINED_TEAM</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">REMOVED_FROM_TEAM</span></code></p></li>
<li><p>Organization</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">INVITED_TO_ORG</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">JOINED_ORG</span></code></p></li>
<li><p>Data Explorer</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">DATA_EXPLORER</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">DATA_EXPLORER_CRUD</span></code></p></li>
<li><p>Billing</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">CREDIT_CARD_ABOUT_TO_EXPIRE</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">CHARGE_SUCCEEDED</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">INVOICE_CLOSED</span></code></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.AlertConfiguration.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.AlertConfiguration.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project where the alert configuration will create.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.AlertConfiguration.updated">
<code class="sig-name descname">updated</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.AlertConfiguration.updated" title="Permalink to this definition">¶</a></dt>
<dd><p>Timestamp in ISO 8601 date and time format in UTC when this alert configuration was last updated.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.AlertConfiguration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alert_configuration_id=None</em>, <em class="sig-param">created=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">event_type=None</em>, <em class="sig-param">matchers=None</em>, <em class="sig-param">metric_threshold=None</em>, <em class="sig-param">notifications=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">updated=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AlertConfiguration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AlertConfiguration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alert_configuration_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier for the alert configuration.</p></li>
<li><p><strong>created</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Timestamp in ISO 8601 date and time format in UTC when this alert configuration was created.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – It is not required, but If the attribute is omitted, by default will be false, and the configuration would be disabled. You must set true to enable the configuration.</p></li>
<li><p><strong>event_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of event that will trigger an alert.
Alert type       Possible values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* Host
- `OUTSIDE_METRIC_THRESHOLD`
- `HOST_RESTARTED`
- `HOST_UPGRADED`
- `HOST_NOW_SECONDARY`
- `HOST_NOW_PRIMARY`
* Replica set
- `NO_PRIMARY`
- `TOO_MANY_ELECTIONS`
* Sharded cluster
- `CLUSTER_MONGOS_IS_MISSING`
- `User`
- `JOINED_GROUP`
- `REMOVED_FROM_GROUP`
- `USER_ROLES_CHANGED_AUDIT`
* Project
- `USERS_AWAITING_APPROVAL`
- `USERS_WITHOUT_MULTI_FACTOR_AUTH`
- `GROUP_CREATED`
* Team
- `JOINED_TEAM`
- `REMOVED_FROM_TEAM`
* Organization
- `INVITED_TO_ORG`
- `JOINED_ORG`
* Data Explorer
- `DATA_EXPLORER`
- `DATA_EXPLORER_CRUD`
* Billing
- `CREDIT_CARD_ABOUT_TO_EXPIRE`
- `CHARGE_SUCCEEDED`
- `INVOICE_CLOSED`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project where the alert configuration will create.</p></li>
<li><p><strong>updated</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Timestamp in ISO 8601 date and time format in UTC when this alert configuration was last updated.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>matchers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fieldName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the field in the target object to match on.
Host alerts support these fields:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">TYPE_NAME</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HOSTNAME</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">PORT</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HOSTNAME_AND_PORT</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">REPLICA_SET_NAME</span></code>
Replica set alerts support these fields:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">REPLICA_SET_NAME</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">SHARD_NAME</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">CLUSTER_NAME</span></code>
Sharded cluster alerts support these fields:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">CLUSTER_NAME</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">SHARD_NAME</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Operator to apply when checking the current metric value against the threshold value.
Accepted values are:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">GREATER_THAN</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">LESS_THAN</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value to test with the specified operator. If <code class="docutils literal notranslate"><span class="pre">field_name</span></code> is set to TYPE_NAME, you can match on the following values:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">SECONDARY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">STANDALONE</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">CONFIG</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MONGOS</span></code></p></li>
</ul>
</li>
</ul>
<p>The <strong>metric_threshold</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">metric_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the metric to check.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - This must be set to AVERAGE. Atlas computes the current metric value as an average.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Operator to apply when checking the current metric value against the threshold value.
Accepted values are:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">GREATER_THAN</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">LESS_THAN</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Threshold value outside of which an alert will be triggered.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">units</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The units for the threshold value. Depends on the type of metric.
Accepted values are:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">RAW</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">BITS</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">BYTES</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">KILOBITS</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">KILOBYTES</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MEGABITS</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MEGABYTES</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GIGABITS</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GIGABYTES</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">TERABYTES</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">PETABYTES</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MILLISECONDS</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">SECONDS</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MINUTES</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HOURS</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">DAYS</span></code></p></li>
</ul>
</li>
</ul>
<p>The <strong>notifications</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">apiToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Slack API token. Required for the SLACK notifications type. If the token later becomes invalid, Atlas sends an email to the project owner and eventually removes the token.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">channelName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Slack channel name. Required for the SLACK notifications type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">datadogApiKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Datadog API Key. Found in the Datadog dashboard. Required for the DATADOG notifications type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">datadogRegion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Region that indicates which API URL to use. Accepted regions are: <code class="docutils literal notranslate"><span class="pre">US</span></code>, <code class="docutils literal notranslate"><span class="pre">EU</span></code>. The default Datadog region is US.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">delayMin</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of minutes to wait after an alert condition is detected before sending out the first notification.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Email address to which alert notifications are sent. Required for the EMAIL notifications type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Flag indicating if email notifications should be sent. Configurable for <code class="docutils literal notranslate"><span class="pre">ORG</span></code>, <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>, and <code class="docutils literal notranslate"><span class="pre">USER</span></code> notifications types.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">flowName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Flowdock flow name in lower-case letters. Required for the <code class="docutils literal notranslate"><span class="pre">FLOWDOCK</span></code> notifications type</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">flowdockApiToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Flowdock personal API token. Required for the <code class="docutils literal notranslate"><span class="pre">FLOWDOCK</span></code> notifications type. If the token later becomes invalid, Atlas sends an email to the project owner and eventually removes the token.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">intervalMin</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of minutes to wait between successive notifications for unacknowledged alerts that are not resolved. The minimum value is 5.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mobileNumber</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Mobile number to which alert notifications are sent. Required for the SMS notifications type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">opsGenieApiKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Opsgenie API Key. Required for the <code class="docutils literal notranslate"><span class="pre">OPS_GENIE</span></code> notifications type. If the key later becomes invalid, Atlas sends an email to the project owner and eventually removes the token.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">opsGenieRegion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Region that indicates which API URL to use. Accepted regions are: <code class="docutils literal notranslate"><span class="pre">US</span></code> ,<code class="docutils literal notranslate"><span class="pre">EU</span></code>. The default Opsgenie region is US.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">orgName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Flowdock organization name in lower-case letters. This is the name that appears after www.flowdock.com/app/ in the URL string. Required for the FLOWDOCK notifications type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">roles</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - PagerDuty service key. Required for the PAGER_DUTY notifications type. If the key later becomes invalid, Atlas sends an email to the project owner and eventually removes the key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Flag indicating if text message notifications should be sent. Configurable for <code class="docutils literal notranslate"><span class="pre">ORG</span></code>, <code class="docutils literal notranslate"><span class="pre">GROUP</span></code>, and <code class="docutils literal notranslate"><span class="pre">USER</span></code> notifications types.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">team_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Unique identifier of a team.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">typeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of alert notification.
Accepted values are:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">DATADOG</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">EMAIL</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">FLOWDOCK</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP</span></code> (Project)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">OPS_GENIE</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ORG</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">PAGER_DUTY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">SLACK</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">SMS</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">TEAM</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">USER</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">VICTOR_OPS</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the Atlas user to which to send notifications. Only a user in the project that owns the alert configuration is allowed here. Required for the <code class="docutils literal notranslate"><span class="pre">USER</span></code> notifications type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">victorOpsApiKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - VictorOps API key. Required for the <code class="docutils literal notranslate"><span class="pre">VICTOR_OPS</span></code> notifications type. If the key later becomes invalid, Atlas sends an email to the project owner and eventually removes the key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">victorOpsRoutingKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - VictorOps routing key. Optional for the <code class="docutils literal notranslate"><span class="pre">VICTOR_OPS</span></code> notifications type. If the key later becomes invalid, Atlas sends an email to the project owner and eventually removes the key.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.AlertConfiguration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AlertConfiguration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.AlertConfiguration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AlertConfiguration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.Auditing">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">Auditing</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">audit_authorization_success=None</em>, <em class="sig-param">audit_filter=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Auditing" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.Auditing</span></code> provides an Auditing resource. This allows auditing to be created.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>audit_authorization_success</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – JSON-formatted audit filter used by the project</p></li>
<li><p><strong>audit_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether the auditing system captures successful authentication attempts for audit filters using the “atype” : “authCheck” auditing event. For more information, see auditAuthorizationSuccess</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Denotes whether or not the project associated with the {project_id} has database auditing enabled.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to configure auditing.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.Auditing.audit_authorization_success">
<code class="sig-name descname">audit_authorization_success</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Auditing.audit_authorization_success" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON-formatted audit filter used by the project</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Auditing.audit_filter">
<code class="sig-name descname">audit_filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Auditing.audit_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the auditing system captures successful authentication attempts for audit filters using the “atype” : “authCheck” auditing event. For more information, see auditAuthorizationSuccess</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Auditing.configuration_type">
<code class="sig-name descname">configuration_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Auditing.configuration_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Denotes the configuration method for the audit filter. Possible values are:</p>
<ul class="simple">
<li><p>NONE - auditing not configured for the project.</p></li>
<li><p>FILTER_BUILDER - auditing configured via Atlas UI filter builder.</p></li>
<li><p>FILTER_JSON - auditing configured via Atlas custom filter or API.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Auditing.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Auditing.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Denotes whether or not the project associated with the {project_id} has database auditing enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Auditing.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Auditing.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique ID for the project to configure auditing.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.Auditing.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">audit_authorization_success=None</em>, <em class="sig-param">audit_filter=None</em>, <em class="sig-param">configuration_type=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">project_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Auditing.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Auditing resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>audit_authorization_success</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – JSON-formatted audit filter used by the project</p></li>
<li><p><strong>audit_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether the auditing system captures successful authentication attempts for audit filters using the “atype” : “authCheck” auditing event. For more information, see auditAuthorizationSuccess</p></li>
<li><p><strong>configuration_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Denotes the configuration method for the audit filter. Possible values are:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">NONE</span> <span class="o">-</span> <span class="n">auditing</span> <span class="ow">not</span> <span class="n">configured</span> <span class="k">for</span> <span class="n">the</span> <span class="n">project</span><span class="o">.</span>
<span class="o">*</span> <span class="n">FILTER_BUILDER</span> <span class="o">-</span> <span class="n">auditing</span> <span class="n">configured</span> <span class="n">via</span> <span class="n">Atlas</span> <span class="n">UI</span> <span class="nb">filter</span> <span class="n">builder</span><span class="o">.</span>
<span class="o">*</span> <span class="n">FILTER_JSON</span> <span class="o">-</span> <span class="n">auditing</span> <span class="n">configured</span> <span class="n">via</span> <span class="n">Atlas</span> <span class="n">custom</span> <span class="nb">filter</span> <span class="ow">or</span> <span class="n">API</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Denotes whether or not the project associated with the {project_id} has database auditing enabled.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to configure auditing.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.Auditing.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Auditing.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.Auditing.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Auditing.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.AwaitableGet509AuthenticationDatabaseUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGet509AuthenticationDatabaseUserResult</code><span class="sig-paren">(</span><em class="sig-param">certificates=None</em>, <em class="sig-param">customer_x509_cas=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGet509AuthenticationDatabaseUserResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.AwaitableGetAlertConfigurationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetAlertConfigurationResult</code><span class="sig-paren">(</span><em class="sig-param">alert_configuration_id=None</em>, <em class="sig-param">created=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">event_type=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">matchers=None</em>, <em class="sig-param">metric_threshold=None</em>, <em class="sig-param">notifications=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">updated=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetAlertConfigurationResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.AwaitableGetAuditingResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetAuditingResult</code><span class="sig-paren">(</span><em class="sig-param">audit_authorization_success=None</em>, <em class="sig-param">audit_filter=None</em>, <em class="sig-param">configuration_type=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">project_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetAuditingResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.AwaitableGetCloudProviderSnapshotBackupPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetCloudProviderSnapshotBackupPolicyResult</code><span class="sig-paren">(</span><em class="sig-param">cluster_id=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">next_snapshot=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">reference_hour_of_day=None</em>, <em class="sig-param">reference_minute_of_hour=None</em>, <em class="sig-param">restore_window_days=None</em>, <em class="sig-param">update_snapshots=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetCloudProviderSnapshotBackupPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.AwaitableGetCloudProviderSnapshotRestoreJobResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetCloudProviderSnapshotRestoreJobResult</code><span class="sig-paren">(</span><em class="sig-param">cancelled=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">delivery_type=None</em>, <em class="sig-param">delivery_urls=None</em>, <em class="sig-param">expired=None</em>, <em class="sig-param">expires_at=None</em>, <em class="sig-param">finished_at=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">job_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">snapshot_id=None</em>, <em class="sig-param">target_cluster_name=None</em>, <em class="sig-param">target_project_id=None</em>, <em class="sig-param">timestamp=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetCloudProviderSnapshotRestoreJobResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.AwaitableGetCloudProviderSnapshotRestoreJobsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetCloudProviderSnapshotRestoreJobsResult</code><span class="sig-paren">(</span><em class="sig-param">cluster_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">results=None</em>, <em class="sig-param">total_count=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetCloudProviderSnapshotRestoreJobsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.AwaitableGetCloudProviderSnapshotResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetCloudProviderSnapshotResult</code><span class="sig-paren">(</span><em class="sig-param">cluster_name=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">expires_at=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">master_key_uuid=None</em>, <em class="sig-param">mongod_version=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">snapshot_id=None</em>, <em class="sig-param">snapshot_type=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">storage_size_bytes=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetCloudProviderSnapshotResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.AwaitableGetCloudProviderSnapshotsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetCloudProviderSnapshotsResult</code><span class="sig-paren">(</span><em class="sig-param">cluster_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">results=None</em>, <em class="sig-param">total_count=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetCloudProviderSnapshotsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.AwaitableGetClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetClusterResult</code><span class="sig-paren">(</span><em class="sig-param">auto_scaling_disk_gb_enabled=None</em>, <em class="sig-param">backing_provider_name=None</em>, <em class="sig-param">backup_enabled=None</em>, <em class="sig-param">bi_connector=None</em>, <em class="sig-param">cluster_type=None</em>, <em class="sig-param">connection_strings=None</em>, <em class="sig-param">disk_size_gb=None</em>, <em class="sig-param">encryption_at_rest_provider=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">mongo_db_major_version=None</em>, <em class="sig-param">mongo_db_version=None</em>, <em class="sig-param">mongo_uri=None</em>, <em class="sig-param">mongo_uri_updated=None</em>, <em class="sig-param">mongo_uri_with_options=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">num_shards=None</em>, <em class="sig-param">paused=None</em>, <em class="sig-param">pit_enabled=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">provider_backup_enabled=None</em>, <em class="sig-param">provider_disk_iops=None</em>, <em class="sig-param">provider_disk_type_name=None</em>, <em class="sig-param">provider_encrypt_ebs_volume=None</em>, <em class="sig-param">provider_instance_size_name=None</em>, <em class="sig-param">provider_name=None</em>, <em class="sig-param">provider_region_name=None</em>, <em class="sig-param">provider_volume_type=None</em>, <em class="sig-param">replication_factor=None</em>, <em class="sig-param">replication_specs=None</em>, <em class="sig-param">snapshot_backup_policies=None</em>, <em class="sig-param">srv_address=None</em>, <em class="sig-param">state_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.AwaitableGetClustersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetClustersResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">results=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetClustersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.AwaitableGetCustomDbRoleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetCustomDbRoleResult</code><span class="sig-paren">(</span><em class="sig-param">actions=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">inherited_roles=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">role_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetCustomDbRoleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.AwaitableGetCustomDbRolesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetCustomDbRolesResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">results=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetCustomDbRolesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.AwaitableGetDatabaseUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetDatabaseUserResult</code><span class="sig-paren">(</span><em class="sig-param">auth_database_name=None</em>, <em class="sig-param">database_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">x509_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetDatabaseUserResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.AwaitableGetDatabaseUsersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetDatabaseUsersResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">results=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetDatabaseUsersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.AwaitableGetGlobalClusterConfigResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetGlobalClusterConfigResult</code><span class="sig-paren">(</span><em class="sig-param">cluster_name=None</em>, <em class="sig-param">custom_zone_mapping=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">managed_namespaces=None</em>, <em class="sig-param">project_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetGlobalClusterConfigResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.AwaitableGetMaintenanceWindowResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetMaintenanceWindowResult</code><span class="sig-paren">(</span><em class="sig-param">day_of_week=None</em>, <em class="sig-param">hour_of_day=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">number_of_deferrals=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">start_asap=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetMaintenanceWindowResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.AwaitableGetNetworkContainerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetNetworkContainerResult</code><span class="sig-paren">(</span><em class="sig-param">atlas_cidr_block=None</em>, <em class="sig-param">azure_subscription_id=None</em>, <em class="sig-param">container_id=None</em>, <em class="sig-param">gcp_project_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">network_name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">provider_name=None</em>, <em class="sig-param">provisioned=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">region_name=None</em>, <em class="sig-param">vnet_name=None</em>, <em class="sig-param">vpc_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetNetworkContainerResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.AwaitableGetNetworkContainersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetNetworkContainersResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">provider_name=None</em>, <em class="sig-param">results=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetNetworkContainersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.AwaitableGetNetworkPeeringResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetNetworkPeeringResult</code><span class="sig-paren">(</span><em class="sig-param">accepter_region_name=None</em>, <em class="sig-param">atlas_cidr_block=None</em>, <em class="sig-param">atlas_id=None</em>, <em class="sig-param">aws_account_id=None</em>, <em class="sig-param">azure_directory_id=None</em>, <em class="sig-param">azure_subscription_id=None</em>, <em class="sig-param">connection_id=None</em>, <em class="sig-param">container_id=None</em>, <em class="sig-param">error_message=None</em>, <em class="sig-param">error_state=None</em>, <em class="sig-param">error_state_name=None</em>, <em class="sig-param">gcp_project_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">network_name=None</em>, <em class="sig-param">peering_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">provider_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">route_table_cidr_block=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">status_name=None</em>, <em class="sig-param">vnet_name=None</em>, <em class="sig-param">vpc_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetNetworkPeeringResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.AwaitableGetNetworkPeeringsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetNetworkPeeringsResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">results=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetNetworkPeeringsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.AwaitableGetPrivateEndpointInterfaceLinkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetPrivateEndpointInterfaceLinkResult</code><span class="sig-paren">(</span><em class="sig-param">connection_status=None</em>, <em class="sig-param">delete_requested=None</em>, <em class="sig-param">error_message=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">interface_endpoint_id=None</em>, <em class="sig-param">private_link_id=None</em>, <em class="sig-param">project_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetPrivateEndpointInterfaceLinkResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.AwaitableGetPrivateEndpointResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetPrivateEndpointResult</code><span class="sig-paren">(</span><em class="sig-param">endpoint_service_name=None</em>, <em class="sig-param">error_message=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">interface_endpoints=None</em>, <em class="sig-param">private_link_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetPrivateEndpointResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.AwaitableGetProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetProjectResult</code><span class="sig-paren">(</span><em class="sig-param">cluster_count=None</em>, <em class="sig-param">created=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">org_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">teams=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.AwaitableGetProjectsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetProjectsResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">results=None</em>, <em class="sig-param">total_count=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetProjectsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.AwaitableGetTeamResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetTeamResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">org_id=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">usernames=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetTeamResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.AwaitableGetTeamsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetTeamsResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">org_id=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">usernames=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetTeamsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">CloudProviderSnapshot</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">retention_in_days=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.CloudProviderSnapshot</span></code> provides a resource to take a cloud provider snapshot on demand.
On-demand snapshots happen immediately, unlike scheduled snapshots which occur at regular intervals. If there is already an on-demand snapshot with a status of queued or inProgress, you must wait until Atlas has completed the on-demand snapshot before taking another.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Atlas cluster that contains the snapshots you want to retrieve.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the on-demand snapshot.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the project for the Atlas cluster.</p></li>
<li><p><strong>retention_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of days that Atlas should retain the on-demand snapshot. Must be at least 1.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.cluster_name">
<code class="sig-name descname">cluster_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.cluster_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Atlas cluster that contains the snapshots you want to retrieve.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC ISO 8601 formatted point in time when Atlas took the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the on-demand snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.expires_at">
<code class="sig-name descname">expires_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.expires_at" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC ISO 8601 formatted point in time when Atlas will delete the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.master_key_uuid">
<code class="sig-name descname">master_key_uuid</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.master_key_uuid" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique ID of the AWS KMS Customer Master Key used to encrypt the snapshot. Only visible for clusters using Encryption at Rest via Customer KMS.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.mongod_version">
<code class="sig-name descname">mongod_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.mongod_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of the MongoDB server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier of the project for the Atlas cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.retention_in_days">
<code class="sig-name descname">retention_in_days</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.retention_in_days" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of days that Atlas should retain the on-demand snapshot. Must be at least 1.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.snapshot_id">
<code class="sig-name descname">snapshot_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.snapshot_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.snapshot_type">
<code class="sig-name descname">snapshot_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.snapshot_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specified the type of snapshot. Valid values are onDemand and scheduled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Current status of the snapshot. One of the following values will be returned: queued, inProgress, completed, failed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.storage_size_bytes">
<code class="sig-name descname">storage_size_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.storage_size_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the size of the snapshot in bytes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the type of cluster: replicaSet or shardedCluster.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">expires_at=None</em>, <em class="sig-param">master_key_uuid=None</em>, <em class="sig-param">mongod_version=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">retention_in_days=None</em>, <em class="sig-param">snapshot_id=None</em>, <em class="sig-param">snapshot_type=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">storage_size_bytes=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudProviderSnapshot resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Atlas cluster that contains the snapshots you want to retrieve.</p></li>
<li><p><strong>created_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – UTC ISO 8601 formatted point in time when Atlas took the snapshot.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the on-demand snapshot.</p></li>
<li><p><strong>expires_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – UTC ISO 8601 formatted point in time when Atlas will delete the snapshot.</p></li>
<li><p><strong>master_key_uuid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique ID of the AWS KMS Customer Master Key used to encrypt the snapshot. Only visible for clusters using Encryption at Rest via Customer KMS.</p></li>
<li><p><strong>mongod_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of the MongoDB server.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the project for the Atlas cluster.</p></li>
<li><p><strong>retention_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of days that Atlas should retain the on-demand snapshot. Must be at least 1.</p></li>
<li><p><strong>snapshot_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the snapshot.</p></li>
<li><p><strong>snapshot_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specified the type of snapshot. Valid values are onDemand and scheduled.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Current status of the snapshot. One of the following values will be returned: queued, inProgress, completed, failed.</p></li>
<li><p><strong>storage_size_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the size of the snapshot in bytes.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of cluster: replicaSet or shardedCluster.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">CloudProviderSnapshotBackupPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">reference_hour_of_day=None</em>, <em class="sig-param">reference_minute_of_hour=None</em>, <em class="sig-param">restore_window_days=None</em>, <em class="sig-param">update_snapshots=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.CloudProviderSnapshotBackupPolicy</span></code> provides a resource that enables you to view and modify the snapshot schedule and retention settings for an Atlas cluster with Cloud Provider Snapshots enabled.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Atlas cluster that contains the snapshot backup policy you want to retrieve.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Contains a document for each backup policy item in the desired updated backup policy.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `policies.#.id` - (Required) Unique identifier of the backup policy that you want to update. policies.#.id is a value obtained via the .Cluster resource. provider_backup_enabled of the .Cluster resource must be set to true. See the example above for how to refer to the .Cluster resource for policies.#.id
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the project for the Atlas cluster.</p></li>
<li><p><strong>reference_hour_of_day</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – UTC Hour of day between 0 and 23, inclusive, representing which hour of the day that Atlas takes snapshots for backup policy items.</p></li>
<li><p><strong>reference_minute_of_hour</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – UTC Minutes after referenceHourOfDay that Atlas takes snapshots for backup policy items. Must be between 0 and 59, inclusive.</p></li>
<li><p><strong>restore_window_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of days back in time you can restore to with point-in-time accuracy. Must be a positive, non-zero integer.</p></li>
<li><p><strong>update_snapshots</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specify true to apply the retention changes in the updated backup policy to snapshots that Atlas took previously.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyItems</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">frequencyInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frequencyType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.cluster_id">
<code class="sig-name descname">cluster_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the Atlas cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.cluster_name">
<code class="sig-name descname">cluster_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.cluster_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Atlas cluster that contains the snapshot backup policy you want to retrieve.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.next_snapshot">
<code class="sig-name descname">next_snapshot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.next_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Timestamp in the number of seconds that have elapsed since the UNIX epoch when Atlas takes the next snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.policies">
<code class="sig-name descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains a document for each backup policy item in the desired updated backup policy.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">policies.#.id</span></code> - (Required) Unique identifier of the backup policy that you want to update. policies.#.id is a value obtained via the .Cluster resource. provider_backup_enabled of the .Cluster resource must be set to true. See the example above for how to refer to the .Cluster resource for policies.#.id</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyItems</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">frequencyInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frequencyType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionValue</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier of the project for the Atlas cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.reference_hour_of_day">
<code class="sig-name descname">reference_hour_of_day</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.reference_hour_of_day" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC Hour of day between 0 and 23, inclusive, representing which hour of the day that Atlas takes snapshots for backup policy items.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.reference_minute_of_hour">
<code class="sig-name descname">reference_minute_of_hour</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.reference_minute_of_hour" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC Minutes after referenceHourOfDay that Atlas takes snapshots for backup policy items. Must be between 0 and 59, inclusive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.restore_window_days">
<code class="sig-name descname">restore_window_days</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.restore_window_days" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of days back in time you can restore to with point-in-time accuracy. Must be a positive, non-zero integer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.update_snapshots">
<code class="sig-name descname">update_snapshots</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.update_snapshots" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify true to apply the retention changes in the updated backup policy to snapshots that Atlas took previously.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_id=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">next_snapshot=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">reference_hour_of_day=None</em>, <em class="sig-param">reference_minute_of_hour=None</em>, <em class="sig-param">restore_window_days=None</em>, <em class="sig-param">update_snapshots=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudProviderSnapshotBackupPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the Atlas cluster.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Atlas cluster that contains the snapshot backup policy you want to retrieve.</p></li>
<li><p><strong>next_snapshot</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Timestamp in the number of seconds that have elapsed since the UNIX epoch when Atlas takes the next snapshot.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Contains a document for each backup policy item in the desired updated backup policy.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `policies.#.id` - (Required) Unique identifier of the backup policy that you want to update. policies.#.id is a value obtained via the .Cluster resource. provider_backup_enabled of the .Cluster resource must be set to true. See the example above for how to refer to the .Cluster resource for policies.#.id
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the project for the Atlas cluster.</p></li>
<li><p><strong>reference_hour_of_day</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – UTC Hour of day between 0 and 23, inclusive, representing which hour of the day that Atlas takes snapshots for backup policy items.</p></li>
<li><p><strong>reference_minute_of_hour</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – UTC Minutes after referenceHourOfDay that Atlas takes snapshots for backup policy items. Must be between 0 and 59, inclusive.</p></li>
<li><p><strong>restore_window_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of days back in time you can restore to with point-in-time accuracy. Must be a positive, non-zero integer.</p></li>
<li><p><strong>update_snapshots</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specify true to apply the retention changes in the updated backup policy to snapshots that Atlas took previously.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyItems</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">frequencyInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frequencyType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">CloudProviderSnapshotRestoreJob</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">delivery_type=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">snapshot_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.CloudProviderSnapshotRestoreJob</span></code> provides a resource to create a new restore job from a cloud provider snapshot of a specified cluster. The restore job can be one of two types:</p>
<ul class="simple">
<li><p><strong>automated:</strong> Atlas automatically restores the snapshot with snapshotId to the Atlas cluster with name targetClusterName in the Atlas project with targetGroupId.</p></li>
<li><p><strong>download:</strong> Atlas provides a URL to download a .tar.gz of the snapshot with snapshotId. The contents of the archive contain the data files for your Atlas cluster.</p></li>
</ul>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Atlas cluster whose snapshot you want to restore.</p></li>
<li><p><strong>delivery_type</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Type of restore job to create. Possible values are: <strong>download</strong> or <strong>automated</strong>, only one must be set it in <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the project for the Atlas cluster whose snapshot you want to restore.</p></li>
<li><p><strong>snapshot_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the snapshot to restore.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>delivery_type</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automated</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">download</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_cluster_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the target Atlas cluster to which the restore job restores the snapshot. Only required if deliveryType is automated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.cancelled">
<code class="sig-name descname">cancelled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.cancelled" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the restore job was canceled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.cluster_name">
<code class="sig-name descname">cluster_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.cluster_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Atlas cluster whose snapshot you want to restore.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC ISO 8601 formatted point in time when Atlas created the restore job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.delivery_type">
<code class="sig-name descname">delivery_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.delivery_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of restore job to create. Possible values are: <strong>download</strong> or <strong>automated</strong>, only one must be set it in <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automated</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">download</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_cluster_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the target Atlas cluster to which the restore job restores the snapshot. Only required if deliveryType is automated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.delivery_urls">
<code class="sig-name descname">delivery_urls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.delivery_urls" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more URLs for the compressed snapshot files for manual download. Only visible if deliveryType is download.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.expired">
<code class="sig-name descname">expired</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.expired" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the restore job expired.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.expires_at">
<code class="sig-name descname">expires_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.expires_at" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC ISO 8601 formatted point in time when the restore job expires.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.finished_at">
<code class="sig-name descname">finished_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.finished_at" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC ISO 8601 formatted point in time when the restore job completed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier of the project for the Atlas cluster whose snapshot you want to restore.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.snapshot_id">
<code class="sig-name descname">snapshot_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.snapshot_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the snapshot to restore.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.snapshot_restore_job_id">
<code class="sig-name descname">snapshot_restore_job_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.snapshot_restore_job_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier of the restore job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.timestamp">
<code class="sig-name descname">timestamp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.timestamp" title="Permalink to this definition">¶</a></dt>
<dd><p>Timestamp in ISO 8601 date and time format in UTC when the snapshot associated to snapshotId was taken.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cancelled=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">delivery_type=None</em>, <em class="sig-param">delivery_urls=None</em>, <em class="sig-param">expired=None</em>, <em class="sig-param">expires_at=None</em>, <em class="sig-param">finished_at=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">snapshot_id=None</em>, <em class="sig-param">snapshot_restore_job_id=None</em>, <em class="sig-param">timestamp=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudProviderSnapshotRestoreJob resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cancelled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether the restore job was canceled.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Atlas cluster whose snapshot you want to restore.</p></li>
<li><p><strong>created_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – UTC ISO 8601 formatted point in time when Atlas created the restore job.</p></li>
<li><p><strong>delivery_type</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Type of restore job to create. Possible values are: <strong>download</strong> or <strong>automated</strong>, only one must be set it in <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>delivery_urls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more URLs for the compressed snapshot files for manual download. Only visible if deliveryType is download.</p></li>
<li><p><strong>expired</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether the restore job expired.</p></li>
<li><p><strong>expires_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – UTC ISO 8601 formatted point in time when the restore job expires.</p></li>
<li><p><strong>finished_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – UTC ISO 8601 formatted point in time when the restore job completed.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the project for the Atlas cluster whose snapshot you want to restore.</p></li>
<li><p><strong>snapshot_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the snapshot to restore.</p></li>
<li><p><strong>snapshot_restore_job_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the restore job.</p></li>
<li><p><strong>timestamp</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Timestamp in ISO 8601 date and time format in UTC when the snapshot associated to snapshotId was taken.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>delivery_type</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automated</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">download</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_cluster_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the target Atlas cluster to which the restore job restores the snapshot. Only required if deliveryType is automated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">advanced_configuration=None</em>, <em class="sig-param">auto_scaling_disk_gb_enabled=None</em>, <em class="sig-param">backing_provider_name=None</em>, <em class="sig-param">backup_enabled=None</em>, <em class="sig-param">bi_connector=None</em>, <em class="sig-param">cluster_type=None</em>, <em class="sig-param">disk_size_gb=None</em>, <em class="sig-param">encryption_at_rest_provider=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">mongo_db_major_version=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">num_shards=None</em>, <em class="sig-param">pit_enabled=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">provider_backup_enabled=None</em>, <em class="sig-param">provider_disk_iops=None</em>, <em class="sig-param">provider_disk_type_name=None</em>, <em class="sig-param">provider_encrypt_ebs_volume=None</em>, <em class="sig-param">provider_instance_size_name=None</em>, <em class="sig-param">provider_name=None</em>, <em class="sig-param">provider_region_name=None</em>, <em class="sig-param">provider_volume_type=None</em>, <em class="sig-param">replication_factor=None</em>, <em class="sig-param">replication_specs=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.Cluster</span></code> provides a Cluster resource. The resource lets you create, edit and delete clusters. The resource requires your Project ID.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
<p><strong>IMPORTANT:</strong>
<span class="raw-html-m2r"><br></span> &amp;#8226; Free tier cluster creation (M0) is not supported via API or by this Provider.
<span class="raw-html-m2r"><br></span> &amp;#8226; Shared tier clusters (M2, M5) cannot be upgraded to higher tiers via API or by this Provider.
<span class="raw-html-m2r"><br></span> &amp;#8226; Changes to cluster configurations can affect costs. Before making changes, please see <a class="reference external" href="https://docs.atlas.mongodb.com/billing/">Billing</a>.
<span class="raw-html-m2r"><br></span> &amp;#8226; If your Atlas project contains a custom role that uses actions introduced in a specific MongoDB version, you cannot create a cluster with a MongoDB version less than that version unless you delete the custom role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_scaling_disk_gb_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether disk auto-scaling is enabled. The default is true.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- Set to `true` to enable disk auto-scaling.
- Set to `false` to disable disk auto-scaling.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>backing_provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud service provider on which the server for a multi-tenant cluster is provisioned.</p></li>
<li><p><strong>backup_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Legacy Option - Set to true to enable Atlas continuous backups for the cluster.</p></li>
<li><p><strong>bi_connector</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies BI Connector for Atlas configuration on this cluster. BI Connector for Atlas is only available for M10+ clusters. See BI Connector below for more details.</p></li>
<li><p><strong>cluster_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of the cluster that you want to modify. You cannot convert a sharded cluster deployment to a replica set deployment.</p></li>
<li><p><strong>disk_size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size in gigabytes of the server’s root volume. You can add capacity by increasing this number, up to a maximum possible value of 4096 (i.e., 4 TB). This value must be a positive integer.</p></li>
<li><p><strong>encryption_at_rest_provider</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set the Encryption at Rest parameter.  Possible values are AWS, GCP, AZURE or NONE.  Requires M10 or greater and for backup_enabled to be false or omitted.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array containing key-value pairs that tag and categorize the cluster. Each key and value has a maximum length of 255 characters. You cannot set the key <code class="docutils literal notranslate"><span class="pre">Infrastructure</span> <span class="pre">Tool</span></code>, it is used for internal purposes to track aggregate usage.</p></li>
<li><p><strong>mongo_db_major_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of the cluster to deploy. Atlas supports the following MongoDB versions for M10+ clusters: <code class="docutils literal notranslate"><span class="pre">3.6</span></code>, <code class="docutils literal notranslate"><span class="pre">4.0</span></code>, or <code class="docutils literal notranslate"><span class="pre">4.2</span></code>. You must set this value to <code class="docutils literal notranslate"><span class="pre">4.2</span></code> if <code class="docutils literal notranslate"><span class="pre">provider_instance_size_name</span></code> is either M2 or M5.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the cluster as it appears in Atlas. Once the cluster is created, its name cannot be changed.</p></li>
<li><p><strong>num_shards</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of shards to deploy in the specified zone.</p></li>
<li><p><strong>pit_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <ul>
<li><p>Flag that indicates if the cluster uses Point-in-Time backups. If set to true, provider_backup_enabled must also be set to true.</p></li>
</ul>
</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to create the database user.</p></li>
<li><p><strong>provider_backup_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag indicating if the cluster uses Cloud Provider Snapshots for backups.</p></li>
<li><p><strong>provider_disk_iops</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum input/output operations per second (IOPS) the system can perform. The possible values depend on the selected providerSettings.instanceSizeName and diskSizeGB.</p></li>
<li><p><strong>provider_disk_type_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Azure disk type of the server’s root volume. If omitted, Atlas uses the default disk type for the selected providerSettings.instanceSizeName.  Example disk types and associated storage sizes: P4 - 32GB, P6 - 64GB, P10 - 128GB, P20 - 512GB, P30 - 1024GB, P40 - 2048GB, P50 - 4095GB.  More information and the most update to date disk types/storage sizes can be located at <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/clusters-create-one/">https://docs.atlas.mongodb.com/reference/api/clusters-create-one/</a>.</p></li>
<li><p><strong>provider_encrypt_ebs_volume</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If enabled, the Amazon EBS encryption feature encrypts the server’s root volume for both data at rest within the volume and for data moving between the volume and the instance.</p></li>
<li><p><strong>provider_instance_size_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Atlas provides different instance sizes, each with a default storage capacity and RAM size. The instance size you select is used for all the data-bearing servers in your cluster. See <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/clusters-create-one/">Create a Cluster</a> <code class="docutils literal notranslate"><span class="pre">providerSettings.instanceSizeName</span></code> for valid values and default resources.</p></li>
<li><p><strong>provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud service provider on which the servers are provisioned.</p></li>
<li><p><strong>provider_region_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Physical location of your MongoDB cluster. The region you choose can affect network latency for clients accessing your databases.  Requires the Atlas Region name, see the reference list for <a class="reference external" href="https://docs.atlas.mongodb.com/reference/amazon-aws/">AWS</a>, <a class="reference external" href="https://docs.atlas.mongodb.com/reference/google-gcp/">GCP</a>, <a class="reference external" href="https://docs.atlas.mongodb.com/reference/microsoft-azure/">Azure</a>.
Do not specify this field when creating a multi-region cluster using the replicationSpec document or a Global Cluster with the replicationSpecs array.</p></li>
<li><p><strong>provider_volume_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the volume. The possible values are: <code class="docutils literal notranslate"><span class="pre">STANDARD</span></code> and <code class="docutils literal notranslate"><span class="pre">PROVISIONED</span></code>.  <code class="docutils literal notranslate"><span class="pre">PROVISIONED</span></code> required if setting IOPS higher than the default instance IOPS.</p></li>
<li><p><strong>replication_factor</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of replica set members. Each member keeps a copy of your databases, providing high availability and data redundancy. The possible values are 3, 5, or 7. The default value is 3.</p></li>
<li><p><strong>replication_specs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configuration for cluster regions.  See Replication Spec below for more details.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>advanced_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fail_index_key_too_long</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - When true, documents can only be updated or inserted if, for all indexed fields on the target collection, the corresponding index entries do not exceed 1024 bytes. When false, mongod writes documents that exceed the limit but does not index them.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">javascript_enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - When true, the cluster allows execution of operations that perform server-side executions of JavaScript. When false, the cluster disables execution of those operations.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum_enabled_tls_protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Sets the minimum Transport Layer Security (TLS) version the cluster accepts for incoming connections.Valid values are:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">no_table_scan</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - When true, the cluster disables the execution of any query that requires a collection scan to return results. When false, the cluster allows the execution of those operations.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oplog_size_mb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The custom oplog size of the cluster. Without a value that indicates that the cluster uses the default oplog size calculated by Atlas.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sample_refresh_interval_bi_connector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Interval in seconds at which the mongosqld process re-samples data to create its relational schema. The default value is 300. The specified value must be a positive integer. Available only for Atlas deployments in which BI Connector for Atlas is enabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sample_size_bi_connector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of documents per database to sample when gathering schema information. Defaults to 100. Available only for Atlas deployments in which BI Connector for Atlas is enabled.</p></li>
</ul>
<p>The <strong>bi_connector</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies whether or not BI Connector for Atlas is enabled on the cluster.</p>
<ul>
<li><p>Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to enable BI Connector for Atlas.</p></li>
<li><p>Set to <code class="docutils literal notranslate"><span class="pre">false</span></code> to disable BI Connector for Atlas.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">read_preference</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the read preference to be used by BI Connector for Atlas on the cluster. Each BI Connector for Atlas read preference contains a distinct combination of <a class="reference external" href="https://docs.mongodb.com/manual/core/read-preference/">readPreference</a> and <a class="reference external" href="https://docs.mongodb.com/manual/core/read-preference/#tag-sets">readPreferenceTags</a> options. For details on BI Connector for Atlas read preferences, refer to the <a class="reference external" href="https://docs.atlas.mongodb.com/tutorial/create-global-writes-cluster/#bic-read-preferences">BI Connector Read Preferences Table</a>.</p></li>
</ul>
<p>The <strong>labels</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The key that you want to write.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value that you want to write.</p></li>
</ul>
<p>The <strong>replication_specs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Unique identifer of the replication document for a zone in a Global Cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">num_shards</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of shards to deploy in the specified zone.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regionsConfigs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Physical location of the region. Each regionsConfig document describes the region’s priority in elections and the number and type of MongoDB nodes Atlas deploys to the region. You must order each regionsConfigs document by regionsConfig.priority, descending. See Region Config below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">analyticsNodes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of analytics nodes for Atlas to deploy to the region. Analytics nodes are useful for handling analytic data such as reporting queries from BI Connector for Atlas. Analytics nodes are read-only, and can never become the primary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">electableNodes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of electable nodes for Atlas to deploy to the region. Electable nodes can become the primary and can facilitate local reads.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Election priority of the region. For regions with only read-only nodes, set this value to 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">readOnlyNodes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of read-only nodes for Atlas to deploy to the region. Read-only nodes can never become the primary, but can facilitate local-reads. Specify 0 if you do not want any read-only nodes in the region.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name for the region specified.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zoneName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name for the zone in a Global Cluster.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.auto_scaling_disk_gb_enabled">
<code class="sig-name descname">auto_scaling_disk_gb_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.auto_scaling_disk_gb_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether disk auto-scaling is enabled. The default is true.</p>
<ul class="simple">
<li><p>Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to enable disk auto-scaling.</p></li>
<li><p>Set to <code class="docutils literal notranslate"><span class="pre">false</span></code> to disable disk auto-scaling.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.backing_provider_name">
<code class="sig-name descname">backing_provider_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.backing_provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud service provider on which the server for a multi-tenant cluster is provisioned.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.backup_enabled">
<code class="sig-name descname">backup_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.backup_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Legacy Option - Set to true to enable Atlas continuous backups for the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.bi_connector">
<code class="sig-name descname">bi_connector</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.bi_connector" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies BI Connector for Atlas configuration on this cluster. BI Connector for Atlas is only available for M10+ clusters. See BI Connector below for more details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies whether or not BI Connector for Atlas is enabled on the cluster.</p>
<ul>
<li><p>Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to enable BI Connector for Atlas.</p></li>
<li><p>Set to <code class="docutils literal notranslate"><span class="pre">false</span></code> to disable BI Connector for Atlas.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">read_preference</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the read preference to be used by BI Connector for Atlas on the cluster. Each BI Connector for Atlas read preference contains a distinct combination of <a class="reference external" href="https://docs.mongodb.com/manual/core/read-preference/">readPreference</a> and <a class="reference external" href="https://docs.mongodb.com/manual/core/read-preference/#tag-sets">readPreferenceTags</a> options. For details on BI Connector for Atlas read preferences, refer to the <a class="reference external" href="https://docs.atlas.mongodb.com/tutorial/create-global-writes-cluster/#bic-read-preferences">BI Connector Read Preferences Table</a>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.cluster_id">
<code class="sig-name descname">cluster_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The cluster ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.cluster_type">
<code class="sig-name descname">cluster_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.cluster_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the type of the cluster that you want to modify. You cannot convert a sharded cluster deployment to a replica set deployment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.connection_strings">
<code class="sig-name descname">connection_strings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.connection_strings" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of connection strings that your applications use to connect to this cluster. More info in <a class="reference external" href="https://docs.mongodb.com/manual/reference/connection-string/">Connection-strings</a>. Use the parameters in this object to connect your applications to this cluster. To learn more about the formats of connection strings, see <a class="reference external" href="https://docs.atlas.mongodb.com/reference/faq/connection-changes/">Connection String Options</a>. NOTE: Atlas returns the contents of this object after the cluster is operational, not while it builds the cluster.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connection_strings.standard</span></code> -   Public mongodb:// connection string for this cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connection_strings.standard_srv</span></code> - Public mongodb+srv:// connection string for this cluster. The mongodb+srv protocol tells the driver to look up the seed list of hosts in DNS. Atlas synchronizes this list with the nodes in a cluster. If the connection string uses this URI format, you don’t need to append the seed list or change the URI if the nodes change. Use this URI format if your driver supports it. If it doesn’t, use connectionStrings.standard.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connection_strings.aws_private_link</span></code> -  <a class="reference external" href="https://docs.atlas.mongodb.com/security-private-endpoint/#private-endpoint-connection-strings">Private-endpoint-aware</a> mongodb://connection strings for each interface VPC endpoint you configured to connect to this cluster. Returned only if you created a AWS PrivateLink connection to this cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connection_strings.aws_private_link_srv</span></code> - <a class="reference external" href="https://docs.atlas.mongodb.com/security-private-endpoint/#private-endpoint-connection-strings">Private-endpoint-aware</a> mongodb+srv://connection strings for each interface VPC endpoint you configured to connect to this cluster. Returned only if you created a AWS PrivateLink connection to this cluster. Use this URI format if your driver supports it. If it doesn’t, use connectionStrings.awsPrivateLink.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connection_strings.private</span></code> -   <a class="reference external" href="https://docs.atlas.mongodb.com/security-vpc-peering/#vpc-peering">Network-peering-endpoint-aware</a> mongodb://connection strings for each interface VPC endpoint you configured to connect to this cluster. Returned only if you created a network peering connection to this cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connection_strings.private_srv</span></code> -  <a class="reference external" href="https://docs.atlas.mongodb.com/security-vpc-peering/#vpc-peering">Network-peering-endpoint-aware</a> mongodb+srv://connection strings for each interface VPC endpoint you configured to connect to this cluster. Returned only if you created a network peering connection to this cluster.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">awsPrivateLink</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">awsPrivateLinkSrv</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateSrv</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">standard</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">standardSrv</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.disk_size_gb">
<code class="sig-name descname">disk_size_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.disk_size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The size in gigabytes of the server’s root volume. You can add capacity by increasing this number, up to a maximum possible value of 4096 (i.e., 4 TB). This value must be a positive integer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.encryption_at_rest_provider">
<code class="sig-name descname">encryption_at_rest_provider</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.encryption_at_rest_provider" title="Permalink to this definition">¶</a></dt>
<dd><p>Set the Encryption at Rest parameter.  Possible values are AWS, GCP, AZURE or NONE.  Requires M10 or greater and for backup_enabled to be false or omitted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>Array containing key-value pairs that tag and categorize the cluster. Each key and value has a maximum length of 255 characters. You cannot set the key <code class="docutils literal notranslate"><span class="pre">Infrastructure</span> <span class="pre">Tool</span></code>, it is used for internal purposes to track aggregate usage.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The key that you want to write.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value that you want to write.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.mongo_db_major_version">
<code class="sig-name descname">mongo_db_major_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.mongo_db_major_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of the cluster to deploy. Atlas supports the following MongoDB versions for M10+ clusters: <code class="docutils literal notranslate"><span class="pre">3.6</span></code>, <code class="docutils literal notranslate"><span class="pre">4.0</span></code>, or <code class="docutils literal notranslate"><span class="pre">4.2</span></code>. You must set this value to <code class="docutils literal notranslate"><span class="pre">4.2</span></code> if <code class="docutils literal notranslate"><span class="pre">provider_instance_size_name</span></code> is either M2 or M5.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.mongo_db_version">
<code class="sig-name descname">mongo_db_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.mongo_db_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of MongoDB the cluster runs, in <code class="docutils literal notranslate"><span class="pre">major-version</span></code>.<code class="docutils literal notranslate"><span class="pre">minor-version</span></code> format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.mongo_uri">
<code class="sig-name descname">mongo_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.mongo_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>Base connection string for the cluster. Atlas only displays this field after the cluster is operational, not while it builds the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.mongo_uri_updated">
<code class="sig-name descname">mongo_uri_updated</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.mongo_uri_updated" title="Permalink to this definition">¶</a></dt>
<dd><p>Lists when the connection string was last updated. The connection string changes, for example, if you change a replica set to a sharded cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.mongo_uri_with_options">
<code class="sig-name descname">mongo_uri_with_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.mongo_uri_with_options" title="Permalink to this definition">¶</a></dt>
<dd><p>connection string for connecting to the Atlas cluster. Includes the replicaSet, ssl, and authSource query parameters in the connection string with values appropriate for the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the cluster as it appears in Atlas. Once the cluster is created, its name cannot be changed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.num_shards">
<code class="sig-name descname">num_shards</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.num_shards" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of shards to deploy in the specified zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.paused">
<code class="sig-name descname">paused</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.paused" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag that indicates whether the cluster is paused or not.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.pit_enabled">
<code class="sig-name descname">pit_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.pit_enabled" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li><p>Flag that indicates if the cluster uses Point-in-Time backups. If set to true, provider_backup_enabled must also be set to true.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique ID for the project to create the database user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.provider_backup_enabled">
<code class="sig-name descname">provider_backup_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.provider_backup_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag indicating if the cluster uses Cloud Provider Snapshots for backups.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.provider_disk_iops">
<code class="sig-name descname">provider_disk_iops</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.provider_disk_iops" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum input/output operations per second (IOPS) the system can perform. The possible values depend on the selected providerSettings.instanceSizeName and diskSizeGB.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.provider_disk_type_name">
<code class="sig-name descname">provider_disk_type_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.provider_disk_type_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Azure disk type of the server’s root volume. If omitted, Atlas uses the default disk type for the selected providerSettings.instanceSizeName.  Example disk types and associated storage sizes: P4 - 32GB, P6 - 64GB, P10 - 128GB, P20 - 512GB, P30 - 1024GB, P40 - 2048GB, P50 - 4095GB.  More information and the most update to date disk types/storage sizes can be located at <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/clusters-create-one/">https://docs.atlas.mongodb.com/reference/api/clusters-create-one/</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.provider_encrypt_ebs_volume">
<code class="sig-name descname">provider_encrypt_ebs_volume</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.provider_encrypt_ebs_volume" title="Permalink to this definition">¶</a></dt>
<dd><p>If enabled, the Amazon EBS encryption feature encrypts the server’s root volume for both data at rest within the volume and for data moving between the volume and the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.provider_instance_size_name">
<code class="sig-name descname">provider_instance_size_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.provider_instance_size_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Atlas provides different instance sizes, each with a default storage capacity and RAM size. The instance size you select is used for all the data-bearing servers in your cluster. See <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/clusters-create-one/">Create a Cluster</a> <code class="docutils literal notranslate"><span class="pre">providerSettings.instanceSizeName</span></code> for valid values and default resources.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.provider_name">
<code class="sig-name descname">provider_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud service provider on which the servers are provisioned.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.provider_region_name">
<code class="sig-name descname">provider_region_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.provider_region_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Physical location of your MongoDB cluster. The region you choose can affect network latency for clients accessing your databases.  Requires the Atlas Region name, see the reference list for <a class="reference external" href="https://docs.atlas.mongodb.com/reference/amazon-aws/">AWS</a>, <a class="reference external" href="https://docs.atlas.mongodb.com/reference/google-gcp/">GCP</a>, <a class="reference external" href="https://docs.atlas.mongodb.com/reference/microsoft-azure/">Azure</a>.
Do not specify this field when creating a multi-region cluster using the replicationSpec document or a Global Cluster with the replicationSpecs array.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.provider_volume_type">
<code class="sig-name descname">provider_volume_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.provider_volume_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the volume. The possible values are: <code class="docutils literal notranslate"><span class="pre">STANDARD</span></code> and <code class="docutils literal notranslate"><span class="pre">PROVISIONED</span></code>.  <code class="docutils literal notranslate"><span class="pre">PROVISIONED</span></code> required if setting IOPS higher than the default instance IOPS.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.replication_factor">
<code class="sig-name descname">replication_factor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.replication_factor" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of replica set members. Each member keeps a copy of your databases, providing high availability and data redundancy. The possible values are 3, 5, or 7. The default value is 3.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.replication_specs">
<code class="sig-name descname">replication_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.replication_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for cluster regions.  See Replication Spec below for more details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Unique identifer of the replication document for a zone in a Global Cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">num_shards</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of shards to deploy in the specified zone.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regionsConfigs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Physical location of the region. Each regionsConfig document describes the region’s priority in elections and the number and type of MongoDB nodes Atlas deploys to the region. You must order each regionsConfigs document by regionsConfig.priority, descending. See Region Config below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">analyticsNodes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of analytics nodes for Atlas to deploy to the region. Analytics nodes are useful for handling analytic data such as reporting queries from BI Connector for Atlas. Analytics nodes are read-only, and can never become the primary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">electableNodes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of electable nodes for Atlas to deploy to the region. Electable nodes can become the primary and can facilitate local reads.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Election priority of the region. For regions with only read-only nodes, set this value to 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">readOnlyNodes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of read-only nodes for Atlas to deploy to the region. Read-only nodes can never become the primary, but can facilitate local-reads. Specify 0 if you do not want any read-only nodes in the region.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name for the region specified.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zoneName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name for the zone in a Global Cluster.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.snapshot_backup_policies">
<code class="sig-name descname">snapshot_backup_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.snapshot_backup_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>current snapshot schedule and retention settings for the cluster.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The cluster ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">next_snapshot</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policies</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Unique identifer of the replication document for a zone in a Global Cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyItems</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">frequencyInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frequencyType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Unique identifer of the replication document for a zone in a Global Cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionValue</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">reference_hour_of_day</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reference_minute_of_hour</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">restore_window_days</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">update_snapshots</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.srv_address">
<code class="sig-name descname">srv_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.srv_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Connection string for connecting to the Atlas cluster. The +srv modifier forces the connection to use TLS/SSL. See the mongoURI for additional options.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Cluster.state_name">
<code class="sig-name descname">state_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.state_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Current state of the cluster. The possible states are:</p>
<ul class="simple">
<li><p>IDLE</p></li>
<li><p>CREATING</p></li>
<li><p>UPDATING</p></li>
<li><p>DELETING</p></li>
<li><p>DELETED</p></li>
<li><p>REPAIRING</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">advanced_configuration=None</em>, <em class="sig-param">auto_scaling_disk_gb_enabled=None</em>, <em class="sig-param">backing_provider_name=None</em>, <em class="sig-param">backup_enabled=None</em>, <em class="sig-param">bi_connector=None</em>, <em class="sig-param">cluster_id=None</em>, <em class="sig-param">cluster_type=None</em>, <em class="sig-param">connection_strings=None</em>, <em class="sig-param">disk_size_gb=None</em>, <em class="sig-param">encryption_at_rest_provider=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">mongo_db_major_version=None</em>, <em class="sig-param">mongo_db_version=None</em>, <em class="sig-param">mongo_uri=None</em>, <em class="sig-param">mongo_uri_updated=None</em>, <em class="sig-param">mongo_uri_with_options=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">num_shards=None</em>, <em class="sig-param">paused=None</em>, <em class="sig-param">pit_enabled=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">provider_backup_enabled=None</em>, <em class="sig-param">provider_disk_iops=None</em>, <em class="sig-param">provider_disk_type_name=None</em>, <em class="sig-param">provider_encrypt_ebs_volume=None</em>, <em class="sig-param">provider_instance_size_name=None</em>, <em class="sig-param">provider_name=None</em>, <em class="sig-param">provider_region_name=None</em>, <em class="sig-param">provider_volume_type=None</em>, <em class="sig-param">replication_factor=None</em>, <em class="sig-param">replication_specs=None</em>, <em class="sig-param">snapshot_backup_policies=None</em>, <em class="sig-param">srv_address=None</em>, <em class="sig-param">state_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_scaling_disk_gb_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether disk auto-scaling is enabled. The default is true.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- Set to `true` to enable disk auto-scaling.
- Set to `false` to disable disk auto-scaling.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>backing_provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud service provider on which the server for a multi-tenant cluster is provisioned.</p></li>
<li><p><strong>backup_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Legacy Option - Set to true to enable Atlas continuous backups for the cluster.</p></li>
<li><p><strong>bi_connector</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies BI Connector for Atlas configuration on this cluster. BI Connector for Atlas is only available for M10+ clusters. See BI Connector below for more details.</p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cluster ID.</p></li>
<li><p><strong>cluster_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of the cluster that you want to modify. You cannot convert a sharded cluster deployment to a replica set deployment.</p></li>
<li><p><strong>connection_strings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Set of connection strings that your applications use to connect to this cluster. More info in <a class="reference external" href="https://docs.mongodb.com/manual/reference/connection-string/">Connection-strings</a>. Use the parameters in this object to connect your applications to this cluster. To learn more about the formats of connection strings, see <a class="reference external" href="https://docs.atlas.mongodb.com/reference/faq/connection-changes/">Connection String Options</a>. NOTE: Atlas returns the contents of this object after the cluster is operational, not while it builds the cluster.</p>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- `connection_strings.standard` -   Public mongodb:// connection string for this cluster.
- `connection_strings.standard_srv` - Public mongodb+srv:// connection string for this cluster. The mongodb+srv protocol tells the driver to look up the seed list of hosts in DNS. Atlas synchronizes this list with the nodes in a cluster. If the connection string uses this URI format, you don’t need to append the seed list or change the URI if the nodes change. Use this URI format if your driver supports it. If it doesn’t, use connectionStrings.standard.
- `connection_strings.aws_private_link` -  [Private-endpoint-aware](https://docs.atlas.mongodb.com/security-private-endpoint/#private-endpoint-connection-strings) mongodb://connection strings for each interface VPC endpoint you configured to connect to this cluster. Returned only if you created a AWS PrivateLink connection to this cluster.
- `connection_strings.aws_private_link_srv` - [Private-endpoint-aware](https://docs.atlas.mongodb.com/security-private-endpoint/#private-endpoint-connection-strings) mongodb+srv://connection strings for each interface VPC endpoint you configured to connect to this cluster. Returned only if you created a AWS PrivateLink connection to this cluster. Use this URI format if your driver supports it. If it doesn’t, use connectionStrings.awsPrivateLink.
- `connection_strings.private` -   [Network-peering-endpoint-aware](https://docs.atlas.mongodb.com/security-vpc-peering/#vpc-peering) mongodb://connection strings for each interface VPC endpoint you configured to connect to this cluster. Returned only if you created a network peering connection to this cluster.
- `connection_strings.private_srv` -  [Network-peering-endpoint-aware](https://docs.atlas.mongodb.com/security-vpc-peering/#vpc-peering) mongodb+srv://connection strings for each interface VPC endpoint you configured to connect to this cluster. Returned only if you created a network peering connection to this cluster.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>disk_size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size in gigabytes of the server’s root volume. You can add capacity by increasing this number, up to a maximum possible value of 4096 (i.e., 4 TB). This value must be a positive integer.</p></li>
<li><p><strong>encryption_at_rest_provider</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set the Encryption at Rest parameter.  Possible values are AWS, GCP, AZURE or NONE.  Requires M10 or greater and for backup_enabled to be false or omitted.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array containing key-value pairs that tag and categorize the cluster. Each key and value has a maximum length of 255 characters. You cannot set the key <code class="docutils literal notranslate"><span class="pre">Infrastructure</span> <span class="pre">Tool</span></code>, it is used for internal purposes to track aggregate usage.</p></li>
<li><p><strong>mongo_db_major_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of the cluster to deploy. Atlas supports the following MongoDB versions for M10+ clusters: <code class="docutils literal notranslate"><span class="pre">3.6</span></code>, <code class="docutils literal notranslate"><span class="pre">4.0</span></code>, or <code class="docutils literal notranslate"><span class="pre">4.2</span></code>. You must set this value to <code class="docutils literal notranslate"><span class="pre">4.2</span></code> if <code class="docutils literal notranslate"><span class="pre">provider_instance_size_name</span></code> is either M2 or M5.</p></li>
<li><p><strong>mongo_db_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of MongoDB the cluster runs, in <code class="docutils literal notranslate"><span class="pre">major-version</span></code>.<code class="docutils literal notranslate"><span class="pre">minor-version</span></code> format.</p></li>
<li><p><strong>mongo_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base connection string for the cluster. Atlas only displays this field after the cluster is operational, not while it builds the cluster.</p></li>
<li><p><strong>mongo_uri_updated</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Lists when the connection string was last updated. The connection string changes, for example, if you change a replica set to a sharded cluster.</p></li>
<li><p><strong>mongo_uri_with_options</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – connection string for connecting to the Atlas cluster. Includes the replicaSet, ssl, and authSource query parameters in the connection string with values appropriate for the cluster.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the cluster as it appears in Atlas. Once the cluster is created, its name cannot be changed.</p></li>
<li><p><strong>num_shards</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of shards to deploy in the specified zone.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag that indicates whether the cluster is paused or not.</p></li>
<li><p><strong>pit_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <ul>
<li><p>Flag that indicates if the cluster uses Point-in-Time backups. If set to true, provider_backup_enabled must also be set to true.</p></li>
</ul>
</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to create the database user.</p></li>
<li><p><strong>provider_backup_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag indicating if the cluster uses Cloud Provider Snapshots for backups.</p></li>
<li><p><strong>provider_disk_iops</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum input/output operations per second (IOPS) the system can perform. The possible values depend on the selected providerSettings.instanceSizeName and diskSizeGB.</p></li>
<li><p><strong>provider_disk_type_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Azure disk type of the server’s root volume. If omitted, Atlas uses the default disk type for the selected providerSettings.instanceSizeName.  Example disk types and associated storage sizes: P4 - 32GB, P6 - 64GB, P10 - 128GB, P20 - 512GB, P30 - 1024GB, P40 - 2048GB, P50 - 4095GB.  More information and the most update to date disk types/storage sizes can be located at <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/clusters-create-one/">https://docs.atlas.mongodb.com/reference/api/clusters-create-one/</a>.</p></li>
<li><p><strong>provider_encrypt_ebs_volume</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If enabled, the Amazon EBS encryption feature encrypts the server’s root volume for both data at rest within the volume and for data moving between the volume and the instance.</p></li>
<li><p><strong>provider_instance_size_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Atlas provides different instance sizes, each with a default storage capacity and RAM size. The instance size you select is used for all the data-bearing servers in your cluster. See <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/clusters-create-one/">Create a Cluster</a> <code class="docutils literal notranslate"><span class="pre">providerSettings.instanceSizeName</span></code> for valid values and default resources.</p>
</p></li>
<li><p><strong>provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud service provider on which the servers are provisioned.</p></li>
<li><p><strong>provider_region_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Physical location of your MongoDB cluster. The region you choose can affect network latency for clients accessing your databases.  Requires the Atlas Region name, see the reference list for <a class="reference external" href="https://docs.atlas.mongodb.com/reference/amazon-aws/">AWS</a>, <a class="reference external" href="https://docs.atlas.mongodb.com/reference/google-gcp/">GCP</a>, <a class="reference external" href="https://docs.atlas.mongodb.com/reference/microsoft-azure/">Azure</a>.
Do not specify this field when creating a multi-region cluster using the replicationSpec document or a Global Cluster with the replicationSpecs array.</p>
</p></li>
<li><p><strong>provider_volume_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the volume. The possible values are: <code class="docutils literal notranslate"><span class="pre">STANDARD</span></code> and <code class="docutils literal notranslate"><span class="pre">PROVISIONED</span></code>.  <code class="docutils literal notranslate"><span class="pre">PROVISIONED</span></code> required if setting IOPS higher than the default instance IOPS.</p></li>
<li><p><strong>replication_factor</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of replica set members. Each member keeps a copy of your databases, providing high availability and data redundancy. The possible values are 3, 5, or 7. The default value is 3.</p></li>
<li><p><strong>replication_specs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configuration for cluster regions.  See Replication Spec below for more details.</p></li>
<li><p><strong>snapshot_backup_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – current snapshot schedule and retention settings for the cluster.</p></li>
<li><p><strong>srv_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Connection string for connecting to the Atlas cluster. The +srv modifier forces the connection to use TLS/SSL. See the mongoURI for additional options.</p></li>
<li><p><strong>state_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Current state of the cluster. The possible states are:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">IDLE</span>
<span class="o">-</span> <span class="n">CREATING</span>
<span class="o">-</span> <span class="n">UPDATING</span>
<span class="o">-</span> <span class="n">DELETING</span>
<span class="o">-</span> <span class="n">DELETED</span>
<span class="o">-</span> <span class="n">REPAIRING</span>
</pre></div>
</div>
<p>The <strong>advanced_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fail_index_key_too_long</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - When true, documents can only be updated or inserted if, for all indexed fields on the target collection, the corresponding index entries do not exceed 1024 bytes. When false, mongod writes documents that exceed the limit but does not index them.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">javascript_enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - When true, the cluster allows execution of operations that perform server-side executions of JavaScript. When false, the cluster disables execution of those operations.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum_enabled_tls_protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Sets the minimum Transport Layer Security (TLS) version the cluster accepts for incoming connections.Valid values are:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">no_table_scan</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - When true, the cluster disables the execution of any query that requires a collection scan to return results. When false, the cluster allows the execution of those operations.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oplog_size_mb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The custom oplog size of the cluster. Without a value that indicates that the cluster uses the default oplog size calculated by Atlas.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sample_refresh_interval_bi_connector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Interval in seconds at which the mongosqld process re-samples data to create its relational schema. The default value is 300. The specified value must be a positive integer. Available only for Atlas deployments in which BI Connector for Atlas is enabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sample_size_bi_connector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of documents per database to sample when gathering schema information. Defaults to 100. Available only for Atlas deployments in which BI Connector for Atlas is enabled.</p></li>
</ul>
<p>The <strong>bi_connector</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies whether or not BI Connector for Atlas is enabled on the cluster.</p>
<ul>
<li><p>Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to enable BI Connector for Atlas.</p></li>
<li><p>Set to <code class="docutils literal notranslate"><span class="pre">false</span></code> to disable BI Connector for Atlas.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">read_preference</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the read preference to be used by BI Connector for Atlas on the cluster. Each BI Connector for Atlas read preference contains a distinct combination of <a class="reference external" href="https://docs.mongodb.com/manual/core/read-preference/">readPreference</a> and <a class="reference external" href="https://docs.mongodb.com/manual/core/read-preference/#tag-sets">readPreferenceTags</a> options. For details on BI Connector for Atlas read preferences, refer to the <a class="reference external" href="https://docs.atlas.mongodb.com/tutorial/create-global-writes-cluster/#bic-read-preferences">BI Connector Read Preferences Table</a>.</p></li>
</ul>
<p>The <strong>connection_strings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">awsPrivateLink</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">awsPrivateLinkSrv</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateSrv</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">standard</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">standardSrv</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>labels</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The key that you want to write.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value that you want to write.</p></li>
</ul>
<p>The <strong>replication_specs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Unique identifer of the replication document for a zone in a Global Cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">num_shards</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of shards to deploy in the specified zone.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regionsConfigs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Physical location of the region. Each regionsConfig document describes the region’s priority in elections and the number and type of MongoDB nodes Atlas deploys to the region. You must order each regionsConfigs document by regionsConfig.priority, descending. See Region Config below for more details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">analyticsNodes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of analytics nodes for Atlas to deploy to the region. Analytics nodes are useful for handling analytic data such as reporting queries from BI Connector for Atlas. Analytics nodes are read-only, and can never become the primary.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">electableNodes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of electable nodes for Atlas to deploy to the region. Electable nodes can become the primary and can facilitate local reads.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Election priority of the region. For regions with only read-only nodes, set this value to 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">readOnlyNodes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of read-only nodes for Atlas to deploy to the region. Read-only nodes can never become the primary, but can facilitate local-reads. Specify 0 if you do not want any read-only nodes in the region.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name for the region specified.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zoneName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name for the zone in a Global Cluster.</p></li>
</ul>
<p>The <strong>snapshot_backup_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The cluster ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">next_snapshot</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Unique identifer of the replication document for a zone in a Global Cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyItems</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">frequencyInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frequencyType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Unique identifer of the replication document for a zone in a Global Cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retentionValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">reference_hour_of_day</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reference_minute_of_hour</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">restore_window_days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">update_snapshots</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.CustomDbRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">CustomDbRole</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">actions=None</em>, <em class="sig-param">inherited_roles=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">role_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CustomDbRole" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.CustomDbRole</span></code> provides a Custom DB Role resource. The customDBRoles resource lets you retrieve, create and modify the custom MongoDB roles in your cluster. Use custom MongoDB roles to specify custom sets of actions which cannot be described by the built-in Atlas database user privileges.</p>
<blockquote>
<div><p><strong>IMPORTANT</strong> Custom roles cannot use actions unavailable to any cluster version in your project. Custom roles are defined at the project level, and must be compatible with each MongoDB version used by your project’s clusters. If you have a cluster in your project with MongoDB 3.4, you cannot create a custom role that uses actions introduced in MongoDB 3.6, such as useUUID.</p>
<p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to create the database user.</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the inherited role. This can either be another custom role or a built-in role.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>actions</strong> object supports the following:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the privilege action. For a complete list of actions available in the Atlas API, see <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/custom-role-actions">Custom Role Actions</a>
..</p>
<blockquote>
<div><p><strong>Note</strong>: The privilege actions available to the Custom Roles API resource represent a subset of the privilege actions available in the Atlas Custom Roles UI.</p>
</div></blockquote>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">resources</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Contains information on where the action is granted. Each object in the array either indicates a database and collection on which the action is granted, or indicates that the action is granted on the cluster resource.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cluster</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">collectionName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">database_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Database on which the inherited role is granted.</p></li>
</ul>
</li>
</ul>
<p>The <strong>inherited_roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">database_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Database on which the inherited role is granted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the inherited role. This can either be another custom role or a built-in role.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.CustomDbRole.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CustomDbRole.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique ID for the project to create the database user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.CustomDbRole.role_name">
<code class="sig-name descname">role_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.CustomDbRole.role_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the inherited role. This can either be another custom role or a built-in role.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.CustomDbRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">actions=None</em>, <em class="sig-param">inherited_roles=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">role_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CustomDbRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CustomDbRole resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to create the database user.</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the inherited role. This can either be another custom role or a built-in role.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>actions</strong> object supports the following:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the privilege action. For a complete list of actions available in the Atlas API, see <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/custom-role-actions">Custom Role Actions</a>
..</p>
<blockquote>
<div><p><strong>Note</strong>: The privilege actions available to the Custom Roles API resource represent a subset of the privilege actions available in the Atlas Custom Roles UI.</p>
</div></blockquote>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">resources</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Contains information on where the action is granted. Each object in the array either indicates a database and collection on which the action is granted, or indicates that the action is granted on the cluster resource.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cluster</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">collectionName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">database_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Database on which the inherited role is granted.</p></li>
</ul>
</li>
</ul>
<p>The <strong>inherited_roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">database_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Database on which the inherited role is granted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the inherited role. This can either be another custom role or a built-in role.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.CustomDbRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CustomDbRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.CustomDbRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CustomDbRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.DatabaseUser">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">DatabaseUser</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auth_database_name=None</em>, <em class="sig-param">database_name=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">x509_type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.DatabaseUser" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a DatabaseUser resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] auth_database_name: The user’s authentication database. A user must provide both a username and authentication database to log into MongoDB. In Atlas deployments of MongoDB, the authentication database is always the admin database.
:param pulumi.Input[str] database_name: Database on which the user has the specified role. A role on the <code class="docutils literal notranslate"><span class="pre">admin</span></code> database can include privileges that apply to the other databases.
:param pulumi.Input[str] project_id: The unique ID for the project to create the database user.
:param pulumi.Input[list] roles: List of user’s roles and the databases / collections on which the roles apply. A role allows the user to perform particular actions on the specified database. A role on the admin database can include privileges that apply to the other databases as well. See Roles below for more details.
:param pulumi.Input[str] username: Username for authenticating to MongoDB.
:param pulumi.Input[str] x509_type: X.509 method by which the provided username is authenticated. If no value is given, Atlas uses the default value of NONE. The accepted types are:</p>
<p>The <strong>labels</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The key that you want to write.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value that you want to write.</p></li>
</ul>
<p>The <strong>roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">collectionName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Collection for which the role applies. You can specify a collection for the <code class="docutils literal notranslate"><span class="pre">read</span></code> and <code class="docutils literal notranslate"><span class="pre">readWrite</span></code> roles. If you do not specify a collection for <code class="docutils literal notranslate"><span class="pre">read</span></code> and <code class="docutils literal notranslate"><span class="pre">readWrite</span></code>, the role applies to all collections in the database (excluding some collections in the <code class="docutils literal notranslate"><span class="pre">system</span></code>. database).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">database_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Database on which the user has the specified role. A role on the <code class="docutils literal notranslate"><span class="pre">admin</span></code> database can include privileges that apply to the other databases.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the role to grant. See <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/database-users-create-a-user/">Create a Database User</a> <code class="docutils literal notranslate"><span class="pre">roles.roleName</span></code> for valid values and restrictions.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.DatabaseUser.auth_database_name">
<code class="sig-name descname">auth_database_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.DatabaseUser.auth_database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The user’s authentication database. A user must provide both a username and authentication database to log into MongoDB. In Atlas deployments of MongoDB, the authentication database is always the admin database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.DatabaseUser.database_name">
<code class="sig-name descname">database_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.DatabaseUser.database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Database on which the user has the specified role. A role on the <code class="docutils literal notranslate"><span class="pre">admin</span></code> database can include privileges that apply to the other databases.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.DatabaseUser.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.DatabaseUser.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique ID for the project to create the database user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.DatabaseUser.roles">
<code class="sig-name descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.DatabaseUser.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>List of user’s roles and the databases / collections on which the roles apply. A role allows the user to perform particular actions on the specified database. A role on the admin database can include privileges that apply to the other databases as well. See Roles below for more details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">collectionName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Collection for which the role applies. You can specify a collection for the <code class="docutils literal notranslate"><span class="pre">read</span></code> and <code class="docutils literal notranslate"><span class="pre">readWrite</span></code> roles. If you do not specify a collection for <code class="docutils literal notranslate"><span class="pre">read</span></code> and <code class="docutils literal notranslate"><span class="pre">readWrite</span></code>, the role applies to all collections in the database (excluding some collections in the <code class="docutils literal notranslate"><span class="pre">system</span></code>. database).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">database_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Database on which the user has the specified role. A role on the <code class="docutils literal notranslate"><span class="pre">admin</span></code> database can include privileges that apply to the other databases.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the role to grant. See <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/database-users-create-a-user/">Create a Database User</a> <code class="docutils literal notranslate"><span class="pre">roles.roleName</span></code> for valid values and restrictions.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.DatabaseUser.username">
<code class="sig-name descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.DatabaseUser.username" title="Permalink to this definition">¶</a></dt>
<dd><p>Username for authenticating to MongoDB.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.DatabaseUser.x509_type">
<code class="sig-name descname">x509_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.DatabaseUser.x509_type" title="Permalink to this definition">¶</a></dt>
<dd><p>X.509 method by which the provided username is authenticated. If no value is given, Atlas uses the default value of NONE. The accepted types are:</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.DatabaseUser.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auth_database_name=None</em>, <em class="sig-param">database_name=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">x509_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.DatabaseUser.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DatabaseUser resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s authentication database. A user must provide both a username and authentication database to log into MongoDB. In Atlas deployments of MongoDB, the authentication database is always the admin database.</p></li>
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database on which the user has the specified role. A role on the <code class="docutils literal notranslate"><span class="pre">admin</span></code> database can include privileges that apply to the other databases.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to create the database user.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of user’s roles and the databases / collections on which the roles apply. A role allows the user to perform particular actions on the specified database. A role on the admin database can include privileges that apply to the other databases as well. See Roles below for more details.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username for authenticating to MongoDB.</p></li>
<li><p><strong>x509_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – X.509 method by which the provided username is authenticated. If no value is given, Atlas uses the default value of NONE. The accepted types are:</p></li>
</ul>
</dd>
</dl>
<p>The <strong>labels</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The key that you want to write.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value that you want to write.</p></li>
</ul>
<p>The <strong>roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">collectionName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Collection for which the role applies. You can specify a collection for the <code class="docutils literal notranslate"><span class="pre">read</span></code> and <code class="docutils literal notranslate"><span class="pre">readWrite</span></code> roles. If you do not specify a collection for <code class="docutils literal notranslate"><span class="pre">read</span></code> and <code class="docutils literal notranslate"><span class="pre">readWrite</span></code>, the role applies to all collections in the database (excluding some collections in the <code class="docutils literal notranslate"><span class="pre">system</span></code>. database).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">database_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Database on which the user has the specified role. A role on the <code class="docutils literal notranslate"><span class="pre">admin</span></code> database can include privileges that apply to the other databases.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the role to grant. See <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/database-users-create-a-user/">Create a Database User</a> <code class="docutils literal notranslate"><span class="pre">roles.roleName</span></code> for valid values and restrictions.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.DatabaseUser.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.DatabaseUser.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.DatabaseUser.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.DatabaseUser.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.EncryptionAtRest">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">EncryptionAtRest</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">aws_kms=None</em>, <em class="sig-param">azure_key_vault=None</em>, <em class="sig-param">google_cloud_kms=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.EncryptionAtRest" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.EncryptionAtRest</span></code> Atlas encrypts your data at rest using encrypted storage media. 
Using keys you manage with AWS KMS, Atlas encrypts your data a second time when it writes it to the MongoDB encrypted storage engine. 
You can use the following clouds: AWS CMK, AZURE KEY VAULT and GOOGLE KEY VAULT to encrypt the MongoDB master encryption keys.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aws_kms</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies AWS KMS configuration details and whether Encryption at Rest is enabled for an Atlas project.</p></li>
<li><p><strong>azure_key_vault</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies Azure Key Vault configuration details and whether Encryption at Rest is enabled for an Atlas project.</p></li>
<li><p><strong>google_cloud_kms</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies GCP KMS configuration details and whether Encryption at Rest is enabled for an Atlas project.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier for the project.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>aws_kms</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">access_key_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IAM access key ID with permissions to access the customer master key specified by customerMasterKeyID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customer_master_key_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The AWS customer master key used to encrypt and decrypt the MongoDB master keys.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether Encryption at Rest is enabled for an Atlas project. To disable Encryption at Rest, pass only this parameter with a value of false. When you disable Encryption at Rest, Atlas also removes the configuration details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The AWS region in which the AWS customer master key exists: CA_CENTRAL_1, US_EAST_1, US_EAST_2, US_WEST_1, US_WEST_2, SA_EAST_1</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret_access_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IAM secret access key with permissions to access the customer master key specified by customerMasterKeyID.</p></li>
</ul>
<p>The <strong>azure_key_vault</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">azure_environment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure environment where the Azure account credentials reside. Valid values are the following: AZURE, AZURE_CHINA, AZURE_GERMANY</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client ID, also known as the application ID, for an Azure application associated with the Azure AD tenant.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether Encryption at Rest is enabled for an Atlas project. To disable Encryption at Rest, pass only this parameter with a value of false. When you disable Encryption at Rest, Atlas also removes the configuration details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_identifier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique identifier of a key in an Azure Key Vault.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an Azure Key Vault containing your key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Azure Resource group that contains an Azure Key Vault.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The secret associated with the Azure Key Vault specified by azureKeyVault.tenantID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subscription_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique identifier associated with an Azure subscription.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique identifier for an Azure AD tenant within an Azure subscription.</p></li>
</ul>
<p>The <strong>google_cloud_kms</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether Encryption at Rest is enabled for an Atlas project. To disable Encryption at Rest, pass only this parameter with a value of false. When you disable Encryption at Rest, Atlas also removes the configuration details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_version_resource_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Key Version Resource ID from your GCP account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String-formatted JSON object containing GCP KMS credentials from your GCP account.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.EncryptionAtRest.aws_kms">
<code class="sig-name descname">aws_kms</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.EncryptionAtRest.aws_kms" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies AWS KMS configuration details and whether Encryption at Rest is enabled for an Atlas project.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">access_key_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The IAM access key ID with permissions to access the customer master key specified by customerMasterKeyID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customer_master_key_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The AWS customer master key used to encrypt and decrypt the MongoDB master keys.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether Encryption at Rest is enabled for an Atlas project. To disable Encryption at Rest, pass only this parameter with a value of false. When you disable Encryption at Rest, Atlas also removes the configuration details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The AWS region in which the AWS customer master key exists: CA_CENTRAL_1, US_EAST_1, US_EAST_2, US_WEST_1, US_WEST_2, SA_EAST_1</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret_access_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The IAM secret access key with permissions to access the customer master key specified by customerMasterKeyID.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.EncryptionAtRest.azure_key_vault">
<code class="sig-name descname">azure_key_vault</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.EncryptionAtRest.azure_key_vault" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies Azure Key Vault configuration details and whether Encryption at Rest is enabled for an Atlas project.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">azure_environment</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Azure environment where the Azure account credentials reside. Valid values are the following: AZURE, AZURE_CHINA, AZURE_GERMANY</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client ID, also known as the application ID, for an Azure application associated with the Azure AD tenant.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether Encryption at Rest is enabled for an Atlas project. To disable Encryption at Rest, pass only this parameter with a value of false. When you disable Encryption at Rest, Atlas also removes the configuration details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_identifier</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique identifier of a key in an Azure Key Vault.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an Azure Key Vault containing your key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Azure Resource group that contains an Azure Key Vault.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The secret associated with the Azure Key Vault specified by azureKeyVault.tenantID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subscription_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique identifier associated with an Azure subscription.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unique identifier for an Azure AD tenant within an Azure subscription.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.EncryptionAtRest.google_cloud_kms">
<code class="sig-name descname">google_cloud_kms</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.EncryptionAtRest.google_cloud_kms" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies GCP KMS configuration details and whether Encryption at Rest is enabled for an Atlas project.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether Encryption at Rest is enabled for an Atlas project. To disable Encryption at Rest, pass only this parameter with a value of false. When you disable Encryption at Rest, Atlas also removes the configuration details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_version_resource_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Key Version Resource ID from your GCP account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String-formatted JSON object containing GCP KMS credentials from your GCP account.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.EncryptionAtRest.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.EncryptionAtRest.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier for the project.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.EncryptionAtRest.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">aws_kms=None</em>, <em class="sig-param">azure_key_vault=None</em>, <em class="sig-param">google_cloud_kms=None</em>, <em class="sig-param">project_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.EncryptionAtRest.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EncryptionAtRest resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aws_kms</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies AWS KMS configuration details and whether Encryption at Rest is enabled for an Atlas project.</p></li>
<li><p><strong>azure_key_vault</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies Azure Key Vault configuration details and whether Encryption at Rest is enabled for an Atlas project.</p></li>
<li><p><strong>google_cloud_kms</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies GCP KMS configuration details and whether Encryption at Rest is enabled for an Atlas project.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier for the project.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>aws_kms</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">access_key_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IAM access key ID with permissions to access the customer master key specified by customerMasterKeyID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customer_master_key_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The AWS customer master key used to encrypt and decrypt the MongoDB master keys.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether Encryption at Rest is enabled for an Atlas project. To disable Encryption at Rest, pass only this parameter with a value of false. When you disable Encryption at Rest, Atlas also removes the configuration details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The AWS region in which the AWS customer master key exists: CA_CENTRAL_1, US_EAST_1, US_EAST_2, US_WEST_1, US_WEST_2, SA_EAST_1</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret_access_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IAM secret access key with permissions to access the customer master key specified by customerMasterKeyID.</p></li>
</ul>
<p>The <strong>azure_key_vault</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">azure_environment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure environment where the Azure account credentials reside. Valid values are the following: AZURE, AZURE_CHINA, AZURE_GERMANY</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client ID, also known as the application ID, for an Azure application associated with the Azure AD tenant.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether Encryption at Rest is enabled for an Atlas project. To disable Encryption at Rest, pass only this parameter with a value of false. When you disable Encryption at Rest, Atlas also removes the configuration details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_identifier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique identifier of a key in an Azure Key Vault.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an Azure Key Vault containing your key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Azure Resource group that contains an Azure Key Vault.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The secret associated with the Azure Key Vault specified by azureKeyVault.tenantID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subscription_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique identifier associated with an Azure subscription.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique identifier for an Azure AD tenant within an Azure subscription.</p></li>
</ul>
<p>The <strong>google_cloud_kms</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether Encryption at Rest is enabled for an Atlas project. To disable Encryption at Rest, pass only this parameter with a value of false. When you disable Encryption at Rest, Atlas also removes the configuration details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_version_resource_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Key Version Resource ID from your GCP account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String-formatted JSON object containing GCP KMS credentials from your GCP account.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.EncryptionAtRest.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.EncryptionAtRest.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.EncryptionAtRest.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.EncryptionAtRest.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.Get509AuthenticationDatabaseUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">Get509AuthenticationDatabaseUserResult</code><span class="sig-paren">(</span><em class="sig-param">certificates=None</em>, <em class="sig-param">customer_x509_cas=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Get509AuthenticationDatabaseUserResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by get509AuthenticationDatabaseUser.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.Get509AuthenticationDatabaseUserResult.certificates">
<code class="sig-name descname">certificates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Get509AuthenticationDatabaseUserResult.certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of objects where each details one unexpired database user certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Get509AuthenticationDatabaseUserResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Get509AuthenticationDatabaseUserResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.GetAlertConfigurationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetAlertConfigurationResult</code><span class="sig-paren">(</span><em class="sig-param">alert_configuration_id=None</em>, <em class="sig-param">created=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">event_type=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">matchers=None</em>, <em class="sig-param">metric_threshold=None</em>, <em class="sig-param">notifications=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">updated=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetAlertConfigurationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAlertConfiguration.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetAlertConfigurationResult.created">
<code class="sig-name descname">created</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetAlertConfigurationResult.created" title="Permalink to this definition">¶</a></dt>
<dd><p>Timestamp in ISO 8601 date and time format in UTC when this alert configuration was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetAlertConfigurationResult.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetAlertConfigurationResult.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to true, the alert configuration is enabled. If enabled is not exported it is set to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetAlertConfigurationResult.event_type">
<code class="sig-name descname">event_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetAlertConfigurationResult.event_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of event that will trigger an alert.
Alert type. Possible values:</p>
<ul class="simple">
<li><p>Host</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">OUTSIDE_METRIC_THRESHOLD</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HOST_RESTARTED</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HOST_UPGRADED</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HOST_NOW_SECONDARY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HOST_NOW_PRIMARY</span></code></p></li>
<li><p>Replica set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">NO_PRIMARY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">TOO_MANY_ELECTIONS</span></code>
Sharded cluster</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">CLUSTER_MONGOS_IS_MISSING</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">User</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">JOINED_GROUP</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">REMOVED_FROM_GROUP</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">USER_ROLES_CHANGED_AUDIT</span></code></p></li>
<li><p>Project</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">USERS_AWAITING_APPROVAL</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">USERS_WITHOUT_MULTI_FACTOR_AUTH</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP_CREATED</span></code></p></li>
<li><p>Team</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">JOINED_TEAM</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">REMOVED_FROM_TEAM</span></code></p></li>
<li><p>Organization</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">INVITED_TO_ORG</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">JOINED_ORG</span></code></p></li>
<li><p>Data Explorer</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">DATA_EXPLORER</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">DATA_EXPLORER_CRUD</span></code></p></li>
<li><p>Billing</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">CREDIT_CARD_ABOUT_TO_EXPIRE</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">CHARGE_SUCCEEDED</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">INVOICE_CLOSED</span></code></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetAlertConfigurationResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetAlertConfigurationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetAlertConfigurationResult.updated">
<code class="sig-name descname">updated</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetAlertConfigurationResult.updated" title="Permalink to this definition">¶</a></dt>
<dd><p>Timestamp in ISO 8601 date and time format in UTC when this alert configuration was last updated.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.GetAuditingResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetAuditingResult</code><span class="sig-paren">(</span><em class="sig-param">audit_authorization_success=None</em>, <em class="sig-param">audit_filter=None</em>, <em class="sig-param">configuration_type=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">project_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetAuditingResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAuditing.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetAuditingResult.audit_authorization_success">
<code class="sig-name descname">audit_authorization_success</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetAuditingResult.audit_authorization_success" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON-formatted audit filter used by the project</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetAuditingResult.audit_filter">
<code class="sig-name descname">audit_filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetAuditingResult.audit_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the auditing system captures successful authentication attempts for audit filters using the “atype” : “authCheck” auditing event. For more information, see auditAuthorizationSuccess</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetAuditingResult.configuration_type">
<code class="sig-name descname">configuration_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetAuditingResult.configuration_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Denotes the configuration method for the audit filter. Possible values are: NONE - auditing not configured for the project.m FILTER_BUILDER - auditing configured via Atlas UI filter builderm FILTER_JSON - auditing configured via Atlas custom filter or API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetAuditingResult.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetAuditingResult.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Denotes whether or not the project associated with the {GROUP-ID} has database auditing enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetAuditingResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetAuditingResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetCloudProviderSnapshotBackupPolicyResult</code><span class="sig-paren">(</span><em class="sig-param">cluster_id=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">next_snapshot=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">reference_hour_of_day=None</em>, <em class="sig-param">reference_minute_of_hour=None</em>, <em class="sig-param">restore_window_days=None</em>, <em class="sig-param">update_snapshots=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCloudProviderSnapshotBackupPolicy.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.cluster_id">
<code class="sig-name descname">cluster_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the Atlas cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.next_snapshot">
<code class="sig-name descname">next_snapshot</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.next_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC ISO 8601 formatted point in time when Atlas will take the next snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.policies">
<code class="sig-name descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of policy definitions for the cluster.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">policies.#.id</span></code> - Unique identifier of the backup policy.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.reference_hour_of_day">
<code class="sig-name descname">reference_hour_of_day</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.reference_hour_of_day" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC Hour of day between 0 and 23 representing which hour of the day that Atlas takes a snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.reference_minute_of_hour">
<code class="sig-name descname">reference_minute_of_hour</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.reference_minute_of_hour" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC Minute of day between 0 and 59 representing which minute of the referenceHourOfDay that Atlas takes the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.restore_window_days">
<code class="sig-name descname">restore_window_days</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.restore_window_days" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a restore window in days for the cloud provider backup to maintain.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetCloudProviderSnapshotRestoreJobResult</code><span class="sig-paren">(</span><em class="sig-param">cancelled=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">delivery_type=None</em>, <em class="sig-param">delivery_urls=None</em>, <em class="sig-param">expired=None</em>, <em class="sig-param">expires_at=None</em>, <em class="sig-param">finished_at=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">job_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">snapshot_id=None</em>, <em class="sig-param">target_cluster_name=None</em>, <em class="sig-param">target_project_id=None</em>, <em class="sig-param">timestamp=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCloudProviderSnapshotRestoreJob.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.cancelled">
<code class="sig-name descname">cancelled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.cancelled" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the restore job was canceled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC ISO 8601 formatted point in time when Atlas created the restore job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.delivery_type">
<code class="sig-name descname">delivery_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.delivery_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of restore job to create. Possible values are: automated and download.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.delivery_urls">
<code class="sig-name descname">delivery_urls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.delivery_urls" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more URLs for the compressed snapshot files for manual download. Only visible if deliveryType is download.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.expired">
<code class="sig-name descname">expired</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.expired" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the restore job expired.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.expires_at">
<code class="sig-name descname">expires_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.expires_at" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC ISO 8601 formatted point in time when the restore job expires.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.finished_at">
<code class="sig-name descname">finished_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.finished_at" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC ISO 8601 formatted point in time when the restore job completed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.snapshot_id">
<code class="sig-name descname">snapshot_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.snapshot_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the source snapshot ID of the restore job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.target_cluster_name">
<code class="sig-name descname">target_cluster_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.target_cluster_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the target Atlas cluster to which the restore job restores the snapshot. Only visible if deliveryType is automated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.timestamp">
<code class="sig-name descname">timestamp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.timestamp" title="Permalink to this definition">¶</a></dt>
<dd><p>Timestamp in ISO 8601 date and time format in UTC when the snapshot associated to snapshotId was taken.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetCloudProviderSnapshotRestoreJobsResult</code><span class="sig-paren">(</span><em class="sig-param">cluster_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">results=None</em>, <em class="sig-param">total_count=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCloudProviderSnapshotRestoreJobs.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobsResult.results">
<code class="sig-name descname">results</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobsResult.results" title="Permalink to this definition">¶</a></dt>
<dd><p>Includes cloudProviderSnapshotRestoreJob object for each item detailed in the results array section.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetCloudProviderSnapshotResult</code><span class="sig-paren">(</span><em class="sig-param">cluster_name=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">expires_at=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">master_key_uuid=None</em>, <em class="sig-param">mongod_version=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">snapshot_id=None</em>, <em class="sig-param">snapshot_type=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">storage_size_bytes=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCloudProviderSnapshot.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotResult.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC ISO 8601 formatted point in time when Atlas took the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>UDescription of the snapshot. Only present for on-demand snapshots.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotResult.expires_at">
<code class="sig-name descname">expires_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotResult.expires_at" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC ISO 8601 formatted point in time when Atlas will delete the snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotResult.master_key_uuid">
<code class="sig-name descname">master_key_uuid</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotResult.master_key_uuid" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique ID of the AWS KMS Customer Master Key used to encrypt the snapshot. Only visible for clusters using Encryption at Rest via Customer KMS.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotResult.mongod_version">
<code class="sig-name descname">mongod_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotResult.mongod_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of the MongoDB server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotResult.snapshot_type">
<code class="sig-name descname">snapshot_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotResult.snapshot_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specified the type of snapshot. Valid values are onDemand and scheduled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Current status of the snapshot. One of the following values: queued, inProgress, completed, failed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotResult.storage_size_bytes">
<code class="sig-name descname">storage_size_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotResult.storage_size_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the size of the snapshot in bytes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the type of cluster: replicaSet or shardedCluster.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetCloudProviderSnapshotsResult</code><span class="sig-paren">(</span><em class="sig-param">cluster_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">results=None</em>, <em class="sig-param">total_count=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCloudProviderSnapshots.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotsResult.results">
<code class="sig-name descname">results</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotsResult.results" title="Permalink to this definition">¶</a></dt>
<dd><p>Includes cloudProviderSnapshot object for each item detailed in the results array section.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.GetClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetClusterResult</code><span class="sig-paren">(</span><em class="sig-param">auto_scaling_disk_gb_enabled=None</em>, <em class="sig-param">backing_provider_name=None</em>, <em class="sig-param">backup_enabled=None</em>, <em class="sig-param">bi_connector=None</em>, <em class="sig-param">cluster_type=None</em>, <em class="sig-param">connection_strings=None</em>, <em class="sig-param">disk_size_gb=None</em>, <em class="sig-param">encryption_at_rest_provider=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">mongo_db_major_version=None</em>, <em class="sig-param">mongo_db_version=None</em>, <em class="sig-param">mongo_uri=None</em>, <em class="sig-param">mongo_uri_updated=None</em>, <em class="sig-param">mongo_uri_with_options=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">num_shards=None</em>, <em class="sig-param">paused=None</em>, <em class="sig-param">pit_enabled=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">provider_backup_enabled=None</em>, <em class="sig-param">provider_disk_iops=None</em>, <em class="sig-param">provider_disk_type_name=None</em>, <em class="sig-param">provider_encrypt_ebs_volume=None</em>, <em class="sig-param">provider_instance_size_name=None</em>, <em class="sig-param">provider_name=None</em>, <em class="sig-param">provider_region_name=None</em>, <em class="sig-param">provider_volume_type=None</em>, <em class="sig-param">replication_factor=None</em>, <em class="sig-param">replication_specs=None</em>, <em class="sig-param">snapshot_backup_policies=None</em>, <em class="sig-param">srv_address=None</em>, <em class="sig-param">state_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCluster.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.auto_scaling_disk_gb_enabled">
<code class="sig-name descname">auto_scaling_disk_gb_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.auto_scaling_disk_gb_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether disk auto-scaling is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.backing_provider_name">
<code class="sig-name descname">backing_provider_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.backing_provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates Cloud service provider on which the server for a multi-tenant cluster is provisioned.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.backup_enabled">
<code class="sig-name descname">backup_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.backup_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Legacy Option, Indicates whether Atlas continuous backups are enabled for the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.bi_connector">
<code class="sig-name descname">bi_connector</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.bi_connector" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates BI Connector for Atlas configuration on this cluster. BI Connector for Atlas is only available for M10+ clusters. See BI Connector below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.cluster_type">
<code class="sig-name descname">cluster_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.cluster_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates the type of the cluster that you want to modify. You cannot convert a sharded cluster deployment to a replica set deployment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.connection_strings">
<code class="sig-name descname">connection_strings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.connection_strings" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of connection strings that your applications use to connect to this cluster. More info in <a class="reference external" href="https://docs.mongodb.com/manual/reference/connection-string/">Connection-strings</a>. Use the parameters in this object to connect your applications to this cluster. To learn more about the formats of connection strings, see <a class="reference external" href="https://docs.atlas.mongodb.com/reference/faq/connection-changes/">Connection String Options</a>. NOTE: Atlas returns the contents of this object after the cluster is operational, not while it builds the cluster.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connection_strings.standard</span></code> -   Public mongodb:// connection string for this cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connection_strings.standard_srv</span></code> - Public mongodb+srv:// connection string for this cluster. The mongodb+srv protocol tells the driver to look up the seed list of hosts in DNS. Atlas synchronizes this list with the nodes in a cluster. If the connection string uses this URI format, you don’t need to append the seed list or change the URI if the nodes change. Use this URI format if your driver supports it. If it doesn’t, use connectionStrings.standard.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connection_strings.aws_private_link</span></code> -  <a class="reference external" href="https://docs.atlas.mongodb.com/security-private-endpoint/#private-endpoint-connection-strings">Private-endpoint-aware</a> mongodb://connection strings for each interface VPC endpoint you configured to connect to this cluster. Returned only if you created a AWS PrivateLink connection to this cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connection_strings.aws_private_link_srv</span></code> - <a class="reference external" href="https://docs.atlas.mongodb.com/security-private-endpoint/#private-endpoint-connection-strings">Private-endpoint-aware</a> mongodb+srv://connection strings for each interface VPC endpoint you configured to connect to this cluster. Returned only if you created a AWS PrivateLink connection to this cluster. Use this URI format if your driver supports it. If it doesn’t, use connectionStrings.awsPrivateLink.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connection_strings.private</span></code> -   <a class="reference external" href="https://docs.atlas.mongodb.com/security-vpc-peering/#vpc-peering">Network-peering-endpoint-aware</a> mongodb://connection strings for each interface VPC endpoint you configured to connect to this cluster. Returned only if you created a network peering connection to this cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connection_strings.private_srv</span></code> -  <a class="reference external" href="https://docs.atlas.mongodb.com/security-vpc-peering/#vpc-peering">Network-peering-endpoint-aware</a> mongodb+srv://connection strings for each interface VPC endpoint you configured to connect to this cluster. Returned only if you created a network peering connection to this cluster.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.disk_size_gb">
<code class="sig-name descname">disk_size_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.disk_size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates the size in gigabytes of the server’s root volume (AWS/GCP Only).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.encryption_at_rest_provider">
<code class="sig-name descname">encryption_at_rest_provider</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.encryption_at_rest_provider" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether Encryption at Rest is enabled or disabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.mongo_db_major_version">
<code class="sig-name descname">mongo_db_major_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.mongo_db_major_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates the version of the cluster to deploy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.mongo_db_version">
<code class="sig-name descname">mongo_db_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.mongo_db_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of MongoDB the cluster runs, in <code class="docutils literal notranslate"><span class="pre">major-version</span></code>.<code class="docutils literal notranslate"><span class="pre">minor-version</span></code> format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.mongo_uri">
<code class="sig-name descname">mongo_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.mongo_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>Base connection string for the cluster. Atlas only displays this field after the cluster is operational, not while it builds the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.mongo_uri_updated">
<code class="sig-name descname">mongo_uri_updated</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.mongo_uri_updated" title="Permalink to this definition">¶</a></dt>
<dd><p>Lists when the connection string was last updated. The connection string changes, for example, if you change a replica set to a sharded cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.mongo_uri_with_options">
<code class="sig-name descname">mongo_uri_with_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.mongo_uri_with_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes connection string for connecting to the Atlas cluster. Includes the replicaSet, ssl, and authSource query parameters in the connection string with values appropriate for the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the current plugin</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.num_shards">
<code class="sig-name descname">num_shards</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.num_shards" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of shards to deploy in the specified zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.paused">
<code class="sig-name descname">paused</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.paused" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag that indicates whether the cluster is paused or not.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.pit_enabled">
<code class="sig-name descname">pit_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.pit_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag that indicates if the cluster uses Point-in-Time backups.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.provider_backup_enabled">
<code class="sig-name descname">provider_backup_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.provider_backup_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag indicating if the cluster uses Cloud Provider Snapshots for backups.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.provider_disk_iops">
<code class="sig-name descname">provider_disk_iops</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.provider_disk_iops" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates the maximum input/output operations per second (IOPS) the system can perform. The possible values depend on the selected providerSettings.instanceSizeName and diskSizeGB.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.provider_disk_type_name">
<code class="sig-name descname">provider_disk_type_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.provider_disk_type_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes Azure disk type of the server’s root volume (Azure Only).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.provider_encrypt_ebs_volume">
<code class="sig-name descname">provider_encrypt_ebs_volume</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.provider_encrypt_ebs_volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the Amazon EBS encryption is enabled. This feature encrypts the server’s root volume for both data at rest within the volume and data moving between the volume and the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.provider_instance_size_name">
<code class="sig-name descname">provider_instance_size_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.provider_instance_size_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Atlas provides different instance sizes, each with a default storage capacity and RAM size.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.provider_name">
<code class="sig-name descname">provider_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates the cloud service provider on which the servers are provisioned.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.provider_region_name">
<code class="sig-name descname">provider_region_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.provider_region_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates Physical location of your MongoDB cluster. The region you choose can affect network latency for clients accessing your databases.  Requires the Atlas Region name, see the reference list for <a class="reference external" href="https://docs.atlas.mongodb.com/reference/amazon-aws/">AWS</a>, <a class="reference external" href="https://docs.atlas.mongodb.com/reference/google-gcp/">GCP</a>, <a class="reference external" href="https://docs.atlas.mongodb.com/reference/microsoft-azure/">Azure</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.provider_volume_type">
<code class="sig-name descname">provider_volume_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.provider_volume_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates the type of the volume. The possible values are: <code class="docutils literal notranslate"><span class="pre">STANDARD</span></code> and <code class="docutils literal notranslate"><span class="pre">PROVISIONED</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.replication_factor">
<code class="sig-name descname">replication_factor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.replication_factor" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of replica set members. Each member keeps a copy of your databases, providing high availability and data redundancy. The possible values are 3, 5, or 7. The default value is 3.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.replication_specs">
<code class="sig-name descname">replication_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.replication_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for cluster regions.  See Replication Spec below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.snapshot_backup_policies">
<code class="sig-name descname">snapshot_backup_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.snapshot_backup_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>current snapshot schedule and retention settings for the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.srv_address">
<code class="sig-name descname">srv_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.srv_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Connection string for connecting to the Atlas cluster. The +srv modifier forces the connection to use TLS/SSL. See the mongoURI for additional options.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClusterResult.state_name">
<code class="sig-name descname">state_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.state_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates the current state of the cluster. The possible states are:</p>
<ul class="simple">
<li><p>IDLE</p></li>
<li><p>CREATING</p></li>
<li><p>UPDATING</p></li>
<li><p>DELETING</p></li>
<li><p>DELETED</p></li>
<li><p>REPAIRING</p></li>
</ul>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.GetClustersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetClustersResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">results=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetClustersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getClusters.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClustersResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClustersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetClustersResult.results">
<code class="sig-name descname">results</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetClustersResult.results" title="Permalink to this definition">¶</a></dt>
<dd><p>A list where each represents a Cluster. See Cluster below for more details.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.GetCustomDbRoleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetCustomDbRoleResult</code><span class="sig-paren">(</span><em class="sig-param">actions=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">inherited_roles=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">role_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetCustomDbRoleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCustomDbRole.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCustomDbRoleResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCustomDbRoleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.GetCustomDbRolesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetCustomDbRolesResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">results=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetCustomDbRolesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCustomDbRoles.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCustomDbRolesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCustomDbRolesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetCustomDbRolesResult.results">
<code class="sig-name descname">results</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetCustomDbRolesResult.results" title="Permalink to this definition">¶</a></dt>
<dd><p>A list where each represents a custom db roles.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.GetDatabaseUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetDatabaseUserResult</code><span class="sig-paren">(</span><em class="sig-param">auth_database_name=None</em>, <em class="sig-param">database_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">x509_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetDatabaseUserResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDatabaseUser.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetDatabaseUserResult.database_name">
<code class="sig-name descname">database_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetDatabaseUserResult.database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Database on which the user has the specified role. A role on the <code class="docutils literal notranslate"><span class="pre">admin</span></code> database can include privileges that apply to the other databases.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetDatabaseUserResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetDatabaseUserResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetDatabaseUserResult.roles">
<code class="sig-name descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetDatabaseUserResult.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>List of user’s roles and the databases / collections on which the roles apply. A role allows the user to perform particular actions on the specified database. A role on the admin database can include privileges that apply to the other databases as well. See Roles below for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetDatabaseUserResult.x509_type">
<code class="sig-name descname">x509_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetDatabaseUserResult.x509_type" title="Permalink to this definition">¶</a></dt>
<dd><p>X.509 method by which the provided username is authenticated.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.GetDatabaseUsersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetDatabaseUsersResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">results=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetDatabaseUsersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDatabaseUsers.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetDatabaseUsersResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetDatabaseUsersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetDatabaseUsersResult.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetDatabaseUsersResult.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the Atlas project the user belongs to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetDatabaseUsersResult.results">
<code class="sig-name descname">results</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetDatabaseUsersResult.results" title="Permalink to this definition">¶</a></dt>
<dd><p>A list where each represents a Database user.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.GetGlobalClusterConfigResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetGlobalClusterConfigResult</code><span class="sig-paren">(</span><em class="sig-param">cluster_name=None</em>, <em class="sig-param">custom_zone_mapping=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">managed_namespaces=None</em>, <em class="sig-param">project_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetGlobalClusterConfigResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGlobalClusterConfig.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetGlobalClusterConfigResult.custom_zone_mapping">
<code class="sig-name descname">custom_zone_mapping</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetGlobalClusterConfigResult.custom_zone_mapping" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of all custom zone mappings defined for the Global Cluster. Atlas automatically maps each location code to the closest geographical zone. Custom zone mappings allow administrators to override these automatic mappings. If your Global Cluster does not have any custom zone mappings, this document is empty.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetGlobalClusterConfigResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetGlobalClusterConfigResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetGlobalClusterConfigResult.managed_namespaces">
<code class="sig-name descname">managed_namespaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetGlobalClusterConfigResult.managed_namespaces" title="Permalink to this definition">¶</a></dt>
<dd><p>Add a managed namespaces to a Global Cluster. For more information about managed namespaces, see <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/global-clusters/">Global Clusters</a>. See Managed Namespace below for more details.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.GetMaintenanceWindowResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetMaintenanceWindowResult</code><span class="sig-paren">(</span><em class="sig-param">day_of_week=None</em>, <em class="sig-param">hour_of_day=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">number_of_deferrals=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">start_asap=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetMaintenanceWindowResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getMaintenanceWindow.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetMaintenanceWindowResult.day_of_week">
<code class="sig-name descname">day_of_week</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetMaintenanceWindowResult.day_of_week" title="Permalink to this definition">¶</a></dt>
<dd><p>Day of the week when you would like the maintenance window to start as a 1-based integer: S=1, M=2, T=3, W=4, T=5, F=6, S=7.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetMaintenanceWindowResult.hour_of_day">
<code class="sig-name descname">hour_of_day</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetMaintenanceWindowResult.hour_of_day" title="Permalink to this definition">¶</a></dt>
<dd><p>Hour of the day when you would like the maintenance window to start. This parameter uses the 24-hour clock, where midnight is 0, noon is 12  (Time zone is UTC).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetMaintenanceWindowResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetMaintenanceWindowResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetMaintenanceWindowResult.number_of_deferrals">
<code class="sig-name descname">number_of_deferrals</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetMaintenanceWindowResult.number_of_deferrals" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of times the current maintenance event for this project has been deferred, you can set a maximum of 2 deferrals.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetMaintenanceWindowResult.start_asap">
<code class="sig-name descname">start_asap</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetMaintenanceWindowResult.start_asap" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag indicating whether project maintenance has been directed to start immediately. If you request that maintenance begin immediately, this field returns true from the time the request was made until the time the maintenance event completes.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.GetNetworkContainerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetNetworkContainerResult</code><span class="sig-paren">(</span><em class="sig-param">atlas_cidr_block=None</em>, <em class="sig-param">azure_subscription_id=None</em>, <em class="sig-param">container_id=None</em>, <em class="sig-param">gcp_project_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">network_name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">provider_name=None</em>, <em class="sig-param">provisioned=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">region_name=None</em>, <em class="sig-param">vnet_name=None</em>, <em class="sig-param">vpc_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainerResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetworkContainer.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkContainerResult.atlas_cidr_block">
<code class="sig-name descname">atlas_cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainerResult.atlas_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>CIDR block that Atlas uses for your clusters. Atlas uses the specified CIDR block for all other Network Peering connections created in the project. The Atlas CIDR block must be at least a /24 and at most a /21 in one of the following <a class="reference external" href="https://tools.ietf.org/html/rfc1918.html#section-3">private networks</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkContainerResult.azure_subscription_id">
<code class="sig-name descname">azure_subscription_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainerResult.azure_subscription_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifer of the Azure subscription in which the VNet resides.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkContainerResult.gcp_project_id">
<code class="sig-name descname">gcp_project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainerResult.gcp_project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the GCP project in which the Network Peering connection resides.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkContainerResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainerResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkContainerResult.network_name">
<code class="sig-name descname">network_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainerResult.network_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Network Peering connection in the Atlas project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkContainerResult.provider_name">
<code class="sig-name descname">provider_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainerResult.provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud provider for this Network Peering connection. If omitted, Atlas sets this parameter to AWS.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkContainerResult.provisioned">
<code class="sig-name descname">provisioned</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainerResult.provisioned" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the project has Network Peering connections deployed in the container.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkContainerResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainerResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The Atlas Azure region name for where this container will exist.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkContainerResult.region_name">
<code class="sig-name descname">region_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainerResult.region_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Atlas AWS region name for where this container will exist.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkContainerResult.vnet_name">
<code class="sig-name descname">vnet_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainerResult.vnet_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Azure VNet. This value is null until you provision an Azure VNet in the container.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkContainerResult.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainerResult.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the project’s VPC.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.GetNetworkContainersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetNetworkContainersResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">provider_name=None</em>, <em class="sig-param">results=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetworkContainers.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkContainersResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkContainersResult.provider_name">
<code class="sig-name descname">provider_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainersResult.provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud provider for this Network Peering connection. If omitted, Atlas sets this parameter to AWS.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkContainersResult.results">
<code class="sig-name descname">results</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainersResult.results" title="Permalink to this definition">¶</a></dt>
<dd><p>A list where each represents a Network Peering Container.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetNetworkPeeringResult</code><span class="sig-paren">(</span><em class="sig-param">accepter_region_name=None</em>, <em class="sig-param">atlas_cidr_block=None</em>, <em class="sig-param">atlas_id=None</em>, <em class="sig-param">aws_account_id=None</em>, <em class="sig-param">azure_directory_id=None</em>, <em class="sig-param">azure_subscription_id=None</em>, <em class="sig-param">connection_id=None</em>, <em class="sig-param">container_id=None</em>, <em class="sig-param">error_message=None</em>, <em class="sig-param">error_state=None</em>, <em class="sig-param">error_state_name=None</em>, <em class="sig-param">gcp_project_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">network_name=None</em>, <em class="sig-param">peering_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">provider_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">route_table_cidr_block=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">status_name=None</em>, <em class="sig-param">vnet_name=None</em>, <em class="sig-param">vpc_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetworkPeering.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.accepter_region_name">
<code class="sig-name descname">accepter_region_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.accepter_region_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the region where the peer VPC resides. For complete lists of supported regions, see <a class="reference external" href="https://docs.atlas.mongodb.com/reference/amazon-aws/">Amazon Web Services</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.atlas_cidr_block">
<code class="sig-name descname">atlas_cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.atlas_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier for an Azure AD directory.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.aws_account_id">
<code class="sig-name descname">aws_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.aws_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account ID of the owner of the peer VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.azure_directory_id">
<code class="sig-name descname">azure_directory_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.azure_directory_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier for an Azure AD directory.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.azure_subscription_id">
<code class="sig-name descname">azure_subscription_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.azure_subscription_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifer of the Azure subscription in which the VNet resides.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.connection_id">
<code class="sig-name descname">connection_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier for the peering connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.error_message">
<code class="sig-name descname">error_message</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.error_message" title="Permalink to this definition">¶</a></dt>
<dd><p>When <code class="docutils literal notranslate"><span class="pre">&quot;status&quot;</span> <span class="pre">:</span> <span class="pre">&quot;FAILED&quot;</span></code>, Atlas provides a description of the error.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.error_state">
<code class="sig-name descname">error_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.error_state" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the Atlas error when <code class="docutils literal notranslate"><span class="pre">status</span></code> is <code class="docutils literal notranslate"><span class="pre">Failed</span></code>, Otherwise, Atlas returns <code class="docutils literal notranslate"><span class="pre">null</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.error_state_name">
<code class="sig-name descname">error_state_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.error_state_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Error state, if any. The VPC peering connection error state value can be one of the following: <code class="docutils literal notranslate"><span class="pre">REJECTED</span></code>, <code class="docutils literal notranslate"><span class="pre">EXPIRED</span></code>, <code class="docutils literal notranslate"><span class="pre">INVALID_ARGUMENT</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.gcp_project_id">
<code class="sig-name descname">gcp_project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.gcp_project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>GCP project ID of the owner of the network peer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.network_name">
<code class="sig-name descname">network_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.network_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the network peer to which Atlas connects.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.provider_name">
<code class="sig-name descname">provider_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud provider for this VPC peering connection. If omitted, Atlas sets this parameter to AWS. (Possible Values <code class="docutils literal notranslate"><span class="pre">AWS</span></code>, <code class="docutils literal notranslate"><span class="pre">AZURE</span></code>, <code class="docutils literal notranslate"><span class="pre">GCP</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of your Azure resource group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.route_table_cidr_block">
<code class="sig-name descname">route_table_cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.route_table_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>Peer VPC CIDR block or subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the Atlas network peering connection: <code class="docutils literal notranslate"><span class="pre">ADDING_PEER</span></code>, <code class="docutils literal notranslate"><span class="pre">AVAILABLE</span></code>, <code class="docutils literal notranslate"><span class="pre">FAILED</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETING</span></code>, <code class="docutils literal notranslate"><span class="pre">WAITING_FOR_USER</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.status_name">
<code class="sig-name descname">status_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.status_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC peering connection status value can be one of the following: <code class="docutils literal notranslate"><span class="pre">INITIATING</span></code>, <code class="docutils literal notranslate"><span class="pre">PENDING_ACCEPTANCE</span></code>, <code class="docutils literal notranslate"><span class="pre">FAILED</span></code>, <code class="docutils literal notranslate"><span class="pre">FINALIZING</span></code>, <code class="docutils literal notranslate"><span class="pre">AVAILABLE</span></code>, <code class="docutils literal notranslate"><span class="pre">TERMINATING</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.vnet_name">
<code class="sig-name descname">vnet_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.vnet_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of your Azure VNet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the peer VPC.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetNetworkPeeringsResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">results=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetworkPeerings.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringsResult.results">
<code class="sig-name descname">results</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringsResult.results" title="Permalink to this definition">¶</a></dt>
<dd><p>A list where each represents a Network Peering Connection.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.GetPrivateEndpointInterfaceLinkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetPrivateEndpointInterfaceLinkResult</code><span class="sig-paren">(</span><em class="sig-param">connection_status=None</em>, <em class="sig-param">delete_requested=None</em>, <em class="sig-param">error_message=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">interface_endpoint_id=None</em>, <em class="sig-param">private_link_id=None</em>, <em class="sig-param">project_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateEndpointInterfaceLinkResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPrivateEndpointInterfaceLink.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetPrivateEndpointInterfaceLinkResult.connection_status">
<code class="sig-name descname">connection_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateEndpointInterfaceLinkResult.connection_status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the interface endpoint.
Returns one of the following values:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetPrivateEndpointInterfaceLinkResult.delete_requested">
<code class="sig-name descname">delete_requested</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateEndpointInterfaceLinkResult.delete_requested" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates if Atlas received a request to remove the interface endpoint from the private endpoint connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetPrivateEndpointInterfaceLinkResult.error_message">
<code class="sig-name descname">error_message</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateEndpointInterfaceLinkResult.error_message" title="Permalink to this definition">¶</a></dt>
<dd><p>Error message pertaining to the interface endpoint. Returns null if there are no errors.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetPrivateEndpointInterfaceLinkResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateEndpointInterfaceLinkResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.GetPrivateEndpointResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetPrivateEndpointResult</code><span class="sig-paren">(</span><em class="sig-param">endpoint_service_name=None</em>, <em class="sig-param">error_message=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">interface_endpoints=None</em>, <em class="sig-param">private_link_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateEndpointResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPrivateEndpoint.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetPrivateEndpointResult.endpoint_service_name">
<code class="sig-name descname">endpoint_service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateEndpointResult.endpoint_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the PrivateLink endpoint service in AWS. Returns null while the endpoint service is being created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetPrivateEndpointResult.error_message">
<code class="sig-name descname">error_message</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateEndpointResult.error_message" title="Permalink to this definition">¶</a></dt>
<dd><p>Error message pertaining to the AWS PrivateLink connection. Returns null if there are no errors.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetPrivateEndpointResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateEndpointResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetPrivateEndpointResult.interface_endpoints">
<code class="sig-name descname">interface_endpoints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateEndpointResult.interface_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifiers of the interface endpoints in your VPC that you added to the AWS PrivateLink connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetPrivateEndpointResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateEndpointResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the AWS PrivateLink connection.
Returns one of the following values:</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.GetProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetProjectResult</code><span class="sig-paren">(</span><em class="sig-param">cluster_count=None</em>, <em class="sig-param">created=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">org_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">teams=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProject.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetProjectResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetProjectResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetProjectResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetProjectResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the project you want to create. (Cannot be changed via this Provider after creation.)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetProjectResult.org_id">
<code class="sig-name descname">org_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetProjectResult.org_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the organization you want to create the project within.
<em>``cluster_count`` - The number of Atlas clusters deployed in the project.</em><code class="docutils literal notranslate"><span class="pre">created</span></code> - The ISO-8601-formatted timestamp of when Atlas created the project.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">teams.#.team_id</span></code> - The unique identifier of the team you want to associate with the project. The team and project must share the same parent organization.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">teams.#.role_names</span></code> - Each string in the array represents a project role assigned to the team. Every user associated with the team inherits these roles.
The following are valid roles:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP_OWNER</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP_READ_ONLY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP_DATA_ACCESS_ADMIN</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP_DATA_ACCESS_READ_WRITE</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP_DATA_ACCESS_READ_ONLY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP_CLUSTER_MANAGER</span></code></p></li>
</ul>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.GetProjectsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetProjectsResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">results=None</em>, <em class="sig-param">total_count=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetProjectsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProjects.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetProjectsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetProjectsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.GetTeamResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetTeamResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">org_id=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">usernames=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetTeamResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTeam.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetTeamResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetTeamResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetTeamResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetTeamResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the team you want to create.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetTeamResult.usernames">
<code class="sig-name descname">usernames</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetTeamResult.usernames" title="Permalink to this definition">¶</a></dt>
<dd><p>The users who are part of the organization.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.GetTeamsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetTeamsResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">org_id=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">usernames=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetTeamsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTeams.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.GetTeamsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GetTeamsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_mongodbatlas.GlobalClusterConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GlobalClusterConfig</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">custom_zone_mappings=None</em>, <em class="sig-param">managed_namespaces=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GlobalClusterConfig" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.GlobalClusterConfig</span></code> provides a Global Cluster Configuration resource.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>custom_zone_mappings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Each element in the list maps one ISO location code to a zone in your Global Cluster. See Custom Zone Mapping below for more details.</p></li>
<li><p><strong>managed_namespaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>Add a managed namespaces to a Global Cluster. For more information about managed namespaces, see <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/global-clusters/">Global Clusters</a>. See Managed Namespace below for more details.</p>
</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to create the database user.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `cluster_name - (Required) The name of the Global Cluster.
</pre></div>
</div>
<p>The <strong>custom_zone_mappings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ISO location code to which you want to map a zone in your Global Cluster. You can find a list of all supported location codes <a class="reference external" href="https://cloud.mongodb.com/static/atlas/country_iso_codes.txt">here</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the zone in your Global Cluster that you want to map to location.</p></li>
</ul>
<p>The <strong>managed_namespaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">collection</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the collection associated with the managed namespace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customShardKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The custom shard key for the collection. Global Clusters require a compound shard key consisting of a location field and a user-selected second key, the custom shard key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">db</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the database containing the collection.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.GlobalClusterConfig.custom_zone_mapping">
<code class="sig-name descname">custom_zone_mapping</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GlobalClusterConfig.custom_zone_mapping" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of all custom zone mappings defined for the Global Cluster. Atlas automatically maps each location code to the closest geographical zone. Custom zone mappings allow administrators to override these automatic mappings. If your Global Cluster does not have any custom zone mappings, this document is empty.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GlobalClusterConfig.custom_zone_mappings">
<code class="sig-name descname">custom_zone_mappings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GlobalClusterConfig.custom_zone_mappings" title="Permalink to this definition">¶</a></dt>
<dd><p>Each element in the list maps one ISO location code to a zone in your Global Cluster. See Custom Zone Mapping below for more details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ISO location code to which you want to map a zone in your Global Cluster. You can find a list of all supported location codes <a class="reference external" href="https://cloud.mongodb.com/static/atlas/country_iso_codes.txt">here</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zone</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the zone in your Global Cluster that you want to map to location.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GlobalClusterConfig.managed_namespaces">
<code class="sig-name descname">managed_namespaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GlobalClusterConfig.managed_namespaces" title="Permalink to this definition">¶</a></dt>
<dd><p>Add a managed namespaces to a Global Cluster. For more information about managed namespaces, see <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/global-clusters/">Global Clusters</a>. See Managed Namespace below for more details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">collection</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the collection associated with the managed namespace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customShardKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The custom shard key for the collection. Global Clusters require a compound shard key consisting of a location field and a user-selected second key, the custom shard key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">db</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the database containing the collection.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.GlobalClusterConfig.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.GlobalClusterConfig.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique ID for the project to create the database user.</p>
<ul class="simple">
<li><p><a href="#id34"><span class="problematic" id="id35">`</span></a>cluster_name - (Required) The name of the Global Cluster.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.GlobalClusterConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">custom_zone_mapping=None</em>, <em class="sig-param">custom_zone_mappings=None</em>, <em class="sig-param">managed_namespaces=None</em>, <em class="sig-param">project_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GlobalClusterConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GlobalClusterConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>custom_zone_mapping</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of all custom zone mappings defined for the Global Cluster. Atlas automatically maps each location code to the closest geographical zone. Custom zone mappings allow administrators to override these automatic mappings. If your Global Cluster does not have any custom zone mappings, this document is empty.</p></li>
<li><p><strong>custom_zone_mappings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Each element in the list maps one ISO location code to a zone in your Global Cluster. See Custom Zone Mapping below for more details.</p></li>
<li><p><strong>managed_namespaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>Add a managed namespaces to a Global Cluster. For more information about managed namespaces, see <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/global-clusters/">Global Clusters</a>. See Managed Namespace below for more details.</p>
</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to create the database user.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `cluster_name - (Required) The name of the Global Cluster.
</pre></div>
</div>
<p>The <strong>custom_zone_mappings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ISO location code to which you want to map a zone in your Global Cluster. You can find a list of all supported location codes <a class="reference external" href="https://cloud.mongodb.com/static/atlas/country_iso_codes.txt">here</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the zone in your Global Cluster that you want to map to location.</p></li>
</ul>
<p>The <strong>managed_namespaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">collection</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the collection associated with the managed namespace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customShardKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The custom shard key for the collection. Global Clusters require a compound shard key consisting of a location field and a user-selected second key, the custom shard key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">db</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the database containing the collection.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.GlobalClusterConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GlobalClusterConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.GlobalClusterConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GlobalClusterConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.MaintenanceWindow">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">MaintenanceWindow</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">day_of_week=None</em>, <em class="sig-param">defer=None</em>, <em class="sig-param">hour_of_day=None</em>, <em class="sig-param">number_of_deferrals=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.MaintenanceWindow" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.MaintenanceWindow</span></code> provides a resource to schedule a maintenance window for your MongoDB Atlas Project and/or set to defer a scheduled maintenance up to two times.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<ul class="simple">
<li><p>Urgent Maintenance Activities Cannot Wait: Urgent maintenance activities such as security patches cannot wait for your chosen window. Atlas will start those maintenance activities when needed.</p></li>
</ul>
<p>Once maintenance is scheduled for your cluster, you cannot change your maintenance window until the current maintenance efforts have completed.</p>
<ul class="simple">
<li><p>Maintenance Requires Replica Set Elections: Atlas performs maintenance the same way as the manual maintenance procedure. This requires at least one replica set election during the maintenance window per replica set.</p></li>
<li><p>Maintenance Starts As Close to the Hour As Possible: Maintenance always begins as close to the scheduled hour as possible, but in-progress cluster updates or expected system issues could delay the start time.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>day_of_week</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Day of the week when you would like the maintenance window to start as a 1-based integer: S=1, M=2, T=3, W=4, T=5, F=6, S=7.</p></li>
<li><p><strong>defer</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defer maintenance for the given project for one week.</p></li>
<li><p><strong>hour_of_day</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Hour of the day when you would like the maintenance window to start. This parameter uses the 24-hour clock, where midnight is 0, noon is 12 (Time zone is UTC).</p></li>
<li><p><strong>number_of_deferrals</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of times the current maintenance event for this project has been deferred, you can set a maximum of 2 deferrals.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the project for the Maintenance Window.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.MaintenanceWindow.day_of_week">
<code class="sig-name descname">day_of_week</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.MaintenanceWindow.day_of_week" title="Permalink to this definition">¶</a></dt>
<dd><p>Day of the week when you would like the maintenance window to start as a 1-based integer: S=1, M=2, T=3, W=4, T=5, F=6, S=7.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.MaintenanceWindow.defer">
<code class="sig-name descname">defer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.MaintenanceWindow.defer" title="Permalink to this definition">¶</a></dt>
<dd><p>Defer maintenance for the given project for one week.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.MaintenanceWindow.hour_of_day">
<code class="sig-name descname">hour_of_day</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.MaintenanceWindow.hour_of_day" title="Permalink to this definition">¶</a></dt>
<dd><p>Hour of the day when you would like the maintenance window to start. This parameter uses the 24-hour clock, where midnight is 0, noon is 12 (Time zone is UTC).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.MaintenanceWindow.number_of_deferrals">
<code class="sig-name descname">number_of_deferrals</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.MaintenanceWindow.number_of_deferrals" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of times the current maintenance event for this project has been deferred, you can set a maximum of 2 deferrals.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.MaintenanceWindow.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.MaintenanceWindow.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier of the project for the Maintenance Window.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.MaintenanceWindow.start_asap">
<code class="sig-name descname">start_asap</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.MaintenanceWindow.start_asap" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag indicating whether project maintenance has been directed to start immediately. If you request that maintenance begin immediately, this field returns true from the time the request was made until the time the maintenance event completes.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.MaintenanceWindow.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">day_of_week=None</em>, <em class="sig-param">defer=None</em>, <em class="sig-param">hour_of_day=None</em>, <em class="sig-param">number_of_deferrals=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">start_asap=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.MaintenanceWindow.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MaintenanceWindow resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>day_of_week</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Day of the week when you would like the maintenance window to start as a 1-based integer: S=1, M=2, T=3, W=4, T=5, F=6, S=7.</p></li>
<li><p><strong>defer</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defer maintenance for the given project for one week.</p></li>
<li><p><strong>hour_of_day</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Hour of the day when you would like the maintenance window to start. This parameter uses the 24-hour clock, where midnight is 0, noon is 12 (Time zone is UTC).</p></li>
<li><p><strong>number_of_deferrals</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of times the current maintenance event for this project has been deferred, you can set a maximum of 2 deferrals.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the project for the Maintenance Window.</p></li>
<li><p><strong>start_asap</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag indicating whether project maintenance has been directed to start immediately. If you request that maintenance begin immediately, this field returns true from the time the request was made until the time the maintenance event completes.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.MaintenanceWindow.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.MaintenanceWindow.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.MaintenanceWindow.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.MaintenanceWindow.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.NetworkContainer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">NetworkContainer</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">atlas_cidr_block=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">provider_name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">region_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.NetworkContainer</span></code> provides a Network Peering Container resource. The resource lets you create, edit and delete network peering containers. The resource requires your Project ID.</p>
<blockquote>
<div><p><strong>IMPORTANT:</strong> This resource creates one Network Peering container into which Atlas can deploy Network Peering connections. An Atlas project can have a maximum of one container for each cloud provider. You must have either the Project Owner or Organization Owner role to successfully call this endpoint.</p>
</div></blockquote>
<p>The following table outlines the maximum number of Network Peering containers per cloud provider:</p>
<ul class="simple">
<li><p>Cloud Provider:  GCP - Container Limit: One container per project.</p></li>
<li><p>Cloud Provider:  AWS and Azure - Container Limit: One container per cloud provider region.</p></li>
</ul>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <strong>group_id</strong> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>atlas_cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>CIDR block that Atlas uses for your clusters. Atlas uses the specified CIDR block for all other Network Peering connections created in the project. The Atlas CIDR block must be at least a /24 and at most a /21 in one of the following <a class="reference external" href="https://tools.ietf.org/html/rfc1918.html#section-3">private networks</a>.</p>
</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to create the database user.</p></li>
<li><p><strong>provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud provider for this Network Peering connection. If omitted, Atlas sets this parameter to AWS.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Atlas Azure region name for where this container will exist.</p></li>
<li><p><strong>region_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Atlas AWS region name for where this container will exist.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkContainer.atlas_cidr_block">
<code class="sig-name descname">atlas_cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.atlas_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>CIDR block that Atlas uses for your clusters. Atlas uses the specified CIDR block for all other Network Peering connections created in the project. The Atlas CIDR block must be at least a /24 and at most a /21 in one of the following <a class="reference external" href="https://tools.ietf.org/html/rfc1918.html#section-3">private networks</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkContainer.azure_subscription_id">
<code class="sig-name descname">azure_subscription_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.azure_subscription_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifer of the Azure subscription in which the VNet resides.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkContainer.container_id">
<code class="sig-name descname">container_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.container_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Network Peering Container ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkContainer.gcp_project_id">
<code class="sig-name descname">gcp_project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.gcp_project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the GCP project in which the Network Peering connection resides.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkContainer.network_name">
<code class="sig-name descname">network_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.network_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Network Peering connection in the Atlas project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkContainer.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique ID for the project to create the database user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkContainer.provider_name">
<code class="sig-name descname">provider_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud provider for this Network Peering connection. If omitted, Atlas sets this parameter to AWS.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkContainer.provisioned">
<code class="sig-name descname">provisioned</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.provisioned" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the project has Network Peering connections deployed in the container.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkContainer.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The Atlas Azure region name for where this container will exist.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkContainer.region_name">
<code class="sig-name descname">region_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.region_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Atlas AWS region name for where this container will exist.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkContainer.vnet_name">
<code class="sig-name descname">vnet_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.vnet_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Azure VNet. This value is null until you provision an Azure VNet in the container.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkContainer.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the project’s VPC.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.NetworkContainer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">atlas_cidr_block=None</em>, <em class="sig-param">azure_subscription_id=None</em>, <em class="sig-param">container_id=None</em>, <em class="sig-param">gcp_project_id=None</em>, <em class="sig-param">network_name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">provider_name=None</em>, <em class="sig-param">provisioned=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">region_name=None</em>, <em class="sig-param">vnet_name=None</em>, <em class="sig-param">vpc_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkContainer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>atlas_cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>CIDR block that Atlas uses for your clusters. Atlas uses the specified CIDR block for all other Network Peering connections created in the project. The Atlas CIDR block must be at least a /24 and at most a /21 in one of the following <a class="reference external" href="https://tools.ietf.org/html/rfc1918.html#section-3">private networks</a>.</p>
</p></li>
<li><p><strong>azure_subscription_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifer of the Azure subscription in which the VNet resides.</p></li>
<li><p><strong>container_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Network Peering Container ID.</p></li>
<li><p><strong>gcp_project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the GCP project in which the Network Peering connection resides.</p></li>
<li><p><strong>network_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Network Peering connection in the Atlas project.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to create the database user.</p></li>
<li><p><strong>provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud provider for this Network Peering connection. If omitted, Atlas sets this parameter to AWS.</p></li>
<li><p><strong>provisioned</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether the project has Network Peering connections deployed in the container.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Atlas Azure region name for where this container will exist.</p></li>
<li><p><strong>region_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Atlas AWS region name for where this container will exist.</p></li>
<li><p><strong>vnet_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Azure VNet. This value is null until you provision an Azure VNet in the container.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the project’s VPC.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.NetworkContainer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.NetworkContainer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.NetworkPeering">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">NetworkPeering</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accepter_region_name=None</em>, <em class="sig-param">atlas_cidr_block=None</em>, <em class="sig-param">atlas_gcp_project_id=None</em>, <em class="sig-param">atlas_vpc_name=None</em>, <em class="sig-param">aws_account_id=None</em>, <em class="sig-param">azure_directory_id=None</em>, <em class="sig-param">azure_subscription_id=None</em>, <em class="sig-param">container_id=None</em>, <em class="sig-param">gcp_project_id=None</em>, <em class="sig-param">network_name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">provider_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">route_table_cidr_block=None</em>, <em class="sig-param">vnet_name=None</em>, <em class="sig-param">vpc_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a NetworkPeering resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] accepter_region_name: Specifies the region where the peer VPC resides. For complete lists of supported regions, see <a class="reference external" href="https://docs.atlas.mongodb.com/reference/amazon-aws/">Amazon Web Services</a>.
:param pulumi.Input[str] atlas_cidr_block: Unique identifier for an Azure AD directory.
:param pulumi.Input[str] atlas_gcp_project_id: The Atlas GCP Project ID for the GCP VPC used by your atlas cluster that it is need to set up the reciprocal connection.
:param pulumi.Input[str] atlas_vpc_name: The Atlas VPC Name is used by your atlas clister that it is need to set up the reciprocal connection.
:param pulumi.Input[str] aws_account_id: Account ID of the owner of the peer VPC.
:param pulumi.Input[str] azure_directory_id: Unique identifier for an Azure AD directory.
:param pulumi.Input[str] azure_subscription_id: Unique identifer of the Azure subscription in which the VNet resides.
:param pulumi.Input[str] container_id: Unique identifier of the Atlas VPC container for the region. You can create an Atlas VPC container using the Create Container endpoint. You cannot create more than one container per region. To retrieve a list of container IDs, use the Get list of VPC containers endpoint.
:param pulumi.Input[str] gcp_project_id: GCP project ID of the owner of the network peer.
:param pulumi.Input[str] network_name: Name of the network peer to which Atlas connects.
:param pulumi.Input[str] project_id: The unique ID for the project to create the database user.
:param pulumi.Input[str] provider_name: Cloud provider for this VPC peering connection. (Possible Values <code class="docutils literal notranslate"><span class="pre">AWS</span></code>, <code class="docutils literal notranslate"><span class="pre">AZURE</span></code>, <code class="docutils literal notranslate"><span class="pre">GCP</span></code>).
:param pulumi.Input[str] resource_group_name: Name of your Azure resource group.
:param pulumi.Input[str] route_table_cidr_block: Peer VPC CIDR block or subnet.
:param pulumi.Input[str] vnet_name: Name of your Azure VNet.
:param pulumi.Input[str] vpc_id: Unique identifier of the peer VPC.</p>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkPeering.accepter_region_name">
<code class="sig-name descname">accepter_region_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.accepter_region_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the region where the peer VPC resides. For complete lists of supported regions, see <a class="reference external" href="https://docs.atlas.mongodb.com/reference/amazon-aws/">Amazon Web Services</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkPeering.atlas_cidr_block">
<code class="sig-name descname">atlas_cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.atlas_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier for an Azure AD directory.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkPeering.atlas_gcp_project_id">
<code class="sig-name descname">atlas_gcp_project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.atlas_gcp_project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Atlas GCP Project ID for the GCP VPC used by your atlas cluster that it is need to set up the reciprocal connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkPeering.atlas_vpc_name">
<code class="sig-name descname">atlas_vpc_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.atlas_vpc_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Atlas VPC Name is used by your atlas clister that it is need to set up the reciprocal connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkPeering.aws_account_id">
<code class="sig-name descname">aws_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.aws_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account ID of the owner of the peer VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkPeering.azure_directory_id">
<code class="sig-name descname">azure_directory_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.azure_directory_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier for an Azure AD directory.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkPeering.azure_subscription_id">
<code class="sig-name descname">azure_subscription_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.azure_subscription_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifer of the Azure subscription in which the VNet resides.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkPeering.connection_id">
<code class="sig-name descname">connection_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier for the peering connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkPeering.container_id">
<code class="sig-name descname">container_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.container_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the Atlas VPC container for the region. You can create an Atlas VPC container using the Create Container endpoint. You cannot create more than one container per region. To retrieve a list of container IDs, use the Get list of VPC containers endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkPeering.error_message">
<code class="sig-name descname">error_message</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.error_message" title="Permalink to this definition">¶</a></dt>
<dd><p>When <code class="docutils literal notranslate"><span class="pre">&quot;status&quot;</span> <span class="pre">:</span> <span class="pre">&quot;FAILED&quot;</span></code>, Atlas provides a description of the error.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkPeering.error_state">
<code class="sig-name descname">error_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.error_state" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the Atlas error when <code class="docutils literal notranslate"><span class="pre">status</span></code> is <code class="docutils literal notranslate"><span class="pre">Failed</span></code>, Otherwise, Atlas returns <code class="docutils literal notranslate"><span class="pre">null</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkPeering.error_state_name">
<code class="sig-name descname">error_state_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.error_state_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Error state, if any. The VPC peering connection error state value can be one of the following: <code class="docutils literal notranslate"><span class="pre">REJECTED</span></code>, <code class="docutils literal notranslate"><span class="pre">EXPIRED</span></code>, <code class="docutils literal notranslate"><span class="pre">INVALID_ARGUMENT</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkPeering.gcp_project_id">
<code class="sig-name descname">gcp_project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.gcp_project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>GCP project ID of the owner of the network peer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkPeering.network_name">
<code class="sig-name descname">network_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.network_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the network peer to which Atlas connects.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkPeering.peer_id">
<code class="sig-name descname">peer_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.peer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Network Peering Container ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkPeering.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique ID for the project to create the database user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkPeering.provider_name">
<code class="sig-name descname">provider_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud provider for this VPC peering connection. (Possible Values <code class="docutils literal notranslate"><span class="pre">AWS</span></code>, <code class="docutils literal notranslate"><span class="pre">AZURE</span></code>, <code class="docutils literal notranslate"><span class="pre">GCP</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkPeering.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of your Azure resource group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkPeering.route_table_cidr_block">
<code class="sig-name descname">route_table_cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.route_table_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>Peer VPC CIDR block or subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkPeering.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.status" title="Permalink to this definition">¶</a></dt>
<dd><p>(Azure/GCP Only) Status of the Atlas network peering connection.  Azure/GCP: <code class="docutils literal notranslate"><span class="pre">ADDING_PEER</span></code>, <code class="docutils literal notranslate"><span class="pre">AVAILABLE</span></code>, <code class="docutils literal notranslate"><span class="pre">FAILED</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETING</span></code> GCP Only:  <code class="docutils literal notranslate"><span class="pre">WAITING_FOR_USER</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkPeering.status_name">
<code class="sig-name descname">status_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.status_name" title="Permalink to this definition">¶</a></dt>
<dd><p>(AWS Only) The VPC peering connection status value can be one of the following: <code class="docutils literal notranslate"><span class="pre">INITIATING</span></code>, <code class="docutils literal notranslate"><span class="pre">PENDING_ACCEPTANCE</span></code>, <code class="docutils literal notranslate"><span class="pre">FAILED</span></code>, <code class="docutils literal notranslate"><span class="pre">FINALIZING</span></code>, <code class="docutils literal notranslate"><span class="pre">AVAILABLE</span></code>, <code class="docutils literal notranslate"><span class="pre">TERMINATING</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkPeering.vnet_name">
<code class="sig-name descname">vnet_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.vnet_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of your Azure VNet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.NetworkPeering.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the peer VPC.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.NetworkPeering.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accepter_region_name=None</em>, <em class="sig-param">atlas_cidr_block=None</em>, <em class="sig-param">atlas_gcp_project_id=None</em>, <em class="sig-param">atlas_id=None</em>, <em class="sig-param">atlas_vpc_name=None</em>, <em class="sig-param">aws_account_id=None</em>, <em class="sig-param">azure_directory_id=None</em>, <em class="sig-param">azure_subscription_id=None</em>, <em class="sig-param">connection_id=None</em>, <em class="sig-param">container_id=None</em>, <em class="sig-param">error_message=None</em>, <em class="sig-param">error_state=None</em>, <em class="sig-param">error_state_name=None</em>, <em class="sig-param">gcp_project_id=None</em>, <em class="sig-param">network_name=None</em>, <em class="sig-param">peer_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">provider_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">route_table_cidr_block=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">status_name=None</em>, <em class="sig-param">vnet_name=None</em>, <em class="sig-param">vpc_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkPeering resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accepter_region_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the region where the peer VPC resides. For complete lists of supported regions, see <a class="reference external" href="https://docs.atlas.mongodb.com/reference/amazon-aws/">Amazon Web Services</a>.</p>
</p></li>
<li><p><strong>atlas_cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier for an Azure AD directory.</p></li>
<li><p><strong>atlas_gcp_project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Atlas GCP Project ID for the GCP VPC used by your atlas cluster that it is need to set up the reciprocal connection.</p></li>
<li><p><strong>atlas_vpc_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Atlas VPC Name is used by your atlas clister that it is need to set up the reciprocal connection.</p></li>
<li><p><strong>aws_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account ID of the owner of the peer VPC.</p></li>
<li><p><strong>azure_directory_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier for an Azure AD directory.</p></li>
<li><p><strong>azure_subscription_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifer of the Azure subscription in which the VNet resides.</p></li>
<li><p><strong>connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier for the peering connection.</p></li>
<li><p><strong>container_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the Atlas VPC container for the region. You can create an Atlas VPC container using the Create Container endpoint. You cannot create more than one container per region. To retrieve a list of container IDs, use the Get list of VPC containers endpoint.</p></li>
<li><p><strong>error_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">&quot;status&quot;</span> <span class="pre">:</span> <span class="pre">&quot;FAILED&quot;</span></code>, Atlas provides a description of the error.</p></li>
<li><p><strong>error_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the Atlas error when <code class="docutils literal notranslate"><span class="pre">status</span></code> is <code class="docutils literal notranslate"><span class="pre">Failed</span></code>, Otherwise, Atlas returns <code class="docutils literal notranslate"><span class="pre">null</span></code>.</p></li>
<li><p><strong>error_state_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Error state, if any. The VPC peering connection error state value can be one of the following: <code class="docutils literal notranslate"><span class="pre">REJECTED</span></code>, <code class="docutils literal notranslate"><span class="pre">EXPIRED</span></code>, <code class="docutils literal notranslate"><span class="pre">INVALID_ARGUMENT</span></code>.</p></li>
<li><p><strong>gcp_project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – GCP project ID of the owner of the network peer.</p></li>
<li><p><strong>network_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the network peer to which Atlas connects.</p></li>
<li><p><strong>peer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Network Peering Container ID.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to create the database user.</p></li>
<li><p><strong>provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud provider for this VPC peering connection. (Possible Values <code class="docutils literal notranslate"><span class="pre">AWS</span></code>, <code class="docutils literal notranslate"><span class="pre">AZURE</span></code>, <code class="docutils literal notranslate"><span class="pre">GCP</span></code>).</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of your Azure resource group.</p></li>
<li><p><strong>route_table_cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Peer VPC CIDR block or subnet.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Azure/GCP Only) Status of the Atlas network peering connection.  Azure/GCP: <code class="docutils literal notranslate"><span class="pre">ADDING_PEER</span></code>, <code class="docutils literal notranslate"><span class="pre">AVAILABLE</span></code>, <code class="docutils literal notranslate"><span class="pre">FAILED</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETING</span></code> GCP Only:  <code class="docutils literal notranslate"><span class="pre">WAITING_FOR_USER</span></code>.</p></li>
<li><p><strong>status_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (AWS Only) The VPC peering connection status value can be one of the following: <code class="docutils literal notranslate"><span class="pre">INITIATING</span></code>, <code class="docutils literal notranslate"><span class="pre">PENDING_ACCEPTANCE</span></code>, <code class="docutils literal notranslate"><span class="pre">FAILED</span></code>, <code class="docutils literal notranslate"><span class="pre">FINALIZING</span></code>, <code class="docutils literal notranslate"><span class="pre">AVAILABLE</span></code>, <code class="docutils literal notranslate"><span class="pre">TERMINATING</span></code>.</p></li>
<li><p><strong>vnet_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of your Azure VNet.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the peer VPC.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.NetworkPeering.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.NetworkPeering.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.PrivateEndpoint">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">PrivateEndpoint</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">provider_name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpoint" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.PrivateEndpoint</span></code> provides a Private Endpoint resource. This represents a Private Endpoint Connection that can be created in an Atlas project.</p>
<blockquote>
<div><p><strong>IMPORTANT:</strong>You must have one of the following roles to successfully handle the resource:</p>
<ul class="simple">
<li><p>Organization Owner</p></li>
<li><p>Project Owner</p></li>
</ul>
<p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required   Unique identifier for the project.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud provider region in which you want to create the private endpoint connection.
Accepted values are:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `us-east-1`
* `us-east-2`
* `us-west-1`
* `us-west-2`
* `ca-central-1`
* `sa-east-1`
* `eu-north-1`
* `eu-west-1`
* `eu-west-2`
* `eu-west-3`
* `eu-central-1`
* `me-south-1`
* `ap-northeast-1`
* `ap-northeast-2`
* `ap-south-1`
* `ap-southeast-1`
* `ap-southeast-2`
* `ap-east-1`
</pre></div>
</div>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.PrivateEndpoint.endpoint_service_name">
<code class="sig-name descname">endpoint_service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpoint.endpoint_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the PrivateLink endpoint service in AWS. Returns null while the endpoint service is being created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.PrivateEndpoint.error_message">
<code class="sig-name descname">error_message</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpoint.error_message" title="Permalink to this definition">¶</a></dt>
<dd><p>Error message pertaining to the AWS PrivateLink connection. Returns null if there are no errors.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.PrivateEndpoint.interface_endpoints">
<code class="sig-name descname">interface_endpoints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpoint.interface_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifiers of the interface endpoints in your VPC that you added to the AWS PrivateLink connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.PrivateEndpoint.private_link_id">
<code class="sig-name descname">private_link_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpoint.private_link_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the AWS PrivateLink connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.PrivateEndpoint.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpoint.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Required    Unique identifier for the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.PrivateEndpoint.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpoint.region" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud provider region in which you want to create the private endpoint connection.
Accepted values are:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">us-east-1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">us-east-2</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">us-west-1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">us-west-2</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ca-central-1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sa-east-1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eu-north-1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eu-west-1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eu-west-2</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eu-west-3</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eu-central-1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">me-south-1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ap-northeast-1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ap-northeast-2</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ap-south-1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ap-southeast-1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ap-southeast-2</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ap-east-1</span></code></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.PrivateEndpoint.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpoint.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the AWS PrivateLink connection.
Returns one of the following values:</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.PrivateEndpoint.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">endpoint_service_name=None</em>, <em class="sig-param">error_message=None</em>, <em class="sig-param">interface_endpoints=None</em>, <em class="sig-param">private_link_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">provider_name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpoint.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PrivateEndpoint resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>endpoint_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the PrivateLink endpoint service in AWS. Returns null while the endpoint service is being created.</p></li>
<li><p><strong>error_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Error message pertaining to the AWS PrivateLink connection. Returns null if there are no errors.</p></li>
<li><p><strong>interface_endpoints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Unique identifiers of the interface endpoints in your VPC that you added to the AWS PrivateLink connection.</p></li>
<li><p><strong>private_link_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the AWS PrivateLink connection.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required   Unique identifier for the project.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud provider region in which you want to create the private endpoint connection.
Accepted values are:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `us-east-1`
* `us-east-2`
* `us-west-1`
* `us-west-2`
* `ca-central-1`
* `sa-east-1`
* `eu-north-1`
* `eu-west-1`
* `eu-west-2`
* `eu-west-3`
* `eu-central-1`
* `me-south-1`
* `ap-northeast-1`
* `ap-northeast-2`
* `ap-south-1`
* `ap-southeast-1`
* `ap-southeast-2`
* `ap-east-1`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of the AWS PrivateLink connection.
Returns one of the following values:</p>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.PrivateEndpoint.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpoint.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.PrivateEndpoint.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpoint.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.PrivateEndpointInterfaceLink">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">PrivateEndpointInterfaceLink</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">interface_endpoint_id=None</em>, <em class="sig-param">private_link_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpointInterfaceLink" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.PrivateEndpointInterfaceLink</span></code> provides a Private Endpoint Interface Link resource. This represents a Private Endpoint Interface Link, which adds one interface endpoint to a private endpoint connection in an Atlas project.</p>
<blockquote>
<div><p><strong>IMPORTANT:</strong>You must have one of the following roles to successfully handle the resource:</p>
<ul class="simple">
<li><p>Organization Owner</p></li>
<li><p>Project Owner</p></li>
</ul>
<p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>interface_endpoint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the interface endpoint you created in your VPC with the AWS resource.</p></li>
<li><p><strong>private_link_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the AWS PrivateLink connection which is created by <code class="docutils literal notranslate"><span class="pre">.PrivateEndpoint</span></code> resource.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier for the project.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.PrivateEndpointInterfaceLink.connection_status">
<code class="sig-name descname">connection_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpointInterfaceLink.connection_status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the interface endpoint.
Returns one of the following values:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.PrivateEndpointInterfaceLink.delete_requested">
<code class="sig-name descname">delete_requested</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpointInterfaceLink.delete_requested" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates if Atlas received a request to remove the interface endpoint from the private endpoint connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.PrivateEndpointInterfaceLink.error_message">
<code class="sig-name descname">error_message</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpointInterfaceLink.error_message" title="Permalink to this definition">¶</a></dt>
<dd><p>Error message pertaining to the interface endpoint. Returns null if there are no errors.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.PrivateEndpointInterfaceLink.interface_endpoint_id">
<code class="sig-name descname">interface_endpoint_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpointInterfaceLink.interface_endpoint_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the interface endpoint you created in your VPC with the AWS resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.PrivateEndpointInterfaceLink.private_link_id">
<code class="sig-name descname">private_link_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpointInterfaceLink.private_link_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the AWS PrivateLink connection which is created by <code class="docutils literal notranslate"><span class="pre">.PrivateEndpoint</span></code> resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.PrivateEndpointInterfaceLink.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpointInterfaceLink.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier for the project.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.PrivateEndpointInterfaceLink.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">connection_status=None</em>, <em class="sig-param">delete_requested=None</em>, <em class="sig-param">error_message=None</em>, <em class="sig-param">interface_endpoint_id=None</em>, <em class="sig-param">private_link_id=None</em>, <em class="sig-param">project_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpointInterfaceLink.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PrivateEndpointInterfaceLink resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of the interface endpoint.
Returns one of the following values:</p></li>
<li><p><strong>delete_requested</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates if Atlas received a request to remove the interface endpoint from the private endpoint connection.</p></li>
<li><p><strong>error_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Error message pertaining to the interface endpoint. Returns null if there are no errors.</p></li>
<li><p><strong>interface_endpoint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the interface endpoint you created in your VPC with the AWS resource.</p></li>
<li><p><strong>private_link_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the AWS PrivateLink connection which is created by <code class="docutils literal notranslate"><span class="pre">.PrivateEndpoint</span></code> resource.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier for the project.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.PrivateEndpointInterfaceLink.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpointInterfaceLink.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.PrivateEndpointInterfaceLink.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpointInterfaceLink.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.PrivateIpMode">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">PrivateIpMode</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateIpMode" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.PrivateIpMode</span></code> provides a Private IP Mode resource. This allows one to disable Connect via Peering Only mode for a MongoDB Atlas Project.</p>
<blockquote>
<div><p><strong>Deprecated Feature</strong>: <span class="raw-html-m2r"><br></span> This feature has been deprecated. Use <a class="reference external" href="https://dochub.mongodb.org/core/atlas-horizon-faq">Split Horizon connection strings</a> to connect to your cluster. These connection strings allow you to connect using both VPC/VNet Peering and whitelisted public IP addresses. To learn more about support for Split Horizon, see <a class="reference external" href="https://dochub.mongodb.org/core/atlas-horizon-faq">this FAQ</a>. You need this endpoint to <a class="reference external" href="https://docs.atlas.mongodb.com/reference/faq/connection-changes/#disable-peering-mode">disable Peering Only</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether Connect via Peering Only mode is enabled or disabled for an Atlas project</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to enable Only Private IP Mode.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.PrivateIpMode.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.PrivateIpMode.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether Connect via Peering Only mode is enabled or disabled for an Atlas project</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.PrivateIpMode.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.PrivateIpMode.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique ID for the project to enable Only Private IP Mode.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.PrivateIpMode.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">project_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateIpMode.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PrivateIpMode resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether Connect via Peering Only mode is enabled or disabled for an Atlas project</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to enable Only Private IP Mode.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.PrivateIpMode.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateIpMode.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.PrivateIpMode.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateIpMode.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.Project">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">Project</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">org_id=None</em>, <em class="sig-param">teams=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Project" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Project resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] name: The name of the project you want to create. (Cannot be changed via this Provider after creation.)
:param pulumi.Input[str] org_id: The ID of the organization you want to create the project within.</p>
<p>The <strong>teams</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">roleNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Each string in the array represents a project role you want to assign to the team. Every user associated with the team inherits these roles. You must specify an array even if you are only associating a single role with the team.
The following are valid roles:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP_OWNER</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP_READ_ONLY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP_DATA_ACCESS_ADMIN</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP_DATA_ACCESS_READ_WRITE</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP_DATA_ACCESS_READ_ONLY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP_CLUSTER_MANAGER</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">team_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique identifier of the team you want to associate with the project. The team and project must share the same parent organization.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.Project.cluster_count">
<code class="sig-name descname">cluster_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Project.cluster_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of Atlas clusters deployed in the project..</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Project.created">
<code class="sig-name descname">created</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Project.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The ISO-8601-formatted timestamp of when Atlas created the project..</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Project.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Project.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the project you want to create. (Cannot be changed via this Provider after creation.)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Project.org_id">
<code class="sig-name descname">org_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Project.org_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the organization you want to create the project within.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.Project.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_count=None</em>, <em class="sig-param">created=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">org_id=None</em>, <em class="sig-param">teams=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Project.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Project resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of Atlas clusters deployed in the project..</p></li>
<li><p><strong>created</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO-8601-formatted timestamp of when Atlas created the project..</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the project you want to create. (Cannot be changed via this Provider after creation.)</p></li>
<li><p><strong>org_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the organization you want to create the project within.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>teams</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">roleNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Each string in the array represents a project role you want to assign to the team. Every user associated with the team inherits these roles. You must specify an array even if you are only associating a single role with the team.
The following are valid roles:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP_OWNER</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP_READ_ONLY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP_DATA_ACCESS_ADMIN</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP_DATA_ACCESS_READ_WRITE</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP_DATA_ACCESS_READ_ONLY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP_CLUSTER_MANAGER</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">team_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unique identifier of the team you want to associate with the project. The team and project must share the same parent organization.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.Project.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Project.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.Project.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Project.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.ProjectIpWhitelist">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">ProjectIpWhitelist</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">aws_security_group=None</em>, <em class="sig-param">cidr_block=None</em>, <em class="sig-param">comment=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpWhitelist" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.ProjectIpWhitelist</span></code> provides an IP Whitelist entry resource. The whitelist grants access from IPs, CIDRs or AWS Security Groups (if VPC Peering is enabled) to clusters within the Project.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
<p><strong>IMPORTANT:</strong>
When you remove an entry from the whitelist, existing connections from the removed address(es) may remain open for a variable amount of time. How much time passes before Atlas closes the connection depends on several factors, including how the connection was established, the particular behavior of the application or driver using the address, and the connection protocol (e.g., TCP or UDP). This is particularly important to consider when changing an existing IP address or CIDR block as they cannot be updated via the Provider (comments can however), hence a change will force the destruction and recreation of entries.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aws_security_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the whitelisted AWS security group. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">cidr_block</span></code> and <code class="docutils literal notranslate"><span class="pre">ip_address</span></code>.</p></li>
<li><p><strong>cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whitelist entry in Classless Inter-Domain Routing (CIDR) notation. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">aws_security_group</span></code> and <code class="docutils literal notranslate"><span class="pre">ip_address</span></code>.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Comment to add to the whitelist entry.</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whitelisted IP address. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">aws_security_group</span></code> and <code class="docutils literal notranslate"><span class="pre">cidr_block</span></code>.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which to add the whitelist entry.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.ProjectIpWhitelist.aws_security_group">
<code class="sig-name descname">aws_security_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpWhitelist.aws_security_group" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the whitelisted AWS security group. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">cidr_block</span></code> and <code class="docutils literal notranslate"><span class="pre">ip_address</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.ProjectIpWhitelist.cidr_block">
<code class="sig-name descname">cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpWhitelist.cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>Whitelist entry in Classless Inter-Domain Routing (CIDR) notation. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">aws_security_group</span></code> and <code class="docutils literal notranslate"><span class="pre">ip_address</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.ProjectIpWhitelist.comment">
<code class="sig-name descname">comment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpWhitelist.comment" title="Permalink to this definition">¶</a></dt>
<dd><p>Comment to add to the whitelist entry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.ProjectIpWhitelist.ip_address">
<code class="sig-name descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpWhitelist.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Whitelisted IP address. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">aws_security_group</span></code> and <code class="docutils literal notranslate"><span class="pre">cidr_block</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.ProjectIpWhitelist.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpWhitelist.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which to add the whitelist entry.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.ProjectIpWhitelist.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">aws_security_group=None</em>, <em class="sig-param">cidr_block=None</em>, <em class="sig-param">comment=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">project_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpWhitelist.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectIpWhitelist resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aws_security_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the whitelisted AWS security group. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">cidr_block</span></code> and <code class="docutils literal notranslate"><span class="pre">ip_address</span></code>.</p></li>
<li><p><strong>cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whitelist entry in Classless Inter-Domain Routing (CIDR) notation. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">aws_security_group</span></code> and <code class="docutils literal notranslate"><span class="pre">ip_address</span></code>.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Comment to add to the whitelist entry.</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whitelisted IP address. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">aws_security_group</span></code> and <code class="docutils literal notranslate"><span class="pre">cidr_block</span></code>.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which to add the whitelist entry.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.ProjectIpWhitelist.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpWhitelist.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.ProjectIpWhitelist.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpWhitelist.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">private_key=None</em>, <em class="sig-param">public_key=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the mongodbatlas package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – MongoDB Atlas Programmatic Private Key</p></li>
<li><p><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – MongoDB Atlas Programmatic Public Key</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_mongodbatlas.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.Team">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">Team</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">org_id=None</em>, <em class="sig-param">usernames=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Team" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.Teams</span></code> provides a Team resource. The resource lets you create, edit and delete Teams. Also, Teams can be assigned to multiple projects, and team members’ access to the project is determined by the team’s project role.</p>
<blockquote>
<div><p><strong>IMPORTANT:</strong> MongoDB Atlas Team limits: max 250 teams in an organization and max 100 teams per project.</p>
<p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<p>MongoDB Atlas Team limits: max 250 teams in an organization and max 100 teams per project.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the team you want to create.</p></li>
<li><p><strong>org_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier for the organization you want to associate the team with.</p></li>
<li><p><strong>usernames</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – You can only add Atlas users who are part of the organization. Users who have not accepted an invitation to join the organization cannot be added as team members. There is a maximum of 250 Atlas users per team.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.Team.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Team.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the team you want to create.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Team.org_id">
<code class="sig-name descname">org_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Team.org_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier for the organization you want to associate the team with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Team.team_id">
<code class="sig-name descname">team_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Team.team_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier for the team.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.Team.usernames">
<code class="sig-name descname">usernames</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.Team.usernames" title="Permalink to this definition">¶</a></dt>
<dd><p>You can only add Atlas users who are part of the organization. Users who have not accepted an invitation to join the organization cannot be added as team members. There is a maximum of 250 Atlas users per team.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.Team.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">org_id=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">usernames=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Team.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Team resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the team you want to create.</p></li>
<li><p><strong>org_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier for the organization you want to associate the team with.</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier for the team.</p></li>
<li><p><strong>usernames</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – You can only add Atlas users who are part of the organization. Users who have not accepted an invitation to join the organization cannot be added as team members. There is a maximum of 250 Atlas users per team.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.Team.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Team.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.Team.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Team.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.Teams">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">Teams</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">org_id=None</em>, <em class="sig-param">usernames=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Teams" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Teams resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<dl class="method">
<dt id="pulumi_mongodbatlas.Teams.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">org_id=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">usernames=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Teams.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Teams resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.Teams.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Teams.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.Teams.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Teams.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.X509AuthenticationDatabaseUser">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">X509AuthenticationDatabaseUser</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">customer_x509_cas=None</em>, <em class="sig-param">months_until_expiration=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.X509AuthenticationDatabaseUser" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.X509AuthenticationDatabaseUser</span></code> provides a X509 Authentication Database User resource. The .X509AuthenticationDatabaseUser resource lets you manage MongoDB users who authenticate using X.509 certificates. You can manage these X.509 certificates or let Atlas do it for you.</p>
<table class="docutils align-default">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Management</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Atlas</p></td>
<td><p>Atlas manages your Certificate Authority and can generate certificates for your MongoDB users. No additional X.509 configuration is required.</p></td>
</tr>
<tr class="row-odd"><td><p>Customer</p></td>
<td><p>You must provide a Certificate Authority and generate certificates for your MongoDB users.</p></td>
</tr>
</tbody>
</table>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>customer_x509_cas</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PEM string containing one or more customer CAs for database user authentication.</p></li>
<li><p><strong>months_until_expiration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – A number of months that the created certificate is valid for before expiry, up to 24 months. By default is 3.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier for the Atlas project associated with the X.509 configuration.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username of the database user to create a certificate for.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_mongodbatlas.X509AuthenticationDatabaseUser.certificates">
<code class="sig-name descname">certificates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.X509AuthenticationDatabaseUser.certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of objects where each details one unexpired database user certificate.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">created_at</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notAfter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.X509AuthenticationDatabaseUser.current_certificate">
<code class="sig-name descname">current_certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.X509AuthenticationDatabaseUser.current_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains the last X.509 certificate and private key created for a database user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.X509AuthenticationDatabaseUser.customer_x509_cas">
<code class="sig-name descname">customer_x509_cas</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.X509AuthenticationDatabaseUser.customer_x509_cas" title="Permalink to this definition">¶</a></dt>
<dd><p>PEM string containing one or more customer CAs for database user authentication.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.X509AuthenticationDatabaseUser.months_until_expiration">
<code class="sig-name descname">months_until_expiration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.X509AuthenticationDatabaseUser.months_until_expiration" title="Permalink to this definition">¶</a></dt>
<dd><p>A number of months that the created certificate is valid for before expiry, up to 24 months. By default is 3.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.X509AuthenticationDatabaseUser.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.X509AuthenticationDatabaseUser.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier for the Atlas project associated with the X.509 configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mongodbatlas.X509AuthenticationDatabaseUser.username">
<code class="sig-name descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mongodbatlas.X509AuthenticationDatabaseUser.username" title="Permalink to this definition">¶</a></dt>
<dd><p>Username of the database user to create a certificate for.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.X509AuthenticationDatabaseUser.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">certificates=None</em>, <em class="sig-param">current_certificate=None</em>, <em class="sig-param">customer_x509_cas=None</em>, <em class="sig-param">months_until_expiration=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.X509AuthenticationDatabaseUser.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing X509AuthenticationDatabaseUser resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>certificates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of objects where each details one unexpired database user certificate.</p></li>
<li><p><strong>current_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Contains the last X.509 certificate and private key created for a database user.</p></li>
<li><p><strong>customer_x509_cas</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PEM string containing one or more customer CAs for database user authentication.</p></li>
<li><p><strong>months_until_expiration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – A number of months that the created certificate is valid for before expiry, up to 24 months. By default is 3.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier for the Atlas project associated with the X.509 configuration.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username of the database user to create a certificate for.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>certificates</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">created_at</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notAfter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_mongodbatlas.X509AuthenticationDatabaseUser.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.X509AuthenticationDatabaseUser.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.X509AuthenticationDatabaseUser.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.X509AuthenticationDatabaseUser.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_mongodbatlas.get509_authentication_database_user">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get509_authentication_database_user</code><span class="sig-paren">(</span><em class="sig-param">project_id=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.get509_authentication_database_user" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.X509AuthenticationDatabaseUser</span></code> describe a X509 Authentication Database User. This represents a X509 Authentication Database User.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project_id</strong> (<em>str</em>) – Identifier for the Atlas project associated with the X.509 configuration.</p></li>
<li><p><strong>username</strong> (<em>str</em>) – Username of the database user to create a certificate for.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_mongodbatlas.get_alert_configuration">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_alert_configuration</code><span class="sig-paren">(</span><em class="sig-param">alert_configuration_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.get_alert_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.AlertConfiguration</span></code> describes an Alert Configuration.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <strong>group_id</strong> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>alert_configuration_id</strong> (<em>str</em>) – Unique identifier for the alert configuration.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The ID of the project where the alert configuration will create.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_mongodbatlas.get_auditing">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_auditing</code><span class="sig-paren">(</span><em class="sig-param">project_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.get_auditing" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.Auditing</span></code> describes a Auditing.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <strong>group_id</strong> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to create the database user.</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_mongodbatlas.get_cloud_provider_snapshot">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_cloud_provider_snapshot</code><span class="sig-paren">(</span><em class="sig-param">cluster_name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">snapshot_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.get_cloud_provider_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.CloudProviderSnapshot</span></code> provides an Cloud Provider Snapshot entry datasource. Atlas Cloud Provider Snapshots provide localized backup storage using the native snapshot functionality of the cluster’s cloud service provider.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cluster_name</strong> (<em>str</em>) – The name of the Atlas cluster that contains the snapshot you want to retrieve.</p></li>
<li><p><strong>snapshot_id</strong> (<em>str</em>) – The unique identifier of the snapshot you want to retrieve.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_mongodbatlas.get_cloud_provider_snapshot_backup_policy">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_cloud_provider_snapshot_backup_policy</code><span class="sig-paren">(</span><em class="sig-param">cluster_name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.get_cloud_provider_snapshot_backup_policy" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.CloudProviderSnapshotBackupPolicy</span></code> provides a Cloud Provider Snapshot Backup Policy entry datasource. An Atlas Cloud Provider Snapshot Backup Policy provides the current snapshot schedule and retention settings for the cluster.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cluster_name</strong> (<em>str</em>) – The name of the Atlas cluster that contains the snapshots backup policy you want to retrieve.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The unique identifier of the project for the Atlas cluster.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_mongodbatlas.get_cloud_provider_snapshot_restore_job">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_cloud_provider_snapshot_restore_job</code><span class="sig-paren">(</span><em class="sig-param">cluster_name=None</em>, <em class="sig-param">job_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.get_cloud_provider_snapshot_restore_job" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.CloudProviderSnapshotRestoreJob</span></code> provides a Cloud Provider Snapshot Restore Job entry datasource. Gets all cloud provider snapshot restore jobs for the specified cluster.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cluster_name</strong> (<em>str</em>) – The name of the Atlas cluster for which you want to retrieve the restore job.</p></li>
<li><p><strong>job_id</strong> (<em>str</em>) – The unique identifier of the restore job to retrieve.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The unique identifier of the project for the Atlas cluster.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_mongodbatlas.get_cloud_provider_snapshot_restore_jobs">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_cloud_provider_snapshot_restore_jobs</code><span class="sig-paren">(</span><em class="sig-param">cluster_name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.get_cloud_provider_snapshot_restore_jobs" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.getCloudProviderSnapshotRestoreJobs</span></code> provides a Cloud Provider Snapshot Restore Jobs entry datasource. Gets all cloud provider snapshot restore jobs for the specified cluster.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cluster_name</strong> (<em>str</em>) – The name of the Atlas cluster for which you want to retrieve restore jobs.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The unique identifier of the project for the Atlas cluster.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_mongodbatlas.get_cloud_provider_snapshots">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_cloud_provider_snapshots</code><span class="sig-paren">(</span><em class="sig-param">cluster_name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.get_cloud_provider_snapshots" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.getCloudProviderSnapshots</span></code> provides an Cloud Provider Snapshot entry datasource. Atlas Cloud Provider Snapshots provide localized backup storage using the native snapshot functionality of the cluster’s cloud service provider.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>cluster_name</strong> (<em>str</em>) – The name of the Atlas cluster that contains the snapshot you want to retrieve.</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_mongodbatlas.get_cluster">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_cluster</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.get_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.Cluster</span></code> describes a Cluster. The. The data source requires your Project ID.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
<p><strong>IMPORTANT:</strong>
<span class="raw-html-m2r"><br></span> &amp;#8226; Changes to cluster configurations can affect costs. Before making changes, please see <a class="reference external" href="https://docs.atlas.mongodb.com/billing/">Billing</a>.
<span class="raw-html-m2r"><br></span> &amp;#8226; If your Atlas project contains a custom role that uses actions introduced in a specific MongoDB version, you cannot create a cluster with a MongoDB version less than that version unless you delete the custom role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Name of the cluster as it appears in Atlas. Once the cluster is created, its name cannot be changed.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to create the database user.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_mongodbatlas.get_clusters">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_clusters</code><span class="sig-paren">(</span><em class="sig-param">project_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.get_clusters" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.Cluster</span></code> describes all Clusters by the provided project_id. The data source requires your Project ID.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
<p><strong>IMPORTANT:</strong>
<span class="raw-html-m2r"><br></span> &amp;#8226; Changes to cluster configurations can affect costs. Before making changes, please see <a class="reference external" href="https://docs.atlas.mongodb.com/billing/">Billing</a>.
<span class="raw-html-m2r"><br></span> &amp;#8226; If your Atlas project contains a custom role that uses actions introduced in a specific MongoDB version, you cannot create a cluster with a MongoDB version less than that version unless you delete the custom role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to get the clusters.</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_mongodbatlas.get_custom_db_role">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_custom_db_role</code><span class="sig-paren">(</span><em class="sig-param">inherited_roles=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">role_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.get_custom_db_role" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.CustomDbRole</span></code> describe a Custom DB Role. This represents a custom db role.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to create the database user.</p></li>
<li><p><strong>role_name</strong> (<em>str</em>) – Name of the custom role.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>inherited_roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">database_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the custom role.</p></li>
</ul>
</dd></dl>

<dl class="function">
<dt id="pulumi_mongodbatlas.get_custom_db_roles">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_custom_db_roles</code><span class="sig-paren">(</span><em class="sig-param">project_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.get_custom_db_roles" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.getCustomDbRoles</span></code> describe all Custom DB Roles. This represents a custom db roles.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to get all custom db roles.</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_mongodbatlas.get_database_user">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_database_user</code><span class="sig-paren">(</span><em class="sig-param">auth_database_name=None</em>, <em class="sig-param">database_name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.get_database_user" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.DatabaseUser</span></code> describe a Database User. This represents a database user which will be applied to all clusters within the project.</p>
<p>Each user has a set of roles that provide access to the project’s databases. User’s roles apply to all the clusters in the project: if two clusters have a <code class="docutils literal notranslate"><span class="pre">products</span></code> database and a user has a role granting <code class="docutils literal notranslate"><span class="pre">read</span></code> access on the products database, the user has that access on both clusters.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>auth_database_name</strong> (<em>str</em>) – The user’s authentication database. A user must provide both a username and authentication database to log into MongoDB. In Atlas deployments of MongoDB, the authentication database is almost always the admin database, for X509 it is $external.</p></li>
<li><p><strong>database_name</strong> (<em>str</em>) – Database on which the user has the specified role. A role on the <code class="docutils literal notranslate"><span class="pre">admin</span></code> database can include privileges that apply to the other databases.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to create the database user.</p></li>
<li><p><strong>username</strong> (<em>str</em>) – Username for authenticating to MongoDB.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_mongodbatlas.get_database_users">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_database_users</code><span class="sig-paren">(</span><em class="sig-param">project_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.get_database_users" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.getDatabaseUsers</span></code> describe all Database Users. This represents a database user which will be applied to all clusters within the project.</p>
<p>Each user has a set of roles that provide access to the project’s databases. User’s roles apply to all the clusters in the project: if two clusters have a <code class="docutils literal notranslate"><span class="pre">products</span></code> database and a user has a role granting <code class="docutils literal notranslate"><span class="pre">read</span></code> access on the products database, the user has that access on both clusters.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to get all database users.</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_mongodbatlas.get_global_cluster_config">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_global_cluster_config</code><span class="sig-paren">(</span><em class="sig-param">cluster_name=None</em>, <em class="sig-param">managed_namespaces=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.get_global_cluster_config" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.GlobalClusterConfig</span></code> describes all managed namespaces and custom zone mappings associated with the specified Global Cluster.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>managed_namespaces</strong> (<em>list</em>) – <p>Add a managed namespaces to a Global Cluster. For more information about managed namespaces, see <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/global-clusters/">Global Clusters</a>. See Managed Namespace below for more details.</p>
</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to create the database user.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `cluster_name - (Required) The name of the Global Cluster.
</pre></div>
</div>
<p>The <strong>managed_namespaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">collection</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - (Required) The name of the collection associated with the managed namespace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customShardKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - (Required)   The custom shard key for the collection. Global Clusters require a compound shard key consisting of a location field and a user-selected second key, the custom shard key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">db</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - (Required) The name of the database containing the collection.</p></li>
</ul>
</dd></dl>

<dl class="function">
<dt id="pulumi_mongodbatlas.get_maintenance_window">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_maintenance_window</code><span class="sig-paren">(</span><em class="sig-param">project_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.get_maintenance_window" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.MaintenanceWindow</span></code> provides a Maintenance Window entry datasource. Gets information regarding the configured maintenance window for a MongoDB Atlas project.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>project_id</strong> (<em>str</em>) – The unique identifier of the project for the Maintenance Window.</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_mongodbatlas.get_network_container">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_network_container</code><span class="sig-paren">(</span><em class="sig-param">container_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.get_network_container" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.NetworkContainer</span></code> describes a Network Peering Container. The resource requires your Project ID and container ID.</p>
<blockquote>
<div><p><strong>IMPORTANT:</strong> This resource creates one Network Peering container into which Atlas can deploy Network Peering connections. An Atlas project can have a maximum of one container for each cloud provider. You must have either the Project Owner or Organization Owner role to successfully call this endpoint.</p>
<p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <strong>group_id</strong> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>container_id</strong> (<em>str</em>) – The Network Peering Container ID.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to create the database user.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_mongodbatlas.get_network_containers">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_network_containers</code><span class="sig-paren">(</span><em class="sig-param">project_id=None</em>, <em class="sig-param">provider_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.get_network_containers" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.getNetworkContainers</span></code> describes all Network Peering Containers. The data source requires your Project ID.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <strong>group_id</strong> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to create the database user.</p></li>
<li><p><strong>provider_name</strong> (<em>str</em>) – Cloud provider for this Network peering container. Accepted values are AWS, GCP, and Azure.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_mongodbatlas.get_network_peering">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_network_peering</code><span class="sig-paren">(</span><em class="sig-param">peering_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.get_network_peering" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.NetworkPeering</span></code> describes a Network Peering Connection.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <strong>group_id</strong> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>peering_id</strong> (<em>str</em>) – Atlas assigned unique ID for the peering connection.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to create the database user.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_mongodbatlas.get_network_peerings">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_network_peerings</code><span class="sig-paren">(</span><em class="sig-param">project_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.get_network_peerings" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.getNetworkPeerings</span></code> describes all Network Peering Connections.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <strong>group_id</strong> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to create the database user.</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_mongodbatlas.get_private_endpoint">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_private_endpoint</code><span class="sig-paren">(</span><em class="sig-param">private_link_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.get_private_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.PrivateEndpoint</span></code> describe a Private Endpoint. This represents a Private Endpoint Connection to retrieve details regarding a private endpoint by id in an Atlas project</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>private_link_id</strong> (<em>str</em>) – Unique identifier of the AWS PrivateLink connection.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – Unique identifier for the project.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_mongodbatlas.get_private_endpoint_interface_link">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_private_endpoint_interface_link</code><span class="sig-paren">(</span><em class="sig-param">interface_endpoint_id=None</em>, <em class="sig-param">private_link_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.get_private_endpoint_interface_link" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">mongodbatlas_private_endpoint_link</span></code> describe a Private Endpoint Link. This represents a Private Endpoint Link Connection that wants to retrieve details in an Atlas project.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>private_link_id</strong> (<em>str</em>) – Unique identifier of the AWS PrivateLink connection.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – Unique identifier for the project.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_mongodbatlas.get_project">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_project</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.get_project" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.Project</span></code> describes a MongoDB Atlas Project. This represents a project that has been created.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The unique ID for the project.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_mongodbatlas.get_projects">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_projects</code><span class="sig-paren">(</span><em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.get_projects" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.getProjects</span></code> describe all Projects. This represents projects that have been created.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_mongodbatlas.get_team">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_team</code><span class="sig-paren">(</span><em class="sig-param">org_id=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.get_team" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">.Teams</span></code> describes a Team. The resource requires your Organization ID, Project ID and Team ID.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>org_id</strong> (<em>str</em>) – The unique identifier for the organization you want to associate the team with.</p></li>
<li><p><strong>team_id</strong> (<em>str</em>) – The unique identifier for the team.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_mongodbatlas.get_teams">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_teams</code><span class="sig-paren">(</span><em class="sig-param">org_id=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.get_teams" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

</div>
