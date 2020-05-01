---
title: Module nas
title_tag: Module nas | Package pulumi_alicloud | Python SDK
linktitle: nas
notitle: true
---

<div class="section" id="nas">
<h1>nas<a class="headerlink" href="#nas" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.nas"></span><dl class="py class">
<dt id="pulumi_alicloud.nas.AccessGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.nas.</code><code class="sig-name descname">AccessGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.AccessGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Nas Access Group resource.</p>
<p>In NAS, the permission group acts as a whitelist that allows you to restrict file system access. You can allow specified IP addresses or CIDR blocks to access the file system, and assign different levels of access permission to different IP addresses or CIDR blocks by adding rules to the permission group.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.33.0+.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Access Group description.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A Name of one Access Group.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A Type of one Access Group. Valid values: <code class="docutils literal notranslate"><span class="pre">Vpc</span></code> and <code class="docutils literal notranslate"><span class="pre">Classic</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.nas.AccessGroup.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.AccessGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The Access Group description.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.AccessGroup.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.AccessGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A Name of one Access Group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.AccessGroup.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.AccessGroup.type" title="Permalink to this definition">¶</a></dt>
<dd><p>A Type of one Access Group. Valid values: <code class="docutils literal notranslate"><span class="pre">Vpc</span></code> and <code class="docutils literal notranslate"><span class="pre">Classic</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.nas.AccessGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.AccessGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Access Group description.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A Name of one Access Group.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A Type of one Access Group. Valid values: <code class="docutils literal notranslate"><span class="pre">Vpc</span></code> and <code class="docutils literal notranslate"><span class="pre">Classic</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.nas.AccessGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.AccessGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.nas.AccessGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.AccessGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.nas.AccessRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.nas.</code><code class="sig-name descname">AccessRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rw_access_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_cidr_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_access_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.AccessRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Nas Access Rule resource.</p>
<p>When NAS is activated, the Default VPC Permission Group is automatically generated. It allows all IP addresses in a VPC to access the mount point with full permissions. Full permissions include Read/Write permission with no restriction on root users.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.34.0+.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Permission group name.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Priority level. Range: 1-100. Default value: 1.</p></li>
<li><p><strong>rw_access_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Read-write permission type: RDWR (default), RDONLY.</p></li>
<li><p><strong>source_cidr_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Address or address segment.</p></li>
<li><p><strong>user_access_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User permission type: no_squash (default), root_squash, all_squash.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.nas.AccessRule.access_group_name">
<code class="sig-name descname">access_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.AccessRule.access_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Permission group name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.AccessRule.access_rule_id">
<code class="sig-name descname">access_rule_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.AccessRule.access_rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The nas access rule ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.AccessRule.priority">
<code class="sig-name descname">priority</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.AccessRule.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Priority level. Range: 1-100. Default value: 1.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.AccessRule.rw_access_type">
<code class="sig-name descname">rw_access_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.AccessRule.rw_access_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Read-write permission type: RDWR (default), RDONLY.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.AccessRule.source_cidr_ip">
<code class="sig-name descname">source_cidr_ip</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.AccessRule.source_cidr_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Address or address segment.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.AccessRule.user_access_type">
<code class="sig-name descname">user_access_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.AccessRule.user_access_type" title="Permalink to this definition">¶</a></dt>
<dd><p>User permission type: no_squash (default), root_squash, all_squash.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.nas.AccessRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_rule_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rw_access_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_cidr_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_access_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.AccessRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Permission group name.</p></li>
<li><p><strong>access_rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The nas access rule ID.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Priority level. Range: 1-100. Default value: 1.</p></li>
<li><p><strong>rw_access_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Read-write permission type: RDWR (default), RDONLY.</p></li>
<li><p><strong>source_cidr_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Address or address segment.</p></li>
<li><p><strong>user_access_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User permission type: no_squash (default), root_squash, all_squash.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.nas.AccessRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.AccessRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.nas.AccessRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.AccessRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.nas.AwaitableGetAccessGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.nas.</code><code class="sig-name descname">AwaitableGetAccessGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.AwaitableGetAccessGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.nas.AwaitableGetAccessRulesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.nas.</code><code class="sig-name descname">AwaitableGetAccessRulesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rw_access</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_cidr_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_access</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.AwaitableGetAccessRulesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.nas.AwaitableGetFileSystemsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.nas.</code><code class="sig-name descname">AwaitableGetFileSystemsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">descriptions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">systems</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.AwaitableGetFileSystemsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.nas.AwaitableGetMountTargetsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.nas.</code><code class="sig-name descname">AwaitableGetMountTargetsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mount_target_domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">targets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.AwaitableGetMountTargetsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.nas.AwaitableGetProtocolsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.nas.</code><code class="sig-name descname">AwaitableGetProtocolsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocols</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.AwaitableGetProtocolsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.nas.FileSystem">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.nas.</code><code class="sig-name descname">FileSystem</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.FileSystem" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Nas File System resource.</p>
<p>After activating NAS, you can create a file system and purchase a storage package for it in the NAS console. The NAS console also enables you to view the file system details and remove unnecessary file systems.</p>
<p>For information about NAS file system and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/27530.htm">Manage file systems</a></p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.33.0+.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The File System description.</p></li>
<li><p><strong>protocol_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Protocol Type of a File System. Valid values: <code class="docutils literal notranslate"><span class="pre">NFS</span></code> and <code class="docutils literal notranslate"><span class="pre">SMB</span></code>.</p></li>
<li><p><strong>storage_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Storage Type of a File System. Valid values: <code class="docutils literal notranslate"><span class="pre">Capacity</span></code> and <code class="docutils literal notranslate"><span class="pre">Performance</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.nas.FileSystem.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.FileSystem.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The File System description.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.FileSystem.protocol_type">
<code class="sig-name descname">protocol_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.FileSystem.protocol_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Protocol Type of a File System. Valid values: <code class="docutils literal notranslate"><span class="pre">NFS</span></code> and <code class="docutils literal notranslate"><span class="pre">SMB</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.FileSystem.storage_type">
<code class="sig-name descname">storage_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.FileSystem.storage_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Storage Type of a File System. Valid values: <code class="docutils literal notranslate"><span class="pre">Capacity</span></code> and <code class="docutils literal notranslate"><span class="pre">Performance</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.nas.FileSystem.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.FileSystem.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FileSystem resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The File System description.</p></li>
<li><p><strong>protocol_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Protocol Type of a File System. Valid values: <code class="docutils literal notranslate"><span class="pre">NFS</span></code> and <code class="docutils literal notranslate"><span class="pre">SMB</span></code>.</p></li>
<li><p><strong>storage_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Storage Type of a File System. Valid values: <code class="docutils literal notranslate"><span class="pre">Capacity</span></code> and <code class="docutils literal notranslate"><span class="pre">Performance</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.nas.FileSystem.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.FileSystem.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.nas.FileSystem.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.FileSystem.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.nas.GetAccessGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.nas.</code><code class="sig-name descname">GetAccessGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.GetAccessGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccessGroups.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetAccessGroupsResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetAccessGroupsResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Destription of the AccessGroup.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetAccessGroupsResult.groups">
<code class="sig-name descname">groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetAccessGroupsResult.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of AccessGroups. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetAccessGroupsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetAccessGroupsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetAccessGroupsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetAccessGroupsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of AccessGroup IDs, the value is set to <code class="docutils literal notranslate"><span class="pre">names</span></code> .</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetAccessGroupsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetAccessGroupsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of AccessGroup names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetAccessGroupsResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetAccessGroupsResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>AccessGroupType of the AccessGroup.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.nas.GetAccessRulesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.nas.</code><code class="sig-name descname">GetAccessRulesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rw_access</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_cidr_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_access</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.GetAccessRulesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccessRules.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetAccessRulesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetAccessRulesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetAccessRulesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetAccessRulesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of rule IDs, Each element set to <code class="docutils literal notranslate"><span class="pre">access_rule_id</span></code> (Each element formats as <code class="docutils literal notranslate"><span class="pre">&lt;access_group_name&gt;:&lt;access</span> <span class="pre">rule</span> <span class="pre">id&gt;</span></code> before 1.53.0).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetAccessRulesResult.rules">
<code class="sig-name descname">rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetAccessRulesResult.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of AccessRules. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetAccessRulesResult.rw_access">
<code class="sig-name descname">rw_access</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetAccessRulesResult.rw_access" title="Permalink to this definition">¶</a></dt>
<dd><p>RWAccess of the AccessRule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetAccessRulesResult.source_cidr_ip">
<code class="sig-name descname">source_cidr_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetAccessRulesResult.source_cidr_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>SourceCidrIp of the AccessRule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetAccessRulesResult.user_access">
<code class="sig-name descname">user_access</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetAccessRulesResult.user_access" title="Permalink to this definition">¶</a></dt>
<dd><p>UserAccess of the AccessRule</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.nas.GetFileSystemsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.nas.</code><code class="sig-name descname">GetFileSystemsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">descriptions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">systems</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.GetFileSystemsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getFileSystems.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetFileSystemsResult.descriptions">
<code class="sig-name descname">descriptions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetFileSystemsResult.descriptions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of FileSystem descriptions.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetFileSystemsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetFileSystemsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetFileSystemsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetFileSystemsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of FileSystem Id.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetFileSystemsResult.protocol_type">
<code class="sig-name descname">protocol_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetFileSystemsResult.protocol_type" title="Permalink to this definition">¶</a></dt>
<dd><p>ProtocolType block of the FileSystem</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetFileSystemsResult.storage_type">
<code class="sig-name descname">storage_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetFileSystemsResult.storage_type" title="Permalink to this definition">¶</a></dt>
<dd><p>StorageType block of the FileSystem.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetFileSystemsResult.systems">
<code class="sig-name descname">systems</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetFileSystemsResult.systems" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of VPCs. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.nas.GetMountTargetsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.nas.</code><code class="sig-name descname">GetMountTargetsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mount_target_domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">targets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.GetMountTargetsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getMountTargets.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetMountTargetsResult.access_group_name">
<code class="sig-name descname">access_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetMountTargetsResult.access_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>AccessGroup of The MountTarget.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetMountTargetsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetMountTargetsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetMountTargetsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetMountTargetsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of MountTargetDomain.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetMountTargetsResult.mount_target_domain">
<code class="sig-name descname">mount_target_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetMountTargetsResult.mount_target_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>MountTargetDomain of the MountTarget.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code>- NetworkType of The MountTarget.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetMountTargetsResult.targets">
<code class="sig-name descname">targets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetMountTargetsResult.targets" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of MountTargetDomains. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetMountTargetsResult.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetMountTargetsResult.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>VpcId of The MountTarget.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetMountTargetsResult.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetMountTargetsResult.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>VSwitchId of The MountTarget.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.nas.GetProtocolsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.nas.</code><code class="sig-name descname">GetProtocolsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocols</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.GetProtocolsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProtocols.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetProtocolsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetProtocolsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.GetProtocolsResult.protocols">
<code class="sig-name descname">protocols</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.GetProtocolsResult.protocols" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of supported protocol type..</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.nas.MountTarget">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.nas.</code><code class="sig-name descname">MountTarget</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.MountTarget" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Nas Mount Target resource.</p>
<blockquote>
<div><p>NOTE: Available in v1.34.0+.</p>
<p>NOTE: Currently this resource support create a mount point in a classic network only when current region is China mainland regions.</p>
<p>NOTE: You must grant NAS with specific RAM permissions when creating a classic mount targets,
and it only can be achieved by creating a classic mount target mannually.
See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/60431.htm">Add a mount point</a> and <a class="reference external" href="https://www.alibabacloud.com/help/faq-detail/42176.htm">Why do I need RAM permissions to create a mount point in a classic network</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Permission group name.</p></li>
<li><p><strong>file_system_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – File system ID.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether the MountTarget is active. An inactive MountTarget is inusable. Valid values are Active(default) and Inactive.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – VSwitch ID.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.nas.MountTarget.access_group_name">
<code class="sig-name descname">access_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.MountTarget.access_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Permission group name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.MountTarget.file_system_id">
<code class="sig-name descname">file_system_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.MountTarget.file_system_id" title="Permalink to this definition">¶</a></dt>
<dd><p>File system ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.MountTarget.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.MountTarget.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the MountTarget is active. An inactive MountTarget is inusable. Valid values are Active(default) and Inactive.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.nas.MountTarget.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.nas.MountTarget.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>VSwitch ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.nas.MountTarget.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.MountTarget.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MountTarget resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Permission group name.</p></li>
<li><p><strong>file_system_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – File system ID.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether the MountTarget is active. An inactive MountTarget is inusable. Valid values are Active(default) and Inactive.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – VSwitch ID.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.nas.MountTarget.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.MountTarget.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.nas.MountTarget.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.MountTarget.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.nas.get_access_groups">
<code class="sig-prename descclassname">pulumi_alicloud.nas.</code><code class="sig-name descname">get_access_groups</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.get_access_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides user-available access groups. Use when you can create mount points</p>
<blockquote>
<div><p>NOTE: Available in 1.35.0+</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description</strong> (<em>str</em>) – Filter results by a specific Description.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter AccessGroups by name.</p></li>
<li><p><strong>type</strong> (<em>str</em>) – Filter results by a specific AccessGroupType.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.nas.get_access_rules">
<code class="sig-prename descclassname">pulumi_alicloud.nas.</code><code class="sig-name descname">get_access_rules</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rw_access</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_cidr_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_access</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.get_access_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides AccessRule available to the user.</p>
<blockquote>
<div><p>NOTE: Available in 1.35.0+</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>access_group_name</strong> (<em>str</em>) – Filter results by a specific AccessGroupName.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – A list of rule IDs.</p></li>
<li><p><strong>rw_access</strong> (<em>str</em>) – Filter results by a specific RWAccess.</p></li>
<li><p><strong>source_cidr_ip</strong> (<em>str</em>) – Filter results by a specific SourceCidrIp.</p></li>
<li><p><strong>user_access</strong> (<em>str</em>) – Filter results by a specific UserAccess.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.nas.get_file_systems">
<code class="sig-prename descclassname">pulumi_alicloud.nas.</code><code class="sig-name descname">get_file_systems</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.get_file_systems" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides FileSystems available to the user.</p>
<blockquote>
<div><p>NOTE: Available in 1.35.0+</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description_regex</strong> (<em>str</em>) – A regex string to filter the results by the ：FileSystem description.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – A list of FileSystemId.</p></li>
<li><p><strong>protocol_type</strong> (<em>str</em>) – Filter results by a specific ProtocolType.</p></li>
<li><p><strong>storage_type</strong> (<em>str</em>) – Filter results by a specific StorageType.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.nas.get_mount_targets">
<code class="sig-prename descclassname">pulumi_alicloud.nas.</code><code class="sig-name descname">get_mount_targets</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_system_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mount_target_domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.get_mount_targets" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides MountTargets available to the user.</p>
<blockquote>
<div><p>NOTE: Available in 1.35.0+</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>access_group_name</strong> (<em>str</em>) – Filter results by a specific AccessGroupName.</p></li>
<li><p><strong>file_system_id</strong> (<em>str</em>) – The ID of the FileSystem that owns the MountTarget.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – A list of MountTargetDomain.</p></li>
<li><p><strong>mount_target_domain</strong> (<em>str</em>) – Filter results by a specific MountTargetDomain.</p></li>
<li><p><strong>type</strong> (<em>str</em>) – Filter results by a specific NetworkType.</p></li>
<li><p><strong>vpc_id</strong> (<em>str</em>) – Filter results by a specific VpcId.</p></li>
<li><p><strong>vswitch_id</strong> (<em>str</em>) – Filter results by a specific VSwitchId.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.nas.get_protocols">
<code class="sig-prename descclassname">pulumi_alicloud.nas.</code><code class="sig-name descname">get_protocols</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.nas.get_protocols" title="Permalink to this definition">¶</a></dt>
<dd><p>Provide  a data source to retrieve the type of protocol used to create NAS file system.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.42.0</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>type</strong> (<em>str</em>) – The file system type. Valid Values: Performance and Capacity.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>zone_id</strong> (<em>str</em>) – String to filter results by zone id.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
