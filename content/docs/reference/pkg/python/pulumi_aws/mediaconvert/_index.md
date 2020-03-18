---
title: Module mediaconvert
title_tag: Module mediaconvert | Package pulumi_aws | Python SDK
linktitle: mediaconvert
notitle: true
---

<div class="section" id="mediaconvert">
<h1>mediaconvert<a class="headerlink" href="#mediaconvert" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.mediaconvert"></span><dl class="class">
<dt id="pulumi_aws.mediaconvert.Queue">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.mediaconvert.</code><code class="sig-name descname">Queue</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pricing_plan=None</em>, <em class="sig-param">reservation_plan_settings=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mediaconvert.Queue" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AWS Elemental MediaConvert Queue.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/media_convert_queue.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/media_convert_queue.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the queue</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique identifier describing the queue</p></li>
<li><p><strong>pricing_plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether the pricing plan for the queue is on-demand or reserved. Valid values are <code class="docutils literal notranslate"><span class="pre">ON_DEMAND</span></code> or <code class="docutils literal notranslate"><span class="pre">RESERVED</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">ON_DEMAND</span></code>.</p></li>
<li><p><strong>reservation_plan_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A detail pricing plan of the  reserved queue. See below.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A status of the queue. Valid values are <code class="docutils literal notranslate"><span class="pre">ACTIVE</span></code> or <code class="docutils literal notranslate"><span class="pre">RESERVED</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">PAUSED</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>reservation_plan_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">commitment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The length of the term of your reserved queue pricing plan commitment. Valid value is <code class="docutils literal notranslate"><span class="pre">ONE_YEAR</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">renewalType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies whether the term of your reserved queue pricing plan. Valid values are <code class="docutils literal notranslate"><span class="pre">AUTO_RENEW</span></code> or <code class="docutils literal notranslate"><span class="pre">EXPIRE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reservedSlots</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the number of reserved transcode slots (RTS) for queue.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.mediaconvert.Queue.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mediaconvert.Queue.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Arn of the queue</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mediaconvert.Queue.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mediaconvert.Queue.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the queue</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mediaconvert.Queue.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mediaconvert.Queue.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique identifier describing the queue</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mediaconvert.Queue.pricing_plan">
<code class="sig-name descname">pricing_plan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mediaconvert.Queue.pricing_plan" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the pricing plan for the queue is on-demand or reserved. Valid values are <code class="docutils literal notranslate"><span class="pre">ON_DEMAND</span></code> or <code class="docutils literal notranslate"><span class="pre">RESERVED</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">ON_DEMAND</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mediaconvert.Queue.reservation_plan_settings">
<code class="sig-name descname">reservation_plan_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mediaconvert.Queue.reservation_plan_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A detail pricing plan of the  reserved queue. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">commitment</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The length of the term of your reserved queue pricing plan commitment. Valid value is <code class="docutils literal notranslate"><span class="pre">ONE_YEAR</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">renewalType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies whether the term of your reserved queue pricing plan. Valid values are <code class="docutils literal notranslate"><span class="pre">AUTO_RENEW</span></code> or <code class="docutils literal notranslate"><span class="pre">EXPIRE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reservedSlots</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the number of reserved transcode slots (RTS) for queue.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mediaconvert.Queue.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mediaconvert.Queue.status" title="Permalink to this definition">¶</a></dt>
<dd><p>A status of the queue. Valid values are <code class="docutils literal notranslate"><span class="pre">ACTIVE</span></code> or <code class="docutils literal notranslate"><span class="pre">RESERVED</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">PAUSED</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.mediaconvert.Queue.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mediaconvert.Queue.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.mediaconvert.Queue.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pricing_plan=None</em>, <em class="sig-param">reservation_plan_settings=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mediaconvert.Queue.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Queue resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Arn of the queue</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the queue</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique identifier describing the queue</p></li>
<li><p><strong>pricing_plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether the pricing plan for the queue is on-demand or reserved. Valid values are <code class="docutils literal notranslate"><span class="pre">ON_DEMAND</span></code> or <code class="docutils literal notranslate"><span class="pre">RESERVED</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">ON_DEMAND</span></code>.</p></li>
<li><p><strong>reservation_plan_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A detail pricing plan of the  reserved queue. See below.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A status of the queue. Valid values are <code class="docutils literal notranslate"><span class="pre">ACTIVE</span></code> or <code class="docutils literal notranslate"><span class="pre">RESERVED</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">PAUSED</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>reservation_plan_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">commitment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The length of the term of your reserved queue pricing plan commitment. Valid value is <code class="docutils literal notranslate"><span class="pre">ONE_YEAR</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">renewalType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies whether the term of your reserved queue pricing plan. Valid values are <code class="docutils literal notranslate"><span class="pre">AUTO_RENEW</span></code> or <code class="docutils literal notranslate"><span class="pre">EXPIRE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reservedSlots</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the number of reserved transcode slots (RTS) for queue.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.mediaconvert.Queue.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mediaconvert.Queue.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.mediaconvert.Queue.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mediaconvert.Queue.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
