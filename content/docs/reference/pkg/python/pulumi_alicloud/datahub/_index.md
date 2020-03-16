---
title: Module datahub
title_tag: Module datahub | Package pulumi_alicloud | Python SDK
linktitle: datahub
notitle: true
---

<div class="section" id="datahub">
<h1>datahub<a class="headerlink" href="#datahub" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.datahub"></span><dl class="class">
<dt id="pulumi_alicloud.datahub.Project">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.datahub.</code><code class="sig-name descname">Project</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">comment=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.datahub.Project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project is the basic unit of resource management in Datahub Service and is used to isolate and control resources. It contains a set of Topics. You can manage the datahub sources of an application by using projects. <a class="reference external" href="https://help.aliyun.com/document_detail/47440.html">Refer to details</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Currently Datahub service only can be supported in the regions: cn-beijing, cn-hangzhou, cn-shanghai, cn-shenzhen,  ap-southeast-1.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/datahub_project.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/datahub_project.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource*name</strong> (<em>str</em>) – <p>The name of the resource.</p>
</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Comment of the datahub project. It cannot be longer than 255 characters.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the datahub project. Its length is limited to 3-32 and only characters such as letters, digits and ‘<a href="#id3"><span class="problematic" id="id4">*</span></a>’ are allowed. It is case-insensitive.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.datahub.Project.comment">
<code class="sig-name descname">comment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.datahub.Project.comment" title="Permalink to this definition">¶</a></dt>
<dd><p>Comment of the datahub project. It cannot be longer than 255 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.datahub.Project.create_time">
<code class="sig-name descname">create_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.datahub.Project.create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Create time of the datahub project. It is a human-readable string rather than 64-bits UTC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.datahub.Project.last_modify_time">
<code class="sig-name descname">last_modify_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.datahub.Project.last_modify_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Last modify time of the datahub project. It is the same as <em>create_time</em> at the beginning. It is also a human-readable string rather than 64-bits UTC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.datahub.Project.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.datahub.Project.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the datahub project. Its length is limited to 3-32 and only characters such as letters, digits and ‘_’ are allowed. It is case-insensitive.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.datahub.Project.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">comment=None</em>, <em class="sig-param">create_time=None</em>, <em class="sig-param">last_modify_time=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.datahub.Project.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Project resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Comment of the datahub project. It cannot be longer than 255 characters.</p></li>
<li><p><strong>create_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Create time of the datahub project. It is a human-readable string rather than 64-bits UTC.</p></li>
<li><p><strong>last_modify_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Last modify time of the datahub project. It is the same as <em>create_time</em> at the beginning. It is also a human-readable string rather than 64-bits UTC.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the datahub project. Its length is limited to 3-32 and only characters such as letters, digits and ‘_’ are allowed. It is case-insensitive.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.datahub.Project.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.datahub.Project.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.datahub.Project.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.datahub.Project.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.datahub.Subscription">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.datahub.</code><code class="sig-name descname">Subscription</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">comment=None</em>, <em class="sig-param">project_name=None</em>, <em class="sig-param">topic_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.datahub.Subscription" title="Permalink to this definition">¶</a></dt>
<dd><p>The subscription is the basic unit of resource usage in Datahub Service under Publish/Subscribe model. You can manage the relationships between user and topics by using subscriptions. <a class="reference external" href="https://help.aliyun.com/document_detail/47440.html">Refer to details</a>.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/datahub_subscription.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/datahub_subscription.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Comment of the datahub subscription. It cannot be longer than 255 characters.</p></li>
<li><p><strong>project*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of the datahub project that the subscription belongs to. Its length is limited to 3-32 and only characters such as letters, digits and ‘<a href="#id8"><span class="problematic" id="id9">*</span></a>’ are allowed. It is case-insensitive.</p>
</p></li>
<li><p><strong>topic*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of the datahub topic that the subscription belongs to. Its length is limited to 1-128 and only characters such as letters, digits and ‘<a href="#id12"><span class="problematic" id="id13">*</span></a>’ are allowed. It is case-insensitive.</p>
</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.datahub.Subscription.comment">
<code class="sig-name descname">comment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.datahub.Subscription.comment" title="Permalink to this definition">¶</a></dt>
<dd><p>Comment of the datahub subscription. It cannot be longer than 255 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.datahub.Subscription.create_time">
<code class="sig-name descname">create_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.datahub.Subscription.create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Create time of the datahub subscription. It is a human-readable string rather than 64-bits UTC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.datahub.Subscription.last_modify_time">
<code class="sig-name descname">last_modify_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.datahub.Subscription.last_modify_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Last modify time of the datahub subscription. It is the same as <em>create_time</em> at the beginning. It is also a human-readable string rather than 64-bits UTC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.datahub.Subscription.project_name">
<code class="sig-name descname">project_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.datahub.Subscription.project_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the datahub project that the subscription belongs to. Its length is limited to 3-32 and only characters such as letters, digits and ‘_’ are allowed. It is case-insensitive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.datahub.Subscription.sub_id">
<code class="sig-name descname">sub_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.datahub.Subscription.sub_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The identidy of the subscritpion, generate from server side.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.datahub.Subscription.topic_name">
<code class="sig-name descname">topic_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.datahub.Subscription.topic_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the datahub topic that the subscription belongs to. Its length is limited to 1-128 and only characters such as letters, digits and ‘_’ are allowed. It is case-insensitive.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.datahub.Subscription.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">comment=None</em>, <em class="sig-param">create_time=None</em>, <em class="sig-param">last_modify_time=None</em>, <em class="sig-param">project_name=None</em>, <em class="sig-param">sub_id=None</em>, <em class="sig-param">topic_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.datahub.Subscription.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Subscription resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Comment of the datahub subscription. It cannot be longer than 255 characters.</p></li>
<li><p><strong>create_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Create time of the datahub subscription. It is a human-readable string rather than 64-bits UTC.</p></li>
<li><p><strong>last_modify_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Last modify time of the datahub subscription. It is the same as <em>create_time</em> at the beginning. It is also a human-readable string rather than 64-bits UTC.</p></li>
<li><p><strong>project*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of the datahub project that the subscription belongs to. Its length is limited to 3-32 and only characters such as letters, digits and ‘<a href="#id16"><span class="problematic" id="id17">*</span></a>’ are allowed. It is case-insensitive.</p>
</p></li>
<li><p><strong>sub_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identidy of the subscritpion, generate from server side.</p></li>
<li><p><strong>topic*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of the datahub topic that the subscription belongs to. Its length is limited to 1-128 and only characters such as letters, digits and ‘<a href="#id20"><span class="problematic" id="id21">*</span></a>’ are allowed. It is case-insensitive.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.datahub.Subscription.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.datahub.Subscription.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.datahub.Subscription.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.datahub.Subscription.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.datahub.Topic">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.datahub.</code><code class="sig-name descname">Topic</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">comment=None</em>, <em class="sig-param">life_cycle=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project_name=None</em>, <em class="sig-param">record_schema=None</em>, <em class="sig-param">record_type=None</em>, <em class="sig-param">shard_count=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.datahub.Topic" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Topic resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] comment: Comment of the datahub topic. It cannot be longer than 255 characters.
:param pulumi.Input[float] life<em>cycle: How many days this topic lives. The permitted range of values is [1, 7]. The default value is 3.
:param pulumi.Input[str] name: The name of the datahub topic. Its length is limited to 1-128 and only characters such as letters, digits and ‘</em>’ are allowed. It is case-insensitive.
:param pulumi.Input[str] project_name: The name of the datahub project that this topic belongs to. It is case-insensitive.
:param pulumi.Input[dict] record_schema: Schema of this topic, required only for TUPLE topic. Supported data types (case-insensitive) are:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">BIGINT</span>
<span class="o">-</span> <span class="n">STRING</span>
<span class="o">-</span> <span class="n">BOOLEAN</span>
<span class="o">-</span> <span class="n">DOUBLE</span>
<span class="o">-</span> <span class="n">TIMESTAMP</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>record_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of this topic. Its value must be one of {BLOB, TUPLE}. For BLOB topic, data will be organized as binary and encoded by BASE64. For TUPLE topic, data has fixed schema. The default value is “TUPLE” with a schema {STRING}.</p></li>
<li><p><strong>shard_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of shards this topic contains. The permitted range of values is [1, 10]. The default value is 1.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.datahub.Topic.comment">
<code class="sig-name descname">comment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.datahub.Topic.comment" title="Permalink to this definition">¶</a></dt>
<dd><p>Comment of the datahub topic. It cannot be longer than 255 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.datahub.Topic.create_time">
<code class="sig-name descname">create_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.datahub.Topic.create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Create time of the datahub topic. It is a human-readable string rather than 64-bits UTC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.datahub.Topic.last_modify_time">
<code class="sig-name descname">last_modify_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.datahub.Topic.last_modify_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Last modify time of the datahub topic. It is the same as <em>create_time</em> at the beginning. It is also a human-readable string rather than 64-bits UTC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.datahub.Topic.life_cycle">
<code class="sig-name descname">life_cycle</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.datahub.Topic.life_cycle" title="Permalink to this definition">¶</a></dt>
<dd><p>How many days this topic lives. The permitted range of values is [1, 7]. The default value is 3.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.datahub.Topic.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.datahub.Topic.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the datahub topic. Its length is limited to 1-128 and only characters such as letters, digits and ‘_’ are allowed. It is case-insensitive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.datahub.Topic.project_name">
<code class="sig-name descname">project_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.datahub.Topic.project_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the datahub project that this topic belongs to. It is case-insensitive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.datahub.Topic.record_schema">
<code class="sig-name descname">record_schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.datahub.Topic.record_schema" title="Permalink to this definition">¶</a></dt>
<dd><p>Schema of this topic, required only for TUPLE topic. Supported data types (case-insensitive) are:</p>
<ul class="simple">
<li><p>BIGINT</p></li>
<li><p>STRING</p></li>
<li><p>BOOLEAN</p></li>
<li><p>DOUBLE</p></li>
<li><p>TIMESTAMP</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.datahub.Topic.record_type">
<code class="sig-name descname">record_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.datahub.Topic.record_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of this topic. Its value must be one of {BLOB, TUPLE}. For BLOB topic, data will be organized as binary and encoded by BASE64. For TUPLE topic, data has fixed schema. The default value is “TUPLE” with a schema {STRING}.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.datahub.Topic.shard_count">
<code class="sig-name descname">shard_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.datahub.Topic.shard_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of shards this topic contains. The permitted range of values is [1, 10]. The default value is 1.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.datahub.Topic.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">comment=None</em>, <em class="sig-param">create_time=None</em>, <em class="sig-param">last_modify_time=None</em>, <em class="sig-param">life_cycle=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project_name=None</em>, <em class="sig-param">record_schema=None</em>, <em class="sig-param">record_type=None</em>, <em class="sig-param">shard_count=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.datahub.Topic.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Topic resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Comment of the datahub topic. It cannot be longer than 255 characters.</p></li>
<li><p><strong>create_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Create time of the datahub topic. It is a human-readable string rather than 64-bits UTC.</p></li>
<li><p><strong>last_modify_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Last modify time of the datahub topic. It is the same as <em>create_time</em> at the beginning. It is also a human-readable string rather than 64-bits UTC.</p></li>
<li><p><strong>life*cycle</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>How many days this topic lives. The permitted range of values is [1, 7]. The default value is 3.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the datahub topic. Its length is limited to 1-128 and only characters such as letters, digits and ‘<a href="#id24"><span class="problematic" id="id25">*</span></a>’ are allowed. It is case-insensitive.</p></li>
<li><p><strong>project_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the datahub project that this topic belongs to. It is case-insensitive.</p></li>
<li><p><strong>record_schema</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Schema of this topic, required only for TUPLE topic. Supported data types (case-insensitive) are:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">BIGINT</span>
<span class="o">-</span> <span class="n">STRING</span>
<span class="o">-</span> <span class="n">BOOLEAN</span>
<span class="o">-</span> <span class="n">DOUBLE</span>
<span class="o">-</span> <span class="n">TIMESTAMP</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>record_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of this topic. Its value must be one of {BLOB, TUPLE}. For BLOB topic, data will be organized as binary and encoded by BASE64. For TUPLE topic, data has fixed schema. The default value is “TUPLE” with a schema {STRING}.</p></li>
<li><p><strong>shard_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of shards this topic contains. The permitted range of values is [1, 10]. The default value is 1.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.datahub.Topic.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.datahub.Topic.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.datahub.Topic.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.datahub.Topic.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

</div>
