---
title: Module cloudwatch
title_tag: Module cloudwatch | Package pulumi_aws | Python SDK
linktitle: cloudwatch
notitle: true
---

<div class="section" id="cloudwatch">
<h1>cloudwatch<a class="headerlink" href="#cloudwatch" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.cloudwatch"></span><dl class="py class">
<dt id="pulumi_aws.cloudwatch.AwaitableGetLogGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudwatch.</code><code class="sig-name descname">AwaitableGetLogGroupResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creation_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_in_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.AwaitableGetLogGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.cloudwatch.Dashboard">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudwatch.</code><code class="sig-name descname">Dashboard</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dashboard_body</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dashboard_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.Dashboard" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CloudWatch Dashboard resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dashboard_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The detailed information about the dashboard, including what widgets are included and their location on the dashboard. You can read more about the body structure in the <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html">documentation</a>.</p></li>
<li><p><strong>dashboard_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the dashboard.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.Dashboard.dashboard_arn">
<code class="sig-name descname">dashboard_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.Dashboard.dashboard_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the dashboard.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.Dashboard.dashboard_body">
<code class="sig-name descname">dashboard_body</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.Dashboard.dashboard_body" title="Permalink to this definition">¶</a></dt>
<dd><p>The detailed information about the dashboard, including what widgets are included and their location on the dashboard. You can read more about the body structure in the <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html">documentation</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.Dashboard.dashboard_name">
<code class="sig-name descname">dashboard_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.Dashboard.dashboard_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the dashboard.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudwatch.Dashboard.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dashboard_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dashboard_body</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dashboard_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.Dashboard.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Dashboard resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dashboard_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the dashboard.</p></li>
<li><p><strong>dashboard_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The detailed information about the dashboard, including what widgets are included and their location on the dashboard. You can read more about the body structure in the <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html">documentation</a>.</p>
</p></li>
<li><p><strong>dashboard_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the dashboard.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudwatch.Dashboard.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.Dashboard.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudwatch.Dashboard.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.Dashboard.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudwatch.EventPermission">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudwatch.</code><code class="sig-name descname">EventPermission</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">principal</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">statement_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.EventPermission" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to create a CloudWatch Events permission to support cross-account events in the current account default event bus.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action that you are enabling the other account to perform. Defaults to <code class="docutils literal notranslate"><span class="pre">events:PutEvents</span></code>.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block to limit the event bus permissions you are granting to only accounts that fulfill the condition. Specified below.</p></li>
<li><p><strong>principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The 12-digit AWS account ID that you are permitting to put events to your default event bus. Specify <code class="docutils literal notranslate"><span class="pre">*</span></code> to permit any account to put events to your default event bus, optionally limited by <code class="docutils literal notranslate"><span class="pre">condition</span></code>.</p></li>
<li><p><strong>statement_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An identifier string for the external account that you are granting permissions to.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Key for the condition. Valid values: <code class="docutils literal notranslate"><span class="pre">aws:PrincipalOrgID</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of condition. Value values: <code class="docutils literal notranslate"><span class="pre">StringEquals</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value for the key.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.EventPermission.action">
<code class="sig-name descname">action</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.EventPermission.action" title="Permalink to this definition">¶</a></dt>
<dd><p>The action that you are enabling the other account to perform. Defaults to <code class="docutils literal notranslate"><span class="pre">events:PutEvents</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.EventPermission.condition">
<code class="sig-name descname">condition</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.EventPermission.condition" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block to limit the event bus permissions you are granting to only accounts that fulfill the condition. Specified below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Key for the condition. Valid values: <code class="docutils literal notranslate"><span class="pre">aws:PrincipalOrgID</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Type of condition. Value values: <code class="docutils literal notranslate"><span class="pre">StringEquals</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Value for the key.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.EventPermission.principal">
<code class="sig-name descname">principal</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.EventPermission.principal" title="Permalink to this definition">¶</a></dt>
<dd><p>The 12-digit AWS account ID that you are permitting to put events to your default event bus. Specify <code class="docutils literal notranslate"><span class="pre">*</span></code> to permit any account to put events to your default event bus, optionally limited by <code class="docutils literal notranslate"><span class="pre">condition</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.EventPermission.statement_id">
<code class="sig-name descname">statement_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.EventPermission.statement_id" title="Permalink to this definition">¶</a></dt>
<dd><p>An identifier string for the external account that you are granting permissions to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudwatch.EventPermission.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">principal</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">statement_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.EventPermission.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EventPermission resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action that you are enabling the other account to perform. Defaults to <code class="docutils literal notranslate"><span class="pre">events:PutEvents</span></code>.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block to limit the event bus permissions you are granting to only accounts that fulfill the condition. Specified below.</p></li>
<li><p><strong>principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The 12-digit AWS account ID that you are permitting to put events to your default event bus. Specify <code class="docutils literal notranslate"><span class="pre">*</span></code> to permit any account to put events to your default event bus, optionally limited by <code class="docutils literal notranslate"><span class="pre">condition</span></code>.</p></li>
<li><p><strong>statement_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An identifier string for the external account that you are granting permissions to.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Key for the condition. Valid values: <code class="docutils literal notranslate"><span class="pre">aws:PrincipalOrgID</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of condition. Value values: <code class="docutils literal notranslate"><span class="pre">StringEquals</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value for the key.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudwatch.EventPermission.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.EventPermission.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudwatch.EventPermission.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.EventPermission.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudwatch.EventRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudwatch.</code><code class="sig-name descname">EventRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event_pattern</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schedule_expression</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.EventRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CloudWatch Event Rule resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the rule.</p></li>
<li><p><strong>event_pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Event pattern
described a JSON object.
See full documentation of <a class="reference external" href="http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CloudWatchEventsandEventPatterns.html">CloudWatch Events and Event Patterns</a> for details.</p></li>
<li><p><strong>is_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the rule should be enabled (defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The rule’s name. By default generated by this provider.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The rule’s name. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) associated with the role that is used for target invocation.</p></li>
<li><p><strong>schedule_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scheduling expression.
For example, <code class="docutils literal notranslate"><span class="pre">cron(0</span> <span class="pre">20</span> <span class="pre">*</span> <span class="pre">*</span> <span class="pre">?</span> <span class="pre">*)</span></code> or <code class="docutils literal notranslate"><span class="pre">rate(5</span> <span class="pre">minutes)</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.EventRule.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.EventRule.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.EventRule.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.EventRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.EventRule.event_pattern">
<code class="sig-name descname">event_pattern</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.EventRule.event_pattern" title="Permalink to this definition">¶</a></dt>
<dd><p>Event pattern
described a JSON object.
See full documentation of <a class="reference external" href="http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CloudWatchEventsandEventPatterns.html">CloudWatch Events and Event Patterns</a> for details.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.EventRule.is_enabled">
<code class="sig-name descname">is_enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.EventRule.is_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the rule should be enabled (defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.EventRule.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.EventRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The rule’s name. By default generated by this provider.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.EventRule.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.EventRule.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The rule’s name. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.EventRule.role_arn">
<code class="sig-name descname">role_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.EventRule.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) associated with the role that is used for target invocation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.EventRule.schedule_expression">
<code class="sig-name descname">schedule_expression</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.EventRule.schedule_expression" title="Permalink to this definition">¶</a></dt>
<dd><p>The scheduling expression.
For example, <code class="docutils literal notranslate"><span class="pre">cron(0</span> <span class="pre">20</span> <span class="pre">*</span> <span class="pre">*</span> <span class="pre">?</span> <span class="pre">*)</span></code> or <code class="docutils literal notranslate"><span class="pre">rate(5</span> <span class="pre">minutes)</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.EventRule.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.EventRule.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudwatch.EventRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event_pattern</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schedule_expression</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.EventRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EventRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the rule.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the rule.</p></li>
<li><p><strong>event_pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Event pattern
described a JSON object.
See full documentation of <a class="reference external" href="http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CloudWatchEventsandEventPatterns.html">CloudWatch Events and Event Patterns</a> for details.</p>
</p></li>
<li><p><strong>is_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the rule should be enabled (defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The rule’s name. By default generated by this provider.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The rule’s name. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) associated with the role that is used for target invocation.</p></li>
<li><p><strong>schedule_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scheduling expression.
For example, <code class="docutils literal notranslate"><span class="pre">cron(0</span> <span class="pre">20</span> <span class="pre">*</span> <span class="pre">*</span> <span class="pre">?</span> <span class="pre">*)</span></code> or <code class="docutils literal notranslate"><span class="pre">rate(5</span> <span class="pre">minutes)</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudwatch.EventRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.EventRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudwatch.EventRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.EventRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudwatch.EventTarget">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudwatch.</code><code class="sig-name descname">EventTarget</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">batch_target</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ecs_target</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">input</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">input_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">input_transformer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kinesis_target</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rule</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">run_command_targets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sqs_target</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.EventTarget" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CloudWatch Event Target resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) associated of the target.</p></li>
<li><p><strong>batch_target</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Parameters used when you are using the rule to invoke an Amazon Batch Job. Documented below. A maximum of 1 are allowed.</p></li>
<li><p><strong>ecs_target</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Parameters used when you are using the rule to invoke Amazon ECS Task. Documented below. A maximum of 1 are allowed.</p></li>
<li><p><strong>input</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid JSON text passed to the target.</p></li>
<li><p><strong>input_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the <a class="reference external" href="http://goessner.net/articles/JsonPath/">JSONPath</a>
that is used for extracting part of the matched event when passing it to the target.</p></li>
<li><p><strong>input_transformer</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Parameters used when you are providing a custom input to a target based on certain event data.</p></li>
<li><p><strong>kinesis_target</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Parameters used when you are using the rule to invoke an Amazon Kinesis Stream. Documented below. A maximum of 1 are allowed.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. Required if <code class="docutils literal notranslate"><span class="pre">ecs_target</span></code> is used.</p></li>
<li><p><strong>rule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule you want to add targets to.</p></li>
<li><p><strong>run_command_targets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Parameters used when you are using the rule to invoke Amazon EC2 Run Command. Documented below. A maximum of 5 are allowed.</p></li>
<li><p><strong>sqs_target</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Parameters used when you are using the rule to invoke an Amazon SQS Queue. Documented below. A maximum of 1 are allowed.</p></li>
<li><p><strong>target_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique target assignment ID.  If missing, will generate a random, unique id.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>batch_target</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arraySize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jobAttempts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of times to attempt to retry, if the job fails. Valid values are 1 to 10.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jobDefinition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN or name of the job definition to use if the event target is an AWS Batch job. This job definition must already exist.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jobName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name to use for this execution of the job, if the target is an AWS Batch job.</p></li>
</ul>
<p>The <strong>ecs_target</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">group</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies an ECS task group for the task. The maximum length is 255 characters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">launch_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. Valid values are EC2 or FARGATE.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network_configuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Use this if the ECS task uses the awsvpc network mode. This specifies the VPC subnets and security groups associated with the task, and whether a public IP address is to be used. Required if launch_type is FARGATE because the awsvpc mode is required for Fargate tasks.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">assignPublicIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Assign a public IP address to the ENI (Fargate launch type only). Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">security_groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The subnets associated with the task or service.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">platform_version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as 1.1.0. This is used only if LaunchType is FARGATE. For more information about valid platform versions, see <a class="reference external" href="http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html">AWS Fargate Platform Versions</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taskCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of tasks to create based on the TaskDefinition. The default is 1.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taskDefinitionArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the task definition to use if the event target is an Amazon ECS cluster.</p></li>
</ul>
<p>The <strong>input_transformer</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">inputPaths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Key value pairs specified in the form of JSONPath (for example, time = $.time)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">inputTemplate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Structure containing the template body.</p></li>
</ul>
<p>The <strong>kinesis_target</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">partitionKeyPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The JSON path to be extracted from the event and used as the partition key.</p></li>
</ul>
<p>The <strong>run_command_targets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Can be either <code class="docutils literal notranslate"><span class="pre">tag:tag-key</span></code> or <code class="docutils literal notranslate"><span class="pre">InstanceIds</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - If Key is <code class="docutils literal notranslate"><span class="pre">tag:tag-key</span></code>, Values is a list of tag values. If Key is <code class="docutils literal notranslate"><span class="pre">InstanceIds</span></code>, Values is a list of Amazon EC2 instance IDs.</p></li>
</ul>
<p>The <strong>sqs_target</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">messageGroupId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The FIFO message group ID to use as the target.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.EventTarget.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.EventTarget.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) associated of the target.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.EventTarget.batch_target">
<code class="sig-name descname">batch_target</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.EventTarget.batch_target" title="Permalink to this definition">¶</a></dt>
<dd><p>Parameters used when you are using the rule to invoke an Amazon Batch Job. Documented below. A maximum of 1 are allowed.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arraySize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jobAttempts</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of times to attempt to retry, if the job fails. Valid values are 1 to 10.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jobDefinition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN or name of the job definition to use if the event target is an AWS Batch job. This job definition must already exist.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jobName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name to use for this execution of the job, if the target is an AWS Batch job.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.EventTarget.ecs_target">
<code class="sig-name descname">ecs_target</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.EventTarget.ecs_target" title="Permalink to this definition">¶</a></dt>
<dd><p>Parameters used when you are using the rule to invoke Amazon ECS Task. Documented below. A maximum of 1 are allowed.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">group</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies an ECS task group for the task. The maximum length is 255 characters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">launch_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. Valid values are EC2 or FARGATE.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network_configuration</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Use this if the ECS task uses the awsvpc network mode. This specifies the VPC subnets and security groups associated with the task, and whether a public IP address is to be used. Required if launch_type is FARGATE because the awsvpc mode is required for Fargate tasks.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">assignPublicIp</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Assign a public IP address to the ENI (Fargate launch type only). Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">security_groups</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnets</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The subnets associated with the task or service.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">platform_version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as 1.1.0. This is used only if LaunchType is FARGATE. For more information about valid platform versions, see <a class="reference external" href="http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html">AWS Fargate Platform Versions</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taskCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of tasks to create based on the TaskDefinition. The default is 1.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taskDefinitionArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the task definition to use if the event target is an Amazon ECS cluster.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.EventTarget.input">
<code class="sig-name descname">input</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.EventTarget.input" title="Permalink to this definition">¶</a></dt>
<dd><p>Valid JSON text passed to the target.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.EventTarget.input_path">
<code class="sig-name descname">input_path</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.EventTarget.input_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the <a class="reference external" href="http://goessner.net/articles/JsonPath/">JSONPath</a>
that is used for extracting part of the matched event when passing it to the target.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.EventTarget.input_transformer">
<code class="sig-name descname">input_transformer</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.EventTarget.input_transformer" title="Permalink to this definition">¶</a></dt>
<dd><p>Parameters used when you are providing a custom input to a target based on certain event data.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">inputPaths</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Key value pairs specified in the form of JSONPath (for example, time = $.time)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">inputTemplate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Structure containing the template body.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.EventTarget.kinesis_target">
<code class="sig-name descname">kinesis_target</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.EventTarget.kinesis_target" title="Permalink to this definition">¶</a></dt>
<dd><p>Parameters used when you are using the rule to invoke an Amazon Kinesis Stream. Documented below. A maximum of 1 are allowed.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">partitionKeyPath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The JSON path to be extracted from the event and used as the partition key.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.EventTarget.role_arn">
<code class="sig-name descname">role_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.EventTarget.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. Required if <code class="docutils literal notranslate"><span class="pre">ecs_target</span></code> is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.EventTarget.rule">
<code class="sig-name descname">rule</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.EventTarget.rule" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the rule you want to add targets to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.EventTarget.run_command_targets">
<code class="sig-name descname">run_command_targets</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.EventTarget.run_command_targets" title="Permalink to this definition">¶</a></dt>
<dd><p>Parameters used when you are using the rule to invoke Amazon EC2 Run Command. Documented below. A maximum of 5 are allowed.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Can be either <code class="docutils literal notranslate"><span class="pre">tag:tag-key</span></code> or <code class="docutils literal notranslate"><span class="pre">InstanceIds</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - If Key is <code class="docutils literal notranslate"><span class="pre">tag:tag-key</span></code>, Values is a list of tag values. If Key is <code class="docutils literal notranslate"><span class="pre">InstanceIds</span></code>, Values is a list of Amazon EC2 instance IDs.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.EventTarget.sqs_target">
<code class="sig-name descname">sqs_target</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.EventTarget.sqs_target" title="Permalink to this definition">¶</a></dt>
<dd><p>Parameters used when you are using the rule to invoke an Amazon SQS Queue. Documented below. A maximum of 1 are allowed.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">messageGroupId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The FIFO message group ID to use as the target.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.EventTarget.target_id">
<code class="sig-name descname">target_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.EventTarget.target_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique target assignment ID.  If missing, will generate a random, unique id.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudwatch.EventTarget.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">batch_target</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ecs_target</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">input</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">input_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">input_transformer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kinesis_target</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rule</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">run_command_targets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sqs_target</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.EventTarget.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EventTarget resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) associated of the target.</p></li>
<li><p><strong>batch_target</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Parameters used when you are using the rule to invoke an Amazon Batch Job. Documented below. A maximum of 1 are allowed.</p></li>
<li><p><strong>ecs_target</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Parameters used when you are using the rule to invoke Amazon ECS Task. Documented below. A maximum of 1 are allowed.</p></li>
<li><p><strong>input</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid JSON text passed to the target.</p></li>
<li><p><strong>input_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The value of the <a class="reference external" href="http://goessner.net/articles/JsonPath/">JSONPath</a>
that is used for extracting part of the matched event when passing it to the target.</p>
</p></li>
<li><p><strong>input_transformer</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Parameters used when you are providing a custom input to a target based on certain event data.</p></li>
<li><p><strong>kinesis_target</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Parameters used when you are using the rule to invoke an Amazon Kinesis Stream. Documented below. A maximum of 1 are allowed.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. Required if <code class="docutils literal notranslate"><span class="pre">ecs_target</span></code> is used.</p></li>
<li><p><strong>rule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule you want to add targets to.</p></li>
<li><p><strong>run_command_targets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Parameters used when you are using the rule to invoke Amazon EC2 Run Command. Documented below. A maximum of 5 are allowed.</p></li>
<li><p><strong>sqs_target</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Parameters used when you are using the rule to invoke an Amazon SQS Queue. Documented below. A maximum of 1 are allowed.</p></li>
<li><p><strong>target_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique target assignment ID.  If missing, will generate a random, unique id.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>batch_target</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arraySize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jobAttempts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of times to attempt to retry, if the job fails. Valid values are 1 to 10.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jobDefinition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN or name of the job definition to use if the event target is an AWS Batch job. This job definition must already exist.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jobName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name to use for this execution of the job, if the target is an AWS Batch job.</p></li>
</ul>
<p>The <strong>ecs_target</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">group</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies an ECS task group for the task. The maximum length is 255 characters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">launch_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. Valid values are EC2 or FARGATE.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network_configuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Use this if the ECS task uses the awsvpc network mode. This specifies the VPC subnets and security groups associated with the task, and whether a public IP address is to be used. Required if launch_type is FARGATE because the awsvpc mode is required for Fargate tasks.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">assignPublicIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Assign a public IP address to the ENI (Fargate launch type only). Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">security_groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The subnets associated with the task or service.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">platform_version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as 1.1.0. This is used only if LaunchType is FARGATE. For more information about valid platform versions, see <a class="reference external" href="http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html">AWS Fargate Platform Versions</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taskCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of tasks to create based on the TaskDefinition. The default is 1.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taskDefinitionArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the task definition to use if the event target is an Amazon ECS cluster.</p></li>
</ul>
<p>The <strong>input_transformer</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">inputPaths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Key value pairs specified in the form of JSONPath (for example, time = $.time)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">inputTemplate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Structure containing the template body.</p></li>
</ul>
<p>The <strong>kinesis_target</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">partitionKeyPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The JSON path to be extracted from the event and used as the partition key.</p></li>
</ul>
<p>The <strong>run_command_targets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Can be either <code class="docutils literal notranslate"><span class="pre">tag:tag-key</span></code> or <code class="docutils literal notranslate"><span class="pre">InstanceIds</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - If Key is <code class="docutils literal notranslate"><span class="pre">tag:tag-key</span></code>, Values is a list of tag values. If Key is <code class="docutils literal notranslate"><span class="pre">InstanceIds</span></code>, Values is a list of Amazon EC2 instance IDs.</p></li>
</ul>
<p>The <strong>sqs_target</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">messageGroupId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The FIFO message group ID to use as the target.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudwatch.EventTarget.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.EventTarget.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudwatch.EventTarget.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.EventTarget.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudwatch.GetLogGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudwatch.</code><code class="sig-name descname">GetLogGroupResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creation_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_in_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.GetLogGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLogGroup.</p>
<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.GetLogGroupResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.GetLogGroupResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the Cloudwatch log group</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.GetLogGroupResult.creation_time">
<code class="sig-name descname">creation_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.GetLogGroupResult.creation_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation time of the log group, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.GetLogGroupResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.GetLogGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.GetLogGroupResult.kms_key_id">
<code class="sig-name descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.GetLogGroupResult.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the KMS Key to use when encrypting log data.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.GetLogGroupResult.retention_in_days">
<code class="sig-name descname">retention_in_days</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.GetLogGroupResult.retention_in_days" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of days log events retained in the specified log group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.GetLogGroupResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.GetLogGroupResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.cloudwatch.LogDestination">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudwatch.</code><code class="sig-name descname">LogDestination</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogDestination" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CloudWatch Logs destination resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the log destination</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM role that grants Amazon CloudWatch Logs permissions to put data into the target</p></li>
<li><p><strong>target_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the target Amazon Kinesis stream resource for the destination</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogDestination.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogDestination.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) specifying the log destination.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogDestination.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogDestination.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name for the log destination</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogDestination.role_arn">
<code class="sig-name descname">role_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogDestination.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM role that grants Amazon CloudWatch Logs permissions to put data into the target</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogDestination.target_arn">
<code class="sig-name descname">target_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogDestination.target_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the target Amazon Kinesis stream resource for the destination</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudwatch.LogDestination.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_arn</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogDestination.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogDestination resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) specifying the log destination.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the log destination</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM role that grants Amazon CloudWatch Logs permissions to put data into the target</p></li>
<li><p><strong>target_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the target Amazon Kinesis stream resource for the destination</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudwatch.LogDestination.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogDestination.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudwatch.LogDestination.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogDestination.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudwatch.LogDestinationPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudwatch.</code><code class="sig-name descname">LogDestinationPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogDestinationPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CloudWatch Logs destination policy resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy document. This is a JSON formatted string.</p></li>
<li><p><strong>destination_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the subscription filter</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogDestinationPolicy.access_policy">
<code class="sig-name descname">access_policy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogDestinationPolicy.access_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy document. This is a JSON formatted string.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogDestinationPolicy.destination_name">
<code class="sig-name descname">destination_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogDestinationPolicy.destination_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name for the subscription filter</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudwatch.LogDestinationPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogDestinationPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogDestinationPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy document. This is a JSON formatted string.</p></li>
<li><p><strong>destination_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the subscription filter</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudwatch.LogDestinationPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogDestinationPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudwatch.LogDestinationPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogDestinationPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudwatch.LogGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudwatch.</code><code class="sig-name descname">LogGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_in_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CloudWatch Log Group resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the KMS Key to use when encrypting log data. Please note, after the AWS KMS CMK is disassociated from the log group,
AWS CloudWatch Logs stops encrypting newly ingested data for the log group. All previously ingested data remains encrypted, and AWS CloudWatch Logs requires
permissions for the CMK whenever the encrypted data is requested.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the log group. If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>retention_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of days
you want to retain log events in the specified log group.  Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, and 3653.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogGroup.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) specifying the log group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogGroup.kms_key_id">
<code class="sig-name descname">kms_key_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogGroup.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the KMS Key to use when encrypting log data. Please note, after the AWS KMS CMK is disassociated from the log group,
AWS CloudWatch Logs stops encrypting newly ingested data for the log group. All previously ingested data remains encrypted, and AWS CloudWatch Logs requires
permissions for the CMK whenever the encrypted data is requested.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogGroup.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the log group. If omitted, this provider will assign a random, unique name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogGroup.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogGroup.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogGroup.retention_in_days">
<code class="sig-name descname">retention_in_days</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogGroup.retention_in_days" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the number of days
you want to retain log events in the specified log group.  Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, and 3653.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogGroup.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudwatch.LogGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_in_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) specifying the log group.</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the KMS Key to use when encrypting log data. Please note, after the AWS KMS CMK is disassociated from the log group,
AWS CloudWatch Logs stops encrypting newly ingested data for the log group. All previously ingested data remains encrypted, and AWS CloudWatch Logs requires
permissions for the CMK whenever the encrypted data is requested.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the log group. If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>retention_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of days
you want to retain log events in the specified log group.  Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, and 3653.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudwatch.LogGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudwatch.LogGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudwatch.LogMetricFilter">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudwatch.</code><code class="sig-name descname">LogMetricFilter</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_transformation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pattern</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogMetricFilter" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CloudWatch Log Metric Filter resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>log_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the log group to associate the metric filter with.</p></li>
<li><p><strong>metric_transformation</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A block defining collection of information
needed to define how metric data gets emitted. See below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the metric filter.</p></li>
<li><p><strong>pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A valid <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/FilterAndPatternSyntax.html">CloudWatch Logs filter pattern</a>
for extracting metric data out of ingested log events.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>metric_transformation</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default_value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value to emit when a filter pattern does not match a log event.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the CloudWatch metric to which the monitored log information should be published (e.g. <code class="docutils literal notranslate"><span class="pre">ErrorCount</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The destination namespace of the CloudWatch metric.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - What to publish to the metric. For example, if you’re counting the occurrences of a particular term like “Error”, the value will be “1” for each occurrence. If you’re counting the bytes transferred the published value will be the value in the log event.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogMetricFilter.log_group_name">
<code class="sig-name descname">log_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogMetricFilter.log_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the log group to associate the metric filter with.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogMetricFilter.metric_transformation">
<code class="sig-name descname">metric_transformation</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogMetricFilter.metric_transformation" title="Permalink to this definition">¶</a></dt>
<dd><p>A block defining collection of information
needed to define how metric data gets emitted. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default_value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value to emit when a filter pattern does not match a log event.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the CloudWatch metric to which the monitored log information should be published (e.g. <code class="docutils literal notranslate"><span class="pre">ErrorCount</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The destination namespace of the CloudWatch metric.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - What to publish to the metric. For example, if you’re counting the occurrences of a particular term like “Error”, the value will be “1” for each occurrence. If you’re counting the bytes transferred the published value will be the value in the log event.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogMetricFilter.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogMetricFilter.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name for the metric filter.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogMetricFilter.pattern">
<code class="sig-name descname">pattern</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogMetricFilter.pattern" title="Permalink to this definition">¶</a></dt>
<dd><p>A valid <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/FilterAndPatternSyntax.html">CloudWatch Logs filter pattern</a>
for extracting metric data out of ingested log events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudwatch.LogMetricFilter.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_transformation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pattern</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogMetricFilter.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogMetricFilter resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>log_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the log group to associate the metric filter with.</p></li>
<li><p><strong>metric_transformation</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A block defining collection of information
needed to define how metric data gets emitted. See below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the metric filter.</p></li>
<li><p><strong>pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>A valid <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/FilterAndPatternSyntax.html">CloudWatch Logs filter pattern</a>
for extracting metric data out of ingested log events.</p>
</p></li>
</ul>
</dd>
</dl>
<p>The <strong>metric_transformation</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default_value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value to emit when a filter pattern does not match a log event.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the CloudWatch metric to which the monitored log information should be published (e.g. <code class="docutils literal notranslate"><span class="pre">ErrorCount</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The destination namespace of the CloudWatch metric.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - What to publish to the metric. For example, if you’re counting the occurrences of a particular term like “Error”, the value will be “1” for each occurrence. If you’re counting the bytes transferred the published value will be the value in the log event.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudwatch.LogMetricFilter.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogMetricFilter.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudwatch.LogMetricFilter.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogMetricFilter.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudwatch.LogResourcePolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudwatch.</code><code class="sig-name descname">LogResourcePolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_document</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogResourcePolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage a CloudWatch log resource policy.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>policy_document</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Details of the resource policy, including the identity of the principal that is enabled to put logs to this account. This is formatted as a JSON string. Maximum length of 5120 characters.</p></li>
<li><p><strong>policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the resource policy.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogResourcePolicy.policy_document">
<code class="sig-name descname">policy_document</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogResourcePolicy.policy_document" title="Permalink to this definition">¶</a></dt>
<dd><p>Details of the resource policy, including the identity of the principal that is enabled to put logs to this account. This is formatted as a JSON string. Maximum length of 5120 characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogResourcePolicy.policy_name">
<code class="sig-name descname">policy_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogResourcePolicy.policy_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the resource policy.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudwatch.LogResourcePolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_document</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogResourcePolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogResourcePolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>policy_document</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Details of the resource policy, including the identity of the principal that is enabled to put logs to this account. This is formatted as a JSON string. Maximum length of 5120 characters.</p></li>
<li><p><strong>policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the resource policy.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudwatch.LogResourcePolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogResourcePolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudwatch.LogResourcePolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogResourcePolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudwatch.LogStream">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudwatch.</code><code class="sig-name descname">LogStream</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogStream" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CloudWatch Log Stream resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>log_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the log group under which the log stream is to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the log stream. Must not be longer than 512 characters and must not contain <code class="docutils literal notranslate"><span class="pre">:</span></code></p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogStream.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogStream.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) specifying the log stream.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogStream.log_group_name">
<code class="sig-name descname">log_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogStream.log_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the log group under which the log stream is to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogStream.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogStream.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the log stream. Must not be longer than 512 characters and must not contain <code class="docutils literal notranslate"><span class="pre">:</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudwatch.LogStream.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogStream.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogStream resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) specifying the log stream.</p></li>
<li><p><strong>log_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the log group under which the log stream is to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the log stream. Must not be longer than 512 characters and must not contain <code class="docutils literal notranslate"><span class="pre">:</span></code></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudwatch.LogStream.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogStream.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudwatch.LogStream.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogStream.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudwatch.LogSubscriptionFilter">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudwatch.</code><code class="sig-name descname">LogSubscriptionFilter</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">distribution</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter_pattern</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogSubscriptionFilter" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CloudWatch Logs subscription filter resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>destination_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the destination to deliver matching log events to. Kinesis stream or Lambda function ARN.</p></li>
<li><p><strong>distribution</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method used to distribute log data to the destination. By default log data is grouped by log stream, but the grouping can be set to random for a more even distribution. This property is only applicable when the destination is an Amazon Kinesis stream. Valid values are “Random” and “ByLogStream”.</p></li>
<li><p><strong>filter_pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A valid CloudWatch Logs filter pattern for subscribing to a filtered stream of log events.</p></li>
<li><p><strong>log_group</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The name of the log group to associate the subscription filter with</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the subscription filter</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM role that grants Amazon CloudWatch Logs permissions to deliver ingested log events to the destination. If you use Lambda as a destination, you should skip this argument and use <code class="docutils literal notranslate"><span class="pre">lambda.Permission</span></code> resource for granting access from CloudWatch logs to the destination Lambda function.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogSubscriptionFilter.destination_arn">
<code class="sig-name descname">destination_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogSubscriptionFilter.destination_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the destination to deliver matching log events to. Kinesis stream or Lambda function ARN.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogSubscriptionFilter.distribution">
<code class="sig-name descname">distribution</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogSubscriptionFilter.distribution" title="Permalink to this definition">¶</a></dt>
<dd><p>The method used to distribute log data to the destination. By default log data is grouped by log stream, but the grouping can be set to random for a more even distribution. This property is only applicable when the destination is an Amazon Kinesis stream. Valid values are “Random” and “ByLogStream”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogSubscriptionFilter.filter_pattern">
<code class="sig-name descname">filter_pattern</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogSubscriptionFilter.filter_pattern" title="Permalink to this definition">¶</a></dt>
<dd><p>A valid CloudWatch Logs filter pattern for subscribing to a filtered stream of log events.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogSubscriptionFilter.log_group">
<code class="sig-name descname">log_group</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogSubscriptionFilter.log_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the log group to associate the subscription filter with</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogSubscriptionFilter.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogSubscriptionFilter.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name for the subscription filter</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.LogSubscriptionFilter.role_arn">
<code class="sig-name descname">role_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.LogSubscriptionFilter.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM role that grants Amazon CloudWatch Logs permissions to deliver ingested log events to the destination. If you use Lambda as a destination, you should skip this argument and use <code class="docutils literal notranslate"><span class="pre">lambda.Permission</span></code> resource for granting access from CloudWatch logs to the destination Lambda function.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudwatch.LogSubscriptionFilter.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">distribution</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter_pattern</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogSubscriptionFilter.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogSubscriptionFilter resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>destination_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the destination to deliver matching log events to. Kinesis stream or Lambda function ARN.</p></li>
<li><p><strong>distribution</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method used to distribute log data to the destination. By default log data is grouped by log stream, but the grouping can be set to random for a more even distribution. This property is only applicable when the destination is an Amazon Kinesis stream. Valid values are “Random” and “ByLogStream”.</p></li>
<li><p><strong>filter_pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A valid CloudWatch Logs filter pattern for subscribing to a filtered stream of log events.</p></li>
<li><p><strong>log_group</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The name of the log group to associate the subscription filter with</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the subscription filter</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM role that grants Amazon CloudWatch Logs permissions to deliver ingested log events to the destination. If you use Lambda as a destination, you should skip this argument and use <code class="docutils literal notranslate"><span class="pre">lambda.Permission</span></code> resource for granting access from CloudWatch logs to the destination Lambda function.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudwatch.LogSubscriptionFilter.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogSubscriptionFilter.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudwatch.LogSubscriptionFilter.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.LogSubscriptionFilter.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudwatch.MetricAlarm">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudwatch.</code><code class="sig-name descname">MetricAlarm</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">actions_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alarm_actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alarm_description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comparison_operator</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datapoints_to_alarm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dimensions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">evaluate_low_sample_count_percentiles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">evaluation_periods</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extended_statistic</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">insufficient_data_actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_queries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ok_actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">statistic</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold_metric_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">treat_missing_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CloudWatch Metric Alarm resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>actions_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether or not actions should be executed during any changes to the alarm’s state. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>alarm_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of actions to execute when this alarm transitions into an ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p></li>
<li><p><strong>alarm_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the alarm.</p></li>
<li><p><strong>comparison_operator</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The arithmetic operation to use when comparing the specified Statistic and Threshold. The specified Statistic value is used as the first operand. Either of the following is supported: <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqualToThreshold</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanThreshold</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThanThreshold</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThanOrEqualToThreshold</span></code>. Additionally, the values  <code class="docutils literal notranslate"><span class="pre">LessThanLowerOrGreaterThanUpperThreshold</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThanLowerThreshold</span></code>, and <code class="docutils literal notranslate"><span class="pre">GreaterThanUpperThreshold</span></code> are used only for alarms based on anomaly detection models.</p></li>
<li><p><strong>datapoints_to_alarm</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of datapoints that must be breaching to trigger the alarm.</p></li>
<li><p><strong>dimensions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The dimensions for this metric.  For the list of available dimensions see the AWS documentation <a class="reference external" href="http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html">here</a>.</p></li>
<li><p><strong>evaluate_low_sample_count_percentiles</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used only for alarms
based on percentiles. If you specify <code class="docutils literal notranslate"><span class="pre">ignore</span></code>, the alarm state will not
change during periods with too few data points to be statistically significant.
If you specify <code class="docutils literal notranslate"><span class="pre">evaluate</span></code> or omit this parameter, the alarm will always be
evaluated and possibly change state no matter how many data points are available.
The following values are supported: <code class="docutils literal notranslate"><span class="pre">ignore</span></code>, and <code class="docutils literal notranslate"><span class="pre">evaluate</span></code>.</p></li>
<li><p><strong>evaluation_periods</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of periods over which data is compared to the specified threshold.</p></li>
<li><p><strong>extended_statistic</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.</p></li>
<li><p><strong>insufficient_data_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of actions to execute when this alarm transitions into an INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p></li>
<li><p><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for this metric.
See docs for <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html">supported metrics</a>.</p></li>
<li><p><strong>metric_queries</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Enables you to create an alarm based on a metric math expression. You may specify at most 20.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The descriptive name for the alarm. This name must be unique within the user’s AWS account</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The namespace for this metric. See docs for the <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html">list of namespaces</a>.
See docs for <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html">supported metrics</a>.</p>
</p></li>
<li><p><strong>ok_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of actions to execute when this alarm transitions into an OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The period in seconds over which the specified <code class="docutils literal notranslate"><span class="pre">stat</span></code> is applied.</p></li>
<li><p><strong>statistic</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The statistic to apply to the alarm’s associated metric.
Either of the following is supported: <code class="docutils literal notranslate"><span class="pre">SampleCount</span></code>, <code class="docutils literal notranslate"><span class="pre">Average</span></code>, <code class="docutils literal notranslate"><span class="pre">Sum</span></code>, <code class="docutils literal notranslate"><span class="pre">Minimum</span></code>, <code class="docutils literal notranslate"><span class="pre">Maximum</span></code></p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The value against which the specified statistic is compared. This parameter is required for alarms based on static thresholds, but should not be used for alarms based on anomaly detection models.</p></li>
<li><p><strong>threshold_metric_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If this is an alarm based on an anomaly detection model, make this value match the ID of the ANOMALY_DETECTION_BAND function.</p></li>
<li><p><strong>treat_missing_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets how this alarm is to handle missing data points. The following values are supported: <code class="docutils literal notranslate"><span class="pre">missing</span></code>, <code class="docutils literal notranslate"><span class="pre">ignore</span></code>, <code class="docutils literal notranslate"><span class="pre">breaching</span></code> and <code class="docutils literal notranslate"><span class="pre">notBreaching</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">missing</span></code>.</p></li>
<li><p><strong>unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unit for this metric.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>metric_queries</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The math expression to be performed on the returned data, if this object is performing a math expression. This expression can use the id of the other metrics to refer to those metrics, and can also use the id of other expressions to use the result of those expressions. For more information about metric math expressions, see Metric Math Syntax and Functions in the <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax">Amazon CloudWatch User Guide</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A short name used to tie this object to the results in the response. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metric</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The metric to be returned, along with statistics, period, and units. Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The dimensions for this metric.  For the list of available dimensions see the AWS documentation <a class="reference external" href="http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html">here</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metric_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name for this metric.
See docs for <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html">supported metrics</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The namespace for this metric. See docs for the <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html">list of namespaces</a>.
See docs for <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html">supported metrics</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The period in seconds over which the specified <code class="docutils literal notranslate"><span class="pre">stat</span></code> is applied.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The statistic to apply to this metric.
Either of the following is supported: <code class="docutils literal notranslate"><span class="pre">SampleCount</span></code>, <code class="docutils literal notranslate"><span class="pre">Average</span></code>, <code class="docutils literal notranslate"><span class="pre">Sum</span></code>, <code class="docutils literal notranslate"><span class="pre">Minimum</span></code>, <code class="docutils literal notranslate"><span class="pre">Maximum</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unit for this metric.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">returnData</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specify exactly one <code class="docutils literal notranslate"><span class="pre">metric_query</span></code> to be <code class="docutils literal notranslate"><span class="pre">true</span></code> to use that <code class="docutils literal notranslate"><span class="pre">metric_query</span></code> result as the alarm.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.MetricAlarm.actions_enabled">
<code class="sig-name descname">actions_enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm.actions_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether or not actions should be executed during any changes to the alarm’s state. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.MetricAlarm.alarm_actions">
<code class="sig-name descname">alarm_actions</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm.alarm_actions" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of actions to execute when this alarm transitions into an ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.MetricAlarm.alarm_description">
<code class="sig-name descname">alarm_description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm.alarm_description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description for the alarm.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.MetricAlarm.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the cloudwatch metric alarm.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.MetricAlarm.comparison_operator">
<code class="sig-name descname">comparison_operator</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm.comparison_operator" title="Permalink to this definition">¶</a></dt>
<dd><p>The arithmetic operation to use when comparing the specified Statistic and Threshold. The specified Statistic value is used as the first operand. Either of the following is supported: <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqualToThreshold</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanThreshold</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThanThreshold</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThanOrEqualToThreshold</span></code>. Additionally, the values  <code class="docutils literal notranslate"><span class="pre">LessThanLowerOrGreaterThanUpperThreshold</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThanLowerThreshold</span></code>, and <code class="docutils literal notranslate"><span class="pre">GreaterThanUpperThreshold</span></code> are used only for alarms based on anomaly detection models.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.MetricAlarm.datapoints_to_alarm">
<code class="sig-name descname">datapoints_to_alarm</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm.datapoints_to_alarm" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of datapoints that must be breaching to trigger the alarm.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.MetricAlarm.dimensions">
<code class="sig-name descname">dimensions</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm.dimensions" title="Permalink to this definition">¶</a></dt>
<dd><p>The dimensions for this metric.  For the list of available dimensions see the AWS documentation <a class="reference external" href="http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html">here</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.MetricAlarm.evaluate_low_sample_count_percentiles">
<code class="sig-name descname">evaluate_low_sample_count_percentiles</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm.evaluate_low_sample_count_percentiles" title="Permalink to this definition">¶</a></dt>
<dd><p>Used only for alarms
based on percentiles. If you specify <code class="docutils literal notranslate"><span class="pre">ignore</span></code>, the alarm state will not
change during periods with too few data points to be statistically significant.
If you specify <code class="docutils literal notranslate"><span class="pre">evaluate</span></code> or omit this parameter, the alarm will always be
evaluated and possibly change state no matter how many data points are available.
The following values are supported: <code class="docutils literal notranslate"><span class="pre">ignore</span></code>, and <code class="docutils literal notranslate"><span class="pre">evaluate</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.MetricAlarm.evaluation_periods">
<code class="sig-name descname">evaluation_periods</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm.evaluation_periods" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of periods over which data is compared to the specified threshold.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.MetricAlarm.extended_statistic">
<code class="sig-name descname">extended_statistic</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm.extended_statistic" title="Permalink to this definition">¶</a></dt>
<dd><p>The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.MetricAlarm.insufficient_data_actions">
<code class="sig-name descname">insufficient_data_actions</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm.insufficient_data_actions" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of actions to execute when this alarm transitions into an INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.MetricAlarm.metric_name">
<code class="sig-name descname">metric_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for this metric.
See docs for <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html">supported metrics</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.MetricAlarm.metric_queries">
<code class="sig-name descname">metric_queries</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm.metric_queries" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables you to create an alarm based on a metric math expression. You may specify at most 20.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The math expression to be performed on the returned data, if this object is performing a math expression. This expression can use the id of the other metrics to refer to those metrics, and can also use the id of other expressions to use the result of those expressions. For more information about metric math expressions, see Metric Math Syntax and Functions in the <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax">Amazon CloudWatch User Guide</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A short name used to tie this object to the results in the response. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metric</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The metric to be returned, along with statistics, period, and units. Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The dimensions for this metric.  For the list of available dimensions see the AWS documentation <a class="reference external" href="http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html">here</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metric_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name for this metric.
See docs for <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html">supported metrics</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The namespace for this metric. See docs for the <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html">list of namespaces</a>.
See docs for <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html">supported metrics</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The period in seconds over which the specified <code class="docutils literal notranslate"><span class="pre">stat</span></code> is applied.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The statistic to apply to this metric.
Either of the following is supported: <code class="docutils literal notranslate"><span class="pre">SampleCount</span></code>, <code class="docutils literal notranslate"><span class="pre">Average</span></code>, <code class="docutils literal notranslate"><span class="pre">Sum</span></code>, <code class="docutils literal notranslate"><span class="pre">Minimum</span></code>, <code class="docutils literal notranslate"><span class="pre">Maximum</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unit for this metric.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">returnData</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specify exactly one <code class="docutils literal notranslate"><span class="pre">metric_query</span></code> to be <code class="docutils literal notranslate"><span class="pre">true</span></code> to use that <code class="docutils literal notranslate"><span class="pre">metric_query</span></code> result as the alarm.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.MetricAlarm.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The descriptive name for the alarm. This name must be unique within the user’s AWS account</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.MetricAlarm.namespace">
<code class="sig-name descname">namespace</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm.namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The namespace for this metric. See docs for the <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html">list of namespaces</a>.
See docs for <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html">supported metrics</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.MetricAlarm.ok_actions">
<code class="sig-name descname">ok_actions</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm.ok_actions" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of actions to execute when this alarm transitions into an OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.MetricAlarm.period">
<code class="sig-name descname">period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The period in seconds over which the specified <code class="docutils literal notranslate"><span class="pre">stat</span></code> is applied.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.MetricAlarm.statistic">
<code class="sig-name descname">statistic</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm.statistic" title="Permalink to this definition">¶</a></dt>
<dd><p>The statistic to apply to the alarm’s associated metric.
Either of the following is supported: <code class="docutils literal notranslate"><span class="pre">SampleCount</span></code>, <code class="docutils literal notranslate"><span class="pre">Average</span></code>, <code class="docutils literal notranslate"><span class="pre">Sum</span></code>, <code class="docutils literal notranslate"><span class="pre">Minimum</span></code>, <code class="docutils literal notranslate"><span class="pre">Maximum</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.MetricAlarm.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.MetricAlarm.threshold">
<code class="sig-name descname">threshold</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm.threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>The value against which the specified statistic is compared. This parameter is required for alarms based on static thresholds, but should not be used for alarms based on anomaly detection models.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.MetricAlarm.threshold_metric_id">
<code class="sig-name descname">threshold_metric_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm.threshold_metric_id" title="Permalink to this definition">¶</a></dt>
<dd><p>If this is an alarm based on an anomaly detection model, make this value match the ID of the ANOMALY_DETECTION_BAND function.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.MetricAlarm.treat_missing_data">
<code class="sig-name descname">treat_missing_data</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm.treat_missing_data" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets how this alarm is to handle missing data points. The following values are supported: <code class="docutils literal notranslate"><span class="pre">missing</span></code>, <code class="docutils literal notranslate"><span class="pre">ignore</span></code>, <code class="docutils literal notranslate"><span class="pre">breaching</span></code> and <code class="docutils literal notranslate"><span class="pre">notBreaching</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">missing</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudwatch.MetricAlarm.unit">
<code class="sig-name descname">unit</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm.unit" title="Permalink to this definition">¶</a></dt>
<dd><p>The unit for this metric.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudwatch.MetricAlarm.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">actions_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alarm_actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alarm_description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comparison_operator</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datapoints_to_alarm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dimensions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">evaluate_low_sample_count_percentiles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">evaluation_periods</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extended_statistic</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">insufficient_data_actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_queries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ok_actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">statistic</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold_metric_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">treat_missing_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unit</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MetricAlarm resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>actions_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether or not actions should be executed during any changes to the alarm’s state. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>alarm_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of actions to execute when this alarm transitions into an ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p></li>
<li><p><strong>alarm_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the alarm.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the cloudwatch metric alarm.</p></li>
<li><p><strong>comparison_operator</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The arithmetic operation to use when comparing the specified Statistic and Threshold. The specified Statistic value is used as the first operand. Either of the following is supported: <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqualToThreshold</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanThreshold</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThanThreshold</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThanOrEqualToThreshold</span></code>. Additionally, the values  <code class="docutils literal notranslate"><span class="pre">LessThanLowerOrGreaterThanUpperThreshold</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThanLowerThreshold</span></code>, and <code class="docutils literal notranslate"><span class="pre">GreaterThanUpperThreshold</span></code> are used only for alarms based on anomaly detection models.</p></li>
<li><p><strong>datapoints_to_alarm</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of datapoints that must be breaching to trigger the alarm.</p></li>
<li><p><strong>dimensions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>The dimensions for this metric.  For the list of available dimensions see the AWS documentation <a class="reference external" href="http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html">here</a>.</p>
</p></li>
<li><p><strong>evaluate_low_sample_count_percentiles</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used only for alarms
based on percentiles. If you specify <code class="docutils literal notranslate"><span class="pre">ignore</span></code>, the alarm state will not
change during periods with too few data points to be statistically significant.
If you specify <code class="docutils literal notranslate"><span class="pre">evaluate</span></code> or omit this parameter, the alarm will always be
evaluated and possibly change state no matter how many data points are available.
The following values are supported: <code class="docutils literal notranslate"><span class="pre">ignore</span></code>, and <code class="docutils literal notranslate"><span class="pre">evaluate</span></code>.</p></li>
<li><p><strong>evaluation_periods</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of periods over which data is compared to the specified threshold.</p></li>
<li><p><strong>extended_statistic</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.</p></li>
<li><p><strong>insufficient_data_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of actions to execute when this alarm transitions into an INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p></li>
<li><p><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name for this metric.
See docs for <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html">supported metrics</a>.</p>
</p></li>
<li><p><strong>metric_queries</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Enables you to create an alarm based on a metric math expression. You may specify at most 20.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The descriptive name for the alarm. This name must be unique within the user’s AWS account</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The namespace for this metric. See docs for the <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html">list of namespaces</a>.
See docs for <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html">supported metrics</a>.</p>
</p></li>
<li><p><strong>ok_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of actions to execute when this alarm transitions into an OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The period in seconds over which the specified <code class="docutils literal notranslate"><span class="pre">stat</span></code> is applied.</p></li>
<li><p><strong>statistic</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The statistic to apply to the alarm’s associated metric.
Either of the following is supported: <code class="docutils literal notranslate"><span class="pre">SampleCount</span></code>, <code class="docutils literal notranslate"><span class="pre">Average</span></code>, <code class="docutils literal notranslate"><span class="pre">Sum</span></code>, <code class="docutils literal notranslate"><span class="pre">Minimum</span></code>, <code class="docutils literal notranslate"><span class="pre">Maximum</span></code></p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The value against which the specified statistic is compared. This parameter is required for alarms based on static thresholds, but should not be used for alarms based on anomaly detection models.</p></li>
<li><p><strong>threshold_metric_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If this is an alarm based on an anomaly detection model, make this value match the ID of the ANOMALY_DETECTION_BAND function.</p></li>
<li><p><strong>treat_missing_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets how this alarm is to handle missing data points. The following values are supported: <code class="docutils literal notranslate"><span class="pre">missing</span></code>, <code class="docutils literal notranslate"><span class="pre">ignore</span></code>, <code class="docutils literal notranslate"><span class="pre">breaching</span></code> and <code class="docutils literal notranslate"><span class="pre">notBreaching</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">missing</span></code>.</p></li>
<li><p><strong>unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unit for this metric.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>metric_queries</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The math expression to be performed on the returned data, if this object is performing a math expression. This expression can use the id of the other metrics to refer to those metrics, and can also use the id of other expressions to use the result of those expressions. For more information about metric math expressions, see Metric Math Syntax and Functions in the <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax">Amazon CloudWatch User Guide</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A short name used to tie this object to the results in the response. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metric</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The metric to be returned, along with statistics, period, and units. Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The dimensions for this metric.  For the list of available dimensions see the AWS documentation <a class="reference external" href="http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html">here</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metric_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name for this metric.
See docs for <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html">supported metrics</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The namespace for this metric. See docs for the <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html">list of namespaces</a>.
See docs for <a class="reference external" href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html">supported metrics</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The period in seconds over which the specified <code class="docutils literal notranslate"><span class="pre">stat</span></code> is applied.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The statistic to apply to this metric.
Either of the following is supported: <code class="docutils literal notranslate"><span class="pre">SampleCount</span></code>, <code class="docutils literal notranslate"><span class="pre">Average</span></code>, <code class="docutils literal notranslate"><span class="pre">Sum</span></code>, <code class="docutils literal notranslate"><span class="pre">Minimum</span></code>, <code class="docutils literal notranslate"><span class="pre">Maximum</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unit for this metric.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">returnData</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specify exactly one <code class="docutils literal notranslate"><span class="pre">metric_query</span></code> to be <code class="docutils literal notranslate"><span class="pre">true</span></code> to use that <code class="docutils literal notranslate"><span class="pre">metric_query</span></code> result as the alarm.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudwatch.MetricAlarm.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudwatch.MetricAlarm.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.MetricAlarm.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudwatch.get_log_group">
<code class="sig-prename descclassname">pulumi_aws.cloudwatch.</code><code class="sig-name descname">get_log_group</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudwatch.get_log_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about an AWS Cloudwatch Log Group</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the Cloudwatch log group</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
