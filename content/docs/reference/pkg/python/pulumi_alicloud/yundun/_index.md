---
title: Module yundun
title_tag: Module yundun | Package pulumi_alicloud | Python SDK
linktitle: yundun
notitle: true
---

<div class="section" id="yundun">
<h1>yundun<a class="headerlink" href="#yundun" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.yundun"></span><dl class="class">
<dt id="pulumi_alicloud.yundun.AwaitableGetBastionHostInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.yundun.</code><code class="sig-name descname">AwaitableGetBastionHostInstancesResult</code><span class="sig-paren">(</span><em class="sig-param">description_regex=None</em>, <em class="sig-param">descriptions=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.yundun.AwaitableGetBastionHostInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.yundun.AwaitableGetDBAuditInstanceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.yundun.</code><code class="sig-name descname">AwaitableGetDBAuditInstanceResult</code><span class="sig-paren">(</span><em class="sig-param">description_regex=None</em>, <em class="sig-param">descriptions=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.yundun.AwaitableGetDBAuditInstanceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.yundun.BastionHostInstance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.yundun.</code><code class="sig-name descname">BastionHostInstance</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">license_code=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">security_group_ids=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vswitch_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.yundun.BastionHostInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud Bastionhost instance resource (“Yundun_bastionhost” is the short term of this product).</p>
<blockquote>
<div><p><strong>NOTE:</strong> The endpoint of bssopenapi used only support “business.aliyuncs.com” at present.</p>
<p><strong>NOTE:</strong> Available in 1.63.0+ .</p>
<p><strong>NOTE:</strong> In order to destroy Cloud Bastionhost instance , users are required to apply for white list first</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the instance. This name can have a string of 1 to 63 characters.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Duration for initially producing the instance. Valid values: [1~9], 12, 24, 36. Default to 1. At present, the provider does not support modify “period”.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – security group IDs configured to bastionhost</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – vSwtich ID configured to bastionhost</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/yundun_bastionhost_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/yundun_bastionhost_instance.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_alicloud.yundun.BastionHostInstance.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.yundun.BastionHostInstance.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the instance. This name can have a string of 1 to 63 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.yundun.BastionHostInstance.period">
<code class="sig-name descname">period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.yundun.BastionHostInstance.period" title="Permalink to this definition">¶</a></dt>
<dd><p>Duration for initially producing the instance. Valid values: [1~9], 12, 24, 36. Default to 1. At present, the provider does not support modify “period”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.yundun.BastionHostInstance.security_group_ids">
<code class="sig-name descname">security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.yundun.BastionHostInstance.security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>security group IDs configured to bastionhost</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.yundun.BastionHostInstance.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.yundun.BastionHostInstance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.yundun.BastionHostInstance.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.yundun.BastionHostInstance.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>vSwtich ID configured to bastionhost</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.yundun.BastionHostInstance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">license_code=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">security_group_ids=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vswitch_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.yundun.BastionHostInstance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BastionHostInstance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the instance. This name can have a string of 1 to 63 characters.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Duration for initially producing the instance. Valid values: [1~9], 12, 24, 36. Default to 1. At present, the provider does not support modify “period”.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – security group IDs configured to bastionhost</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – vSwtich ID configured to bastionhost</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/yundun_bastionhost_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/yundun_bastionhost_instance.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.yundun.BastionHostInstance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.yundun.BastionHostInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.yundun.BastionHostInstance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.yundun.BastionHostInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.yundun.DBAuditInstance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.yundun.</code><code class="sig-name descname">DBAuditInstance</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">plan_code=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vswitch_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.yundun.DBAuditInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud DBaudit instance resource (“Yundun_dbaudit” is the short term of this product).</p>
<blockquote>
<div><p><strong>NOTE:</strong> The endpoint of bssopenapi used only support “business.aliyuncs.com” at present.</p>
<p><strong>NOTE:</strong> Available in 1.62.0+ .</p>
<p><strong>NOTE:</strong> In order to destroy Cloud DBaudit instance , users are required to apply for white list first</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the instance. This name can have a string of 1 to 63 characters.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Duration for initially producing the instance. Valid values: [1~9], 12, 24, 36. Default to 12. At present, the provider does not support modify “period”.</p></li>
<li><p><strong>plan_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Plan code of the Cloud DBAudit to produce. (alpha.professional, alpha.basic, alpha.premium)</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – vSwtich ID configured to audit</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/yundun_dbaudit_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/yundun_dbaudit_instance.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_alicloud.yundun.DBAuditInstance.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.yundun.DBAuditInstance.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the instance. This name can have a string of 1 to 63 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.yundun.DBAuditInstance.period">
<code class="sig-name descname">period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.yundun.DBAuditInstance.period" title="Permalink to this definition">¶</a></dt>
<dd><p>Duration for initially producing the instance. Valid values: [1~9], 12, 24, 36. Default to 12. At present, the provider does not support modify “period”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.yundun.DBAuditInstance.plan_code">
<code class="sig-name descname">plan_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.yundun.DBAuditInstance.plan_code" title="Permalink to this definition">¶</a></dt>
<dd><p>Plan code of the Cloud DBAudit to produce. (alpha.professional, alpha.basic, alpha.premium)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.yundun.DBAuditInstance.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.yundun.DBAuditInstance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.yundun.DBAuditInstance.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.yundun.DBAuditInstance.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>vSwtich ID configured to audit</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.yundun.DBAuditInstance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">plan_code=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vswitch_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.yundun.DBAuditInstance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DBAuditInstance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the instance. This name can have a string of 1 to 63 characters.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Duration for initially producing the instance. Valid values: [1~9], 12, 24, 36. Default to 12. At present, the provider does not support modify “period”.</p></li>
<li><p><strong>plan_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Plan code of the Cloud DBAudit to produce. (alpha.professional, alpha.basic, alpha.premium)</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – vSwtich ID configured to audit</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/yundun_dbaudit_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/yundun_dbaudit_instance.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.yundun.DBAuditInstance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.yundun.DBAuditInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.yundun.DBAuditInstance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.yundun.DBAuditInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.yundun.GetBastionHostInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.yundun.</code><code class="sig-name descname">GetBastionHostInstancesResult</code><span class="sig-paren">(</span><em class="sig-param">description_regex=None</em>, <em class="sig-param">descriptions=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.yundun.GetBastionHostInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBastionHostInstances.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.yundun.GetBastionHostInstancesResult.instances">
<code class="sig-name descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.yundun.GetBastionHostInstancesResult.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of apis. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.yundun.GetBastionHostInstancesResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.yundun.GetBastionHostInstancesResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags assigned to the bastionhost instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.yundun.GetBastionHostInstancesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.yundun.GetBastionHostInstancesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.yundun.GetDBAuditInstanceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.yundun.</code><code class="sig-name descname">GetDBAuditInstanceResult</code><span class="sig-paren">(</span><em class="sig-param">description_regex=None</em>, <em class="sig-param">descriptions=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.yundun.GetDBAuditInstanceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDBAuditInstance.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.yundun.GetDBAuditInstanceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.yundun.GetDBAuditInstanceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.yundun.get_bastion_host_instances">
<code class="sig-prename descclassname">pulumi_alicloud.yundun.</code><code class="sig-name descname">get_bastion_host_instances</code><span class="sig-paren">(</span><em class="sig-param">description_regex=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.yundun.get_bastion_host_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of cloud Bastionhost instances in an Alibaba Cloud account according to the specified filters.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.63.0+ .</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description_regex</strong> (<em>str</em>) – A regex string to filter results by the instance description.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – Matched instance IDs to filter data source result.</p></li>
<li><p><strong>output_file</strong> (<em>str</em>) – File name to persist data source output.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A map of tags assigned to the bastionhost instance. It must be in the format:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>```
data &quot;yundun.getBastionHostInstances&quot; &quot;instance&quot; {
tags = {
tagKey1 = &quot;tagValue1&quot;
}
}
```
</pre></div>
</div>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/yundun_bastionhost_instances.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/yundun_bastionhost_instances.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.yundun.get_db_audit_instance">
<code class="sig-prename descclassname">pulumi_alicloud.yundun.</code><code class="sig-name descname">get_db_audit_instance</code><span class="sig-paren">(</span><em class="sig-param">description_regex=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.yundun.get_db_audit_instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

</div>
