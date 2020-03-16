---
title: Module rocketmq
title_tag: Module rocketmq | Package pulumi_alicloud | Python SDK
linktitle: rocketmq
notitle: true
---

<div class="section" id="rocketmq">
<h1>rocketmq<a class="headerlink" href="#rocketmq" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.rocketmq"></span><dl class="class">
<dt id="pulumi_alicloud.rocketmq.Acl">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rocketmq.</code><code class="sig-name descname">Acl</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.Acl" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Sag Acl resource. Smart Access Gateway (SAG) provides the access control list (ACL) function in the form of whitelists and blacklists for different SAG instances.</p>
<p>For information about Sag Acl and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/111518.htm">What is access control list (ACL)</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.60.0+</p>
<p><strong>NOTE:</strong> Only the following regions support create Cloud Connect Network. [<code class="docutils literal notranslate"><span class="pre">cn-shanghai</span></code>, <code class="docutils literal notranslate"><span class="pre">cn-shanghai-finance-1</span></code>, <code class="docutils literal notranslate"><span class="pre">cn-hongkong</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-1</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-2</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-3</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-5</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-northeast-1</span></code>, <code class="docutils literal notranslate"><span class="pre">eu-central-1</span></code>]</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/sag_acl.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/sag_acl.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ACL instance. The name can contain 2 to 128 characters including a-z, A-Z, 0-9, periods, underlines, and hyphens. The name must start with an English letter, but cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.Acl.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.Acl.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ACL instance. The name can contain 2 to 128 characters including a-z, A-Z, 0-9, periods, underlines, and hyphens. The name must start with an English letter, but cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.rocketmq.Acl.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.Acl.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Acl resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ACL instance. The name can contain 2 to 128 characters including a-z, A-Z, 0-9, periods, underlines, and hyphens. The name must start with an English letter, but cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.rocketmq.Acl.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.Acl.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rocketmq.Acl.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.Acl.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rocketmq.AclRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rocketmq.</code><code class="sig-name descname">AclRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acl_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dest_cidr=None</em>, <em class="sig-param">dest_port_range=None</em>, <em class="sig-param">direction=None</em>, <em class="sig-param">ip_protocol=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">source_cidr=None</em>, <em class="sig-param">source_port_range=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.AclRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Sag Acl Rule resource. This topic describes how to configure an access control list (ACL) rule for a target Smart Access Gateway instance to permit or deny access to or from specified IP addresses in the ACL rule.</p>
<p>For information about Sag Acl Rule and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/111483.htm">What is access control list (ACL) rule</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.60.0+</p>
<p><strong>NOTE:</strong> Only the following regions support create Cloud Connect Network. [<code class="docutils literal notranslate"><span class="pre">cn-shanghai</span></code>, <code class="docutils literal notranslate"><span class="pre">cn-shanghai-finance-1</span></code>, <code class="docutils literal notranslate"><span class="pre">cn-hongkong</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-1</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-2</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-3</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-5</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-northeast-1</span></code>, <code class="docutils literal notranslate"><span class="pre">eu-central-1</span></code>]</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/sag_acl_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/sag_acl_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the ACL.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the ACL rule. It must be 1 to 512 characters in length.</p></li>
<li><p><strong>dest_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination address. It is an IPv4 address range in CIDR format. Default value: 0.0.0.0/0.</p></li>
<li><p><strong>dest_port_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The range of the destination port. Valid value: 80/80.</p></li>
<li><p><strong>direction</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The direction of the ACL rule. Valid values: in|out.</p></li>
<li><p><strong>ip_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol used by the ACL rule. The value is not case sensitive.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy used by the ACL rule. Valid values: accept|drop.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the ACL rule. Value range: 1 to 100.</p></li>
<li><p><strong>source_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source address. It is an IPv4 address range in the CIDR format. Default value: 0.0.0.0/0.</p></li>
<li><p><strong>source_port_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The range of the source port. Valid value: 80/80.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.AclRule.acl_id">
<code class="sig-name descname">acl_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.AclRule.acl_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the ACL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.AclRule.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.AclRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the ACL rule. It must be 1 to 512 characters in length.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.AclRule.dest_cidr">
<code class="sig-name descname">dest_cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.AclRule.dest_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination address. It is an IPv4 address range in CIDR format. Default value: 0.0.0.0/0.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.AclRule.dest_port_range">
<code class="sig-name descname">dest_port_range</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.AclRule.dest_port_range" title="Permalink to this definition">¶</a></dt>
<dd><p>The range of the destination port. Valid value: 80/80.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.AclRule.direction">
<code class="sig-name descname">direction</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.AclRule.direction" title="Permalink to this definition">¶</a></dt>
<dd><p>The direction of the ACL rule. Valid values: in|out.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.AclRule.ip_protocol">
<code class="sig-name descname">ip_protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.AclRule.ip_protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol used by the ACL rule. The value is not case sensitive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.AclRule.policy">
<code class="sig-name descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.AclRule.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy used by the ACL rule. Valid values: accept|drop.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.AclRule.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.AclRule.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the ACL rule. Value range: 1 to 100.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.AclRule.source_cidr">
<code class="sig-name descname">source_cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.AclRule.source_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>The source address. It is an IPv4 address range in the CIDR format. Default value: 0.0.0.0/0.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.AclRule.source_port_range">
<code class="sig-name descname">source_port_range</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.AclRule.source_port_range" title="Permalink to this definition">¶</a></dt>
<dd><p>The range of the source port. Valid value: 80/80.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.rocketmq.AclRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acl_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dest_cidr=None</em>, <em class="sig-param">dest_port_range=None</em>, <em class="sig-param">direction=None</em>, <em class="sig-param">ip_protocol=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">source_cidr=None</em>, <em class="sig-param">source_port_range=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.AclRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AclRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the ACL.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the ACL rule. It must be 1 to 512 characters in length.</p></li>
<li><p><strong>dest_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination address. It is an IPv4 address range in CIDR format. Default value: 0.0.0.0/0.</p></li>
<li><p><strong>dest_port_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The range of the destination port. Valid value: 80/80.</p></li>
<li><p><strong>direction</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The direction of the ACL rule. Valid values: in|out.</p></li>
<li><p><strong>ip_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol used by the ACL rule. The value is not case sensitive.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy used by the ACL rule. Valid values: accept|drop.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the ACL rule. Value range: 1 to 100.</p></li>
<li><p><strong>source_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source address. It is an IPv4 address range in the CIDR format. Default value: 0.0.0.0/0.</p></li>
<li><p><strong>source_port_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The range of the source port. Valid value: 80/80.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.rocketmq.AclRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.AclRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rocketmq.AclRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.AclRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rocketmq.AwaitableGetGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rocketmq.</code><code class="sig-name descname">AwaitableGetGroupsResult</code><span class="sig-paren">(</span><em class="sig-param">group_id_regex=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">output_file=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.AwaitableGetGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.rocketmq.AwaitableGetInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rocketmq.</code><code class="sig-name descname">AwaitableGetInstancesResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.AwaitableGetInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.rocketmq.AwaitableGetTopicsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rocketmq.</code><code class="sig-name descname">AwaitableGetTopicsResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">topics=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.AwaitableGetTopicsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.rocketmq.ClientUser">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rocketmq.</code><code class="sig-name descname">ClientUser</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bandwidth=None</em>, <em class="sig-param">client_ip=None</em>, <em class="sig-param">kms_encrypted_password=None</em>, <em class="sig-param">kms_encryption_context=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">sag_id=None</em>, <em class="sig-param">user_mail=None</em>, <em class="sig-param">user_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.ClientUser" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Sag ClientUser resource. This topic describes how to manage accounts as an administrator. After you configure the network, you can create multiple accounts and distribute them to end users so that clients can access Alibaba Cloud.</p>
<p>For information about Sag ClientUser and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/108326.htm">What is Sag ClientUser</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.65.0+</p>
<p><strong>NOTE:</strong> Only the following regions support. [<code class="docutils literal notranslate"><span class="pre">cn-shanghai</span></code>, <code class="docutils literal notranslate"><span class="pre">cn-shanghai-finance-1</span></code>, <code class="docutils literal notranslate"><span class="pre">cn-hongkong</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-1</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-2</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-3</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-5</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-northeast-1</span></code>, <code class="docutils literal notranslate"><span class="pre">eu-central-1</span></code>]</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/sag_client_user.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/sag_client_user.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The SAG APP bandwidth that the user can use. Unit: Kbit/s. Maximum value: 2000 Kbit/s.</p></li>
<li><p><strong>client_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address of the SAG APP. If you specify this parameter, the current account always uses the specified IP address.Note The IP address must be in the private CIDR block of the SAG client.If you do not specify this parameter, the system automatically allocates an IP address from the private CIDR block of the SAG client. In this case, each re-connection uses a different IP address.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password used to log on to the SAG APP.Both the user name and the password must be specified. If you specify the user name, the password must be specified, too.</p></li>
<li><p><strong>sag_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the SAG instance created for the SAG APP.</p></li>
<li><p><strong>user_mail</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address of the user. The administrator uses this address to send the account information for logging on to the APP to the user.</p></li>
<li><p><strong>user_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user name. User names in the same SAG APP must be unique.Both the user name and the password must be specified. If you specify the user name, the password must be specified, too.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.ClientUser.bandwidth">
<code class="sig-name descname">bandwidth</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.ClientUser.bandwidth" title="Permalink to this definition">¶</a></dt>
<dd><p>The SAG APP bandwidth that the user can use. Unit: Kbit/s. Maximum value: 2000 Kbit/s.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.ClientUser.client_ip">
<code class="sig-name descname">client_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.ClientUser.client_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address of the SAG APP. If you specify this parameter, the current account always uses the specified IP address.Note The IP address must be in the private CIDR block of the SAG client.If you do not specify this parameter, the system automatically allocates an IP address from the private CIDR block of the SAG client. In this case, each re-connection uses a different IP address.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.ClientUser.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.ClientUser.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password used to log on to the SAG APP.Both the user name and the password must be specified. If you specify the user name, the password must be specified, too.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.ClientUser.sag_id">
<code class="sig-name descname">sag_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.ClientUser.sag_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the SAG instance created for the SAG APP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.ClientUser.user_mail">
<code class="sig-name descname">user_mail</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.ClientUser.user_mail" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address of the user. The administrator uses this address to send the account information for logging on to the APP to the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.ClientUser.user_name">
<code class="sig-name descname">user_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.ClientUser.user_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The user name. User names in the same SAG APP must be unique.Both the user name and the password must be specified. If you specify the user name, the password must be specified, too.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.rocketmq.ClientUser.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bandwidth=None</em>, <em class="sig-param">client_ip=None</em>, <em class="sig-param">kms_encrypted_password=None</em>, <em class="sig-param">kms_encryption_context=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">sag_id=None</em>, <em class="sig-param">user_mail=None</em>, <em class="sig-param">user_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.ClientUser.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ClientUser resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The SAG APP bandwidth that the user can use. Unit: Kbit/s. Maximum value: 2000 Kbit/s.</p></li>
<li><p><strong>client_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address of the SAG APP. If you specify this parameter, the current account always uses the specified IP address.Note The IP address must be in the private CIDR block of the SAG client.If you do not specify this parameter, the system automatically allocates an IP address from the private CIDR block of the SAG client. In this case, each re-connection uses a different IP address.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password used to log on to the SAG APP.Both the user name and the password must be specified. If you specify the user name, the password must be specified, too.</p></li>
<li><p><strong>sag_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the SAG instance created for the SAG APP.</p></li>
<li><p><strong>user_mail</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address of the user. The administrator uses this address to send the account information for logging on to the APP to the user.</p></li>
<li><p><strong>user_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user name. User names in the same SAG APP must be unique.Both the user name and the password must be specified. If you specify the user name, the password must be specified, too.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.rocketmq.ClientUser.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.ClientUser.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rocketmq.ClientUser.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.ClientUser.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rocketmq.DnatEntry">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rocketmq.</code><code class="sig-name descname">DnatEntry</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">external_ip=None</em>, <em class="sig-param">external_port=None</em>, <em class="sig-param">internal_ip=None</em>, <em class="sig-param">internal_port=None</em>, <em class="sig-param">ip_protocol=None</em>, <em class="sig-param">sag_id=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.DnatEntry" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Sag DnatEntry resource. This topic describes how to add a DNAT entry to a Smart Access Gateway (SAG) instance to enable the DNAT function. By using the DNAT function, you can forward requests received by public IP addresses to Alibaba Cloud instances according to custom mapping rules.</p>
<p>For information about Sag DnatEntry and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/124312.htm">What is Sag DnatEntry</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.63.0+</p>
<p><strong>NOTE:</strong> Only the following regions suppor. [<code class="docutils literal notranslate"><span class="pre">cn-shanghai</span></code>, <code class="docutils literal notranslate"><span class="pre">cn-shanghai-finance-1</span></code>, <code class="docutils literal notranslate"><span class="pre">cn-hongkong</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-1</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-2</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-3</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-5</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-northeast-1</span></code>, <code class="docutils literal notranslate"><span class="pre">eu-central-1</span></code>]</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/sag_dnat_entry.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/sag_dnat_entry.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>external_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The external public IP address.when “type” is “Internet”,automatically identify the external ip.</p></li>
<li><p><strong>external_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public port.Value range: 1 to 65535 or “any”.</p></li>
<li><p><strong>internal_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination private IP address.</p></li>
<li><p><strong>internal_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination private port.Value range: 1 to 65535 or “any”.</p></li>
<li><p><strong>ip_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol type. Valid values: TCP: Forwards packets of the TCP protocol. UDP: Forwards packets of the UDP protocol. Any: Forwards packets of all protocols.</p></li>
<li><p><strong>sag_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the SAG instance.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNAT type. Valid values: Intranet: DNAT of private IP addresses. Internet: DNAT of public IP addresses</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.DnatEntry.external_ip">
<code class="sig-name descname">external_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.DnatEntry.external_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The external public IP address.when “type” is “Internet”,automatically identify the external ip.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.DnatEntry.external_port">
<code class="sig-name descname">external_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.DnatEntry.external_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The public port.Value range: 1 to 65535 or “any”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.DnatEntry.internal_ip">
<code class="sig-name descname">internal_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.DnatEntry.internal_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination private IP address.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.DnatEntry.internal_port">
<code class="sig-name descname">internal_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.DnatEntry.internal_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination private port.Value range: 1 to 65535 or “any”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.DnatEntry.ip_protocol">
<code class="sig-name descname">ip_protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.DnatEntry.ip_protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol type. Valid values: TCP: Forwards packets of the TCP protocol. UDP: Forwards packets of the UDP protocol. Any: Forwards packets of all protocols.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.DnatEntry.sag_id">
<code class="sig-name descname">sag_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.DnatEntry.sag_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the SAG instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.DnatEntry.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.DnatEntry.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNAT type. Valid values: Intranet: DNAT of private IP addresses. Internet: DNAT of public IP addresses</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.rocketmq.DnatEntry.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">external_ip=None</em>, <em class="sig-param">external_port=None</em>, <em class="sig-param">internal_ip=None</em>, <em class="sig-param">internal_port=None</em>, <em class="sig-param">ip_protocol=None</em>, <em class="sig-param">sag_id=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.DnatEntry.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DnatEntry resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>external_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The external public IP address.when “type” is “Internet”,automatically identify the external ip.</p></li>
<li><p><strong>external_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public port.Value range: 1 to 65535 or “any”.</p></li>
<li><p><strong>internal_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination private IP address.</p></li>
<li><p><strong>internal_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination private port.Value range: 1 to 65535 or “any”.</p></li>
<li><p><strong>ip_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol type. Valid values: TCP: Forwards packets of the TCP protocol. UDP: Forwards packets of the UDP protocol. Any: Forwards packets of all protocols.</p></li>
<li><p><strong>sag_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the SAG instance.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNAT type. Valid values: Intranet: DNAT of private IP addresses. Internet: DNAT of public IP addresses</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.rocketmq.DnatEntry.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.DnatEntry.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rocketmq.DnatEntry.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.DnatEntry.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rocketmq.GetGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rocketmq.</code><code class="sig-name descname">GetGroupsResult</code><span class="sig-paren">(</span><em class="sig-param">group_id_regex=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">output_file=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.GetGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroups.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.GetGroupsResult.groups">
<code class="sig-name descname">groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.GetGroupsResult.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of groups. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.GetGroupsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.GetGroupsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.GetGroupsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.GetGroupsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of group names.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.rocketmq.GetInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rocketmq.</code><code class="sig-name descname">GetInstancesResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.GetInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstances.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.GetInstancesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.GetInstancesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.GetInstancesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.GetInstancesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of instance IDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.GetInstancesResult.instances">
<code class="sig-name descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.GetInstancesResult.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of instances. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.GetInstancesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.GetInstancesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of instance names.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.rocketmq.GetTopicsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rocketmq.</code><code class="sig-name descname">GetTopicsResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">topics=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.GetTopicsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTopics.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.GetTopicsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.GetTopicsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.GetTopicsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.GetTopicsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of topic names.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.GetTopicsResult.topics">
<code class="sig-name descname">topics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.GetTopicsResult.topics" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of topics. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.rocketmq.Group">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rocketmq.</code><code class="sig-name descname">Group</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">read_enable=None</em>, <em class="sig-param">remark=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an ONS group resource.</p>
<p>For more information about how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/29616.html">RocketMQ Group Management API</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.53.0+</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/ons_group.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/ons_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the group. Two groups on a single instance cannot have the same name. A <code class="docutils literal notranslate"><span class="pre">group_id</span></code> starts with “GID<em>” or “GID-“, and contains letters, numbers, hyphens (-), and underscores (</em>).</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the ONS Instance that owns the groups.</p></li>
<li><p><strong>read_enable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This attribute is used to set the message reading enabled or disabled. It can only be set after the group is used by the client.</p></li>
<li><p><strong>remark</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This attribute is a concise description of group. The length cannot exceed 256.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.Group.group_id">
<code class="sig-name descname">group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.Group.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the group. Two groups on a single instance cannot have the same name. A <code class="docutils literal notranslate"><span class="pre">group_id</span></code> starts with “GID<em>” or “GID-“, and contains letters, numbers, hyphens (-), and underscores (</em>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.Group.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.Group.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the ONS Instance that owns the groups.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.Group.read_enable">
<code class="sig-name descname">read_enable</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.Group.read_enable" title="Permalink to this definition">¶</a></dt>
<dd><p>This attribute is used to set the message reading enabled or disabled. It can only be set after the group is used by the client.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.Group.remark">
<code class="sig-name descname">remark</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.Group.remark" title="Permalink to this definition">¶</a></dt>
<dd><p>This attribute is a concise description of group. The length cannot exceed 256.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.rocketmq.Group.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">read_enable=None</em>, <em class="sig-param">remark=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.Group.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Group resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the group. Two groups on a single instance cannot have the same name. A <code class="docutils literal notranslate"><span class="pre">group_id</span></code> starts with “GID<em>” or “GID-“, and contains letters, numbers, hyphens (-), and underscores (</em>).</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the ONS Instance that owns the groups.</p></li>
<li><p><strong>read_enable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This attribute is used to set the message reading enabled or disabled. It can only be set after the group is used by the client.</p></li>
<li><p><strong>remark</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This attribute is a concise description of group. The length cannot exceed 256.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.rocketmq.Group.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rocketmq.Group.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rocketmq.Instance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rocketmq.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">remark=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an ONS instance resource.</p>
<p>For more information about how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/106354.html">RocketMQ Instance Management API</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> The number of instances in the same region cannot exceed 8. At present, the resource does not support region “mq-internet-access” and “ap-southeast-5”.</p>
<p><strong>NOTE:</strong> Available in 1.51.0+</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/ons_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/ons_instance.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Two instances on a single account in the same region cannot have the same name. The length must be 3 to 64 characters. Chinese characters, English letters digits and hyphen are allowed.</p></li>
<li><p><strong>remark</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This attribute is a concise description of instance. The length cannot exceed 128.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.Instance.instance_status">
<code class="sig-name descname">instance_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.Instance.instance_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of instance. 1 represents the platinum edition instance is in deployment. 2 represents the postpaid edition instance are overdue. 5 represents the postpaid or platinum edition instance is in service. 7 represents the platinum version instance is in upgrade and the service is available.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.Instance.instance_type">
<code class="sig-name descname">instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.Instance.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The edition of instance. 1 represents the postPaid edition, and 2 represents the platinum edition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.Instance.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.Instance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Two instances on a single account in the same region cannot have the same name. The length must be 3 to 64 characters. Chinese characters, English letters digits and hyphen are allowed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.Instance.release_time">
<code class="sig-name descname">release_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.Instance.release_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Platinum edition instance expiration time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.Instance.remark">
<code class="sig-name descname">remark</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.Instance.remark" title="Permalink to this definition">¶</a></dt>
<dd><p>This attribute is a concise description of instance. The length cannot exceed 128.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.rocketmq.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">instance_status=None</em>, <em class="sig-param">instance_type=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">release_time=None</em>, <em class="sig-param">remark=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.Instance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_status</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The status of instance. 1 represents the platinum edition instance is in deployment. 2 represents the postpaid edition instance are overdue. 5 represents the postpaid or platinum edition instance is in service. 7 represents the platinum version instance is in upgrade and the service is available.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The edition of instance. 1 represents the postPaid edition, and 2 represents the platinum edition.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Two instances on a single account in the same region cannot have the same name. The length must be 3 to 64 characters. Chinese characters, English letters digits and hyphen are allowed.</p></li>
<li><p><strong>release_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Platinum edition instance expiration time.</p></li>
<li><p><strong>remark</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This attribute is a concise description of instance. The length cannot exceed 128.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.rocketmq.Instance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rocketmq.Instance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rocketmq.Qos">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rocketmq.</code><code class="sig-name descname">Qos</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.Qos" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Sag Qos resource. Smart Access Gateway (SAG) supports quintuple-based QoS functions to differentiate traffic of different services and ensure high-priority traffic bandwidth.</p>
<p>For information about Sag Qos and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/131306.htm">What is Qos</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.60.0+</p>
<p><strong>NOTE:</strong> Only the following regions support. [<code class="docutils literal notranslate"><span class="pre">cn-shanghai</span></code>, <code class="docutils literal notranslate"><span class="pre">cn-shanghai-finance-1</span></code>, <code class="docutils literal notranslate"><span class="pre">cn-hongkong</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-1</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-2</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-3</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-5</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-northeast-1</span></code>, <code class="docutils literal notranslate"><span class="pre">eu-central-1</span></code>]</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/sag_qos.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/sag_qos.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the QoS policy to be created. The name can contain 2 to 128 characters including a-z, A-Z, 0-9, periods, underlines, and hyphens. The name must start with an English letter, but cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.Qos.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.Qos.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the QoS policy to be created. The name can contain 2 to 128 characters including a-z, A-Z, 0-9, periods, underlines, and hyphens. The name must start with an English letter, but cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.rocketmq.Qos.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.Qos.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Qos resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the QoS policy to be created. The name can contain 2 to 128 characters including a-z, A-Z, 0-9, periods, underlines, and hyphens. The name must start with an English letter, but cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.rocketmq.Qos.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.Qos.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rocketmq.Qos.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.Qos.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rocketmq.QosCar">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rocketmq.</code><code class="sig-name descname">QosCar</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">limit_type=None</em>, <em class="sig-param">max_bandwidth_abs=None</em>, <em class="sig-param">max_bandwidth_percent=None</em>, <em class="sig-param">min_bandwidth_abs=None</em>, <em class="sig-param">min_bandwidth_percent=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">percent_source_type=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">qos_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosCar" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Sag qos car resource. 
You need to create a QoS car to set priorities, rate limits, and quintuple rules for different messages.</p>
<p>For information about Sag Qos Car and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/140065.htm">What is Qos Car</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.60.0+</p>
<p><strong>NOTE:</strong> Only the following regions support. [<code class="docutils literal notranslate"><span class="pre">cn-shanghai</span></code>, <code class="docutils literal notranslate"><span class="pre">cn-shanghai-finance-1</span></code>, <code class="docutils literal notranslate"><span class="pre">cn-hongkong</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-1</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-2</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-3</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-5</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-northeast-1</span></code>, <code class="docutils literal notranslate"><span class="pre">eu-central-1</span></code>]</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/sag_qos_car.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/sag_qos_car.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the QoS speed limiting rule.</p></li>
<li><p><strong>limit_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The speed limiting method. Valid values: Absolute, Percent.</p></li>
<li><p><strong>max_bandwidth_abs</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum bandwidth allowed for the stream specified in the quintuple rule. This parameter is required when the value of the LimitType is Absolute.</p></li>
<li><p><strong>max_bandwidth_percent</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum bandwidth percentage allowed for the stream specified in the quintuple rule. It is based on the maximum upstream bandwidth you set for the associated Smart Access Gateway (SAG) instance.This parameter is required when the value of the LimitType parameter is Percent.</p></li>
<li><p><strong>min_bandwidth_abs</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum bandwidth allowed for the stream specified in the quintuple rule. This parameter is required when the value of the LimitType parameter is Absolute.</p></li>
<li><p><strong>min_bandwidth_percent</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum bandwidth percentage allowed for the stream specified in the quintuple rule. It is based on the maximum upstream bandwidth you set for the associated SAG instance.This parameter is required when the value of the LimitType parameter is Percent.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the QoS speed limiting rule..</p></li>
<li><p><strong>percent_source_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The bandwidth type when the speed is limited based on percentage. Valid values: CcnBandwidth, InternetUpBandwidth.The default value is InternetUpBandwidth.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the specified stream.</p></li>
<li><p><strong>qos_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance ID of the QoS.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.QosCar.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosCar.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the QoS speed limiting rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.QosCar.limit_type">
<code class="sig-name descname">limit_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosCar.limit_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The speed limiting method. Valid values: Absolute, Percent.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.QosCar.max_bandwidth_abs">
<code class="sig-name descname">max_bandwidth_abs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosCar.max_bandwidth_abs" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum bandwidth allowed for the stream specified in the quintuple rule. This parameter is required when the value of the LimitType is Absolute.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.QosCar.max_bandwidth_percent">
<code class="sig-name descname">max_bandwidth_percent</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosCar.max_bandwidth_percent" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum bandwidth percentage allowed for the stream specified in the quintuple rule. It is based on the maximum upstream bandwidth you set for the associated Smart Access Gateway (SAG) instance.This parameter is required when the value of the LimitType parameter is Percent.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.QosCar.min_bandwidth_abs">
<code class="sig-name descname">min_bandwidth_abs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosCar.min_bandwidth_abs" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum bandwidth allowed for the stream specified in the quintuple rule. This parameter is required when the value of the LimitType parameter is Absolute.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.QosCar.min_bandwidth_percent">
<code class="sig-name descname">min_bandwidth_percent</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosCar.min_bandwidth_percent" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum bandwidth percentage allowed for the stream specified in the quintuple rule. It is based on the maximum upstream bandwidth you set for the associated SAG instance.This parameter is required when the value of the LimitType parameter is Percent.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.QosCar.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosCar.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the QoS speed limiting rule..</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.QosCar.percent_source_type">
<code class="sig-name descname">percent_source_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosCar.percent_source_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The bandwidth type when the speed is limited based on percentage. Valid values: CcnBandwidth, InternetUpBandwidth.The default value is InternetUpBandwidth.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.QosCar.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosCar.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the specified stream.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.QosCar.qos_id">
<code class="sig-name descname">qos_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosCar.qos_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance ID of the QoS.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.rocketmq.QosCar.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">limit_type=None</em>, <em class="sig-param">max_bandwidth_abs=None</em>, <em class="sig-param">max_bandwidth_percent=None</em>, <em class="sig-param">min_bandwidth_abs=None</em>, <em class="sig-param">min_bandwidth_percent=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">percent_source_type=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">qos_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosCar.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing QosCar resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the QoS speed limiting rule.</p></li>
<li><p><strong>limit_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The speed limiting method. Valid values: Absolute, Percent.</p></li>
<li><p><strong>max_bandwidth_abs</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum bandwidth allowed for the stream specified in the quintuple rule. This parameter is required when the value of the LimitType is Absolute.</p></li>
<li><p><strong>max_bandwidth_percent</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum bandwidth percentage allowed for the stream specified in the quintuple rule. It is based on the maximum upstream bandwidth you set for the associated Smart Access Gateway (SAG) instance.This parameter is required when the value of the LimitType parameter is Percent.</p></li>
<li><p><strong>min_bandwidth_abs</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum bandwidth allowed for the stream specified in the quintuple rule. This parameter is required when the value of the LimitType parameter is Absolute.</p></li>
<li><p><strong>min_bandwidth_percent</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum bandwidth percentage allowed for the stream specified in the quintuple rule. It is based on the maximum upstream bandwidth you set for the associated SAG instance.This parameter is required when the value of the LimitType parameter is Percent.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the QoS speed limiting rule..</p></li>
<li><p><strong>percent_source_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The bandwidth type when the speed is limited based on percentage. Valid values: CcnBandwidth, InternetUpBandwidth.The default value is InternetUpBandwidth.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the specified stream.</p></li>
<li><p><strong>qos_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance ID of the QoS.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.rocketmq.QosCar.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosCar.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rocketmq.QosCar.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosCar.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rocketmq.QosPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rocketmq.</code><code class="sig-name descname">QosPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dest_cidr=None</em>, <em class="sig-param">dest_port_range=None</em>, <em class="sig-param">end_time=None</em>, <em class="sig-param">ip_protocol=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">qos_id=None</em>, <em class="sig-param">source_cidr=None</em>, <em class="sig-param">source_port_range=None</em>, <em class="sig-param">start_time=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Sag qos policy resource. 
You need to create a QoS policy to set priorities, rate limits, and quintuple rules for different messages.</p>
<p>For information about Sag Qos Policy and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/140065.htm">What is Qos Policy</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.60.0+</p>
<p><strong>NOTE:</strong> Only the following regions support. [<code class="docutils literal notranslate"><span class="pre">cn-shanghai</span></code>, <code class="docutils literal notranslate"><span class="pre">cn-shanghai-finance-1</span></code>, <code class="docutils literal notranslate"><span class="pre">cn-hongkong</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-1</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-2</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-3</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-5</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-northeast-1</span></code>, <code class="docutils literal notranslate"><span class="pre">eu-central-1</span></code>]</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/sag_qos_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/sag_qos_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the QoS policy.</p></li>
<li><p><strong>dest_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination CIDR block.</p></li>
<li><p><strong>dest_port_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination port range.</p></li>
<li><p><strong>end_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The expiration time of the quintuple rule.</p></li>
<li><p><strong>ip_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The transport layer protocol.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the QoS policy.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the quintuple rule. A smaller value indicates a higher priority. If the priorities of two quintuple rules are the same, the rule created earlier is applied first.Value range: 1 to 7.</p></li>
<li><p><strong>qos_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance ID of the QoS policy to which the quintuple rule is created.</p></li>
<li><p><strong>source_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source CIDR block.</p></li>
<li><p><strong>source_port_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source port range of the transport layer.</p></li>
<li><p><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time when the quintuple rule takes effect.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.QosPolicy.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosPolicy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the QoS policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.QosPolicy.dest_cidr">
<code class="sig-name descname">dest_cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosPolicy.dest_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination CIDR block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.QosPolicy.dest_port_range">
<code class="sig-name descname">dest_port_range</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosPolicy.dest_port_range" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination port range.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.QosPolicy.end_time">
<code class="sig-name descname">end_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosPolicy.end_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The expiration time of the quintuple rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.QosPolicy.ip_protocol">
<code class="sig-name descname">ip_protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosPolicy.ip_protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The transport layer protocol.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.QosPolicy.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the QoS policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.QosPolicy.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosPolicy.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the quintuple rule. A smaller value indicates a higher priority. If the priorities of two quintuple rules are the same, the rule created earlier is applied first.Value range: 1 to 7.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.QosPolicy.qos_id">
<code class="sig-name descname">qos_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosPolicy.qos_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance ID of the QoS policy to which the quintuple rule is created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.QosPolicy.source_cidr">
<code class="sig-name descname">source_cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosPolicy.source_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>The source CIDR block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.QosPolicy.source_port_range">
<code class="sig-name descname">source_port_range</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosPolicy.source_port_range" title="Permalink to this definition">¶</a></dt>
<dd><p>The source port range of the transport layer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.QosPolicy.start_time">
<code class="sig-name descname">start_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosPolicy.start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when the quintuple rule takes effect.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.rocketmq.QosPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dest_cidr=None</em>, <em class="sig-param">dest_port_range=None</em>, <em class="sig-param">end_time=None</em>, <em class="sig-param">ip_protocol=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">qos_id=None</em>, <em class="sig-param">source_cidr=None</em>, <em class="sig-param">source_port_range=None</em>, <em class="sig-param">start_time=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing QosPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the QoS policy.</p></li>
<li><p><strong>dest_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination CIDR block.</p></li>
<li><p><strong>dest_port_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination port range.</p></li>
<li><p><strong>end_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The expiration time of the quintuple rule.</p></li>
<li><p><strong>ip_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The transport layer protocol.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the QoS policy.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the quintuple rule. A smaller value indicates a higher priority. If the priorities of two quintuple rules are the same, the rule created earlier is applied first.Value range: 1 to 7.</p></li>
<li><p><strong>qos_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance ID of the QoS policy to which the quintuple rule is created.</p></li>
<li><p><strong>source_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source CIDR block.</p></li>
<li><p><strong>source_port_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source port range of the transport layer.</p></li>
<li><p><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time when the quintuple rule takes effect.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.rocketmq.QosPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rocketmq.QosPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.QosPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rocketmq.SnatEntry">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rocketmq.</code><code class="sig-name descname">SnatEntry</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cidr_block=None</em>, <em class="sig-param">sag_id=None</em>, <em class="sig-param">snat_ip=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.SnatEntry" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Sag SnatEntry resource. This topic describes how to add a SNAT entry to enable the SNAT function. The SNAT function can hide internal IP addresses and resolve private IP address conflicts. With this function, on-premises sites can access internal IP addresses, but cannot be accessed by internal IP addresses. If you do not add a SNAT entry, on-premises sites can access each other only when all related IP addresses do not conflict.</p>
<p>For information about Sag SnatEntry and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/124231.htm">What is Sag SnatEntry</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.61.0+</p>
<p><strong>NOTE:</strong> Only the following regions support. [<code class="docutils literal notranslate"><span class="pre">cn-shanghai</span></code>, <code class="docutils literal notranslate"><span class="pre">cn-shanghai-finance-1</span></code>, <code class="docutils literal notranslate"><span class="pre">cn-hongkong</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-1</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-2</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-3</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-southeast-5</span></code>, <code class="docutils literal notranslate"><span class="pre">ap-northeast-1</span></code>, <code class="docutils literal notranslate"><span class="pre">eu-central-1</span></code>]</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/sag_snat_entry.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/sag_snat_entry.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination CIDR block.</p></li>
<li><p><strong>sag_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the SAG instance.</p></li>
<li><p><strong>snat_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public IP address.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.SnatEntry.cidr_block">
<code class="sig-name descname">cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.SnatEntry.cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination CIDR block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.SnatEntry.sag_id">
<code class="sig-name descname">sag_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.SnatEntry.sag_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the SAG instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.SnatEntry.snat_ip">
<code class="sig-name descname">snat_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.SnatEntry.snat_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The public IP address.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.rocketmq.SnatEntry.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cidr_block=None</em>, <em class="sig-param">sag_id=None</em>, <em class="sig-param">snat_ip=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.SnatEntry.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SnatEntry resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination CIDR block.</p></li>
<li><p><strong>sag_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the SAG instance.</p></li>
<li><p><strong>snat_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public IP address.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.rocketmq.SnatEntry.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.SnatEntry.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rocketmq.SnatEntry.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.SnatEntry.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rocketmq.Topic">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.rocketmq.</code><code class="sig-name descname">Topic</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">message_type=None</em>, <em class="sig-param">perm=None</em>, <em class="sig-param">remark=None</em>, <em class="sig-param">topic=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.Topic" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an ONS topic resource.</p>
<p>For more information about how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/29591.html">RocketMQ Topic Management API</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.53.0+</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/ons_topic.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/ons_topic.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the ONS Instance that owns the topics.</p></li>
<li><p><strong>message_type</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The type of the message. Read <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/29591.html">Ons Topic Create</a> for further details.</p></li>
<li><p><strong>perm</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – This attribute is used to set the read-write mode for the topic. Read <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/56880.html">Request parameters</a> for further details.</p></li>
<li><p><strong>remark</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This attribute is a concise description of topic. The length cannot exceed 128.</p></li>
<li><p><strong>topic</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the topic. Two topics on a single instance cannot have the same name and the name cannot start with ‘GID’ or ‘CID’. The length cannot exceed 64 characters.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.Topic.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.Topic.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the ONS Instance that owns the topics.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.Topic.message_type">
<code class="sig-name descname">message_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.Topic.message_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the message. Read <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/29591.html">Ons Topic Create</a> for further details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.Topic.perm">
<code class="sig-name descname">perm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.Topic.perm" title="Permalink to this definition">¶</a></dt>
<dd><p>This attribute is used to set the read-write mode for the topic. Read <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/56880.html">Request parameters</a> for further details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.Topic.remark">
<code class="sig-name descname">remark</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.Topic.remark" title="Permalink to this definition">¶</a></dt>
<dd><p>This attribute is a concise description of topic. The length cannot exceed 128.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.rocketmq.Topic.topic">
<code class="sig-name descname">topic</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.rocketmq.Topic.topic" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the topic. Two topics on a single instance cannot have the same name and the name cannot start with ‘GID’ or ‘CID’. The length cannot exceed 64 characters.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.rocketmq.Topic.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">message_type=None</em>, <em class="sig-param">perm=None</em>, <em class="sig-param">remark=None</em>, <em class="sig-param">topic=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.Topic.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Topic resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the ONS Instance that owns the topics.</p></li>
<li><p><strong>message_type</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>The type of the message. Read <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/29591.html">Ons Topic Create</a> for further details.</p>
</p></li>
<li><p><strong>perm</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>This attribute is used to set the read-write mode for the topic. Read <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/56880.html">Request parameters</a> for further details.</p>
</p></li>
<li><p><strong>remark</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This attribute is a concise description of topic. The length cannot exceed 128.</p></li>
<li><p><strong>topic</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the topic. Two topics on a single instance cannot have the same name and the name cannot start with ‘GID’ or ‘CID’. The length cannot exceed 64 characters.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.rocketmq.Topic.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.Topic.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rocketmq.Topic.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.Topic.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.rocketmq.get_groups">
<code class="sig-prename descclassname">pulumi_alicloud.rocketmq.</code><code class="sig-name descname">get_groups</code><span class="sig-paren">(</span><em class="sig-param">group_id_regex=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.get_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of ONS Groups in an Alibaba Cloud account according to the specified filters.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.53.0+</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/ons_groups.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/ons_groups.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>group_id_regex</strong> (<em>str</em>) – A regex string to filter results by the group name.</p></li>
<li><p><strong>instance_id</strong> (<em>str</em>) – ID of the ONS Instance that owns the groups.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.rocketmq.get_instances">
<code class="sig-prename descclassname">pulumi_alicloud.rocketmq.</code><code class="sig-name descname">get_instances</code><span class="sig-paren">(</span><em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.get_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of ONS Instances in an Alibaba Cloud account according to the specified filters.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.52.0+</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/ons_instances.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/ons_instances.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of instance IDs to filter results.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by the instance name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.rocketmq.get_topics">
<code class="sig-prename descclassname">pulumi_alicloud.rocketmq.</code><code class="sig-name descname">get_topics</code><span class="sig-paren">(</span><em class="sig-param">instance_id=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.rocketmq.get_topics" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of ONS Topics in an Alibaba Cloud account according to the specified filters.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.53.0+</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/ons_topics.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/ons_topics.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>instance_id</strong> (<em>str</em>) – ID of the ONS Instance that owns the topics.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by the topic name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
