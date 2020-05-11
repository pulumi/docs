---
title: Module slb
title_tag: Module slb | Package pulumi_alicloud | Python SDK
linktitle: slb
notitle: true
---

<div class="section" id="slb">
<h1>slb<a class="headerlink" href="#slb" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.slb"></span><dl class="py class">
<dt id="pulumi_alicloud.slb.Acl">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">Acl</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entry_lists</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.Acl" title="Permalink to this definition">¶</a></dt>
<dd><p>An access control list contains multiple IP addresses or CIDR blocks.
The access control list can help you to define multiple instance listening dimension,
and to meet the multiple usage for single access control list.</p>
<p>Server Load Balancer allows you to configure access control for listeners.
You can configure different whitelists or blacklists for different listeners.</p>
<p>You can configure access control
when you create a listener or change access control configuration after a listener is created.</p>
<blockquote>
<div><p><strong>NOTE:</strong> One access control list can be attached to many Listeners in different load balancer as whitelists or blacklists.</p>
<p><strong>NOTE:</strong> The maximum number of access control lists per region  is 50.</p>
<p><strong>NOTE:</strong> The maximum number of IP addresses added each time is 50.</p>
<p><strong>NOTE:</strong> The maximum number of entries per access control list is 300.</p>
<p><strong>NOTE:</strong> The maximum number of listeners that an access control list can be added to is 50.</p>
</div></blockquote>
<p>For information about slb and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/27539.htm">What is Server Load Balancer</a>.</p>
<p>For information about acl and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/85978.htm">Configure an access control list</a>.</p>
<p>The entry mapping supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">entry</span></code> - (Required) An IP addresses or CIDR blocks.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> - (Optional) the comment of the entry.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>entry_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of entry (IP addresses or CIDR blocks) to be added. At most 50 etnry can be supported in one resource. It contains two sub-fields as <code class="docutils literal notranslate"><span class="pre">Entry</span> <span class="pre">Block</span></code> follows.</p></li>
<li><p><strong>ip_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP Version of access control list is the type of its entry (IP addresses or CIDR blocks). It values ipv4/ipv6. Our plugin provides a default ip_version: “ipv4”.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the access control list.</p></li>
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource group ID.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>entry_lists</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">entry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Acl.entry_lists">
<code class="sig-name descname">entry_lists</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Acl.entry_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of entry (IP addresses or CIDR blocks) to be added. At most 50 etnry can be supported in one resource. It contains two sub-fields as <code class="docutils literal notranslate"><span class="pre">Entry</span> <span class="pre">Block</span></code> follows.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">entry</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Acl.ip_version">
<code class="sig-name descname">ip_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Acl.ip_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP Version of access control list is the type of its entry (IP addresses or CIDR blocks). It values ipv4/ipv6. Our plugin provides a default ip_version: “ipv4”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Acl.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Acl.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the access control list.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Acl.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Acl.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource group ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Acl.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Acl.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.slb.Acl.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entry_lists</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.Acl.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Acl resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>entry_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of entry (IP addresses or CIDR blocks) to be added. At most 50 etnry can be supported in one resource. It contains two sub-fields as <code class="docutils literal notranslate"><span class="pre">Entry</span> <span class="pre">Block</span></code> follows.</p></li>
<li><p><strong>ip_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP Version of access control list is the type of its entry (IP addresses or CIDR blocks). It values ipv4/ipv6. Our plugin provides a default ip_version: “ipv4”.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the access control list.</p></li>
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource group ID.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>entry_lists</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">entry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.slb.Acl.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.Acl.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.slb.Acl.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.Acl.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.slb.Attachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">Attachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend_servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_protection_validation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weight</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.Attachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Attachment resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] backend_servers: The backend servers of the load balancer.
:param pulumi.Input[bool] delete_protection_validation: Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
:param pulumi.Input[list] instance_ids: A list of instance ids to added backend server in the SLB.
:param pulumi.Input[str] load_balancer_id: ID of the load balancer.
:param pulumi.Input[str] server_type: Type of the instances. Valid value ecs, eni. Default to ecs.
:param pulumi.Input[float] weight: Weight of the instances. Valid value range: [0-100]. Default to 100.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Attachment.backend_servers">
<code class="sig-name descname">backend_servers</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Attachment.backend_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>The backend servers of the load balancer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Attachment.delete_protection_validation">
<code class="sig-name descname">delete_protection_validation</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Attachment.delete_protection_validation" title="Permalink to this definition">¶</a></dt>
<dd><p>Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Attachment.instance_ids">
<code class="sig-name descname">instance_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Attachment.instance_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of instance ids to added backend server in the SLB.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Attachment.load_balancer_id">
<code class="sig-name descname">load_balancer_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Attachment.load_balancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the load balancer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Attachment.server_type">
<code class="sig-name descname">server_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Attachment.server_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the instances. Valid value ecs, eni. Default to ecs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Attachment.weight">
<code class="sig-name descname">weight</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Attachment.weight" title="Permalink to this definition">¶</a></dt>
<dd><p>Weight of the instances. Valid value range: [0-100]. Default to 100.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.slb.Attachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend_servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_protection_validation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weight</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.Attachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Attachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend_servers</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The backend servers of the load balancer.</p></li>
<li><p><strong>delete_protection_validation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.</p></li>
<li><p><strong>instance_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of instance ids to added backend server in the SLB.</p></li>
<li><p><strong>load_balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the load balancer.</p></li>
<li><p><strong>server_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the instances. Valid value ecs, eni. Default to ecs.</p></li>
<li><p><strong>weight</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Weight of the instances. Valid value range: [0-100]. Default to 100.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.slb.Attachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.Attachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.slb.Attachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.Attachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.slb.AwaitableGetAclsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">AwaitableGetAclsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">acls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.AwaitableGetAclsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.slb.AwaitableGetAttachmentsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">AwaitableGetAttachmentsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slb_attachments</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.AwaitableGetAttachmentsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.slb.AwaitableGetBackendServersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">AwaitableGetBackendServersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">backend_servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.AwaitableGetBackendServersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.slb.AwaitableGetCaCertificatesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">AwaitableGetCaCertificatesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">certificates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.AwaitableGetCaCertificatesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.slb.AwaitableGetDomainExtensionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">AwaitableGetDomainExtensionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">extensions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frontend_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.AwaitableGetDomainExtensionsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.slb.AwaitableGetListenersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">AwaitableGetListenersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frontend_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slb_listeners</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.AwaitableGetListenersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.slb.AwaitableGetLoadBalancersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">AwaitableGetLoadBalancersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slave_availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slbs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.AwaitableGetLoadBalancersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.slb.AwaitableGetMasterSlaveServerGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">AwaitableGetMasterSlaveServerGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.AwaitableGetMasterSlaveServerGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.slb.AwaitableGetRulesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">AwaitableGetRulesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">frontend_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slb_rules</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.AwaitableGetRulesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.slb.AwaitableGetServerCertificatesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">AwaitableGetServerCertificatesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">certificates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.AwaitableGetServerCertificatesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.slb.AwaitableGetServerGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">AwaitableGetServerGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slb_server_groups</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.AwaitableGetServerGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.slb.AwaitableGetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">AwaitableGetZonesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">available_slb_address_ip_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">available_slb_address_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zones</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.AwaitableGetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.slb.BackendServer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">BackendServer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend_servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_protection_validation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.BackendServer" title="Permalink to this definition">¶</a></dt>
<dd><p>Add a group of backend servers (ECS or ENI instance) to the Server Load Balancer or remove them from it.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.53.0+</p>
</div></blockquote>
<p>The servers mapping supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">server_id</span></code> - (Required) A list backend server ID (ECS instance ID).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> - (Optional) Weight of the backend server. Valid value range: [0-100].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> - (Optional) Type of the backend server. Valid value ecs, eni. Default to eni.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of instances to added backend server in the SLB. It contains three sub-fields as <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">server</span></code> follows.</p></li>
<li><p><strong>delete_protection_validation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.</p></li>
<li><p><strong>load_balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the load balancer.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>backend_servers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">serverId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.slb.BackendServer.backend_servers">
<code class="sig-name descname">backend_servers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.BackendServer.backend_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of instances to added backend server in the SLB. It contains three sub-fields as <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">server</span></code> follows.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">serverId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.BackendServer.delete_protection_validation">
<code class="sig-name descname">delete_protection_validation</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.BackendServer.delete_protection_validation" title="Permalink to this definition">¶</a></dt>
<dd><p>Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.BackendServer.load_balancer_id">
<code class="sig-name descname">load_balancer_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.BackendServer.load_balancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the load balancer.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.slb.BackendServer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend_servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_protection_validation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.BackendServer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BackendServer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of instances to added backend server in the SLB. It contains three sub-fields as <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">server</span></code> follows.</p></li>
<li><p><strong>delete_protection_validation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.</p></li>
<li><p><strong>load_balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the load balancer.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>backend_servers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">serverId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.slb.BackendServer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.BackendServer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.slb.BackendServer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.BackendServer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.slb.CaCertificate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">CaCertificate</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ca_certificate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.CaCertificate" title="Permalink to this definition">¶</a></dt>
<dd><p>A Load Balancer CA Certificate is used by the listener of the protocol https.</p>
<p>For information about slb and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/27539.htm">What is Server Load Balancer</a>.</p>
<p>For information about CA Certificate and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/85968.htm">Configure CA Certificate</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ca_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the content of the CA certificate.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the CA Certificate.</p></li>
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of resource group which the slb_ca certificate belongs.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.slb.CaCertificate.ca_certificate">
<code class="sig-name descname">ca_certificate</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.CaCertificate.ca_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>the content of the CA certificate.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.CaCertificate.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.CaCertificate.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the CA Certificate.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.CaCertificate.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.CaCertificate.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of resource group which the slb_ca certificate belongs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.CaCertificate.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.CaCertificate.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.slb.CaCertificate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ca_certificate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.CaCertificate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CaCertificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ca_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the content of the CA certificate.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the CA Certificate.</p></li>
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of resource group which the slb_ca certificate belongs.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.slb.CaCertificate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.CaCertificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.slb.CaCertificate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.CaCertificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.slb.DomainExtension">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">DomainExtension</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_protection_validation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frontend_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_certificate_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.DomainExtension" title="Permalink to this definition">¶</a></dt>
<dd><p>HTTPS listeners of guaranteed-performance SLB support configuring multiple certificates, allowing you to forward requests with different domain names to different backend servers.
Please refer to the <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/85956.htm?spm=a2c63.p38356.b99.40.1c881563Co8p6w">documentation</a> for details.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.60.0+</p>
<p><strong>NOTE:</strong> The instance with shared loadBalancerSpec doesn’t support domainExtension.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>delete_protection_validation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain name,</p></li>
<li><p><strong>frontend_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The frontend port used by the HTTPS listener of the SLB instance. Valid values: 1–65535.</p></li>
<li><p><strong>load_balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the SLB instance.</p></li>
<li><p><strong>server_certificate_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the certificate used by the domain name.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.slb.DomainExtension.delete_protection_validation">
<code class="sig-name descname">delete_protection_validation</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.DomainExtension.delete_protection_validation" title="Permalink to this definition">¶</a></dt>
<dd><p>Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.DomainExtension.domain">
<code class="sig-name descname">domain</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.DomainExtension.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain name,</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.DomainExtension.frontend_port">
<code class="sig-name descname">frontend_port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.DomainExtension.frontend_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The frontend port used by the HTTPS listener of the SLB instance. Valid values: 1–65535.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.DomainExtension.load_balancer_id">
<code class="sig-name descname">load_balancer_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.DomainExtension.load_balancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the SLB instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.DomainExtension.server_certificate_id">
<code class="sig-name descname">server_certificate_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.DomainExtension.server_certificate_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the certificate used by the domain name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.slb.DomainExtension.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_protection_validation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frontend_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_certificate_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.DomainExtension.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DomainExtension resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>delete_protection_validation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain name,</p></li>
<li><p><strong>frontend_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The frontend port used by the HTTPS listener of the SLB instance. Valid values: 1–65535.</p></li>
<li><p><strong>load_balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the SLB instance.</p></li>
<li><p><strong>server_certificate_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the certificate used by the domain name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.slb.DomainExtension.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.DomainExtension.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.slb.DomainExtension.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.DomainExtension.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.slb.GetAclsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">GetAclsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">acls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.GetAclsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAcls.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetAclsResult.acls">
<code class="sig-name descname">acls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetAclsResult.acls" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SLB  acls. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetAclsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetAclsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetAclsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetAclsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SLB acls IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetAclsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetAclsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SLB acls names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetAclsResult.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetAclsResult.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource group ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetAclsResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetAclsResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.slb.GetAttachmentsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">GetAttachmentsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slb_attachments</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.GetAttachmentsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAttachments.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetAttachmentsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetAttachmentsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetAttachmentsResult.slb_attachments">
<code class="sig-name descname">slb_attachments</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetAttachmentsResult.slb_attachments" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SLB attachments. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.slb.GetBackendServersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">GetBackendServersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">backend_servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.GetBackendServersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBackendServers.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetBackendServersResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetBackendServersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.slb.GetCaCertificatesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">GetCaCertificatesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">certificates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.GetCaCertificatesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCaCertificates.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetCaCertificatesResult.certificates">
<code class="sig-name descname">certificates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetCaCertificatesResult.certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SLB ca certificates. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetCaCertificatesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetCaCertificatesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetCaCertificatesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetCaCertificatesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SLB ca certificates IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetCaCertificatesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetCaCertificatesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SLB ca certificates names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetCaCertificatesResult.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetCaCertificatesResult.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource group Id of CA certificate.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetCaCertificatesResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetCaCertificatesResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>(Available in v1.66.0+) A mapping of tags to assign to the resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.slb.GetDomainExtensionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">GetDomainExtensionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">extensions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frontend_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.GetDomainExtensionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDomainExtensions.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetDomainExtensionsResult.extensions">
<code class="sig-name descname">extensions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetDomainExtensionsResult.extensions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SLB domain extension. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetDomainExtensionsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetDomainExtensionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.slb.GetListenersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">GetListenersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frontend_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slb_listeners</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.GetListenersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getListeners.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetListenersResult.frontend_port">
<code class="sig-name descname">frontend_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetListenersResult.frontend_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Frontend port used to receive incoming traffic and distribute it to the backend servers.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetListenersResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetListenersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetListenersResult.protocol">
<code class="sig-name descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetListenersResult.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>Listener protocol. Possible values: <code class="docutils literal notranslate"><span class="pre">http</span></code>, <code class="docutils literal notranslate"><span class="pre">https</span></code>, <code class="docutils literal notranslate"><span class="pre">tcp</span></code> and <code class="docutils literal notranslate"><span class="pre">udp</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetListenersResult.slb_listeners">
<code class="sig-name descname">slb_listeners</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetListenersResult.slb_listeners" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SLB listeners. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.slb.GetLoadBalancersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">GetLoadBalancersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slave_availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slbs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.GetLoadBalancersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLoadBalancers.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetLoadBalancersResult.address">
<code class="sig-name descname">address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetLoadBalancersResult.address" title="Permalink to this definition">¶</a></dt>
<dd><p>Service address of the SLB.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetLoadBalancersResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetLoadBalancersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetLoadBalancersResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetLoadBalancersResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of slb IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetLoadBalancersResult.master_availability_zone">
<code class="sig-name descname">master_availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetLoadBalancersResult.master_availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Master availability zone of the SLBs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetLoadBalancersResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetLoadBalancersResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of slb names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetLoadBalancersResult.network_type">
<code class="sig-name descname">network_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetLoadBalancersResult.network_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Network type of the SLB. Possible values: <code class="docutils literal notranslate"><span class="pre">vpc</span></code> and <code class="docutils literal notranslate"><span class="pre">classic</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetLoadBalancersResult.slave_availability_zone">
<code class="sig-name descname">slave_availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetLoadBalancersResult.slave_availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Slave availability zone of the SLBs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetLoadBalancersResult.slbs">
<code class="sig-name descname">slbs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetLoadBalancersResult.slbs" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SLBs. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetLoadBalancersResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetLoadBalancersResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags assigned to the SLB instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetLoadBalancersResult.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetLoadBalancersResult.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the VPC the SLB belongs to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetLoadBalancersResult.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetLoadBalancersResult.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the VSwitch the SLB belongs to.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.slb.GetMasterSlaveServerGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">GetMasterSlaveServerGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.GetMasterSlaveServerGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getMasterSlaveServerGroups.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetMasterSlaveServerGroupsResult.groups">
<code class="sig-name descname">groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetMasterSlaveServerGroupsResult.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SLB master slave server groups. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetMasterSlaveServerGroupsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetMasterSlaveServerGroupsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetMasterSlaveServerGroupsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetMasterSlaveServerGroupsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SLB master slave server groups IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetMasterSlaveServerGroupsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetMasterSlaveServerGroupsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SLB master slave server groups names.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.slb.GetRulesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">GetRulesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">frontend_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slb_rules</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.GetRulesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRules.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetRulesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetRulesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetRulesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetRulesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SLB listener rules IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetRulesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetRulesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SLB listener rules names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetRulesResult.slb_rules">
<code class="sig-name descname">slb_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetRulesResult.slb_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SLB listener rules. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.slb.GetServerCertificatesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">GetServerCertificatesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">certificates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.GetServerCertificatesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServerCertificates.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetServerCertificatesResult.certificates">
<code class="sig-name descname">certificates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetServerCertificatesResult.certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SLB server certificates. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetServerCertificatesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetServerCertificatesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetServerCertificatesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetServerCertificatesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SLB server certificates IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetServerCertificatesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetServerCertificatesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SLB server certificates names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetServerCertificatesResult.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetServerCertificatesResult.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of resource group which the slb server certificates belongs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetServerCertificatesResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetServerCertificatesResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>(Available in v1.66.0+) A mapping of tags to assign to the resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.slb.GetServerGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">GetServerGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slb_server_groups</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.GetServerGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServerGroups.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetServerGroupsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetServerGroupsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetServerGroupsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetServerGroupsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SLB VServer groups IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetServerGroupsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetServerGroupsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SLB VServer groups names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetServerGroupsResult.slb_server_groups">
<code class="sig-name descname">slb_server_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetServerGroupsResult.slb_server_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SLB VServer groups. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.slb.GetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">GetZonesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">available_slb_address_ip_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">available_slb_address_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zones</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.GetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getZones.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetZonesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetZonesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetZonesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetZonesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of zone IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.GetZonesResult.zones">
<code class="sig-name descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.GetZonesResult.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of availability zones. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.slb.Listener">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">Listener</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bandwidth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cookie</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cookie_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_protection_validation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_http2</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">established_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">forward_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frontend_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gzip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_connect_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_http_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_interval</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">healthy_threshold</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">idle_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lb_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lb_protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">listener_forward</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_slave_server_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">persistence_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduler</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_certificate_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_certificate_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sticky_session</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sticky_session_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_cipher_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unhealthy_threshold</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">x_forwarded_for</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.Listener" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Application Load Balancer Listener resource.</p>
<p>For information about slb and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/27539.htm">What is Server Load Balancer</a>.</p>
<p>For information about listener and how to use it, to see the following:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/27592.htm">Configure a HTTP Listener</a>.</p></li>
<li><p><a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/27593.htm">Configure a HTTPS Listener</a>.</p></li>
<li><p><a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/27594.htm">Configure a TCP Listener</a>.</p></li>
<li><p><a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/27595.htm">Configure a UDP Listener</a>.</p></li>
</ul>
<p>load balance support 4 protocal to listen on, they are <code class="docutils literal notranslate"><span class="pre">http</span></code>,<code class="docutils literal notranslate"><span class="pre">https</span></code>,<code class="docutils literal notranslate"><span class="pre">tcp</span></code>,<code class="docutils literal notranslate"><span class="pre">udp</span></code>, the every listener support which portocal following:</p>
<p>The listener mapping supports the following:</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the id of access control list to be apply on the listener, is the id of resource alicloud_slb_acl. If <code class="docutils literal notranslate"><span class="pre">acl_status</span></code> is “on”, it is mandatory. Otherwise, it will be ignored.</p></li>
<li><p><strong>acl_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether to enable “acl(access control list)”, the acl is specified by <code class="docutils literal notranslate"><span class="pre">acl_id</span></code>. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>acl_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Mode for handling the acl specified by acl_id. If <code class="docutils literal notranslate"><span class="pre">acl_status</span></code> is “on”, it is mandatory. Otherwise, it will be ignored. Valid values are <code class="docutils literal notranslate"><span class="pre">white</span></code> and <code class="docutils literal notranslate"><span class="pre">black</span></code>. <code class="docutils literal notranslate"><span class="pre">white</span></code> means the Listener can only be accessed by client ip belongs to the acl; <code class="docutils literal notranslate"><span class="pre">black</span></code> means the Listener can not be accessed by client ip belongs to the acl.</p></li>
<li><p><strong>backend_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Port used by the Server Load Balancer instance backend. Valid value range: [1-65535].</p></li>
<li><p><strong>bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Bandwidth peak of Listener. For the public network instance charged per traffic consumed, the Bandwidth on Listener can be set to -1, indicating the bandwidth peak is unlimited. Valid values are [-1, 1-1000] in Mbps.</p></li>
<li><p><strong>cookie</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cookie configured on the server. It is mandatory when <code class="docutils literal notranslate"><span class="pre">sticky_session</span></code> is “on” and <code class="docutils literal notranslate"><span class="pre">sticky_session_type</span></code> is “server”. Otherwise, it will be ignored. Valid value：String in line with RFC 2965, with length being 1- 200. It only contains characters such as ASCII codes, English letters and digits instead of the comma, semicolon or spacing, and it cannot start with $.</p></li>
<li><p><strong>cookie_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Cookie timeout. It is mandatory when <code class="docutils literal notranslate"><span class="pre">sticky_session</span></code> is “on” and <code class="docutils literal notranslate"><span class="pre">sticky_session_type</span></code> is “insert”. Otherwise, it will be ignored. Valid value range: [1-86400] in seconds.</p></li>
<li><p><strong>delete_protection_validation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of slb listener. This description can have a string of 1 to 80 characters. Default value: null.</p></li>
<li><p><strong>enable_http2</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether to enable https listener support http2 or not. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">on</span></code>.</p></li>
<li><p><strong>established_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout of tcp listener established connection idle timeout. Valid value range: [10-900] in seconds. Default to 900.</p></li>
<li><p><strong>forward_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port that http redirect to https.</p></li>
<li><p><strong>frontend_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Port used by the Server Load Balancer instance frontend. Valid value range: [1-65535].</p></li>
<li><p><strong>gzip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable “Gzip Compression”. If enabled, files of specific file types will be compressed, otherwise, no files will be compressed. Default to true. Available in v1.13.0+.</p></li>
<li><p><strong>health_check</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether to enable health check. Valid values are<code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. TCP and UDP listener’s HealthCheck is always on, so it will be ignore when launching TCP or UDP listener.</p></li>
<li><p><strong>health_check_connect_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Port used for health check. Valid value range: [1-65535]. Default to “None” means the backend server port is used.</p></li>
<li><p><strong>health_check_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain name used for health check. When it used to launch TCP listener, <code class="docutils literal notranslate"><span class="pre">health_check_type</span></code> must be “http”. Its length is limited to 1-80 and only characters such as letters, digits, ‘-‘ and ‘.’ are allowed. When it is not set or empty,  Server Load Balancer uses the private network IP address of each backend server as Domain used for health check.</p></li>
<li><p><strong>health_check_http_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Regular health check HTTP status code. Multiple codes are segmented by “,”. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Default to <code class="docutils literal notranslate"><span class="pre">http_2xx</span></code>.  Valid values are: <code class="docutils literal notranslate"><span class="pre">http_2xx</span></code>,  <code class="docutils literal notranslate"><span class="pre">http_3xx</span></code>, <code class="docutils literal notranslate"><span class="pre">http_4xx</span></code> and <code class="docutils literal notranslate"><span class="pre">http_5xx</span></code>.</p></li>
<li><p><strong>health_check_interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time interval of health checks. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Valid value range: [1-50] in seconds. Default to 2.</p></li>
<li><p><strong>health_check_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method of health check. Valid values: [“head”, “get”].</p></li>
<li><p><strong>health_check_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum timeout of each health check response. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Valid value range: [1-300] in seconds. Default to 5. Note: If <code class="docutils literal notranslate"><span class="pre">health_check_timeout</span></code> &lt; <code class="docutils literal notranslate"><span class="pre">health_check_interval</span></code>, its will be replaced by <code class="docutils literal notranslate"><span class="pre">health_check_interval</span></code>.</p></li>
<li><p><strong>health_check_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of health check. Valid values are: <code class="docutils literal notranslate"><span class="pre">tcp</span></code> and <code class="docutils literal notranslate"><span class="pre">http</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">tcp</span></code> . TCP supports TCP and HTTP health check mode, you can select the particular mode depending on your application.</p></li>
<li><p><strong>health_check_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI used for health check. When it used to launch TCP listener, <code class="docutils literal notranslate"><span class="pre">health_check_type</span></code> must be “http”. Its length is limited to 1-80 and it must start with /. Only characters such as letters, digits, ‘-’, ‘/’, ‘.’, ‘%’, ‘?’, #’ and ‘&amp;’ are allowed.</p></li>
<li><p><strong>healthy_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Threshold determining the result of the health check is success. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Valid value range: [1-10] in seconds. Default to 3.</p></li>
<li><p><strong>idle_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout of http or https listener established connection idle timeout. Valid value range: [1-60] in seconds. Default to 15.</p></li>
<li><p><strong>listener_forward</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether to enable http redirect to https, Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>load_balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Load Balancer ID which is used to launch a new listener.</p></li>
<li><p><strong>persistence_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout of connection persistence. Valid value range: [0-3600] in seconds. Default to 0 and means closing it.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol to listen on. Valid values are [<code class="docutils literal notranslate"><span class="pre">http</span></code>, <code class="docutils literal notranslate"><span class="pre">https</span></code>, <code class="docutils literal notranslate"><span class="pre">tcp</span></code>, <code class="docutils literal notranslate"><span class="pre">udp</span></code>].</p></li>
<li><p><strong>request_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout of http or https listener request (which does not get response from backend) timeout. Valid value range: [1-180] in seconds. Default to 60.</p></li>
<li><p><strong>scheduler</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Scheduling algorithm, Valid values are <code class="docutils literal notranslate"><span class="pre">wrr</span></code>, <code class="docutils literal notranslate"><span class="pre">rr</span></code> and <code class="docutils literal notranslate"><span class="pre">wlc</span></code>.  Default to “wrr”.</p></li>
<li><p><strong>server_certificate_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SLB Server certificate ID. It is required when <code class="docutils literal notranslate"><span class="pre">protocol</span></code> is <code class="docutils literal notranslate"><span class="pre">https</span></code>.</p></li>
<li><p><strong>server_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the id of server group to be apply on the listener, is the id of resource <code class="docutils literal notranslate"><span class="pre">slb.ServerGroup</span></code>.</p></li>
<li><p><strong>ssl_certificate_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – It has been deprecated from 1.59.0 and using <code class="docutils literal notranslate"><span class="pre">server_certificate_id</span></code> instead.</p></li>
<li><p><strong>sticky_session</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether to enable session persistence, Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>sticky_session_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Mode for handling the cookie. If <code class="docutils literal notranslate"><span class="pre">sticky_session</span></code> is “on”, it is mandatory. Otherwise, it will be ignored. Valid values are <code class="docutils literal notranslate"><span class="pre">insert</span></code> and <code class="docutils literal notranslate"><span class="pre">server</span></code>. <code class="docutils literal notranslate"><span class="pre">insert</span></code> means it is inserted from Server Load Balancer; <code class="docutils literal notranslate"><span class="pre">server</span></code> means the Server Load Balancer learns from the backend server.</p></li>
<li><p><strong>tls_cipher_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Https listener TLS cipher policy. Valid values are <code class="docutils literal notranslate"><span class="pre">tls_cipher_policy_1_0</span></code>, <code class="docutils literal notranslate"><span class="pre">tls_cipher_policy_1_1</span></code>, <code class="docutils literal notranslate"><span class="pre">tls_cipher_policy_1_2</span></code>, <code class="docutils literal notranslate"><span class="pre">tls_cipher_policy_1_2_strict</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">tls_cipher_policy_1_0</span></code>. Currently the <code class="docutils literal notranslate"><span class="pre">tls_cipher_policy</span></code> can not be updated when load balancer instance is “Shared-Performance”.</p></li>
<li><p><strong>unhealthy_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Threshold determining the result of the health check is fail. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Valid value range: [1-10] in seconds. Default to 3.</p></li>
<li><p><strong>x_forwarded_for</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Whether to set additional HTTP Header field “X-Forwarded-For” (documented below). Available in v1.13.0+.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>x_forwarded_for</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">retriveClientIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retriveSlbId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use the XForwardedFor header to obtain the ID of the SLB instance. Default to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retriveSlbIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use the XForwardedFor_SLBIP header to obtain the public IP address of the SLB instance. Default to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retriveSlbProto</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use the XForwardedFor_proto header to obtain the protocol used by the listener. Default to false.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.acl_id">
<code class="sig-name descname">acl_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.acl_id" title="Permalink to this definition">¶</a></dt>
<dd><p>the id of access control list to be apply on the listener, is the id of resource alicloud_slb_acl. If <code class="docutils literal notranslate"><span class="pre">acl_status</span></code> is “on”, it is mandatory. Otherwise, it will be ignored.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.acl_status">
<code class="sig-name descname">acl_status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.acl_status" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable “acl(access control list)”, the acl is specified by <code class="docutils literal notranslate"><span class="pre">acl_id</span></code>. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.acl_type">
<code class="sig-name descname">acl_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.acl_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Mode for handling the acl specified by acl_id. If <code class="docutils literal notranslate"><span class="pre">acl_status</span></code> is “on”, it is mandatory. Otherwise, it will be ignored. Valid values are <code class="docutils literal notranslate"><span class="pre">white</span></code> and <code class="docutils literal notranslate"><span class="pre">black</span></code>. <code class="docutils literal notranslate"><span class="pre">white</span></code> means the Listener can only be accessed by client ip belongs to the acl; <code class="docutils literal notranslate"><span class="pre">black</span></code> means the Listener can not be accessed by client ip belongs to the acl.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.backend_port">
<code class="sig-name descname">backend_port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.backend_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Port used by the Server Load Balancer instance backend. Valid value range: [1-65535].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.bandwidth">
<code class="sig-name descname">bandwidth</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.bandwidth" title="Permalink to this definition">¶</a></dt>
<dd><p>Bandwidth peak of Listener. For the public network instance charged per traffic consumed, the Bandwidth on Listener can be set to -1, indicating the bandwidth peak is unlimited. Valid values are [-1, 1-1000] in Mbps.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.cookie">
<code class="sig-name descname">cookie</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.cookie" title="Permalink to this definition">¶</a></dt>
<dd><p>The cookie configured on the server. It is mandatory when <code class="docutils literal notranslate"><span class="pre">sticky_session</span></code> is “on” and <code class="docutils literal notranslate"><span class="pre">sticky_session_type</span></code> is “server”. Otherwise, it will be ignored. Valid value：String in line with RFC 2965, with length being 1- 200. It only contains characters such as ASCII codes, English letters and digits instead of the comma, semicolon or spacing, and it cannot start with $.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.cookie_timeout">
<code class="sig-name descname">cookie_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.cookie_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Cookie timeout. It is mandatory when <code class="docutils literal notranslate"><span class="pre">sticky_session</span></code> is “on” and <code class="docutils literal notranslate"><span class="pre">sticky_session_type</span></code> is “insert”. Otherwise, it will be ignored. Valid value range: [1-86400] in seconds.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.delete_protection_validation">
<code class="sig-name descname">delete_protection_validation</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.delete_protection_validation" title="Permalink to this definition">¶</a></dt>
<dd><p>Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of slb listener. This description can have a string of 1 to 80 characters. Default value: null.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.enable_http2">
<code class="sig-name descname">enable_http2</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.enable_http2" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable https listener support http2 or not. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">on</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.established_timeout">
<code class="sig-name descname">established_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.established_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Timeout of tcp listener established connection idle timeout. Valid value range: [10-900] in seconds. Default to 900.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.forward_port">
<code class="sig-name descname">forward_port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.forward_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port that http redirect to https.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.frontend_port">
<code class="sig-name descname">frontend_port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.frontend_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Port used by the Server Load Balancer instance frontend. Valid value range: [1-65535].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.gzip">
<code class="sig-name descname">gzip</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.gzip" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable “Gzip Compression”. If enabled, files of specific file types will be compressed, otherwise, no files will be compressed. Default to true. Available in v1.13.0+.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.health_check">
<code class="sig-name descname">health_check</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.health_check" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable health check. Valid values are<code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. TCP and UDP listener’s HealthCheck is always on, so it will be ignore when launching TCP or UDP listener.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.health_check_connect_port">
<code class="sig-name descname">health_check_connect_port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.health_check_connect_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Port used for health check. Valid value range: [1-65535]. Default to “None” means the backend server port is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.health_check_domain">
<code class="sig-name descname">health_check_domain</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.health_check_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain name used for health check. When it used to launch TCP listener, <code class="docutils literal notranslate"><span class="pre">health_check_type</span></code> must be “http”. Its length is limited to 1-80 and only characters such as letters, digits, ‘-‘ and ‘.’ are allowed. When it is not set or empty,  Server Load Balancer uses the private network IP address of each backend server as Domain used for health check.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.health_check_http_code">
<code class="sig-name descname">health_check_http_code</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.health_check_http_code" title="Permalink to this definition">¶</a></dt>
<dd><p>Regular health check HTTP status code. Multiple codes are segmented by “,”. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Default to <code class="docutils literal notranslate"><span class="pre">http_2xx</span></code>.  Valid values are: <code class="docutils literal notranslate"><span class="pre">http_2xx</span></code>,  <code class="docutils literal notranslate"><span class="pre">http_3xx</span></code>, <code class="docutils literal notranslate"><span class="pre">http_4xx</span></code> and <code class="docutils literal notranslate"><span class="pre">http_5xx</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.health_check_interval">
<code class="sig-name descname">health_check_interval</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.health_check_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>Time interval of health checks. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Valid value range: [1-50] in seconds. Default to 2.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.health_check_method">
<code class="sig-name descname">health_check_method</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.health_check_method" title="Permalink to this definition">¶</a></dt>
<dd><p>The method of health check. Valid values: [“head”, “get”].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.health_check_timeout">
<code class="sig-name descname">health_check_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.health_check_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum timeout of each health check response. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Valid value range: [1-300] in seconds. Default to 5. Note: If <code class="docutils literal notranslate"><span class="pre">health_check_timeout</span></code> &lt; <code class="docutils literal notranslate"><span class="pre">health_check_interval</span></code>, its will be replaced by <code class="docutils literal notranslate"><span class="pre">health_check_interval</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.health_check_type">
<code class="sig-name descname">health_check_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.health_check_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of health check. Valid values are: <code class="docutils literal notranslate"><span class="pre">tcp</span></code> and <code class="docutils literal notranslate"><span class="pre">http</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">tcp</span></code> . TCP supports TCP and HTTP health check mode, you can select the particular mode depending on your application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.health_check_uri">
<code class="sig-name descname">health_check_uri</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.health_check_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI used for health check. When it used to launch TCP listener, <code class="docutils literal notranslate"><span class="pre">health_check_type</span></code> must be “http”. Its length is limited to 1-80 and it must start with /. Only characters such as letters, digits, ‘-’, ‘/’, ‘.’, ‘%’, ‘?’, #’ and ‘&amp;’ are allowed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.healthy_threshold">
<code class="sig-name descname">healthy_threshold</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.healthy_threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>Threshold determining the result of the health check is success. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Valid value range: [1-10] in seconds. Default to 3.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.idle_timeout">
<code class="sig-name descname">idle_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.idle_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Timeout of http or https listener established connection idle timeout. Valid value range: [1-60] in seconds. Default to 15.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.listener_forward">
<code class="sig-name descname">listener_forward</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.listener_forward" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable http redirect to https, Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.load_balancer_id">
<code class="sig-name descname">load_balancer_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.load_balancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Load Balancer ID which is used to launch a new listener.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.persistence_timeout">
<code class="sig-name descname">persistence_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.persistence_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Timeout of connection persistence. Valid value range: [0-3600] in seconds. Default to 0 and means closing it.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.protocol">
<code class="sig-name descname">protocol</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol to listen on. Valid values are [<code class="docutils literal notranslate"><span class="pre">http</span></code>, <code class="docutils literal notranslate"><span class="pre">https</span></code>, <code class="docutils literal notranslate"><span class="pre">tcp</span></code>, <code class="docutils literal notranslate"><span class="pre">udp</span></code>].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.request_timeout">
<code class="sig-name descname">request_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.request_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Timeout of http or https listener request (which does not get response from backend) timeout. Valid value range: [1-180] in seconds. Default to 60.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.scheduler">
<code class="sig-name descname">scheduler</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.scheduler" title="Permalink to this definition">¶</a></dt>
<dd><p>Scheduling algorithm, Valid values are <code class="docutils literal notranslate"><span class="pre">wrr</span></code>, <code class="docutils literal notranslate"><span class="pre">rr</span></code> and <code class="docutils literal notranslate"><span class="pre">wlc</span></code>.  Default to “wrr”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.server_certificate_id">
<code class="sig-name descname">server_certificate_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.server_certificate_id" title="Permalink to this definition">¶</a></dt>
<dd><p>SLB Server certificate ID. It is required when <code class="docutils literal notranslate"><span class="pre">protocol</span></code> is <code class="docutils literal notranslate"><span class="pre">https</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.server_group_id">
<code class="sig-name descname">server_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.server_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>the id of server group to be apply on the listener, is the id of resource <code class="docutils literal notranslate"><span class="pre">slb.ServerGroup</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.ssl_certificate_id">
<code class="sig-name descname">ssl_certificate_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.ssl_certificate_id" title="Permalink to this definition">¶</a></dt>
<dd><p>It has been deprecated from 1.59.0 and using <code class="docutils literal notranslate"><span class="pre">server_certificate_id</span></code> instead.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.sticky_session">
<code class="sig-name descname">sticky_session</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.sticky_session" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable session persistence, Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.sticky_session_type">
<code class="sig-name descname">sticky_session_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.sticky_session_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Mode for handling the cookie. If <code class="docutils literal notranslate"><span class="pre">sticky_session</span></code> is “on”, it is mandatory. Otherwise, it will be ignored. Valid values are <code class="docutils literal notranslate"><span class="pre">insert</span></code> and <code class="docutils literal notranslate"><span class="pre">server</span></code>. <code class="docutils literal notranslate"><span class="pre">insert</span></code> means it is inserted from Server Load Balancer; <code class="docutils literal notranslate"><span class="pre">server</span></code> means the Server Load Balancer learns from the backend server.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.tls_cipher_policy">
<code class="sig-name descname">tls_cipher_policy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.tls_cipher_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Https listener TLS cipher policy. Valid values are <code class="docutils literal notranslate"><span class="pre">tls_cipher_policy_1_0</span></code>, <code class="docutils literal notranslate"><span class="pre">tls_cipher_policy_1_1</span></code>, <code class="docutils literal notranslate"><span class="pre">tls_cipher_policy_1_2</span></code>, <code class="docutils literal notranslate"><span class="pre">tls_cipher_policy_1_2_strict</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">tls_cipher_policy_1_0</span></code>. Currently the <code class="docutils literal notranslate"><span class="pre">tls_cipher_policy</span></code> can not be updated when load balancer instance is “Shared-Performance”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.unhealthy_threshold">
<code class="sig-name descname">unhealthy_threshold</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.unhealthy_threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>Threshold determining the result of the health check is fail. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Valid value range: [1-10] in seconds. Default to 3.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Listener.x_forwarded_for">
<code class="sig-name descname">x_forwarded_for</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Listener.x_forwarded_for" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to set additional HTTP Header field “X-Forwarded-For” (documented below). Available in v1.13.0+.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">retriveClientIp</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retriveSlbId</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to use the XForwardedFor header to obtain the ID of the SLB instance. Default to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retriveSlbIp</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to use the XForwardedFor_SLBIP header to obtain the public IP address of the SLB instance. Default to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retriveSlbProto</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to use the XForwardedFor_proto header to obtain the protocol used by the listener. Default to false.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.slb.Listener.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bandwidth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cookie</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cookie_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_protection_validation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_http2</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">established_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">forward_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frontend_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gzip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_connect_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_http_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_interval</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">healthy_threshold</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">idle_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lb_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lb_protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">listener_forward</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_slave_server_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">persistence_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduler</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_certificate_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_certificate_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sticky_session</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sticky_session_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_cipher_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unhealthy_threshold</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">x_forwarded_for</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.Listener.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Listener resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the id of access control list to be apply on the listener, is the id of resource alicloud_slb_acl. If <code class="docutils literal notranslate"><span class="pre">acl_status</span></code> is “on”, it is mandatory. Otherwise, it will be ignored.</p></li>
<li><p><strong>acl_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether to enable “acl(access control list)”, the acl is specified by <code class="docutils literal notranslate"><span class="pre">acl_id</span></code>. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>acl_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Mode for handling the acl specified by acl_id. If <code class="docutils literal notranslate"><span class="pre">acl_status</span></code> is “on”, it is mandatory. Otherwise, it will be ignored. Valid values are <code class="docutils literal notranslate"><span class="pre">white</span></code> and <code class="docutils literal notranslate"><span class="pre">black</span></code>. <code class="docutils literal notranslate"><span class="pre">white</span></code> means the Listener can only be accessed by client ip belongs to the acl; <code class="docutils literal notranslate"><span class="pre">black</span></code> means the Listener can not be accessed by client ip belongs to the acl.</p></li>
<li><p><strong>backend_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Port used by the Server Load Balancer instance backend. Valid value range: [1-65535].</p></li>
<li><p><strong>bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Bandwidth peak of Listener. For the public network instance charged per traffic consumed, the Bandwidth on Listener can be set to -1, indicating the bandwidth peak is unlimited. Valid values are [-1, 1-1000] in Mbps.</p></li>
<li><p><strong>cookie</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cookie configured on the server. It is mandatory when <code class="docutils literal notranslate"><span class="pre">sticky_session</span></code> is “on” and <code class="docutils literal notranslate"><span class="pre">sticky_session_type</span></code> is “server”. Otherwise, it will be ignored. Valid value：String in line with RFC 2965, with length being 1- 200. It only contains characters such as ASCII codes, English letters and digits instead of the comma, semicolon or spacing, and it cannot start with $.</p></li>
<li><p><strong>cookie_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Cookie timeout. It is mandatory when <code class="docutils literal notranslate"><span class="pre">sticky_session</span></code> is “on” and <code class="docutils literal notranslate"><span class="pre">sticky_session_type</span></code> is “insert”. Otherwise, it will be ignored. Valid value range: [1-86400] in seconds.</p></li>
<li><p><strong>delete_protection_validation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of slb listener. This description can have a string of 1 to 80 characters. Default value: null.</p></li>
<li><p><strong>enable_http2</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether to enable https listener support http2 or not. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">on</span></code>.</p></li>
<li><p><strong>established_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout of tcp listener established connection idle timeout. Valid value range: [10-900] in seconds. Default to 900.</p></li>
<li><p><strong>forward_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port that http redirect to https.</p></li>
<li><p><strong>frontend_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Port used by the Server Load Balancer instance frontend. Valid value range: [1-65535].</p></li>
<li><p><strong>gzip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable “Gzip Compression”. If enabled, files of specific file types will be compressed, otherwise, no files will be compressed. Default to true. Available in v1.13.0+.</p></li>
<li><p><strong>health_check</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether to enable health check. Valid values are<code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. TCP and UDP listener’s HealthCheck is always on, so it will be ignore when launching TCP or UDP listener.</p></li>
<li><p><strong>health_check_connect_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Port used for health check. Valid value range: [1-65535]. Default to “None” means the backend server port is used.</p></li>
<li><p><strong>health_check_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain name used for health check. When it used to launch TCP listener, <code class="docutils literal notranslate"><span class="pre">health_check_type</span></code> must be “http”. Its length is limited to 1-80 and only characters such as letters, digits, ‘-‘ and ‘.’ are allowed. When it is not set or empty,  Server Load Balancer uses the private network IP address of each backend server as Domain used for health check.</p></li>
<li><p><strong>health_check_http_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Regular health check HTTP status code. Multiple codes are segmented by “,”. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Default to <code class="docutils literal notranslate"><span class="pre">http_2xx</span></code>.  Valid values are: <code class="docutils literal notranslate"><span class="pre">http_2xx</span></code>,  <code class="docutils literal notranslate"><span class="pre">http_3xx</span></code>, <code class="docutils literal notranslate"><span class="pre">http_4xx</span></code> and <code class="docutils literal notranslate"><span class="pre">http_5xx</span></code>.</p></li>
<li><p><strong>health_check_interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time interval of health checks. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Valid value range: [1-50] in seconds. Default to 2.</p></li>
<li><p><strong>health_check_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method of health check. Valid values: [“head”, “get”].</p></li>
<li><p><strong>health_check_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum timeout of each health check response. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Valid value range: [1-300] in seconds. Default to 5. Note: If <code class="docutils literal notranslate"><span class="pre">health_check_timeout</span></code> &lt; <code class="docutils literal notranslate"><span class="pre">health_check_interval</span></code>, its will be replaced by <code class="docutils literal notranslate"><span class="pre">health_check_interval</span></code>.</p></li>
<li><p><strong>health_check_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of health check. Valid values are: <code class="docutils literal notranslate"><span class="pre">tcp</span></code> and <code class="docutils literal notranslate"><span class="pre">http</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">tcp</span></code> . TCP supports TCP and HTTP health check mode, you can select the particular mode depending on your application.</p></li>
<li><p><strong>health_check_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI used for health check. When it used to launch TCP listener, <code class="docutils literal notranslate"><span class="pre">health_check_type</span></code> must be “http”. Its length is limited to 1-80 and it must start with /. Only characters such as letters, digits, ‘-’, ‘/’, ‘.’, ‘%’, ‘?’, #’ and ‘&amp;’ are allowed.</p></li>
<li><p><strong>healthy_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Threshold determining the result of the health check is success. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Valid value range: [1-10] in seconds. Default to 3.</p></li>
<li><p><strong>idle_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout of http or https listener established connection idle timeout. Valid value range: [1-60] in seconds. Default to 15.</p></li>
<li><p><strong>listener_forward</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether to enable http redirect to https, Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>load_balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Load Balancer ID which is used to launch a new listener.</p></li>
<li><p><strong>persistence_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout of connection persistence. Valid value range: [0-3600] in seconds. Default to 0 and means closing it.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol to listen on. Valid values are [<code class="docutils literal notranslate"><span class="pre">http</span></code>, <code class="docutils literal notranslate"><span class="pre">https</span></code>, <code class="docutils literal notranslate"><span class="pre">tcp</span></code>, <code class="docutils literal notranslate"><span class="pre">udp</span></code>].</p></li>
<li><p><strong>request_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout of http or https listener request (which does not get response from backend) timeout. Valid value range: [1-180] in seconds. Default to 60.</p></li>
<li><p><strong>scheduler</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Scheduling algorithm, Valid values are <code class="docutils literal notranslate"><span class="pre">wrr</span></code>, <code class="docutils literal notranslate"><span class="pre">rr</span></code> and <code class="docutils literal notranslate"><span class="pre">wlc</span></code>.  Default to “wrr”.</p></li>
<li><p><strong>server_certificate_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SLB Server certificate ID. It is required when <code class="docutils literal notranslate"><span class="pre">protocol</span></code> is <code class="docutils literal notranslate"><span class="pre">https</span></code>.</p></li>
<li><p><strong>server_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the id of server group to be apply on the listener, is the id of resource <code class="docutils literal notranslate"><span class="pre">slb.ServerGroup</span></code>.</p></li>
<li><p><strong>ssl_certificate_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – It has been deprecated from 1.59.0 and using <code class="docutils literal notranslate"><span class="pre">server_certificate_id</span></code> instead.</p></li>
<li><p><strong>sticky_session</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether to enable session persistence, Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>sticky_session_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Mode for handling the cookie. If <code class="docutils literal notranslate"><span class="pre">sticky_session</span></code> is “on”, it is mandatory. Otherwise, it will be ignored. Valid values are <code class="docutils literal notranslate"><span class="pre">insert</span></code> and <code class="docutils literal notranslate"><span class="pre">server</span></code>. <code class="docutils literal notranslate"><span class="pre">insert</span></code> means it is inserted from Server Load Balancer; <code class="docutils literal notranslate"><span class="pre">server</span></code> means the Server Load Balancer learns from the backend server.</p></li>
<li><p><strong>tls_cipher_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Https listener TLS cipher policy. Valid values are <code class="docutils literal notranslate"><span class="pre">tls_cipher_policy_1_0</span></code>, <code class="docutils literal notranslate"><span class="pre">tls_cipher_policy_1_1</span></code>, <code class="docutils literal notranslate"><span class="pre">tls_cipher_policy_1_2</span></code>, <code class="docutils literal notranslate"><span class="pre">tls_cipher_policy_1_2_strict</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">tls_cipher_policy_1_0</span></code>. Currently the <code class="docutils literal notranslate"><span class="pre">tls_cipher_policy</span></code> can not be updated when load balancer instance is “Shared-Performance”.</p></li>
<li><p><strong>unhealthy_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Threshold determining the result of the health check is fail. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Valid value range: [1-10] in seconds. Default to 3.</p></li>
<li><p><strong>x_forwarded_for</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Whether to set additional HTTP Header field “X-Forwarded-For” (documented below). Available in v1.13.0+.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>x_forwarded_for</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">retriveClientIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retriveSlbId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use the XForwardedFor header to obtain the ID of the SLB instance. Default to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retriveSlbIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use the XForwardedFor_SLBIP header to obtain the public IP address of the SLB instance. Default to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retriveSlbProto</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use the XForwardedFor_proto header to obtain the protocol used by the listener. Default to false.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.slb.Listener.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.Listener.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.slb.Listener.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.Listener.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.slb.LoadBalancer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">LoadBalancer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_ip_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bandwidth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_protection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slave_zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">specification</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.LoadBalancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Application Load Balancer resource.</p>
<blockquote>
<div><p><strong>NOTE:</strong> At present, to avoid some unnecessary regulation confusion, SLB can not support alicloud international account to create “paybybandwidth” instance.</p>
<p><strong>NOTE:</strong> The supported specifications vary by region. Currently not all regions support guaranteed-performance instances.
For more details about guaranteed-performance instance, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/27657.htm">Guaranteed-performance instances</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the IP address of the private network for the SLB instance, which must be in the destination CIDR block of the correspond ing switch.</p></li>
<li><p><strong>address_ip_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP version of the SLB instance to be created, which can be set to ipv4 or ipv6 . Default to “ipv4”. Now, only internet instance support ipv6 address.</p></li>
<li><p><strong>address_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The network type of the SLB instance. Valid values: [“internet”, “intranet”]. If load balancer launched in VPC, this value must be “intranet”.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">internet</span><span class="p">:</span> <span class="n">After</span> <span class="n">an</span> <span class="n">Internet</span> <span class="n">SLB</span> <span class="n">instance</span> <span class="ow">is</span> <span class="n">created</span><span class="p">,</span> <span class="n">the</span> <span class="n">system</span> <span class="n">allocates</span> <span class="n">a</span> <span class="n">public</span> <span class="n">IP</span> <span class="n">address</span> <span class="n">so</span> <span class="n">that</span> <span class="n">the</span> <span class="n">instance</span> <span class="n">can</span> <span class="n">forward</span> <span class="n">requests</span> <span class="kn">from</span> <span class="nn">the</span> <span class="n">Internet</span><span class="o">.</span>
<span class="o">-</span> <span class="n">intranet</span><span class="p">:</span> <span class="n">After</span> <span class="n">an</span> <span class="n">intranet</span> <span class="n">SLB</span> <span class="n">instance</span> <span class="ow">is</span> <span class="n">created</span><span class="p">,</span> <span class="n">the</span> <span class="n">system</span> <span class="n">allocates</span> <span class="n">an</span> <span class="n">intranet</span> <span class="n">IP</span> <span class="n">address</span> <span class="n">so</span> <span class="n">that</span> <span class="n">the</span> <span class="n">instance</span> <span class="n">can</span> <span class="n">only</span> <span class="n">forward</span> <span class="n">intranet</span> <span class="n">requests</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Valid
value is between 1 and 1000, If argument “internet_charge_type” is “paybytraffic”, then this value will be ignore.</p></li>
<li><p><strong>delete_protection</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether enable the deletion protection or not. on: Enable deletion protection. off: Disable deletion protection. Default to off. Only postpaid instance support this function.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The billing method of the load balancer. Valid values are “PrePaid” and “PostPaid”. Default to “PostPaid”.</p></li>
<li><p><strong>internet</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Field ‘internet’ has been deprecated from provider version 1.55.3. Use ‘address_type’ replaces it.</p></li>
<li><p><strong>internet_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid
values are <code class="docutils literal notranslate"><span class="pre">PayByBandwidth</span></code>, <code class="docutils literal notranslate"><span class="pre">PayByTraffic</span></code>. If this value is “PayByBandwidth”, then argument “internet” must be “true”. Default is “PayByTraffic”. If load balancer launched in VPC, this value must be “PayByTraffic”.
Before version 1.10.1, the valid values are “paybybandwidth” and “paybytraffic”.</p></li>
<li><p><strong>master_zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The primary zone ID of the SLB instance. If not specified, the system will be randomly assigned. You can query the primary and standby zones in a region by calling the DescribeZone API.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration that you will buy the resource, in month. It is valid when <code class="docutils literal notranslate"><span class="pre">instance_charge_type</span></code> is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Default to 1. Valid values: [1-9, 12, 24, 36].</p></li>
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of resource group which the SLB belongs.</p></li>
<li><p><strong>slave_zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The standby zone ID of the SLB instance. If not specified, the system will be randomly assigned. You can query the primary and standby zones in a region by calling the DescribeZone API.</p></li>
<li><p><strong>specification</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The specification of the Server Load Balancer instance. Default to empty string indicating it is “Shared-Performance” instance.
Launching “<a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/27657.htm">Performance-guaranteed</a>” instance, it is must be specified and it valid values are: “slb.s1.small”, “slb.s2.small”, “slb.s2.medium”,
“slb.s3.small”, “slb.s3.medium”, “slb.s3.large” and “slb.s4.large”.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource. The <code class="docutils literal notranslate"><span class="pre">tags</span></code> can have a maximum of 10 tag for every load balancer instance.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VSwitch ID to launch in. If <code class="docutils literal notranslate"><span class="pre">address_type</span></code> is internet, it will be ignore.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.slb.LoadBalancer.address">
<code class="sig-name descname">address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.LoadBalancer.address" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify the IP address of the private network for the SLB instance, which must be in the destination CIDR block of the correspond ing switch.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.LoadBalancer.address_ip_version">
<code class="sig-name descname">address_ip_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.LoadBalancer.address_ip_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP version of the SLB instance to be created, which can be set to ipv4 or ipv6 . Default to “ipv4”. Now, only internet instance support ipv6 address.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.LoadBalancer.address_type">
<code class="sig-name descname">address_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.LoadBalancer.address_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The network type of the SLB instance. Valid values: [“internet”, “intranet”]. If load balancer launched in VPC, this value must be “intranet”.</p>
<ul class="simple">
<li><p>internet: After an Internet SLB instance is created, the system allocates a public IP address so that the instance can forward requests from the Internet.</p></li>
<li><p>intranet: After an intranet SLB instance is created, the system allocates an intranet IP address so that the instance can only forward intranet requests.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.LoadBalancer.bandwidth">
<code class="sig-name descname">bandwidth</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.LoadBalancer.bandwidth" title="Permalink to this definition">¶</a></dt>
<dd><p>Valid
value is between 1 and 1000, If argument “internet_charge_type” is “paybytraffic”, then this value will be ignore.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.LoadBalancer.delete_protection">
<code class="sig-name descname">delete_protection</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.LoadBalancer.delete_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether enable the deletion protection or not. on: Enable deletion protection. off: Disable deletion protection. Default to off. Only postpaid instance support this function.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.LoadBalancer.instance_charge_type">
<code class="sig-name descname">instance_charge_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.LoadBalancer.instance_charge_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The billing method of the load balancer. Valid values are “PrePaid” and “PostPaid”. Default to “PostPaid”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.LoadBalancer.internet">
<code class="sig-name descname">internet</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.LoadBalancer.internet" title="Permalink to this definition">¶</a></dt>
<dd><p>Field ‘internet’ has been deprecated from provider version 1.55.3. Use ‘address_type’ replaces it.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.LoadBalancer.internet_charge_type">
<code class="sig-name descname">internet_charge_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.LoadBalancer.internet_charge_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Valid
values are <code class="docutils literal notranslate"><span class="pre">PayByBandwidth</span></code>, <code class="docutils literal notranslate"><span class="pre">PayByTraffic</span></code>. If this value is “PayByBandwidth”, then argument “internet” must be “true”. Default is “PayByTraffic”. If load balancer launched in VPC, this value must be “PayByTraffic”.
Before version 1.10.1, the valid values are “paybybandwidth” and “paybytraffic”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.LoadBalancer.master_zone_id">
<code class="sig-name descname">master_zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.LoadBalancer.master_zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary zone ID of the SLB instance. If not specified, the system will be randomly assigned. You can query the primary and standby zones in a region by calling the DescribeZone API.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.LoadBalancer.period">
<code class="sig-name descname">period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.LoadBalancer.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The duration that you will buy the resource, in month. It is valid when <code class="docutils literal notranslate"><span class="pre">instance_charge_type</span></code> is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Default to 1. Valid values: [1-9, 12, 24, 36].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.LoadBalancer.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.LoadBalancer.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of resource group which the SLB belongs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.LoadBalancer.slave_zone_id">
<code class="sig-name descname">slave_zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.LoadBalancer.slave_zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The standby zone ID of the SLB instance. If not specified, the system will be randomly assigned. You can query the primary and standby zones in a region by calling the DescribeZone API.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.LoadBalancer.specification">
<code class="sig-name descname">specification</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.LoadBalancer.specification" title="Permalink to this definition">¶</a></dt>
<dd><p>The specification of the Server Load Balancer instance. Default to empty string indicating it is “Shared-Performance” instance.
Launching “<a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/27657.htm">Performance-guaranteed</a>” instance, it is must be specified and it valid values are: “slb.s1.small”, “slb.s2.small”, “slb.s2.medium”,
“slb.s3.small”, “slb.s3.medium”, “slb.s3.large” and “slb.s4.large”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.LoadBalancer.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.LoadBalancer.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource. The <code class="docutils literal notranslate"><span class="pre">tags</span></code> can have a maximum of 10 tag for every load balancer instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.LoadBalancer.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.LoadBalancer.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VSwitch ID to launch in. If <code class="docutils literal notranslate"><span class="pre">address_type</span></code> is internet, it will be ignore.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.slb.LoadBalancer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_ip_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bandwidth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_protection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slave_zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">specification</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.LoadBalancer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LoadBalancer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the IP address of the private network for the SLB instance, which must be in the destination CIDR block of the correspond ing switch.</p></li>
<li><p><strong>address_ip_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP version of the SLB instance to be created, which can be set to ipv4 or ipv6 . Default to “ipv4”. Now, only internet instance support ipv6 address.</p></li>
<li><p><strong>address_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The network type of the SLB instance. Valid values: [“internet”, “intranet”]. If load balancer launched in VPC, this value must be “intranet”.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">internet</span><span class="p">:</span> <span class="n">After</span> <span class="n">an</span> <span class="n">Internet</span> <span class="n">SLB</span> <span class="n">instance</span> <span class="ow">is</span> <span class="n">created</span><span class="p">,</span> <span class="n">the</span> <span class="n">system</span> <span class="n">allocates</span> <span class="n">a</span> <span class="n">public</span> <span class="n">IP</span> <span class="n">address</span> <span class="n">so</span> <span class="n">that</span> <span class="n">the</span> <span class="n">instance</span> <span class="n">can</span> <span class="n">forward</span> <span class="n">requests</span> <span class="kn">from</span> <span class="nn">the</span> <span class="n">Internet</span><span class="o">.</span>
<span class="o">-</span> <span class="n">intranet</span><span class="p">:</span> <span class="n">After</span> <span class="n">an</span> <span class="n">intranet</span> <span class="n">SLB</span> <span class="n">instance</span> <span class="ow">is</span> <span class="n">created</span><span class="p">,</span> <span class="n">the</span> <span class="n">system</span> <span class="n">allocates</span> <span class="n">an</span> <span class="n">intranet</span> <span class="n">IP</span> <span class="n">address</span> <span class="n">so</span> <span class="n">that</span> <span class="n">the</span> <span class="n">instance</span> <span class="n">can</span> <span class="n">only</span> <span class="n">forward</span> <span class="n">intranet</span> <span class="n">requests</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Valid
value is between 1 and 1000, If argument “internet_charge_type” is “paybytraffic”, then this value will be ignore.</p></li>
<li><p><strong>delete_protection</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether enable the deletion protection or not. on: Enable deletion protection. off: Disable deletion protection. Default to off. Only postpaid instance support this function.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The billing method of the load balancer. Valid values are “PrePaid” and “PostPaid”. Default to “PostPaid”.</p></li>
<li><p><strong>internet</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Field ‘internet’ has been deprecated from provider version 1.55.3. Use ‘address_type’ replaces it.</p></li>
<li><p><strong>internet_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid
values are <code class="docutils literal notranslate"><span class="pre">PayByBandwidth</span></code>, <code class="docutils literal notranslate"><span class="pre">PayByTraffic</span></code>. If this value is “PayByBandwidth”, then argument “internet” must be “true”. Default is “PayByTraffic”. If load balancer launched in VPC, this value must be “PayByTraffic”.
Before version 1.10.1, the valid values are “paybybandwidth” and “paybytraffic”.</p></li>
<li><p><strong>master_zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The primary zone ID of the SLB instance. If not specified, the system will be randomly assigned. You can query the primary and standby zones in a region by calling the DescribeZone API.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration that you will buy the resource, in month. It is valid when <code class="docutils literal notranslate"><span class="pre">instance_charge_type</span></code> is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Default to 1. Valid values: [1-9, 12, 24, 36].</p></li>
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of resource group which the SLB belongs.</p></li>
<li><p><strong>slave_zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The standby zone ID of the SLB instance. If not specified, the system will be randomly assigned. You can query the primary and standby zones in a region by calling the DescribeZone API.</p></li>
<li><p><strong>specification</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The specification of the Server Load Balancer instance. Default to empty string indicating it is “Shared-Performance” instance.
Launching “<a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/27657.htm">Performance-guaranteed</a>” instance, it is must be specified and it valid values are: “slb.s1.small”, “slb.s2.small”, “slb.s2.medium”,
“slb.s3.small”, “slb.s3.medium”, “slb.s3.large” and “slb.s4.large”.</p>
</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource. The <code class="docutils literal notranslate"><span class="pre">tags</span></code> can have a maximum of 10 tag for every load balancer instance.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VSwitch ID to launch in. If <code class="docutils literal notranslate"><span class="pre">address_type</span></code> is internet, it will be ignore.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.slb.LoadBalancer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.LoadBalancer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.slb.LoadBalancer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.LoadBalancer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.slb.MasterSlaveServerGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">MasterSlaveServerGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_protection_validation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.MasterSlaveServerGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>A master slave server group contains two ECS instances. The master slave server group can help you to define multiple listening dimension.</p>
<blockquote>
<div><p><strong>NOTE:</strong> One ECS instance can be added into multiple master slave server groups.</p>
<p><strong>NOTE:</strong> One master slave server group can only add two ECS instances, which are master server and slave server.</p>
<p><strong>NOTE:</strong> One master slave server group can be attached with tcp/udp listeners in one load balancer.</p>
<p><strong>NOTE:</strong> One Classic and Internet load balancer, its master slave server group can add Classic and VPC ECS instances.</p>
<p><strong>NOTE:</strong> One Classic and Intranet load balancer, its master slave server group can only add Classic ECS instances.</p>
<p><strong>NOTE:</strong> One VPC load balancer, its master slave server group can only add the same VPC ECS instances.</p>
<p><strong>NOTE:</strong> Available in 1.54.0+</p>
</div></blockquote>
<p>The servers mapping supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">server_ids</span></code> - (Required) A list backend server ID (ECS instance ID).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> - (Required) The port used by the backend server. Valid value range: [1-65535].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> - (Optional) Weight of the backend server. Valid value range: [0-100]. Default to 100.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> - (Optional, Available in 1.51.0+) Type of the backend server. Valid value ecs, eni. Default to eni.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server_type</span></code> - (Optional) The server type of the backend server. Valid value Master, Slave.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">is_backup</span></code> - (Removed from v1.63.0) Determine if the server is executing. Valid value 0, 1.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>delete_protection_validation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.</p></li>
<li><p><strong>load_balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Load Balancer ID which is used to launch a new master slave server group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the master slave server group.</p></li>
<li><p><strong>servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of ECS instances to be added. Only two ECS instances can be supported in one resource. It contains six sub-fields as <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">server</span></code> follows.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>servers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.slb.MasterSlaveServerGroup.delete_protection_validation">
<code class="sig-name descname">delete_protection_validation</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.MasterSlaveServerGroup.delete_protection_validation" title="Permalink to this definition">¶</a></dt>
<dd><p>Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.MasterSlaveServerGroup.load_balancer_id">
<code class="sig-name descname">load_balancer_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.MasterSlaveServerGroup.load_balancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Load Balancer ID which is used to launch a new master slave server group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.MasterSlaveServerGroup.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.MasterSlaveServerGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the master slave server group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.MasterSlaveServerGroup.servers">
<code class="sig-name descname">servers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.MasterSlaveServerGroup.servers" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of ECS instances to be added. Only two ECS instances can be supported in one resource. It contains six sub-fields as <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">server</span></code> follows.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.slb.MasterSlaveServerGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_protection_validation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">servers</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.MasterSlaveServerGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MasterSlaveServerGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>delete_protection_validation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.</p></li>
<li><p><strong>load_balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Load Balancer ID which is used to launch a new master slave server group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the master slave server group.</p></li>
<li><p><strong>servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of ECS instances to be added. Only two ECS instances can be supported in one resource. It contains six sub-fields as <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">server</span></code> follows.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>servers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.slb.MasterSlaveServerGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.MasterSlaveServerGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.slb.MasterSlaveServerGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.MasterSlaveServerGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.slb.Rule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">Rule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cookie</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cookie_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_protection_validation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frontend_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_connect_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_http_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_interval</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">healthy_threshold</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">listener_sync</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduler</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sticky_session</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sticky_session_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unhealthy_threshold</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.Rule" title="Permalink to this definition">¶</a></dt>
<dd><p>A forwarding rule is configured in <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>/<code class="docutils literal notranslate"><span class="pre">HTTPS</span></code> listener and it used to listen a list of backend servers which in one specified virtual backend server group.
You can add forwarding rules to a listener to forward requests based on the domain names or the URL in the request.</p>
<blockquote>
<div><p><strong>NOTE:</strong> One virtual backend server group can be attached in multiple forwarding rules.</p>
<p><strong>NOTE:</strong> At least one “Domain” or “Url” must be specified when creating a new rule.</p>
<p><strong>NOTE:</strong> Having the same ‘Domain’ and ‘Url’ rule can not be created repeatedly in the one listener.</p>
<p><strong>NOTE:</strong> Rule only be created in the <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> or <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code> listener.</p>
<p><strong>NOTE:</strong> Only rule’s virtual server group can be modified.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cookie</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cookie configured on the server. It is mandatory when <code class="docutils literal notranslate"><span class="pre">sticky_session</span></code> is “on” and <code class="docutils literal notranslate"><span class="pre">sticky_session_type</span></code> is “server”. Otherwise, it will be ignored. Valid value：String in line with RFC 2965, with length being 1- 200. It only contains characters such as ASCII codes, English letters and digits instead of the comma, semicolon or spacing, and it cannot start with $.</p></li>
<li><p><strong>cookie_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Cookie timeout. It is mandatory when <code class="docutils literal notranslate"><span class="pre">sticky_session</span></code> is “on” and <code class="docutils literal notranslate"><span class="pre">sticky_session_type</span></code> is “insert”. Otherwise, it will be ignored. Valid value range: [1-86400] in seconds.</p></li>
<li><p><strong>delete_protection_validation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain name of the forwarding rule. It can contain letters a-z, numbers 0-9, hyphens (-), and periods (.),
and wildcard characters. The following two domain name formats are supported:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Standard</span> <span class="n">domain</span> <span class="n">name</span><span class="p">:</span> <span class="n">www</span><span class="o">.</span><span class="n">test</span><span class="o">.</span><span class="n">com</span>
<span class="o">-</span> <span class="n">Wildcard</span> <span class="n">domain</span> <span class="n">name</span><span class="p">:</span> <span class="o">*.</span><span class="n">test</span><span class="o">.</span><span class="n">com</span><span class="o">.</span> <span class="n">wildcard</span> <span class="p">(</span><span class="o">*</span><span class="p">)</span> <span class="n">must</span> <span class="n">be</span> <span class="n">the</span> <span class="n">first</span> <span class="n">character</span> <span class="ow">in</span> <span class="n">the</span> <span class="nb">format</span> <span class="n">of</span> <span class="p">(</span><span class="o">*.</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>frontend_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The listener frontend port which is used to launch the new forwarding rule. Valid range: [1-65535].</p></li>
<li><p><strong>health_check</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether to enable health check. Valid values are<code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. TCP and UDP listener’s HealthCheck is always on, so it will be ignore when launching TCP or UDP listener. This parameter is required  and takes effect only when ListenerSync is set to off.</p></li>
<li><p><strong>health_check_connect_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Port used for health check. Valid value range: [1-65535]. Default to “None” means the backend server port is used.</p></li>
<li><p><strong>health_check_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain name used for health check. When it used to launch TCP listener, <code class="docutils literal notranslate"><span class="pre">health_check_type</span></code> must be “http”. Its length is limited to 1-80 and only characters such as letters, digits, ‘-‘ and ‘.’ are allowed. When it is not set or empty,  Server Load Balancer uses the private network IP address of each backend server as Domain used for health check.</p></li>
<li><p><strong>health_check_http_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Regular health check HTTP status code. Multiple codes are segmented by “,”. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Default to <code class="docutils literal notranslate"><span class="pre">http_2xx</span></code>.  Valid values are: <code class="docutils literal notranslate"><span class="pre">http_2xx</span></code>,  <code class="docutils literal notranslate"><span class="pre">http_3xx</span></code>, <code class="docutils literal notranslate"><span class="pre">http_4xx</span></code> and <code class="docutils literal notranslate"><span class="pre">http_5xx</span></code>.</p></li>
<li><p><strong>health_check_interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time interval of health checks. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Valid value range: [1-50] in seconds. Default to 2.</p></li>
<li><p><strong>health_check_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum timeout of each health check response. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Valid value range: [1-300] in seconds. Default to 5. Note: If <code class="docutils literal notranslate"><span class="pre">health_check_timeout</span></code> &lt; <code class="docutils literal notranslate"><span class="pre">health_check_interval</span></code>, its will be replaced by <code class="docutils literal notranslate"><span class="pre">health_check_interval</span></code>.</p></li>
<li><p><strong>health_check_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI used for health check. When it used to launch TCP listener, <code class="docutils literal notranslate"><span class="pre">health_check_type</span></code> must be “http”. Its length is limited to 1-80 and it must start with /. Only characters such as letters, digits, ‘-’, ‘/’, ‘.’, ‘%’, ‘?’, #’ and ‘&amp;’ are allowed.</p></li>
<li><p><strong>healthy_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Threshold determining the result of the health check is success. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Valid value range: [1-10] in seconds. Default to 3.</p></li>
<li><p><strong>listener_sync</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether a forwarding rule inherits the settings of a health check , session persistence, and scheduling algorithm from a listener. Default to on.</p></li>
<li><p><strong>load_balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Load Balancer ID which is used to launch the new forwarding rule.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the forwarding rule. Our plugin provides a default name: “tf-slb-rule”.</p></li>
<li><p><strong>scheduler</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Scheduling algorithm, Valid values are <code class="docutils literal notranslate"><span class="pre">wrr</span></code>, <code class="docutils literal notranslate"><span class="pre">rr</span></code> and <code class="docutils literal notranslate"><span class="pre">wlc</span></code>.  Default to “wrr”. This parameter is required  and takes effect only when ListenerSync is set to off.</p></li>
<li><p><strong>server_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of a virtual server group that will be forwarded.</p></li>
<li><p><strong>sticky_session</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether to enable session persistence, Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">off</span></code>. This parameter is required  and takes effect only when ListenerSync is set to off.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>sticky_session_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Mode for handling the cookie. If <code class="docutils literal notranslate"><span class="pre">sticky_session</span></code> is “on”, it is mandatory. Otherwise, it will be ignored. Valid values are <code class="docutils literal notranslate"><span class="pre">insert</span></code> and <code class="docutils literal notranslate"><span class="pre">server</span></code>. <code class="docutils literal notranslate"><span class="pre">insert</span></code> means it is inserted from Server Load Balancer; <code class="docutils literal notranslate"><span class="pre">server</span></code> means the Server Load Balancer learns from the backend server.</p></li>
<li><p><strong>unhealthy_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Threshold determining the result of the health check is fail. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Valid value range: [1-10] in seconds. Default to 3.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain of the forwarding rule. It must be 2-80 characters in length. Only letters a-z, numbers 0-9,
and characters ‘-‘ ‘/’ ‘?’ ‘%’ ‘#’ and ‘&amp;’ are allowed. URLs must be started with the character ‘/’, but cannot be ‘/’ alone.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Rule.cookie">
<code class="sig-name descname">cookie</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Rule.cookie" title="Permalink to this definition">¶</a></dt>
<dd><p>The cookie configured on the server. It is mandatory when <code class="docutils literal notranslate"><span class="pre">sticky_session</span></code> is “on” and <code class="docutils literal notranslate"><span class="pre">sticky_session_type</span></code> is “server”. Otherwise, it will be ignored. Valid value：String in line with RFC 2965, with length being 1- 200. It only contains characters such as ASCII codes, English letters and digits instead of the comma, semicolon or spacing, and it cannot start with $.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Rule.cookie_timeout">
<code class="sig-name descname">cookie_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Rule.cookie_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Cookie timeout. It is mandatory when <code class="docutils literal notranslate"><span class="pre">sticky_session</span></code> is “on” and <code class="docutils literal notranslate"><span class="pre">sticky_session_type</span></code> is “insert”. Otherwise, it will be ignored. Valid value range: [1-86400] in seconds.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Rule.delete_protection_validation">
<code class="sig-name descname">delete_protection_validation</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Rule.delete_protection_validation" title="Permalink to this definition">¶</a></dt>
<dd><p>Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Rule.domain">
<code class="sig-name descname">domain</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Rule.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain name of the forwarding rule. It can contain letters a-z, numbers 0-9, hyphens (-), and periods (.),
and wildcard characters. The following two domain name formats are supported:</p>
<ul class="simple">
<li><p>Standard domain name: www.test.com</p></li>
<li><p>Wildcard domain name: <em>.test.com. wildcard (</em>) must be the first character in the format of (<a href="#id5"><span class="problematic" id="id6">*</span></a>.)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Rule.frontend_port">
<code class="sig-name descname">frontend_port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Rule.frontend_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The listener frontend port which is used to launch the new forwarding rule. Valid range: [1-65535].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Rule.health_check">
<code class="sig-name descname">health_check</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Rule.health_check" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable health check. Valid values are<code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. TCP and UDP listener’s HealthCheck is always on, so it will be ignore when launching TCP or UDP listener. This parameter is required  and takes effect only when ListenerSync is set to off.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Rule.health_check_connect_port">
<code class="sig-name descname">health_check_connect_port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Rule.health_check_connect_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Port used for health check. Valid value range: [1-65535]. Default to “None” means the backend server port is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Rule.health_check_domain">
<code class="sig-name descname">health_check_domain</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Rule.health_check_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain name used for health check. When it used to launch TCP listener, <code class="docutils literal notranslate"><span class="pre">health_check_type</span></code> must be “http”. Its length is limited to 1-80 and only characters such as letters, digits, ‘-‘ and ‘.’ are allowed. When it is not set or empty,  Server Load Balancer uses the private network IP address of each backend server as Domain used for health check.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Rule.health_check_http_code">
<code class="sig-name descname">health_check_http_code</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Rule.health_check_http_code" title="Permalink to this definition">¶</a></dt>
<dd><p>Regular health check HTTP status code. Multiple codes are segmented by “,”. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Default to <code class="docutils literal notranslate"><span class="pre">http_2xx</span></code>.  Valid values are: <code class="docutils literal notranslate"><span class="pre">http_2xx</span></code>,  <code class="docutils literal notranslate"><span class="pre">http_3xx</span></code>, <code class="docutils literal notranslate"><span class="pre">http_4xx</span></code> and <code class="docutils literal notranslate"><span class="pre">http_5xx</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Rule.health_check_interval">
<code class="sig-name descname">health_check_interval</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Rule.health_check_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>Time interval of health checks. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Valid value range: [1-50] in seconds. Default to 2.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Rule.health_check_timeout">
<code class="sig-name descname">health_check_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Rule.health_check_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum timeout of each health check response. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Valid value range: [1-300] in seconds. Default to 5. Note: If <code class="docutils literal notranslate"><span class="pre">health_check_timeout</span></code> &lt; <code class="docutils literal notranslate"><span class="pre">health_check_interval</span></code>, its will be replaced by <code class="docutils literal notranslate"><span class="pre">health_check_interval</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Rule.health_check_uri">
<code class="sig-name descname">health_check_uri</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Rule.health_check_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI used for health check. When it used to launch TCP listener, <code class="docutils literal notranslate"><span class="pre">health_check_type</span></code> must be “http”. Its length is limited to 1-80 and it must start with /. Only characters such as letters, digits, ‘-’, ‘/’, ‘.’, ‘%’, ‘?’, #’ and ‘&amp;’ are allowed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Rule.healthy_threshold">
<code class="sig-name descname">healthy_threshold</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Rule.healthy_threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>Threshold determining the result of the health check is success. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Valid value range: [1-10] in seconds. Default to 3.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Rule.listener_sync">
<code class="sig-name descname">listener_sync</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Rule.listener_sync" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether a forwarding rule inherits the settings of a health check , session persistence, and scheduling algorithm from a listener. Default to on.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Rule.load_balancer_id">
<code class="sig-name descname">load_balancer_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Rule.load_balancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Load Balancer ID which is used to launch the new forwarding rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Rule.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Rule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the forwarding rule. Our plugin provides a default name: “tf-slb-rule”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Rule.scheduler">
<code class="sig-name descname">scheduler</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Rule.scheduler" title="Permalink to this definition">¶</a></dt>
<dd><p>Scheduling algorithm, Valid values are <code class="docutils literal notranslate"><span class="pre">wrr</span></code>, <code class="docutils literal notranslate"><span class="pre">rr</span></code> and <code class="docutils literal notranslate"><span class="pre">wlc</span></code>.  Default to “wrr”. This parameter is required  and takes effect only when ListenerSync is set to off.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Rule.server_group_id">
<code class="sig-name descname">server_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Rule.server_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of a virtual server group that will be forwarded.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Rule.sticky_session">
<code class="sig-name descname">sticky_session</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Rule.sticky_session" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable session persistence, Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">off</span></code>. This parameter is required  and takes effect only when ListenerSync is set to off.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Rule.sticky_session_type">
<code class="sig-name descname">sticky_session_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Rule.sticky_session_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Mode for handling the cookie. If <code class="docutils literal notranslate"><span class="pre">sticky_session</span></code> is “on”, it is mandatory. Otherwise, it will be ignored. Valid values are <code class="docutils literal notranslate"><span class="pre">insert</span></code> and <code class="docutils literal notranslate"><span class="pre">server</span></code>. <code class="docutils literal notranslate"><span class="pre">insert</span></code> means it is inserted from Server Load Balancer; <code class="docutils literal notranslate"><span class="pre">server</span></code> means the Server Load Balancer learns from the backend server.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Rule.unhealthy_threshold">
<code class="sig-name descname">unhealthy_threshold</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Rule.unhealthy_threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>Threshold determining the result of the health check is fail. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Valid value range: [1-10] in seconds. Default to 3.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.Rule.url">
<code class="sig-name descname">url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.Rule.url" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain of the forwarding rule. It must be 2-80 characters in length. Only letters a-z, numbers 0-9,
and characters ‘-‘ ‘/’ ‘?’ ‘%’ ‘#’ and ‘&amp;’ are allowed. URLs must be started with the character ‘/’, but cannot be ‘/’ alone.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.slb.Rule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cookie</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cookie_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_protection_validation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frontend_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_connect_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_http_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_interval</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">healthy_threshold</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">listener_sync</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduler</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sticky_session</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sticky_session_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unhealthy_threshold</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.Rule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Rule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cookie</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cookie configured on the server. It is mandatory when <code class="docutils literal notranslate"><span class="pre">sticky_session</span></code> is “on” and <code class="docutils literal notranslate"><span class="pre">sticky_session_type</span></code> is “server”. Otherwise, it will be ignored. Valid value：String in line with RFC 2965, with length being 1- 200. It only contains characters such as ASCII codes, English letters and digits instead of the comma, semicolon or spacing, and it cannot start with $.</p></li>
<li><p><strong>cookie_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Cookie timeout. It is mandatory when <code class="docutils literal notranslate"><span class="pre">sticky_session</span></code> is “on” and <code class="docutils literal notranslate"><span class="pre">sticky_session_type</span></code> is “insert”. Otherwise, it will be ignored. Valid value range: [1-86400] in seconds.</p></li>
<li><p><strong>delete_protection_validation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain name of the forwarding rule. It can contain letters a-z, numbers 0-9, hyphens (-), and periods (.),
and wildcard characters. The following two domain name formats are supported:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Standard</span> <span class="n">domain</span> <span class="n">name</span><span class="p">:</span> <span class="n">www</span><span class="o">.</span><span class="n">test</span><span class="o">.</span><span class="n">com</span>
<span class="o">-</span> <span class="n">Wildcard</span> <span class="n">domain</span> <span class="n">name</span><span class="p">:</span> <span class="o">*.</span><span class="n">test</span><span class="o">.</span><span class="n">com</span><span class="o">.</span> <span class="n">wildcard</span> <span class="p">(</span><span class="o">*</span><span class="p">)</span> <span class="n">must</span> <span class="n">be</span> <span class="n">the</span> <span class="n">first</span> <span class="n">character</span> <span class="ow">in</span> <span class="n">the</span> <span class="nb">format</span> <span class="n">of</span> <span class="p">(</span><span class="o">*.</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>frontend_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The listener frontend port which is used to launch the new forwarding rule. Valid range: [1-65535].</p></li>
<li><p><strong>health_check</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether to enable health check. Valid values are<code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. TCP and UDP listener’s HealthCheck is always on, so it will be ignore when launching TCP or UDP listener. This parameter is required  and takes effect only when ListenerSync is set to off.</p></li>
<li><p><strong>health_check_connect_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Port used for health check. Valid value range: [1-65535]. Default to “None” means the backend server port is used.</p></li>
<li><p><strong>health_check_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain name used for health check. When it used to launch TCP listener, <code class="docutils literal notranslate"><span class="pre">health_check_type</span></code> must be “http”. Its length is limited to 1-80 and only characters such as letters, digits, ‘-‘ and ‘.’ are allowed. When it is not set or empty,  Server Load Balancer uses the private network IP address of each backend server as Domain used for health check.</p></li>
<li><p><strong>health_check_http_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Regular health check HTTP status code. Multiple codes are segmented by “,”. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Default to <code class="docutils literal notranslate"><span class="pre">http_2xx</span></code>.  Valid values are: <code class="docutils literal notranslate"><span class="pre">http_2xx</span></code>,  <code class="docutils literal notranslate"><span class="pre">http_3xx</span></code>, <code class="docutils literal notranslate"><span class="pre">http_4xx</span></code> and <code class="docutils literal notranslate"><span class="pre">http_5xx</span></code>.</p></li>
<li><p><strong>health_check_interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time interval of health checks. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Valid value range: [1-50] in seconds. Default to 2.</p></li>
<li><p><strong>health_check_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum timeout of each health check response. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Valid value range: [1-300] in seconds. Default to 5. Note: If <code class="docutils literal notranslate"><span class="pre">health_check_timeout</span></code> &lt; <code class="docutils literal notranslate"><span class="pre">health_check_interval</span></code>, its will be replaced by <code class="docutils literal notranslate"><span class="pre">health_check_interval</span></code>.</p></li>
<li><p><strong>health_check_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI used for health check. When it used to launch TCP listener, <code class="docutils literal notranslate"><span class="pre">health_check_type</span></code> must be “http”. Its length is limited to 1-80 and it must start with /. Only characters such as letters, digits, ‘-’, ‘/’, ‘.’, ‘%’, ‘?’, #’ and ‘&amp;’ are allowed.</p></li>
<li><p><strong>healthy_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Threshold determining the result of the health check is success. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Valid value range: [1-10] in seconds. Default to 3.</p></li>
<li><p><strong>listener_sync</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether a forwarding rule inherits the settings of a health check , session persistence, and scheduling algorithm from a listener. Default to on.</p></li>
<li><p><strong>load_balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Load Balancer ID which is used to launch the new forwarding rule.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the forwarding rule. Our plugin provides a default name: “tf-slb-rule”.</p></li>
<li><p><strong>scheduler</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Scheduling algorithm, Valid values are <code class="docutils literal notranslate"><span class="pre">wrr</span></code>, <code class="docutils literal notranslate"><span class="pre">rr</span></code> and <code class="docutils literal notranslate"><span class="pre">wlc</span></code>.  Default to “wrr”. This parameter is required  and takes effect only when ListenerSync is set to off.</p></li>
<li><p><strong>server_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of a virtual server group that will be forwarded.</p></li>
<li><p><strong>sticky_session</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether to enable session persistence, Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">off</span></code>. This parameter is required  and takes effect only when ListenerSync is set to off.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>sticky_session_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Mode for handling the cookie. If <code class="docutils literal notranslate"><span class="pre">sticky_session</span></code> is “on”, it is mandatory. Otherwise, it will be ignored. Valid values are <code class="docutils literal notranslate"><span class="pre">insert</span></code> and <code class="docutils literal notranslate"><span class="pre">server</span></code>. <code class="docutils literal notranslate"><span class="pre">insert</span></code> means it is inserted from Server Load Balancer; <code class="docutils literal notranslate"><span class="pre">server</span></code> means the Server Load Balancer learns from the backend server.</p></li>
<li><p><strong>unhealthy_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Threshold determining the result of the health check is fail. It is required when <code class="docutils literal notranslate"><span class="pre">health_check</span></code> is on. Valid value range: [1-10] in seconds. Default to 3.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain of the forwarding rule. It must be 2-80 characters in length. Only letters a-z, numbers 0-9,
and characters ‘-‘ ‘/’ ‘?’ ‘%’ ‘#’ and ‘&amp;’ are allowed. URLs must be started with the character ‘/’, but cannot be ‘/’ alone.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.slb.Rule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.Rule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.slb.Rule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.Rule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.slb.ServerCertificate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">ServerCertificate</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alicloud_certifacte_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alicloud_certifacte_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alicloud_certificate_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alicloud_certificate_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alicloud_certificate_region_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_certificate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.ServerCertificate" title="Permalink to this definition">¶</a></dt>
<dd><p>A Load Balancer Server Certificate is an ssl Certificate used by the listener of the protocol https.</p>
<p>For information about slb and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/27539.htm">What is Server Load Balancer</a>.</p>
<p>For information about Server Certificate and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/85968.htm">Configure Server Certificate</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alicloud_certificate_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – an id of server certificate ssued/proxied by alibaba cloud. but it is not supported on the international site of alibaba cloud now.</p></li>
<li><p><strong>alicloud_certificate_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the name of the certificate specified by <code class="docutils literal notranslate"><span class="pre">alicloud_certificate_id</span></code>.but it is not supported on the international site of alibaba cloud now.</p></li>
<li><p><strong>alicloud_certificate_region_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the region of the certificate specified by <code class="docutils literal notranslate"><span class="pre">alicloud_certificate_id</span></code>. but it is not supported on the international site of alibaba cloud now.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Server Certificate.</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the content of privat key of the ssl certificate specified by <code class="docutils literal notranslate"><span class="pre">server_certificate</span></code>. where <code class="docutils literal notranslate"><span class="pre">alicloud_certificate_id</span></code> is null, it is required, otherwise it is ignored.</p></li>
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of resource group which the slb server certificate belongs.</p></li>
<li><p><strong>server_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the content of the ssl certificate. where <code class="docutils literal notranslate"><span class="pre">alicloud_certificate_id</span></code> is null, it is required, otherwise it is ignored.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.slb.ServerCertificate.alicloud_certificate_id">
<code class="sig-name descname">alicloud_certificate_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.ServerCertificate.alicloud_certificate_id" title="Permalink to this definition">¶</a></dt>
<dd><p>an id of server certificate ssued/proxied by alibaba cloud. but it is not supported on the international site of alibaba cloud now.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.ServerCertificate.alicloud_certificate_name">
<code class="sig-name descname">alicloud_certificate_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.ServerCertificate.alicloud_certificate_name" title="Permalink to this definition">¶</a></dt>
<dd><p>the name of the certificate specified by <code class="docutils literal notranslate"><span class="pre">alicloud_certificate_id</span></code>.but it is not supported on the international site of alibaba cloud now.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.ServerCertificate.alicloud_certificate_region_id">
<code class="sig-name descname">alicloud_certificate_region_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.ServerCertificate.alicloud_certificate_region_id" title="Permalink to this definition">¶</a></dt>
<dd><p>the region of the certificate specified by <code class="docutils literal notranslate"><span class="pre">alicloud_certificate_id</span></code>. but it is not supported on the international site of alibaba cloud now.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.ServerCertificate.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.ServerCertificate.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Server Certificate.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.ServerCertificate.private_key">
<code class="sig-name descname">private_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.ServerCertificate.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>the content of privat key of the ssl certificate specified by <code class="docutils literal notranslate"><span class="pre">server_certificate</span></code>. where <code class="docutils literal notranslate"><span class="pre">alicloud_certificate_id</span></code> is null, it is required, otherwise it is ignored.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.ServerCertificate.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.ServerCertificate.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of resource group which the slb server certificate belongs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.ServerCertificate.server_certificate">
<code class="sig-name descname">server_certificate</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.ServerCertificate.server_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>the content of the ssl certificate. where <code class="docutils literal notranslate"><span class="pre">alicloud_certificate_id</span></code> is null, it is required, otherwise it is ignored.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.ServerCertificate.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.ServerCertificate.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.slb.ServerCertificate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alicloud_certifacte_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alicloud_certifacte_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alicloud_certificate_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alicloud_certificate_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alicloud_certificate_region_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_certificate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.ServerCertificate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServerCertificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alicloud_certificate_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – an id of server certificate ssued/proxied by alibaba cloud. but it is not supported on the international site of alibaba cloud now.</p></li>
<li><p><strong>alicloud_certificate_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the name of the certificate specified by <code class="docutils literal notranslate"><span class="pre">alicloud_certificate_id</span></code>.but it is not supported on the international site of alibaba cloud now.</p></li>
<li><p><strong>alicloud_certificate_region_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the region of the certificate specified by <code class="docutils literal notranslate"><span class="pre">alicloud_certificate_id</span></code>. but it is not supported on the international site of alibaba cloud now.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Server Certificate.</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the content of privat key of the ssl certificate specified by <code class="docutils literal notranslate"><span class="pre">server_certificate</span></code>. where <code class="docutils literal notranslate"><span class="pre">alicloud_certificate_id</span></code> is null, it is required, otherwise it is ignored.</p></li>
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of resource group which the slb server certificate belongs.</p></li>
<li><p><strong>server_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the content of the ssl certificate. where <code class="docutils literal notranslate"><span class="pre">alicloud_certificate_id</span></code> is null, it is required, otherwise it is ignored.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.slb.ServerCertificate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.ServerCertificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.slb.ServerCertificate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.ServerCertificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.slb.ServerGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">ServerGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_protection_validation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.ServerGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>A virtual server group contains several ECS instances. The virtual server group can help you to define multiple listening dimension,
and to meet the personalized requirements of domain name and URL forwarding.</p>
<blockquote>
<div><p><strong>NOTE:</strong> One ECS instance can be added into multiple virtual server groups.</p>
<p><strong>NOTE:</strong> One virtual server group can be attached with multiple listeners in one load balancer.</p>
<p><strong>NOTE:</strong> One Classic and Internet load balancer, its virtual server group can add Classic and VPC ECS instances.</p>
<p><strong>NOTE:</strong> One Classic and Intranet load balancer, its virtual server group can only add Classic ECS instances.</p>
<p><strong>NOTE:</strong> One VPC load balancer, its virtual server group can only add the same VPC ECS instances.</p>
</div></blockquote>
<p>The servers mapping supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">server_ids</span></code> - (Required) A list backend server ID (ECS instance ID).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> - (Required) The port used by the backend server. Valid value range: [1-65535].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> - (Optional) Weight of the backend server. Valid value range: [0-100]. Default to 100.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> - (Optional, Available in 1.51.0+) Type of the backend server. Valid value ecs, eni. Default to eni.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>delete_protection_validation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.</p></li>
<li><p><strong>load_balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Load Balancer ID which is used to launch a new virtual server group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the virtual server group. Our plugin provides a default name: “tf-server-group”.</p></li>
<li><p><strong>servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of ECS instances to be added. At most 20 ECS instances can be supported in one resource. It contains three sub-fields as <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">server</span></code> follows.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>servers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.slb.ServerGroup.delete_protection_validation">
<code class="sig-name descname">delete_protection_validation</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.ServerGroup.delete_protection_validation" title="Permalink to this definition">¶</a></dt>
<dd><p>Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.ServerGroup.load_balancer_id">
<code class="sig-name descname">load_balancer_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.ServerGroup.load_balancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Load Balancer ID which is used to launch a new virtual server group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.ServerGroup.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.ServerGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the virtual server group. Our plugin provides a default name: “tf-server-group”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.slb.ServerGroup.servers">
<code class="sig-name descname">servers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.slb.ServerGroup.servers" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of ECS instances to be added. At most 20 ECS instances can be supported in one resource. It contains three sub-fields as <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">server</span></code> follows.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.slb.ServerGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_protection_validation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">servers</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.ServerGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServerGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>delete_protection_validation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.</p></li>
<li><p><strong>load_balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Load Balancer ID which is used to launch a new virtual server group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the virtual server group. Our plugin provides a default name: “tf-server-group”.</p></li>
<li><p><strong>servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of ECS instances to be added. At most 20 ECS instances can be supported in one resource. It contains three sub-fields as <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">server</span></code> follows.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>servers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.slb.ServerGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.ServerGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.slb.ServerGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.ServerGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.slb.get_acls">
<code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">get_acls</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.get_acls" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the acls in the region.</p>
<p>The entry mapping supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">entry</span></code>   - An IP addresses or CIDR blocks.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> - the comment of the entry.</p></li>
</ul>
<p>The Listener mapping supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">load_balancer_id</span></code> - the id of load balancer instance, the listener belongs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frontend_port</span></code> - the listener port.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code>      - the listener protocol (such as tcp/udp/http/https, etc).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">acl_type</span></code>      - the type of acl (such as white/black).</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of acls IDs to filter results.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by acl name.</p></li>
<li><p><strong>resource_group_id</strong> (<em>str</em>) – The Id of resource group which acl belongs.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.slb.get_attachments">
<code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">get_attachments</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">instance_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.get_attachments" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the server load balancer attachments of the current Alibaba Cloud user.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>instance_ids</strong> (<em>list</em>) – List of attached ECS instance IDs.</p></li>
<li><p><strong>load_balancer_id</strong> (<em>str</em>) – ID of the SLB with attachments.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.slb.get_backend_servers">
<code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">get_backend_servers</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.get_backend_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the server load balancer backend servers related to a server load balancer..</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.53.0+</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – List of attached ECS instance IDs.</p></li>
<li><p><strong>load_balancer_id</strong> (<em>str</em>) – ID of the SLB with attachments.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.slb.get_ca_certificates">
<code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">get_ca_certificates</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.get_ca_certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the CA certificate list.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of ca certificates IDs to filter results.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by ca certificate name.</p></li>
<li><p><strong>resource_group_id</strong> (<em>str</em>) – The Id of resource group which ca certificates belongs.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.slb.get_domain_extensions">
<code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">get_domain_extensions</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">frontend_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.get_domain_extensions" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the domain extensions associated with a server load balancer listener.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.60.0+</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>frontend_port</strong> (<em>float</em>) – The frontend port used by the HTTPS listener of the SLB instance. Valid values: 1–65535.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – IDs of the SLB domain extensions.</p></li>
<li><p><strong>load_balancer_id</strong> (<em>str</em>) – The ID of the SLB instance.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.slb.get_listeners">
<code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">get_listeners</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frontend_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.get_listeners" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the listeners related to a server load balancer of the current Alibaba Cloud user.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description_regex</strong> (<em>str</em>) – A regex string to filter results by SLB listener description.</p></li>
<li><p><strong>frontend_port</strong> (<em>float</em>) – Filter listeners by the specified frontend port.</p></li>
<li><p><strong>load_balancer_id</strong> (<em>str</em>) – ID of the SLB with listeners.</p></li>
<li><p><strong>protocol</strong> (<em>str</em>) – Filter listeners by the specified protocol. Valid values: <code class="docutils literal notranslate"><span class="pre">http</span></code>, <code class="docutils literal notranslate"><span class="pre">https</span></code>, <code class="docutils literal notranslate"><span class="pre">tcp</span></code> and <code class="docutils literal notranslate"><span class="pre">udp</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.slb.get_load_balancers">
<code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">get_load_balancers</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slave_availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.get_load_balancers" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the server load balancers of the current Alibaba Cloud user.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>address</strong> (<em>str</em>) – Service address of the SLBs.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – A list of SLBs IDs.</p></li>
<li><p><strong>master_availability_zone</strong> (<em>str</em>) – Master availability zone of the SLBs.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by SLB name.</p></li>
<li><p><strong>network_type</strong> (<em>str</em>) – Network type of the SLBs. Valid values: <code class="docutils literal notranslate"><span class="pre">vpc</span></code> and <code class="docutils literal notranslate"><span class="pre">classic</span></code>.</p></li>
<li><p><strong>resource_group_id</strong> (<em>str</em>) – The Id of resource group which SLB belongs.</p></li>
<li><p><strong>slave_availability_zone</strong> (<em>str</em>) – Slave availability zone of the SLBs.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A map of tags assigned to the SLB instances. The <code class="docutils literal notranslate"><span class="pre">tags</span></code> can have a maximum of 5 tag. It must be in the format:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>```
data &quot;slb.getLoadBalancers&quot; &quot;taggedInstances&quot; {
tags = {
tagKey1 = &quot;tagValue1&quot;,
tagKey2 = &quot;tagValue2&quot;
}
}
```
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>vpc_id</strong> (<em>str</em>) – ID of the VPC linked to the SLBs.</p></li>
<li><p><strong>vswitch_id</strong> (<em>str</em>) – ID of the VSwitch linked to the SLBs.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.slb.get_master_slave_server_groups">
<code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">get_master_slave_server_groups</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.get_master_slave_server_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the master slave server groups related to a server load balancer.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.54.0+</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of master slave server group IDs to filter results.</p></li>
<li><p><strong>load_balancer_id</strong> (<em>str</em>) – ID of the SLB.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by master slave server group name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.slb.get_rules">
<code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">get_rules</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">frontend_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.get_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the rules associated with a server load balancer listener.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>frontend_port</strong> (<em>float</em>) – SLB listener port.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – A list of rules IDs to filter results.</p></li>
<li><p><strong>load_balancer_id</strong> (<em>str</em>) – ID of the SLB with listener rules.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by rule name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.slb.get_server_certificates">
<code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">get_server_certificates</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.get_server_certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the server certificate list.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of server certificates IDs to filter results.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by server certificate name.</p></li>
<li><p><strong>resource_group_id</strong> (<em>str</em>) – The Id of resource group which the slb server certificates belongs.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.slb.get_server_groups">
<code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">get_server_groups</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.get_server_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the VServer groups related to a server load balancer.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of VServer group IDs to filter results.</p></li>
<li><p><strong>load_balancer_id</strong> (<em>str</em>) – ID of the SLB.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by VServer group name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.slb.get_zones">
<code class="sig-prename descclassname">pulumi_alicloud.slb.</code><code class="sig-name descname">get_zones</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">available_slb_address_ip_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">available_slb_address_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.slb.get_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides availability zones for SLB that can be accessed by an Alibaba Cloud account within the region configured in the provider.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.73.0+.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>available_slb_address_ip_version</strong> (<em>str</em>) – Filter the results by a slb instance address version. Can be either <code class="docutils literal notranslate"><span class="pre">ipv4</span></code>, or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p></li>
<li><p><strong>available_slb_address_type</strong> (<em>str</em>) – Filter the results by a slb instance address type. Can be either <code class="docutils literal notranslate"><span class="pre">Vpc</span></code>, <code class="docutils literal notranslate"><span class="pre">classic_internet</span></code> or <code class="docutils literal notranslate"><span class="pre">classic_intranet</span></code></p></li>
<li><p><strong>enable_details</strong> (<em>bool</em>) – Default to false and only output <code class="docutils literal notranslate"><span class="pre">id</span></code> in the <code class="docutils literal notranslate"><span class="pre">zones</span></code> block. Set it to true can output more details.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
