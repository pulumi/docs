---
title: Module dms
title_tag: Module dms | Package pulumi_alicloud | Python SDK
linktitle: dms
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "alicloud" >}}

<div class="section" id="dms">
<h1>dms<a class="headerlink" href="#dms" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.dms"></span><dl class="py class">
<dt id="pulumi_alicloud.dms.AwaitableGetEnterpriseInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.dms.</code><code class="sig-name descname">AwaitableGetEnterpriseInstancesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">env_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_alias_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_source</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">net_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tid</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dms.AwaitableGetEnterpriseInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.dms.AwaitableGetEnterpriseUsersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.dms.</code><code class="sig-name descname">AwaitableGetEnterpriseUsersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dms.AwaitableGetEnterpriseUsersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.dms.EnterpriseInstance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.dms.</code><code class="sig-name descname">EnterpriseInstance</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_link_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_user</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dba_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dba_uid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ddl_online</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ecs_instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ecs_region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">env_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">export_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_alias</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_source</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">safe_rule</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">safe_rule_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_dsql</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DMS Enterprise Instance resource.</p>
<blockquote>
<div><p><strong>NOTE:</strong> API users must first register in DMS.
<strong>NOTE:</strong> Available in 1.81.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">dms</span><span class="o">.</span><span class="n">EnterpriseInstance</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">database_password</span><span class="o">=</span><span class="s2">&quot;Yourpassword123&quot;</span><span class="p">,</span>
    <span class="n">database_user</span><span class="o">=</span><span class="s2">&quot;your_user_name&quot;</span><span class="p">,</span>
    <span class="n">dba_uid</span><span class="o">=</span><span class="s2">&quot;1182725234xxxxxxx&quot;</span><span class="p">,</span>
    <span class="n">ecs_region</span><span class="o">=</span><span class="s2">&quot;cn-shanghai&quot;</span><span class="p">,</span>
    <span class="n">env_type</span><span class="o">=</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">export_timeout</span><span class="o">=</span><span class="mi">600</span><span class="p">,</span>
    <span class="n">host</span><span class="o">=</span><span class="s2">&quot;rm-uf648hgsxxxxxx.mysql.rds.aliyuncs.com&quot;</span><span class="p">,</span>
    <span class="n">instance_alias</span><span class="o">=</span><span class="s2">&quot;your_alias_name&quot;</span><span class="p">,</span>
    <span class="n">instance_source</span><span class="o">=</span><span class="s2">&quot;RDS&quot;</span><span class="p">,</span>
    <span class="n">instance_type</span><span class="o">=</span><span class="s2">&quot;MySQL&quot;</span><span class="p">,</span>
    <span class="n">network_type</span><span class="o">=</span><span class="s2">&quot;VPC&quot;</span><span class="p">,</span>
    <span class="n">port</span><span class="o">=</span><span class="mi">3306</span><span class="p">,</span>
    <span class="n">query_timeout</span><span class="o">=</span><span class="mi">60</span><span class="p">,</span>
    <span class="n">safe_rule</span><span class="o">=</span><span class="s2">&quot;自由操作&quot;</span><span class="p">,</span>
    <span class="n">tid</span><span class="o">=</span><span class="s2">&quot;12345&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data_link_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cross-database query datalink name.</p></li>
