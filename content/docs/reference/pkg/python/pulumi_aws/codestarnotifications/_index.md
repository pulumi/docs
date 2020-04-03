---
title: Module codestarnotifications
title_tag: Module codestarnotifications | Package pulumi_aws | Python SDK
linktitle: codestarnotifications
notitle: true
---

<div class="section" id="codestarnotifications">
<h1>codestarnotifications<a class="headerlink" href="#codestarnotifications" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.codestarnotifications"></span><dl class="class">
<dt id="pulumi_aws.codestarnotifications.NotificationRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.codestarnotifications.</code><code class="sig-name descname">NotificationRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">detail_type=None</em>, <em class="sig-param">event_type_ids=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">targets=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codestarnotifications.NotificationRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CodeStar Notifications Rule.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>detail_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The level of detail to include in the notifications for this resource. Possible values are <code class="docutils literal notranslate"><span class="pre">BASIC</span></code> and <code class="docutils literal notranslate"><span class="pre">FULL</span></code>.</p></li>
<li><p><strong>event_type_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of event types associated with this notification rule.
For list of allowed events see <a class="reference external" href="https://docs.aws.amazon.com/codestar-notifications/latest/userguide/concepts.html#concepts-api">here</a>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of notification rule.</p></li>
<li><p><strong>resource</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the resource to associate with the notification rule.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the notification rule. Possible values are <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> and <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>, default is <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>targets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configuration blocks containing notification target information. Can be specified multiple times. At least one target must be specified on creation.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>targets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of notification rule target. For example, a SNS Topic ARN.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The status of the notification rule. Possible values are <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> and <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>, default is <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of the notification target. Default value is <code class="docutils literal notranslate"><span class="pre">SNS</span></code>.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.codestarnotifications.NotificationRule.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codestarnotifications.NotificationRule.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The codestar notification rule ARN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codestarnotifications.NotificationRule.detail_type">
<code class="sig-name descname">detail_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codestarnotifications.NotificationRule.detail_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The level of detail to include in the notifications for this resource. Possible values are <code class="docutils literal notranslate"><span class="pre">BASIC</span></code> and <code class="docutils literal notranslate"><span class="pre">FULL</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codestarnotifications.NotificationRule.event_type_ids">
<code class="sig-name descname">event_type_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codestarnotifications.NotificationRule.event_type_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of event types associated with this notification rule.
For list of allowed events see <a class="reference external" href="https://docs.aws.amazon.com/codestar-notifications/latest/userguide/concepts.html#concepts-api">here</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codestarnotifications.NotificationRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codestarnotifications.NotificationRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of notification rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codestarnotifications.NotificationRule.resource">
<code class="sig-name descname">resource</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codestarnotifications.NotificationRule.resource" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the resource to associate with the notification rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codestarnotifications.NotificationRule.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codestarnotifications.NotificationRule.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the notification rule. Possible values are <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> and <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>, default is <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codestarnotifications.NotificationRule.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codestarnotifications.NotificationRule.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.codestarnotifications.NotificationRule.targets">
<code class="sig-name descname">targets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.codestarnotifications.NotificationRule.targets" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration blocks containing notification target information. Can be specified multiple times. At least one target must be specified on creation.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of notification rule target. For example, a SNS Topic ARN.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The status of the notification rule. Possible values are <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> and <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>, default is <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of the notification target. Default value is <code class="docutils literal notranslate"><span class="pre">SNS</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.codestarnotifications.NotificationRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">detail_type=None</em>, <em class="sig-param">event_type_ids=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">targets=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codestarnotifications.NotificationRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NotificationRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The codestar notification rule ARN.</p></li>
<li><p><strong>detail_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The level of detail to include in the notifications for this resource. Possible values are <code class="docutils literal notranslate"><span class="pre">BASIC</span></code> and <code class="docutils literal notranslate"><span class="pre">FULL</span></code>.</p></li>
<li><p><strong>event_type_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A list of event types associated with this notification rule.
For list of allowed events see <a class="reference external" href="https://docs.aws.amazon.com/codestar-notifications/latest/userguide/concepts.html#concepts-api">here</a>.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of notification rule.</p></li>
<li><p><strong>resource</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the resource to associate with the notification rule.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the notification rule. Possible values are <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> and <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>, default is <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>targets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configuration blocks containing notification target information. Can be specified multiple times. At least one target must be specified on creation.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>targets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of notification rule target. For example, a SNS Topic ARN.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The status of the notification rule. Possible values are <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> and <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>, default is <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of the notification target. Default value is <code class="docutils literal notranslate"><span class="pre">SNS</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.codestarnotifications.NotificationRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codestarnotifications.NotificationRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.codestarnotifications.NotificationRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.codestarnotifications.NotificationRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
