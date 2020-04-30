---
title: Module cloud9
title_tag: Module cloud9 | Package pulumi_aws | Python SDK
linktitle: cloud9
notitle: true
---

<div class="section" id="cloud9">
<h1>cloud9<a class="headerlink" href="#cloud9" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.cloud9"></span><dl class="py class">
<dt id="pulumi_aws.cloud9.EnvironmentEC2">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloud9.</code><code class="sig-name descname">EnvironmentEC2</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">automatic_stop_time_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloud9.EnvironmentEC2" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloud9 EC2 Development Environment.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automatic_stop_time_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of minutes until the running instance is shut down after the environment has last been used.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the environment.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of instance to connect to the environment, e.g. <code class="docutils literal notranslate"><span class="pre">t2.micro</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the environment.</p></li>
<li><p><strong>owner_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the environment owner. This can be ARN of any AWS IAM principal. Defaults to the environment’s creator.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the subnet in Amazon VPC that AWS Cloud9 will use to communicate with the Amazon EC2 instance.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.cloud9.EnvironmentEC2.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloud9.EnvironmentEC2.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the environment.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloud9.EnvironmentEC2.automatic_stop_time_minutes">
<code class="sig-name descname">automatic_stop_time_minutes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloud9.EnvironmentEC2.automatic_stop_time_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of minutes until the running instance is shut down after the environment has last been used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloud9.EnvironmentEC2.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloud9.EnvironmentEC2.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the environment.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloud9.EnvironmentEC2.instance_type">
<code class="sig-name descname">instance_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloud9.EnvironmentEC2.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of instance to connect to the environment, e.g. <code class="docutils literal notranslate"><span class="pre">t2.micro</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloud9.EnvironmentEC2.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloud9.EnvironmentEC2.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the environment.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloud9.EnvironmentEC2.owner_arn">
<code class="sig-name descname">owner_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloud9.EnvironmentEC2.owner_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the environment owner. This can be ARN of any AWS IAM principal. Defaults to the environment’s creator.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloud9.EnvironmentEC2.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloud9.EnvironmentEC2.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the subnet in Amazon VPC that AWS Cloud9 will use to communicate with the Amazon EC2 instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloud9.EnvironmentEC2.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloud9.EnvironmentEC2.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloud9.EnvironmentEC2.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloud9.EnvironmentEC2.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the environment (e.g. <code class="docutils literal notranslate"><span class="pre">ssh</span></code> or <code class="docutils literal notranslate"><span class="pre">ec2</span></code>)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloud9.EnvironmentEC2.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">automatic_stop_time_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloud9.EnvironmentEC2.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EnvironmentEC2 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the environment.</p></li>
<li><p><strong>automatic_stop_time_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of minutes until the running instance is shut down after the environment has last been used.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the environment.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of instance to connect to the environment, e.g. <code class="docutils literal notranslate"><span class="pre">t2.micro</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the environment.</p></li>
<li><p><strong>owner_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the environment owner. This can be ARN of any AWS IAM principal. Defaults to the environment’s creator.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the subnet in Amazon VPC that AWS Cloud9 will use to communicate with the Amazon EC2 instance.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the environment (e.g. <code class="docutils literal notranslate"><span class="pre">ssh</span></code> or <code class="docutils literal notranslate"><span class="pre">ec2</span></code>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloud9.EnvironmentEC2.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloud9.EnvironmentEC2.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloud9.EnvironmentEC2.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloud9.EnvironmentEC2.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