<li><p><strong>database_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database access password.</p></li>
<li><p><strong>database_user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database access account.</p></li>
<li><p><strong>dba_uid</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The DBA of the instance is passed into the Alibaba Cloud uid of the DBA.</p></li>
<li><p><strong>ddl_online</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Whether to use online services, currently only supports MySQL and PolarDB. Valid values: <code class="docutils literal notranslate"><span class="pre">0</span></code> Not used, <code class="docutils literal notranslate"><span class="pre">1</span></code> Native online DDL priority, <code class="docutils literal notranslate"><span class="pre">2</span></code> DMS lock-free table structure change priority.</p></li>
<li><p><strong>ecs_instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ECS instance ID. The value of InstanceSource is the ECS self-built library. This value must be passed.</p></li>
<li><p><strong>ecs_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region where the instance is located. This value must be passed when the value of InstanceSource is RDS, ECS self-built library, and VPC dedicated line IDC.</p></li>
<li><p><strong>env_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Environment type. Valid values: <code class="docutils literal notranslate"><span class="pre">product</span></code> production environment, <code class="docutils literal notranslate"><span class="pre">dev</span></code> development environment, <code class="docutils literal notranslate"><span class="pre">pre</span></code> pre-release environment, <code class="docutils literal notranslate"><span class="pre">test</span></code> test environment, <code class="docutils literal notranslate"><span class="pre">sit</span></code> SIT environment, <code class="docutils literal notranslate"><span class="pre">uat</span></code> UAT environment, <code class="docutils literal notranslate"><span class="pre">pet</span></code> pressure test environment, <code class="docutils literal notranslate"><span class="pre">stag</span></code> STAG environment.</p></li>
<li><p><strong>export_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Export timeout, unit: s (seconds).</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Host address of the target database.</p></li>
<li><p><strong>instance_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance alias, to help users quickly distinguish positioning.</p></li>
<li><p><strong>instance_source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source of the database instance. Valid values: <code class="docutils literal notranslate"><span class="pre">PUBLIC_OWN</span></code>, <code class="docutils literal notranslate"><span class="pre">RDS</span></code>, <code class="docutils literal notranslate"><span class="pre">ECS_OWN</span></code>, <code class="docutils literal notranslate"><span class="pre">VPC_IDC</span></code>.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database type. Valid values: <code class="docutils literal notranslate"><span class="pre">MySQL</span></code>, <code class="docutils literal notranslate"><span class="pre">SQLServer</span></code>, <code class="docutils literal notranslate"><span class="pre">PostgreSQL</span></code>, <code class="docutils literal notranslate"><span class="pre">Oracle,</span></code> <code class="docutils literal notranslate"><span class="pre">DRDS</span></code>, <code class="docutils literal notranslate"><span class="pre">OceanBase</span></code>, <code class="docutils literal notranslate"><span class="pre">Mongo</span></code>, <code class="docutils literal notranslate"><span class="pre">Redis</span></code>.</p></li>
<li><p><strong>network_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network type. Valid values: <code class="docutils literal notranslate"><span class="pre">CLASSIC</span></code>, <code class="docutils literal notranslate"><span class="pre">VPC</span></code>.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Access port of the target database.</p></li>
<li><p><strong>query_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Query timeout time, unit: s (seconds).</p></li>
<li><p><strong>safe_rule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security rule of the instance is passed into the name of the security rule in the enterprise.</p></li>
<li><p><strong>sid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SID. This value must be passed when InstanceType is PostgreSQL or Oracle.</p></li>
<li><p><strong>tid</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The tenant ID.</p></li>
<li><p><strong>use_dsql</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Whether to enable cross-instance query. Valid values: <code class="docutils literal notranslate"><span class="pre">0</span></code> not open, <code class="docutils literal notranslate"><span class="pre">1</span></code> open.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – VPC ID. This value must be passed when the value of InstanceSource is VPC dedicated line IDC.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseInstance.data_link_name">
<code class="sig-name descname">data_link_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance.data_link_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cross-database query datalink name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseInstance.database_password">
<code class="sig-name descname">database_password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance.database_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Database access password.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseInstance.database_user">
<code class="sig-name descname">database_user</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance.database_user" title="Permalink to this definition">¶</a></dt>
<dd><p>Database access account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseInstance.dba_nick_name">
<code class="sig-name descname">dba_nick_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance.dba_nick_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance dba nickname.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseInstance.dba_uid">
<code class="sig-name descname">dba_uid</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance.dba_uid" title="Permalink to this definition">¶</a></dt>
<dd><p>The DBA of the instance is passed into the Alibaba Cloud uid of the DBA.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseInstance.ddl_online">
<code class="sig-name descname">ddl_online</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance.ddl_online" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use online services, currently only supports MySQL and PolarDB. Valid values: <code class="docutils literal notranslate"><span class="pre">0</span></code> Not used, <code class="docutils literal notranslate"><span class="pre">1</span></code> Native online DDL priority, <code class="docutils literal notranslate"><span class="pre">2</span></code> DMS lock-free table structure change priority.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseInstance.ecs_instance_id">
<code class="sig-name descname">ecs_instance_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance.ecs_instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ECS instance ID. The value of InstanceSource is the ECS self-built library. This value must be passed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseInstance.ecs_region">
<code class="sig-name descname">ecs_region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance.ecs_region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region where the instance is located. This value must be passed when the value of InstanceSource is RDS, ECS self-built library, and VPC dedicated line IDC.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseInstance.env_type">
<code class="sig-name descname">env_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance.env_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Environment type. Valid values: <code class="docutils literal notranslate"><span class="pre">product</span></code> production environment, <code class="docutils literal notranslate"><span class="pre">dev</span></code> development environment, <code class="docutils literal notranslate"><span class="pre">pre</span></code> pre-release environment, <code class="docutils literal notranslate"><span class="pre">test</span></code> test environment, <code class="docutils literal notranslate"><span class="pre">sit</span></code> SIT environment, <code class="docutils literal notranslate"><span class="pre">uat</span></code> UAT environment, <code class="docutils literal notranslate"><span class="pre">pet</span></code> pressure test environment, <code class="docutils literal notranslate"><span class="pre">stag</span></code> STAG environment.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseInstance.export_timeout">
<code class="sig-name descname">export_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance.export_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Export timeout, unit: s (seconds).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseInstance.host">
<code class="sig-name descname">host</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance.host" title="Permalink to this definition">¶</a></dt>
<dd><p>Host address of the target database.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseInstance.instance_alias">
<code class="sig-name descname">instance_alias</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance.instance_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance alias, to help users quickly distinguish positioning.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseInstance.instance_source">
<code class="sig-name descname">instance_source</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance.instance_source" title="Permalink to this definition">¶</a></dt>
<dd><p>The source of the database instance. Valid values: <code class="docutils literal notranslate"><span class="pre">PUBLIC_OWN</span></code>, <code class="docutils literal notranslate"><span class="pre">RDS</span></code>, <code class="docutils literal notranslate"><span class="pre">ECS_OWN</span></code>, <code class="docutils literal notranslate"><span class="pre">VPC_IDC</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseInstance.instance_type">
<code class="sig-name descname">instance_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Database type. Valid values: <code class="docutils literal notranslate"><span class="pre">MySQL</span></code>, <code class="docutils literal notranslate"><span class="pre">SQLServer</span></code>, <code class="docutils literal notranslate"><span class="pre">PostgreSQL</span></code>, <code class="docutils literal notranslate"><span class="pre">Oracle,</span></code> <code class="docutils literal notranslate"><span class="pre">DRDS</span></code>, <code class="docutils literal notranslate"><span class="pre">OceanBase</span></code>, <code class="docutils literal notranslate"><span class="pre">Mongo</span></code>, <code class="docutils literal notranslate"><span class="pre">Redis</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseInstance.network_type">
<code class="sig-name descname">network_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance.network_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Network type. Valid values: <code class="docutils literal notranslate"><span class="pre">CLASSIC</span></code>, <code class="docutils literal notranslate"><span class="pre">VPC</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseInstance.port">
<code class="sig-name descname">port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance.port" title="Permalink to this definition">¶</a></dt>
<dd><p>Access port of the target database.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseInstance.query_timeout">
<code class="sig-name descname">query_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance.query_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Query timeout time, unit: s (seconds).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseInstance.safe_rule">
<code class="sig-name descname">safe_rule</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance.safe_rule" title="Permalink to this definition">¶</a></dt>
<dd><p>The security rule of the instance is passed into the name of the security rule in the enterprise.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseInstance.sid">
<code class="sig-name descname">sid</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance.sid" title="Permalink to this definition">¶</a></dt>
<dd><p>The SID. This value must be passed when InstanceType is PostgreSQL or Oracle.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseInstance.state">
<code class="sig-name descname">state</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance status.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseInstance.tid">
<code class="sig-name descname">tid</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance.tid" title="Permalink to this definition">¶</a></dt>
<dd><p>The tenant ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseInstance.use_dsql">
<code class="sig-name descname">use_dsql</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance.use_dsql" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable cross-instance query. Valid values: <code class="docutils literal notranslate"><span class="pre">0</span></code> not open, <code class="docutils literal notranslate"><span class="pre">1</span></code> open.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseInstance.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>VPC ID. This value must be passed when the value of InstanceSource is VPC dedicated line IDC.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.dms.EnterpriseInstance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_link_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_user</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dba_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dba_nick_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dba_uid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ddl_online</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ecs_instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ecs_region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">env_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">export_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_alias</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_source</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">safe_rule</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">safe_rule_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_dsql</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EnterpriseInstance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data_link_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cross-database query datalink name.</p></li>
<li><p><strong>database_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database access password.</p></li>
<li><p><strong>database_user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database access account.</p></li>
<li><p><strong>dba_nick_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance dba nickname.</p></li>
<li><p><strong>dba_uid</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The DBA of the instance is passed into the Alibaba Cloud uid of the DBA.</p></li>
<li><p><strong>ddl_online</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Whether to use online services, currently only supports MySQL and PolarDB. Valid values: <code class="docutils literal notranslate"><span class="pre">0</span></code> Not used, <code class="docutils literal notranslate"><span class="pre">1</span></code> Native online DDL priority, <code class="docutils literal notranslate"><span class="pre">2</span></code> DMS lock-free table structure change priority.</p></li>
<li><p><strong>ecs_instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ECS instance ID. The value of InstanceSource is the ECS self-built library. This value must be passed.</p></li>
<li><p><strong>ecs_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region where the instance is located. This value must be passed when the value of InstanceSource is RDS, ECS self-built library, and VPC dedicated line IDC.</p></li>
<li><p><strong>env_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Environment type. Valid values: <code class="docutils literal notranslate"><span class="pre">product</span></code> production environment, <code class="docutils literal notranslate"><span class="pre">dev</span></code> development environment, <code class="docutils literal notranslate"><span class="pre">pre</span></code> pre-release environment, <code class="docutils literal notranslate"><span class="pre">test</span></code> test environment, <code class="docutils literal notranslate"><span class="pre">sit</span></code> SIT environment, <code class="docutils literal notranslate"><span class="pre">uat</span></code> UAT environment, <code class="docutils literal notranslate"><span class="pre">pet</span></code> pressure test environment, <code class="docutils literal notranslate"><span class="pre">stag</span></code> STAG environment.</p></li>
<li><p><strong>export_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Export timeout, unit: s (seconds).</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Host address of the target database.</p></li>
<li><p><strong>instance_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance alias, to help users quickly distinguish positioning.</p></li>
<li><p><strong>instance_source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source of the database instance. Valid values: <code class="docutils literal notranslate"><span class="pre">PUBLIC_OWN</span></code>, <code class="docutils literal notranslate"><span class="pre">RDS</span></code>, <code class="docutils literal notranslate"><span class="pre">ECS_OWN</span></code>, <code class="docutils literal notranslate"><span class="pre">VPC_IDC</span></code>.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database type. Valid values: <code class="docutils literal notranslate"><span class="pre">MySQL</span></code>, <code class="docutils literal notranslate"><span class="pre">SQLServer</span></code>, <code class="docutils literal notranslate"><span class="pre">PostgreSQL</span></code>, <code class="docutils literal notranslate"><span class="pre">Oracle,</span></code> <code class="docutils literal notranslate"><span class="pre">DRDS</span></code>, <code class="docutils literal notranslate"><span class="pre">OceanBase</span></code>, <code class="docutils literal notranslate"><span class="pre">Mongo</span></code>, <code class="docutils literal notranslate"><span class="pre">Redis</span></code>.</p></li>
<li><p><strong>network_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network type. Valid values: <code class="docutils literal notranslate"><span class="pre">CLASSIC</span></code>, <code class="docutils literal notranslate"><span class="pre">VPC</span></code>.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Access port of the target database.</p></li>
<li><p><strong>query_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Query timeout time, unit: s (seconds).</p></li>
<li><p><strong>safe_rule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security rule of the instance is passed into the name of the security rule in the enterprise.</p></li>
<li><p><strong>sid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SID. This value must be passed when InstanceType is PostgreSQL or Oracle.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance status.</p></li>
<li><p><strong>tid</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The tenant ID.</p></li>
<li><p><strong>use_dsql</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Whether to enable cross-instance query. Valid values: <code class="docutils literal notranslate"><span class="pre">0</span></code> not open, <code class="docutils literal notranslate"><span class="pre">1</span></code> open.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – VPC ID. This value must be passed when the value of InstanceSource is VPC dedicated line IDC.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.dms.EnterpriseInstance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.dms.EnterpriseInstance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.dms.EnterpriseUser">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.dms.</code><code class="sig-name descname">EnterpriseUser</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_execute_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_result_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mobile</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nick_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">uid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseUser" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DMS Enterprise User resource. For information about Alidms Enterprise User and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/98001.htm">What is Resource Alidms Enterprise User</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.90.0+.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>max_execute_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum number of inquiries on the day.</p></li>
<li><p><strong>max_result_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Query the maximum number of rows on the day.</p></li>
<li><p><strong>mobile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DingTalk number or mobile number of the user.</p></li>
<li><p><strong>nick_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The nickname of the user.</p></li>
<li><p><strong>role_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The roles that the user plays.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The state of DMS Enterprise User. Valid values: <code class="docutils literal notranslate"><span class="pre">NORMAL</span></code>, <code class="docutils literal notranslate"><span class="pre">DISABLE</span></code>.</p></li>
<li><p><strong>tid</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The tenant ID.</p></li>
<li><p><strong>uid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Alibaba Cloud unique ID (UID) of the user to add.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseUser.max_execute_count">
<code class="sig-name descname">max_execute_count</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseUser.max_execute_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum number of inquiries on the day.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseUser.max_result_count">
<code class="sig-name descname">max_result_count</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseUser.max_result_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Query the maximum number of rows on the day.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseUser.mobile">
<code class="sig-name descname">mobile</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseUser.mobile" title="Permalink to this definition">¶</a></dt>
<dd><p>The DingTalk number or mobile number of the user.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseUser.nick_name">
<code class="sig-name descname">nick_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseUser.nick_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The nickname of the user.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseUser.role_names">
<code class="sig-name descname">role_names</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseUser.role_names" title="Permalink to this definition">¶</a></dt>
<dd><p>The roles that the user plays.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseUser.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseUser.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of DMS Enterprise User. Valid values: <code class="docutils literal notranslate"><span class="pre">NORMAL</span></code>, <code class="docutils literal notranslate"><span class="pre">DISABLE</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseUser.tid">
<code class="sig-name descname">tid</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseUser.tid" title="Permalink to this definition">¶</a></dt>
<dd><p>The tenant ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.EnterpriseUser.uid">
<code class="sig-name descname">uid</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseUser.uid" title="Permalink to this definition">¶</a></dt>
<dd><p>The Alibaba Cloud unique ID (UID) of the user to add.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.dms.EnterpriseUser.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_execute_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_result_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mobile</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nick_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">uid</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseUser.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EnterpriseUser resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>max_execute_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum number of inquiries on the day.</p></li>
<li><p><strong>max_result_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Query the maximum number of rows on the day.</p></li>
<li><p><strong>mobile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DingTalk number or mobile number of the user.</p></li>
<li><p><strong>nick_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The nickname of the user.</p></li>
<li><p><strong>role_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The roles that the user plays.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The state of DMS Enterprise User. Valid values: <code class="docutils literal notranslate"><span class="pre">NORMAL</span></code>, <code class="docutils literal notranslate"><span class="pre">DISABLE</span></code>.</p></li>
<li><p><strong>tid</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The tenant ID.</p></li>
<li><p><strong>uid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Alibaba Cloud unique ID (UID) of the user to add.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.dms.EnterpriseUser.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseUser.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.dms.EnterpriseUser.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dms.EnterpriseUser.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.dms.GetEnterpriseInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.dms.</code><code class="sig-name descname">GetEnterpriseInstancesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">env_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_alias_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_source</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">net_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tid</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dms.GetEnterpriseInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getEnterpriseInstances.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.dms.GetEnterpriseInstancesResult.env_type">
<code class="sig-name descname">env_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.GetEnterpriseInstancesResult.env_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the environment to which the database instance belongs..</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.GetEnterpriseInstancesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.GetEnterpriseInstancesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.GetEnterpriseInstancesResult.instance_source">
<code class="sig-name descname">instance_source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.GetEnterpriseInstancesResult.instance_source" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the database instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.GetEnterpriseInstancesResult.instance_type">
<code class="sig-name descname">instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.GetEnterpriseInstancesResult.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the database instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.GetEnterpriseInstancesResult.instances">
<code class="sig-name descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.GetEnterpriseInstancesResult.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of KMS keys. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.GetEnterpriseInstancesResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.GetEnterpriseInstancesResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the database instance.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.dms.GetEnterpriseUsersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.dms.</code><code class="sig-name descname">GetEnterpriseUsersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dms.GetEnterpriseUsersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getEnterpriseUsers.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.dms.GetEnterpriseUsersResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.GetEnterpriseUsersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.GetEnterpriseUsersResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.GetEnterpriseUsersResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of DMS Enterprise User IDs (UID).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.GetEnterpriseUsersResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.GetEnterpriseUsersResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the user.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.dms.GetEnterpriseUsersResult.users">
<code class="sig-name descname">users</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dms.GetEnterpriseUsersResult.users" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of DMS Enterprise Users. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.dms.get_enterprise_instances">
<code class="sig-prename descclassname">pulumi_alicloud.dms.</code><code class="sig-name descname">get_enterprise_instances</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">env_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_alias_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_source</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">net_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dms.get_enterprise_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of DMS Enterprise Instances in an Alibaba Cloud account according to the specified filters.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.88.0+</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>env_type</strong> (<em>str</em>) – The type of the environment to which the database instance belongs.</p></li>
<li><p><strong>instance_alias_regex</strong> (<em>str</em>) – A regex string to filter the results by the DMS Enterprise Instance instance_alias.</p></li>
<li><p><strong>instance_source</strong> (<em>str</em>) – The source of the database instance.</p></li>
<li><p><strong>instance_type</strong> (<em>str</em>) – The ID of the database instance.</p></li>
<li><p><strong>net_type</strong> (<em>str</em>) – The network type of the database instance. Valid values: CLASSIC and VPC. For more information about the valid values, see the description of the RegisterInstance operation.</p></li>
<li><p><strong>search_key</strong> (<em>str</em>) – The keyword used to query database instances.</p></li>
<li><p><strong>status</strong> (<em>str</em>) – Filter the results by status of the DMS Enterprise Instances. Valid values: <code class="docutils literal notranslate"><span class="pre">NORMAL</span></code>, <code class="docutils literal notranslate"><span class="pre">UNAVAILABLE</span></code>, <code class="docutils literal notranslate"><span class="pre">UNKNOWN</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETED</span></code>, <code class="docutils literal notranslate"><span class="pre">DISABLE</span></code>.</p></li>
<li><p><strong>tid</strong> (<em>float</em>) – The ID of the tenant in Data Management (DMS) Enterprise.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.dms.get_enterprise_users">
<code class="sig-prename descclassname">pulumi_alicloud.dms.</code><code class="sig-name descname">get_enterprise_users</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dms.get_enterprise_users" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of DMS Enterprise Users in an Alibaba Cloud account according to the specified filters.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.90.0+</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of DMS Enterprise User IDs (UID).</p></li>
<li><p><strong>role</strong> (<em>str</em>) – The role of the user to query.</p></li>
<li><p><strong>search_key</strong> (<em>str</em>) – The keyword used to query users.</p></li>
<li><p><strong>status</strong> (<em>str</em>) – The status of the user.</p></li>
<li><p><strong>tid</strong> (<em>float</em>) – The ID of the tenant in DMS Enterprise.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
