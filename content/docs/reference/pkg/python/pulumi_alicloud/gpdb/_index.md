---
title: Module gpdb
title_tag: Module gpdb | Package pulumi_alicloud | Python SDK
linktitle: gpdb
notitle: true
---

<div class="section" id="gpdb">
<h1>gpdb<a class="headerlink" href="#gpdb" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.gpdb"></span><dl class="class">
<dt id="pulumi_alicloud.gpdb.AwaitableGetInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.gpdb.</code><code class="sig-name descname">AwaitableGetInstancesResult</code><span class="sig-paren">(</span><em class="sig-param">availability_zone=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vswitch_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.gpdb.AwaitableGetInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.gpdb.Connection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.gpdb.</code><code class="sig-name descname">Connection</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">connection_prefix=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.gpdb.Connection" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a connection resource to allocate an Internet connection string for instance.</p>
<blockquote>
<div><p><strong>NOTE:</strong>  Available in 1.48.0+</p>
<dl class="simple">
<dt><strong>NOTE:</strong> Each instance will allocate a intranet connection string automatically and its prefix is instance ID.</dt><dd><p>To avoid unnecessary conflict, please specified a internet connection prefix before applying the resource.</p>
</dd>
</dl>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/gpdb_connection.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/gpdb_connection.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Prefix of an Internet connection string. It must be checked for uniqueness. It may consist of lowercase letters, numbers, and underlines, and must start with a letter and have no more than 30 characters. Default to <span class="raw-html-m2r"><instance_id></span> + ‘-tf’.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of instance that can run database.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Internet connection port. Valid value: [3200-3999]. Default to 3306.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.gpdb.Connection.connection_prefix">
<code class="sig-name descname">connection_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.gpdb.Connection.connection_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Prefix of an Internet connection string. It must be checked for uniqueness. It may consist of lowercase letters, numbers, and underlines, and must start with a letter and have no more than 30 characters. Default to <span class="raw-html-m2r"><instance_id></span> + ‘-tf’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.gpdb.Connection.connection_string">
<code class="sig-name descname">connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.gpdb.Connection.connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>Connection instance string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.gpdb.Connection.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.gpdb.Connection.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of instance that can run database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.gpdb.Connection.ip_address">
<code class="sig-name descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.gpdb.Connection.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The ip address of connection string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.gpdb.Connection.port">
<code class="sig-name descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.gpdb.Connection.port" title="Permalink to this definition">¶</a></dt>
<dd><p>Internet connection port. Valid value: [3200-3999]. Default to 3306.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.gpdb.Connection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">connection_prefix=None</em>, <em class="sig-param">connection_string=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">port=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.gpdb.Connection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Connection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Prefix of an Internet connection string. It must be checked for uniqueness. It may consist of lowercase letters, numbers, and underlines, and must start with a letter and have no more than 30 characters. Default to <span class="raw-html-m2r"><instance_id></span> + ‘-tf’.</p></li>
<li><p><strong>connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Connection instance string.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of instance that can run database.</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ip address of connection string.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Internet connection port. Valid value: [3200-3999]. Default to 3306.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.gpdb.Connection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.gpdb.Connection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.gpdb.Connection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.gpdb.Connection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.gpdb.GetInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.gpdb.</code><code class="sig-name descname">GetInstancesResult</code><span class="sig-paren">(</span><em class="sig-param">availability_zone=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vswitch_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.gpdb.GetInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstances.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.gpdb.GetInstancesResult.availability_zone">
<code class="sig-name descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.gpdb.GetInstancesResult.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance availability zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.gpdb.GetInstancesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.gpdb.GetInstancesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.gpdb.GetInstancesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.gpdb.GetInstancesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The ids list of AnalyticDB for PostgreSQL instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.gpdb.GetInstancesResult.instances">
<code class="sig-name descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.gpdb.GetInstancesResult.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of AnalyticDB for PostgreSQL instances. Its every element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.gpdb.GetInstancesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.gpdb.GetInstancesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>The names list of AnalyticDB for PostgreSQL instance.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.gpdb.Instance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.gpdb.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">availability_zone=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">engine=None</em>, <em class="sig-param">engine_version=None</em>, <em class="sig-param">instance_charge_type=None</em>, <em class="sig-param">instance_class=None</em>, <em class="sig-param">instance_group_count=None</em>, <em class="sig-param">security_ip_lists=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vswitch_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.gpdb.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a AnalyticDB for PostgreSQL instance resource supports replica set instances only. the AnalyticDB for PostgreSQL provides stable, reliable, and automatic scalable database services. 
You can see detail product introduction <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/35387.htm">here</a></p>
<blockquote>
<div><p><strong>NOTE:</strong>  Available in 1.47.0+</p>
<p><strong>NOTE:</strong>  The following regions don’t support create Classic network Gpdb instance.
[<code class="docutils literal notranslate"><span class="pre">ap-southeast-2</span></code>,<code class="docutils literal notranslate"><span class="pre">ap-southeast-3</span></code>,<code class="docutils literal notranslate"><span class="pre">ap-southeast-5</span></code>,<code class="docutils literal notranslate"><span class="pre">ap-south-1</span></code>,<code class="docutils literal notranslate"><span class="pre">me-east-1</span></code>,<code class="docutils literal notranslate"><span class="pre">ap-northeast-1</span></code>,<code class="docutils literal notranslate"><span class="pre">eu-west-1</span></code>,<code class="docutils literal notranslate"><span class="pre">us-east-1</span></code>,<code class="docutils literal notranslate"><span class="pre">eu-central-1</span></code>,<code class="docutils literal notranslate"><span class="pre">cn-shanghai-finance-1</span></code>,<code class="docutils literal notranslate"><span class="pre">cn-shenzhen-finance-1</span></code>,<code class="docutils literal notranslate"><span class="pre">cn-hangzhou-finance</span></code>]</p>
<p><strong>NOTE:</strong>  Create instance or change instance would cost 10~15 minutes. Please make full preparation.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/gpdb_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/gpdb_instance.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of DB instance. It a string of 2 to 256 characters.</p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database version. Value options can refer to the latest docs <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/86908.htm">CreateDBInstance</a> <code class="docutils literal notranslate"><span class="pre">EngineVersion</span></code>.</p></li>
<li><p><strong>instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>,System default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>instance_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance specification. see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/86942.htm">Instance specifications</a>.</p></li>
<li><p><strong>instance_group_count</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The number of groups. Valid values: [2,4,8,16,32]</p></li>
<li><p><strong>security_ip_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The virtual switch ID to launch DB instances in one VPC.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.gpdb.Instance.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.gpdb.Instance.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of DB instance. It a string of 2 to 256 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.gpdb.Instance.engine_version">
<code class="sig-name descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.gpdb.Instance.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Database version. Value options can refer to the latest docs <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/86908.htm">CreateDBInstance</a> <code class="docutils literal notranslate"><span class="pre">EngineVersion</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.gpdb.Instance.instance_charge_type">
<code class="sig-name descname">instance_charge_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.gpdb.Instance.instance_charge_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>,System default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.gpdb.Instance.instance_class">
<code class="sig-name descname">instance_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.gpdb.Instance.instance_class" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance specification. see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/86942.htm">Instance specifications</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.gpdb.Instance.instance_group_count">
<code class="sig-name descname">instance_group_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.gpdb.Instance.instance_group_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of groups. Valid values: [2,4,8,16,32]</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.gpdb.Instance.security_ip_lists">
<code class="sig-name descname">security_ip_lists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.gpdb.Instance.security_ip_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.gpdb.Instance.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.gpdb.Instance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.gpdb.Instance.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.gpdb.Instance.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The virtual switch ID to launch DB instances in one VPC.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.gpdb.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">availability_zone=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">engine=None</em>, <em class="sig-param">engine_version=None</em>, <em class="sig-param">instance_charge_type=None</em>, <em class="sig-param">instance_class=None</em>, <em class="sig-param">instance_group_count=None</em>, <em class="sig-param">security_ip_lists=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vswitch_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.gpdb.Instance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of DB instance. It a string of 2 to 256 characters.</p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Database version. Value options can refer to the latest docs <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/86908.htm">CreateDBInstance</a> <code class="docutils literal notranslate"><span class="pre">EngineVersion</span></code>.</p>
</p></li>
<li><p><strong>instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>,System default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>instance_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Instance specification. see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/86942.htm">Instance specifications</a>.</p>
</p></li>
<li><p><strong>instance_group_count</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The number of groups. Valid values: [2,4,8,16,32]</p></li>
<li><p><strong>security_ip_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The virtual switch ID to launch DB instances in one VPC.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.gpdb.Instance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.gpdb.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.gpdb.Instance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.gpdb.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.gpdb.get_instances">
<code class="sig-prename descclassname">pulumi_alicloud.gpdb.</code><code class="sig-name descname">get_instances</code><span class="sig-paren">(</span><em class="sig-param">availability_zone=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vswitch_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.gpdb.get_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">gpdb.getInstances</span></code> data source provides a collection of AnalyticDB for PostgreSQL instances available in Alicloud account.
Filters support regular expression for the instance name or availability_zone.</p>
<blockquote>
<div><p><strong>NOTE:</strong>  Available in 1.47.0+</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/gpdb_instances.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/gpdb_instances.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>availability_zone</strong> (<em>str</em>) – Instance availability zone.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – A list of instance IDs.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to apply to the instance name.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>vswitch_id</strong> (<em>str</em>) – Used to retrieve instances belong to specified <code class="docutils literal notranslate"><span class="pre">vswitch</span></code> resources.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
