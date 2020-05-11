---
title: Module ssm
title_tag: Module ssm | Package pulumi_aws | Python SDK
linktitle: ssm
notitle: true
---

<div class="section" id="ssm">
<h1>ssm<a class="headerlink" href="#ssm" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.ssm"></span><dl class="py class">
<dt id="pulumi_aws.ssm.Activation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ssm.</code><code class="sig-name descname">Activation</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiration_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iam_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_limit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Activation" title="Permalink to this definition">¶</a></dt>
<dd><p>Registers an on-premises server or virtual machine with Amazon EC2 so that it can be managed using Run Command.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">test_role</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;testRole&quot;</span><span class="p">,</span> <span class="n">assume_role_policy</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;  {</span>
<span class="s2">    &quot;Version&quot;: &quot;2012-10-17&quot;,</span>
<span class="s2">    &quot;Statement&quot;: {</span>
<span class="s2">      &quot;Effect&quot;: &quot;Allow&quot;,</span>
<span class="s2">      &quot;Principal&quot;: {&quot;Service&quot;: &quot;ssm.amazonaws.com&quot;},</span>
<span class="s2">      &quot;Action&quot;: &quot;sts:AssumeRole&quot;</span>
<span class="s2">    }</span>
<span class="s2">  }</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
<span class="n">test_attach</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">RolePolicyAttachment</span><span class="p">(</span><span class="s2">&quot;testAttach&quot;</span><span class="p">,</span>
    <span class="n">policy_arn</span><span class="o">=</span><span class="s2">&quot;arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore&quot;</span><span class="p">,</span>
    <span class="n">role</span><span class="o">=</span><span class="n">test_role</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">foo</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ssm</span><span class="o">.</span><span class="n">Activation</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Test&quot;</span><span class="p">,</span>
    <span class="n">iam_role</span><span class="o">=</span><span class="n">test_role</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">registration_limit</span><span class="o">=</span><span class="s2">&quot;5&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the resource that you want to register.</p></li>
<li><p><strong>expiration_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – UTC timestamp in <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.8">RFC3339 format</a> by which this activation request should expire. The default value is 24 hours from resource creation time. This provider will only perform drift detection of its value when present in a configuration.</p></li>
<li><p><strong>iam_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM Role to attach to the managed instance.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default name of the registered managed instance.</p></li>
<li><p><strong>registration_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of managed instances you want to register. The default value is 1 instance.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the object.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.ssm.Activation.activation_code">
<code class="sig-name descname">activation_code</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Activation.activation_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The code the system generates when it processes the activation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Activation.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Activation.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the resource that you want to register.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Activation.expiration_date">
<code class="sig-name descname">expiration_date</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Activation.expiration_date" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC timestamp in <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.8">RFC3339 format</a> by which this activation request should expire. The default value is 24 hours from resource creation time. This provider will only perform drift detection of its value when present in a configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Activation.expired">
<code class="sig-name descname">expired</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Activation.expired" title="Permalink to this definition">¶</a></dt>
<dd><p>If the current activation has expired.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Activation.iam_role">
<code class="sig-name descname">iam_role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Activation.iam_role" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM Role to attach to the managed instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Activation.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Activation.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The default name of the registered managed instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Activation.registration_count">
<code class="sig-name descname">registration_count</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Activation.registration_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of managed instances that are currently registered using this activation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Activation.registration_limit">
<code class="sig-name descname">registration_limit</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Activation.registration_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of managed instances you want to register. The default value is 1 instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Activation.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Activation.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the object.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ssm.Activation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">activation_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiration_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expired</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iam_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_limit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Activation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Activation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>activation_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The code the system generates when it processes the activation.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the resource that you want to register.</p></li>
<li><p><strong>expiration_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>UTC timestamp in <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.8">RFC3339 format</a> by which this activation request should expire. The default value is 24 hours from resource creation time. This provider will only perform drift detection of its value when present in a configuration.</p>
</p></li>
<li><p><strong>expired</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If the current activation has expired.</p></li>
<li><p><strong>iam_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM Role to attach to the managed instance.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default name of the registered managed instance.</p></li>
<li><p><strong>registration_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of managed instances that are currently registered using this activation.</p></li>
<li><p><strong>registration_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of managed instances you want to register. The default value is 1 instance.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the object.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ssm.Activation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Activation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ssm.Activation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Activation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ssm.Association">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ssm.</code><code class="sig-name descname">Association</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">association_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">automation_target_parameter_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compliance_severity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">document_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_concurrency</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_errors</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schedule_expression</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">targets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Association" title="Permalink to this definition">¶</a></dt>
<dd><p>Associates an SSM Document to an instance or EC2 tag.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ssm</span><span class="o">.</span><span class="n">Association</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">targets</span><span class="o">=</span><span class="p">[{</span>
    <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;InstanceIds&quot;</span><span class="p">,</span>
    <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="n">aws_instance</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">]],</span>
<span class="p">}])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>association_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The descriptive name for the association.</p></li>
<li><p><strong>automation_target_parameter_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the target for the association. This target is required for associations that use an <code class="docutils literal notranslate"><span class="pre">Automation</span></code> document and target resources by using rate controls.</p></li>
<li><p><strong>compliance_severity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The compliance severity for the association. Can be one of the following: <code class="docutils literal notranslate"><span class="pre">UNSPECIFIED</span></code>, <code class="docutils literal notranslate"><span class="pre">LOW</span></code>, <code class="docutils literal notranslate"><span class="pre">MEDIUM</span></code>, <code class="docutils literal notranslate"><span class="pre">HIGH</span></code> or <code class="docutils literal notranslate"><span class="pre">CRITICAL</span></code></p></li>
<li><p><strong>document_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The document version you want to associate with the target(s). Can be a specific version or the default version.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance ID to apply an SSM document to. Use <code class="docutils literal notranslate"><span class="pre">targets</span></code> with key <code class="docutils literal notranslate"><span class="pre">InstanceIds</span></code> for document schema versions 2.0 and above.</p></li>
<li><p><strong>max_concurrency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%.</p></li>
<li><p><strong>max_errors</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify a number, for example 10, or a percentage of the target set, for example 10%.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SSM document to apply.</p></li>
<li><p><strong>output_location</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An output location block. Output Location is documented below.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A block of arbitrary string parameters to pass to the SSM document.</p></li>
<li><p><strong>schedule_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A cron expression when the association will be applied to the target(s).</p></li>
<li><p><strong>targets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A block containing the targets of the SSM association. Targets are documented below. AWS currently supports a maximum of 5 targets.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>output_location</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">s3_bucket_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The S3 bucket name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3_key_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The S3 bucket prefix. Results stored in the root if not configured.</p></li>
</ul>
<p>The <strong>targets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Either <code class="docutils literal notranslate"><span class="pre">InstanceIds</span></code> or <code class="docutils literal notranslate"><span class="pre">tag:Tag</span> <span class="pre">Name</span></code> to specify an EC2 tag.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of instance IDs or tag values. AWS currently limits this list size to one value.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.ssm.Association.association_id">
<code class="sig-name descname">association_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Association.association_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the SSM association.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Association.association_name">
<code class="sig-name descname">association_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Association.association_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The descriptive name for the association.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Association.automation_target_parameter_name">
<code class="sig-name descname">automation_target_parameter_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Association.automation_target_parameter_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify the target for the association. This target is required for associations that use an <code class="docutils literal notranslate"><span class="pre">Automation</span></code> document and target resources by using rate controls.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Association.compliance_severity">
<code class="sig-name descname">compliance_severity</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Association.compliance_severity" title="Permalink to this definition">¶</a></dt>
<dd><p>The compliance severity for the association. Can be one of the following: <code class="docutils literal notranslate"><span class="pre">UNSPECIFIED</span></code>, <code class="docutils literal notranslate"><span class="pre">LOW</span></code>, <code class="docutils literal notranslate"><span class="pre">MEDIUM</span></code>, <code class="docutils literal notranslate"><span class="pre">HIGH</span></code> or <code class="docutils literal notranslate"><span class="pre">CRITICAL</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Association.document_version">
<code class="sig-name descname">document_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Association.document_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The document version you want to associate with the target(s). Can be a specific version or the default version.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Association.instance_id">
<code class="sig-name descname">instance_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Association.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance ID to apply an SSM document to. Use <code class="docutils literal notranslate"><span class="pre">targets</span></code> with key <code class="docutils literal notranslate"><span class="pre">InstanceIds</span></code> for document schema versions 2.0 and above.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Association.max_concurrency">
<code class="sig-name descname">max_concurrency</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Association.max_concurrency" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Association.max_errors">
<code class="sig-name descname">max_errors</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Association.max_errors" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify a number, for example 10, or a percentage of the target set, for example 10%.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Association.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Association.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SSM document to apply.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Association.output_location">
<code class="sig-name descname">output_location</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Association.output_location" title="Permalink to this definition">¶</a></dt>
<dd><p>An output location block. Output Location is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">s3_bucket_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The S3 bucket name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3_key_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The S3 bucket prefix. Results stored in the root if not configured.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Association.parameters">
<code class="sig-name descname">parameters</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Association.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A block of arbitrary string parameters to pass to the SSM document.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Association.schedule_expression">
<code class="sig-name descname">schedule_expression</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Association.schedule_expression" title="Permalink to this definition">¶</a></dt>
<dd><p>A cron expression when the association will be applied to the target(s).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Association.targets">
<code class="sig-name descname">targets</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Association.targets" title="Permalink to this definition">¶</a></dt>
<dd><p>A block containing the targets of the SSM association. Targets are documented below. AWS currently supports a maximum of 5 targets.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Either <code class="docutils literal notranslate"><span class="pre">InstanceIds</span></code> or <code class="docutils literal notranslate"><span class="pre">tag:Tag</span> <span class="pre">Name</span></code> to specify an EC2 tag.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of instance IDs or tag values. AWS currently limits this list size to one value.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ssm.Association.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">association_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">association_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">automation_target_parameter_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compliance_severity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">document_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_concurrency</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_errors</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schedule_expression</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">targets</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Association.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Association resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>association_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the SSM association.</p></li>
<li><p><strong>association_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The descriptive name for the association.</p></li>
<li><p><strong>automation_target_parameter_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the target for the association. This target is required for associations that use an <code class="docutils literal notranslate"><span class="pre">Automation</span></code> document and target resources by using rate controls.</p></li>
<li><p><strong>compliance_severity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The compliance severity for the association. Can be one of the following: <code class="docutils literal notranslate"><span class="pre">UNSPECIFIED</span></code>, <code class="docutils literal notranslate"><span class="pre">LOW</span></code>, <code class="docutils literal notranslate"><span class="pre">MEDIUM</span></code>, <code class="docutils literal notranslate"><span class="pre">HIGH</span></code> or <code class="docutils literal notranslate"><span class="pre">CRITICAL</span></code></p></li>
<li><p><strong>document_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The document version you want to associate with the target(s). Can be a specific version or the default version.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance ID to apply an SSM document to. Use <code class="docutils literal notranslate"><span class="pre">targets</span></code> with key <code class="docutils literal notranslate"><span class="pre">InstanceIds</span></code> for document schema versions 2.0 and above.</p></li>
<li><p><strong>max_concurrency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%.</p></li>
<li><p><strong>max_errors</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify a number, for example 10, or a percentage of the target set, for example 10%.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SSM document to apply.</p></li>
<li><p><strong>output_location</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An output location block. Output Location is documented below.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A block of arbitrary string parameters to pass to the SSM document.</p></li>
<li><p><strong>schedule_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A cron expression when the association will be applied to the target(s).</p></li>
<li><p><strong>targets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A block containing the targets of the SSM association. Targets are documented below. AWS currently supports a maximum of 5 targets.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>output_location</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">s3_bucket_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The S3 bucket name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3_key_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The S3 bucket prefix. Results stored in the root if not configured.</p></li>
</ul>
<p>The <strong>targets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Either <code class="docutils literal notranslate"><span class="pre">InstanceIds</span></code> or <code class="docutils literal notranslate"><span class="pre">tag:Tag</span> <span class="pre">Name</span></code> to specify an EC2 tag.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of instance IDs or tag values. AWS currently limits this list size to one value.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ssm.Association.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Association.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ssm.Association.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Association.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ssm.AwaitableGetDocumentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ssm.</code><code class="sig-name descname">AwaitableGetDocumentResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">document_format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">document_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">document_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.AwaitableGetDocumentResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ssm.AwaitableGetParameterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ssm.</code><code class="sig-name descname">AwaitableGetParameterResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_decryption</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.AwaitableGetParameterResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ssm.AwaitableGetPatchBaselineResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ssm.</code><code class="sig-name descname">AwaitableGetPatchBaselineResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">default_baseline</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">operating_system</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.AwaitableGetPatchBaselineResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ssm.Document">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ssm.</code><code class="sig-name descname">Document</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attachments_sources</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">document_format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">document_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Document" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SSM Document resource</p>
<blockquote>
<div><p><strong>NOTE on updating SSM documents:</strong> Only documents with a schema version of 2.0
or greater can update their content once created, see <a class="reference external" href="http://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-ssm-docs.html#document-schemas-features">SSM Schema Features</a>. To update a document with an older
schema version you must recreate the resource.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ssm</span><span class="o">.</span><span class="n">Document</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">content</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;  {</span>
<span class="s2">    &quot;schemaVersion&quot;: &quot;1.2&quot;,</span>
<span class="s2">    &quot;description&quot;: &quot;Check ip configuration of a Linux instance.&quot;,</span>
<span class="s2">    &quot;parameters&quot;: {</span>

<span class="s2">    },</span>
<span class="s2">    &quot;runtimeConfig&quot;: {</span>
<span class="s2">      &quot;aws:runShellScript&quot;: {</span>
<span class="s2">        &quot;properties&quot;: [</span>
<span class="s2">          {</span>
<span class="s2">            &quot;id&quot;: &quot;0.aws:runShellScript&quot;,</span>
<span class="s2">            &quot;runCommand&quot;: [&quot;ifconfig&quot;]</span>
<span class="s2">          }</span>
<span class="s2">        ]</span>
<span class="s2">      }</span>
<span class="s2">    }</span>
<span class="s2">  }</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="n">document_type</span><span class="o">=</span><span class="s2">&quot;Command&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>The permissions attribute specifies how you want to share the document. If you share a document privately,
you must specify the AWS user account IDs for those people who can use the document. If you share a document
publicly, you must specify All as the account ID.</p>
<p>The permissions mapping supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> - The permission type for the document. The permission type can be <code class="docutils literal notranslate"><span class="pre">Share</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">account_ids</span></code> - The AWS user accounts that should have access to the document. The account IDs can either be a group of account IDs or <code class="docutils literal notranslate"><span class="pre">All</span></code>.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attachments_sources</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more configuration blocks describing attachments sources to a version of a document. Defined below.</p></li>
<li><p><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The JSON or YAML content of the document.</p></li>
<li><p><strong>document_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The format of the document. Valid document types include: <code class="docutils literal notranslate"><span class="pre">JSON</span></code> and <code class="docutils literal notranslate"><span class="pre">YAML</span></code></p></li>
<li><p><strong>document_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the document. Valid document types include: <code class="docutils literal notranslate"><span class="pre">Automation</span></code>, <code class="docutils literal notranslate"><span class="pre">Command</span></code>, <code class="docutils literal notranslate"><span class="pre">Package</span></code>, <code class="docutils literal notranslate"><span class="pre">Policy</span></code>, and <code class="docutils literal notranslate"><span class="pre">Session</span></code></p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the document.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Additional Permissions to attach to the document. See Permissions below for details.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the object.</p></li>
<li><p><strong>target_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target type which defines the kinds of resources the document can run on. For example, /AWS::EC2::Instance. For a list of valid resource types, see AWS Resource Types Reference (http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html)</p></li>
</ul>
</dd>
</dl>
<p>The <strong>attachments_sources</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The key describing the location of an attachment to a document. Valid key types include: <code class="docutils literal notranslate"><span class="pre">SourceUrl</span></code> and <code class="docutils literal notranslate"><span class="pre">S3FileUrl</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the document attachment file</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The value describing the location of an attachment to a document</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.ssm.Document.attachments_sources">
<code class="sig-name descname">attachments_sources</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.attachments_sources" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more configuration blocks describing attachments sources to a version of a document. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The key describing the location of an attachment to a document. Valid key types include: <code class="docutils literal notranslate"><span class="pre">SourceUrl</span></code> and <code class="docutils literal notranslate"><span class="pre">S3FileUrl</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the document attachment file</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The value describing the location of an attachment to a document</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Document.content">
<code class="sig-name descname">content</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.content" title="Permalink to this definition">¶</a></dt>
<dd><p>The JSON or YAML content of the document.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Document.created_date">
<code class="sig-name descname">created_date</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.created_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the document was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Document.default_version">
<code class="sig-name descname">default_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.default_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The default version of the document.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Document.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the document.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Document.document_format">
<code class="sig-name descname">document_format</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.document_format" title="Permalink to this definition">¶</a></dt>
<dd><p>The format of the document. Valid document types include: <code class="docutils literal notranslate"><span class="pre">JSON</span></code> and <code class="docutils literal notranslate"><span class="pre">YAML</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Document.document_type">
<code class="sig-name descname">document_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.document_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the document. Valid document types include: <code class="docutils literal notranslate"><span class="pre">Automation</span></code>, <code class="docutils literal notranslate"><span class="pre">Command</span></code>, <code class="docutils literal notranslate"><span class="pre">Package</span></code>, <code class="docutils literal notranslate"><span class="pre">Policy</span></code>, and <code class="docutils literal notranslate"><span class="pre">Session</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Document.hash">
<code class="sig-name descname">hash</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.hash" title="Permalink to this definition">¶</a></dt>
<dd><p>The sha1 or sha256 of the document content</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Document.hash_type">
<code class="sig-name descname">hash_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.hash_type" title="Permalink to this definition">¶</a></dt>
<dd><p>“Sha1” “Sha256”. The hashing algorithm used when hashing the content.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Document.latest_version">
<code class="sig-name descname">latest_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.latest_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The latest version of the document.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Document.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the document.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Document.owner">
<code class="sig-name descname">owner</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.owner" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS user account of the person who created the document.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Document.parameters">
<code class="sig-name descname">parameters</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>The parameters that are available to this document.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default_value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The description of the document.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the document.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Document.permissions">
<code class="sig-name descname">permissions</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>Additional Permissions to attach to the document. See Permissions below for details.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Document.platform_types">
<code class="sig-name descname">platform_types</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.platform_types" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of OS platforms compatible with this SSM document, either “Windows” or “Linux”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Document.schema_version">
<code class="sig-name descname">schema_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.schema_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The schema version of the document.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Document.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.status" title="Permalink to this definition">¶</a></dt>
<dd><p>“Creating”, “Active” or “Deleting”. The current status of the document.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Document.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the object.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Document.target_type">
<code class="sig-name descname">target_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.target_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The target type which defines the kinds of resources the document can run on. For example, /AWS::EC2::Instance. For a list of valid resource types, see AWS Resource Types Reference (http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ssm.Document.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attachments_sources</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">document_format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">document_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hash</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hash_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">latest_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">platform_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Document.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Document resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attachments_sources</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more configuration blocks describing attachments sources to a version of a document. Defined below.</p></li>
<li><p><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The JSON or YAML content of the document.</p></li>
<li><p><strong>created_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date the document was created.</p></li>
<li><p><strong>default_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default version of the document.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the document.</p></li>
<li><p><strong>document_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The format of the document. Valid document types include: <code class="docutils literal notranslate"><span class="pre">JSON</span></code> and <code class="docutils literal notranslate"><span class="pre">YAML</span></code></p></li>
<li><p><strong>document_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the document. Valid document types include: <code class="docutils literal notranslate"><span class="pre">Automation</span></code>, <code class="docutils literal notranslate"><span class="pre">Command</span></code>, <code class="docutils literal notranslate"><span class="pre">Package</span></code>, <code class="docutils literal notranslate"><span class="pre">Policy</span></code>, and <code class="docutils literal notranslate"><span class="pre">Session</span></code></p></li>
<li><p><strong>hash</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The sha1 or sha256 of the document content</p></li>
<li><p><strong>hash_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – “Sha1” “Sha256”. The hashing algorithm used when hashing the content.</p></li>
<li><p><strong>latest_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The latest version of the document.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the document.</p></li>
<li><p><strong>owner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS user account of the person who created the document.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The parameters that are available to this document.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Additional Permissions to attach to the document. See Permissions below for details.</p></li>
<li><p><strong>platform_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of OS platforms compatible with this SSM document, either “Windows” or “Linux”.</p></li>
<li><p><strong>schema_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The schema version of the document.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – “Creating”, “Active” or “Deleting”. The current status of the document.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the object.</p></li>
<li><p><strong>target_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target type which defines the kinds of resources the document can run on. For example, /AWS::EC2::Instance. For a list of valid resource types, see AWS Resource Types Reference (http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html)</p></li>
</ul>
</dd>
</dl>
<p>The <strong>attachments_sources</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The key describing the location of an attachment to a document. Valid key types include: <code class="docutils literal notranslate"><span class="pre">SourceUrl</span></code> and <code class="docutils literal notranslate"><span class="pre">S3FileUrl</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the document attachment file</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The value describing the location of an attachment to a document</p></li>
</ul>
<p>The <strong>parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default_value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of the document.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the document.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ssm.Document.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Document.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ssm.Document.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Document.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ssm.GetDocumentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ssm.</code><code class="sig-name descname">GetDocumentResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">document_format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">document_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">document_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.GetDocumentResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDocument.</p>
<dl class="py attribute">
<dt id="pulumi_aws.ssm.GetDocumentResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.GetDocumentResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the document.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.GetDocumentResult.content">
<code class="sig-name descname">content</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.GetDocumentResult.content" title="Permalink to this definition">¶</a></dt>
<dd><p>The contents of the document.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.GetDocumentResult.document_type">
<code class="sig-name descname">document_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.GetDocumentResult.document_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the document.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.GetDocumentResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.GetDocumentResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ssm.GetParameterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ssm.</code><code class="sig-name descname">GetParameterResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_decryption</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.GetParameterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getParameter.</p>
<dl class="py attribute">
<dt id="pulumi_aws.ssm.GetParameterResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.GetParameterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ssm.GetPatchBaselineResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ssm.</code><code class="sig-name descname">GetPatchBaselineResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">default_baseline</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">operating_system</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.GetPatchBaselineResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPatchBaseline.</p>
<dl class="py attribute">
<dt id="pulumi_aws.ssm.GetPatchBaselineResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.GetPatchBaselineResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the baseline.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.GetPatchBaselineResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.GetPatchBaselineResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.GetPatchBaselineResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.GetPatchBaselineResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the baseline.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ssm.MaintenanceWindow">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ssm.</code><code class="sig-name descname">MaintenanceWindow</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_unassociated_targets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cutoff</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">duration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schedule</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schedule_timezone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SSM Maintenance Window resource</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">production</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ssm</span><span class="o">.</span><span class="n">MaintenanceWindow</span><span class="p">(</span><span class="s2">&quot;production&quot;</span><span class="p">,</span>
    <span class="n">cutoff</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">duration</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
    <span class="n">schedule</span><span class="o">=</span><span class="s2">&quot;cron(0 16 ? * TUE *)&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_unassociated_targets</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether targets must be registered with the Maintenance Window before tasks can be defined for those targets.</p></li>
<li><p><strong>cutoff</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the maintenance window.</p></li>
<li><p><strong>duration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration of the Maintenance Window in hours.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the maintenance window is enabled. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>end_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Timestamp in <a class="reference external" href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO-8601 extended format</a> when to no longer run the maintenance window.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the maintenance window.</p></li>
<li><p><strong>schedule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The schedule of the Maintenance Window in the form of a <a class="reference external" href="https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-cron.html">cron</a> or rate expression.</p></li>
<li><p><strong>schedule_timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Timezone for schedule in <a class="reference external" href="https://www.iana.org/time-zones">Internet Assigned Numbers Authority (IANA) Time Zone Database format</a>. For example: <code class="docutils literal notranslate"><span class="pre">America/Los_Angeles</span></code>, <code class="docutils literal notranslate"><span class="pre">etc/UTC</span></code>, or <code class="docutils literal notranslate"><span class="pre">Asia/Seoul</span></code>.</p></li>
<li><p><strong>start_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Timestamp in <a class="reference external" href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO-8601 extended format</a> when to begin the maintenance window.</p>
</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindow.allow_unassociated_targets">
<code class="sig-name descname">allow_unassociated_targets</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow.allow_unassociated_targets" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether targets must be registered with the Maintenance Window before tasks can be defined for those targets.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindow.cutoff">
<code class="sig-name descname">cutoff</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow.cutoff" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindow.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the maintenance window.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindow.duration">
<code class="sig-name descname">duration</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow.duration" title="Permalink to this definition">¶</a></dt>
<dd><p>The duration of the Maintenance Window in hours.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindow.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the maintenance window is enabled. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindow.end_date">
<code class="sig-name descname">end_date</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow.end_date" title="Permalink to this definition">¶</a></dt>
<dd><p>Timestamp in <a class="reference external" href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO-8601 extended format</a> when to no longer run the maintenance window.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindow.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the maintenance window.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindow.schedule">
<code class="sig-name descname">schedule</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow.schedule" title="Permalink to this definition">¶</a></dt>
<dd><p>The schedule of the Maintenance Window in the form of a <a class="reference external" href="https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-cron.html">cron</a> or rate expression.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindow.schedule_timezone">
<code class="sig-name descname">schedule_timezone</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow.schedule_timezone" title="Permalink to this definition">¶</a></dt>
<dd><p>Timezone for schedule in <a class="reference external" href="https://www.iana.org/time-zones">Internet Assigned Numbers Authority (IANA) Time Zone Database format</a>. For example: <code class="docutils literal notranslate"><span class="pre">America/Los_Angeles</span></code>, <code class="docutils literal notranslate"><span class="pre">etc/UTC</span></code>, or <code class="docutils literal notranslate"><span class="pre">Asia/Seoul</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindow.start_date">
<code class="sig-name descname">start_date</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow.start_date" title="Permalink to this definition">¶</a></dt>
<dd><p>Timestamp in <a class="reference external" href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO-8601 extended format</a> when to begin the maintenance window.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindow.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ssm.MaintenanceWindow.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_unassociated_targets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cutoff</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">duration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schedule</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schedule_timezone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MaintenanceWindow resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_unassociated_targets</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether targets must be registered with the Maintenance Window before tasks can be defined for those targets.</p></li>
<li><p><strong>cutoff</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the maintenance window.</p></li>
<li><p><strong>duration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration of the Maintenance Window in hours.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the maintenance window is enabled. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>end_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Timestamp in <a class="reference external" href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO-8601 extended format</a> when to no longer run the maintenance window.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the maintenance window.</p></li>
<li><p><strong>schedule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The schedule of the Maintenance Window in the form of a <a class="reference external" href="https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-cron.html">cron</a> or rate expression.</p>
</p></li>
<li><p><strong>schedule_timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Timezone for schedule in <a class="reference external" href="https://www.iana.org/time-zones">Internet Assigned Numbers Authority (IANA) Time Zone Database format</a>. For example: <code class="docutils literal notranslate"><span class="pre">America/Los_Angeles</span></code>, <code class="docutils literal notranslate"><span class="pre">etc/UTC</span></code>, or <code class="docutils literal notranslate"><span class="pre">Asia/Seoul</span></code>.</p>
</p></li>
<li><p><strong>start_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Timestamp in <a class="reference external" href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO-8601 extended format</a> when to begin the maintenance window.</p>
</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ssm.MaintenanceWindow.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ssm.MaintenanceWindow.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ssm.MaintenanceWindowTarget">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ssm.</code><code class="sig-name descname">MaintenanceWindowTarget</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_information</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">targets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">window_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTarget" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SSM Maintenance Window Target resource</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">window</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ssm</span><span class="o">.</span><span class="n">MaintenanceWindow</span><span class="p">(</span><span class="s2">&quot;window&quot;</span><span class="p">,</span>
    <span class="n">cutoff</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">duration</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
    <span class="n">schedule</span><span class="o">=</span><span class="s2">&quot;cron(0 16 ? * TUE *)&quot;</span><span class="p">)</span>
<span class="n">target1</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ssm</span><span class="o">.</span><span class="n">MaintenanceWindowTarget</span><span class="p">(</span><span class="s2">&quot;target1&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;This is a maintenance window target&quot;</span><span class="p">,</span>
    <span class="n">resource_type</span><span class="o">=</span><span class="s2">&quot;INSTANCE&quot;</span><span class="p">,</span>
    <span class="n">targets</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;tag:Name&quot;</span><span class="p">,</span>
        <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;acceptance_test&quot;</span><span class="p">],</span>
    <span class="p">}],</span>
    <span class="n">window_id</span><span class="o">=</span><span class="n">window</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">window</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ssm</span><span class="o">.</span><span class="n">MaintenanceWindow</span><span class="p">(</span><span class="s2">&quot;window&quot;</span><span class="p">,</span>
    <span class="n">cutoff</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">duration</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
    <span class="n">schedule</span><span class="o">=</span><span class="s2">&quot;cron(0 16 ? * TUE *)&quot;</span><span class="p">)</span>
<span class="n">target1</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ssm</span><span class="o">.</span><span class="n">MaintenanceWindowTarget</span><span class="p">(</span><span class="s2">&quot;target1&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;This is a maintenance window target&quot;</span><span class="p">,</span>
    <span class="n">resource_type</span><span class="o">=</span><span class="s2">&quot;RESOURCE_GROUP&quot;</span><span class="p">,</span>
    <span class="n">targets</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;resource-groups:ResourceTypeFilters&quot;</span><span class="p">,</span>
        <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="s2">&quot;AWS::EC2::INSTANCE&quot;</span><span class="p">,</span>
            <span class="s2">&quot;AWS::EC2::VPC&quot;</span><span class="p">,</span>
        <span class="p">],</span>
    <span class="p">}],</span>
    <span class="n">window_id</span><span class="o">=</span><span class="n">window</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the maintenance window target.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the maintenance window target.</p></li>
<li><p><strong>owner_information</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.</p></li>
<li><p><strong>resource_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of target being registered with the Maintenance Window. Possible values are <code class="docutils literal notranslate"><span class="pre">INSTANCE</span></code> and <code class="docutils literal notranslate"><span class="pre">RESOURCE_GROUP</span></code>.</p></li>
<li><p><strong>targets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The targets to register with the maintenance window. In other words, the instances to run commands on when the maintenance window runs. You can specify targets using instance IDs, resource group names, or tags that have been applied to instances. For more information about these examples formats see
(<a class="reference external" href="https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-targets-examples.html">https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-targets-examples.html</a>)</p></li>
<li><p><strong>window_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of the maintenance window to register the target with.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>targets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTarget.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTarget.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the maintenance window target.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTarget.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTarget.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the maintenance window target.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTarget.owner_information">
<code class="sig-name descname">owner_information</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTarget.owner_information" title="Permalink to this definition">¶</a></dt>
<dd><p>User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTarget.resource_type">
<code class="sig-name descname">resource_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTarget.resource_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of target being registered with the Maintenance Window. Possible values are <code class="docutils literal notranslate"><span class="pre">INSTANCE</span></code> and <code class="docutils literal notranslate"><span class="pre">RESOURCE_GROUP</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTarget.targets">
<code class="sig-name descname">targets</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTarget.targets" title="Permalink to this definition">¶</a></dt>
<dd><p>The targets to register with the maintenance window. In other words, the instances to run commands on when the maintenance window runs. You can specify targets using instance IDs, resource group names, or tags that have been applied to instances. For more information about these examples formats see
(<a class="reference external" href="https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-targets-examples.html">https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-targets-examples.html</a>)</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTarget.window_id">
<code class="sig-name descname">window_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTarget.window_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of the maintenance window to register the target with.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ssm.MaintenanceWindowTarget.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_information</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">targets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">window_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTarget.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MaintenanceWindowTarget resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the maintenance window target.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the maintenance window target.</p></li>
<li><p><strong>owner_information</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.</p></li>
<li><p><strong>resource_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of target being registered with the Maintenance Window. Possible values are <code class="docutils literal notranslate"><span class="pre">INSTANCE</span></code> and <code class="docutils literal notranslate"><span class="pre">RESOURCE_GROUP</span></code>.</p></li>
<li><p><strong>targets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The targets to register with the maintenance window. In other words, the instances to run commands on when the maintenance window runs. You can specify targets using instance IDs, resource group names, or tags that have been applied to instances. For more information about these examples formats see
(<a class="reference external" href="https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-targets-examples.html">https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-targets-examples.html</a>)</p></li>
<li><p><strong>window_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of the maintenance window to register the target with.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>targets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ssm.MaintenanceWindowTarget.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTarget.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ssm.MaintenanceWindowTarget.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTarget.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ssm.MaintenanceWindowTask">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ssm.</code><code class="sig-name descname">MaintenanceWindowTask</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_info</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_concurrency</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_errors</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">targets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_invocation_parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">window_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SSM Maintenance Window Task resource</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ssm</span><span class="o">.</span><span class="n">MaintenanceWindowTask</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">max_concurrency</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">max_errors</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">priority</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">service_role_arn</span><span class="o">=</span><span class="n">aws_iam_role</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;arn&quot;</span><span class="p">],</span>
    <span class="n">targets</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;InstanceIds&quot;</span><span class="p">,</span>
        <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="n">aws_instance</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">]],</span>
    <span class="p">}],</span>
    <span class="n">task_arn</span><span class="o">=</span><span class="s2">&quot;AWS-RestartEC2Instance&quot;</span><span class="p">,</span>
    <span class="n">task_invocation_parameters</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;automationParameters&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;documentVersion&quot;</span><span class="p">:</span> <span class="s2">&quot;$$LATEST&quot;</span><span class="p">,</span>
            <span class="s2">&quot;parameter&quot;</span><span class="p">:</span> <span class="p">[{</span>
                <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;InstanceId&quot;</span><span class="p">,</span>
                <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="n">aws_instance</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">]],</span>
            <span class="p">}],</span>
        <span class="p">},</span>
    <span class="p">},</span>
    <span class="n">task_type</span><span class="o">=</span><span class="s2">&quot;AUTOMATION&quot;</span><span class="p">,</span>
    <span class="n">window_id</span><span class="o">=</span><span class="n">aws_ssm_maintenance_window</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ssm</span><span class="o">.</span><span class="n">MaintenanceWindowTask</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">max_concurrency</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">max_errors</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">priority</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">service_role_arn</span><span class="o">=</span><span class="n">aws_iam_role</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;arn&quot;</span><span class="p">],</span>
    <span class="n">targets</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;InstanceIds&quot;</span><span class="p">,</span>
        <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="n">aws_instance</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">]],</span>
    <span class="p">}],</span>
    <span class="n">task_arn</span><span class="o">=</span><span class="s2">&quot;AWS-RunShellScript&quot;</span><span class="p">,</span>
    <span class="n">task_invocation_parameters</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;runCommandParameters&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;notificationConfig&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;notificationArn&quot;</span><span class="p">:</span> <span class="n">aws_sns_topic</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;arn&quot;</span><span class="p">],</span>
                <span class="s2">&quot;notificationEvents&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;All&quot;</span><span class="p">],</span>
                <span class="s2">&quot;notificationType&quot;</span><span class="p">:</span> <span class="s2">&quot;Command&quot;</span><span class="p">,</span>
            <span class="p">},</span>
            <span class="s2">&quot;outputS3Bucket&quot;</span><span class="p">:</span> <span class="n">aws_s3_bucket</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;bucket&quot;</span><span class="p">],</span>
            <span class="s2">&quot;outputS3KeyPrefix&quot;</span><span class="p">:</span> <span class="s2">&quot;output&quot;</span><span class="p">,</span>
            <span class="s2">&quot;parameter&quot;</span><span class="p">:</span> <span class="p">[{</span>
                <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;commands&quot;</span><span class="p">,</span>
                <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;date&quot;</span><span class="p">],</span>
            <span class="p">}],</span>
            <span class="s2">&quot;serviceRoleArn&quot;</span><span class="p">:</span> <span class="n">aws_iam_role</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;arn&quot;</span><span class="p">],</span>
            <span class="s2">&quot;timeoutSeconds&quot;</span><span class="p">:</span> <span class="mi">600</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">},</span>
    <span class="n">task_type</span><span class="o">=</span><span class="s2">&quot;RUN_COMMAND&quot;</span><span class="p">,</span>
    <span class="n">window_id</span><span class="o">=</span><span class="n">aws_ssm_maintenance_window</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ssm</span><span class="o">.</span><span class="n">MaintenanceWindowTask</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">max_concurrency</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">max_errors</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">priority</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">service_role_arn</span><span class="o">=</span><span class="n">aws_iam_role</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;arn&quot;</span><span class="p">],</span>
    <span class="n">targets</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;InstanceIds&quot;</span><span class="p">,</span>
        <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="n">aws_instance</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">]],</span>
    <span class="p">}],</span>
    <span class="n">task_arn</span><span class="o">=</span><span class="n">aws_sfn_activity</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">task_invocation_parameters</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;stepFunctionsParameters&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;input&quot;</span><span class="p">:</span> <span class="s2">&quot;{&quot;</span><span class="n">key1</span><span class="s2">&quot;:&quot;</span><span class="n">value1</span><span class="s2">&quot;}&quot;</span><span class="p">,</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;example&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">},</span>
    <span class="n">task_type</span><span class="o">=</span><span class="s2">&quot;STEP_FUNCTIONS&quot;</span><span class="p">,</span>
    <span class="n">window_id</span><span class="o">=</span><span class="n">aws_ssm_maintenance_window</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the maintenance window task.</p></li>
<li><p><strong>logging_info</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A structure containing information about an Amazon S3 bucket to write instance-level logs to. Use <code class="docutils literal notranslate"><span class="pre">task_invocation_parameters</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">run_command_parameters</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">output_s3_*</span></code> arguments instead. Conflicts with <code class="docutils literal notranslate"><span class="pre">task_invocation_parameters</span></code>. Documented below.</p></li>
<li><p><strong>max_concurrency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum number of targets this task can be run for in parallel.</p></li>
<li><p><strong>max_errors</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum number of errors allowed before this task stops being scheduled.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the maintenance window task.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the task in the Maintenance Window, the lower the number the higher the priority. Tasks in a Maintenance Window are scheduled in priority order with tasks that have the same priority scheduled in parallel.</p></li>
<li><p><strong>service_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be assumed when executing the task.</p></li>
<li><p><strong>targets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The targets (either instances or window target ids). Instances are specified using Key=InstanceIds,Values=instanceid1,instanceid2. Window target ids are specified using Key=WindowTargetIds,Values=window target id1, window target id2.</p></li>
<li><p><strong>task_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the task to execute.</p></li>
<li><p><strong>task_invocation_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The parameters for task execution. This argument is conflict with <code class="docutils literal notranslate"><span class="pre">task_parameters</span></code> and <code class="docutils literal notranslate"><span class="pre">logging_info</span></code>.</p></li>
<li><p><strong>task_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A structure containing information about parameters required by the particular <code class="docutils literal notranslate"><span class="pre">task_arn</span></code>. Use <code class="docutils literal notranslate"><span class="pre">parameter</span></code> configuration blocks under the <code class="docutils literal notranslate"><span class="pre">task_invocation_parameters</span></code> configuration block instead. Conflicts with <code class="docutils literal notranslate"><span class="pre">task_invocation_parameters</span></code>. Documented below.</p></li>
<li><p><strong>task_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of task being registered. The only allowed value is <code class="docutils literal notranslate"><span class="pre">RUN_COMMAND</span></code>.</p></li>
<li><p><strong>window_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of the maintenance window to register the task with.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>logging_info</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">s3_bucket_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3BucketPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3_region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>targets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>task_invocation_parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automationParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The parameters for an AUTOMATION task type. Documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">document_version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of an Automation document to use during task execution.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The parameters for the RUN_COMMAND task execution. Documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The parameter name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The array of strings.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">lambdaParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The parameters for a LAMBDA task type. Documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">clientContext</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Pass client-specific information to the Lambda function that you are invoking.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">payload</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - JSON to provide to your Lambda function as input.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">qualifier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specify a Lambda function version or alias name.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">runCommandParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The parameters for a RUN_COMMAND task type. Documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Information about the command(s) to execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">documentHash</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">documentHashType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - SHA-256 or SHA-1. SHA-1 hashes have been deprecated. Valid values: <code class="docutils literal notranslate"><span class="pre">Sha256</span></code> and <code class="docutils literal notranslate"><span class="pre">Sha1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notificationConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configurations for sending notifications about command status changes on a per-instance basis. Documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">notificationArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notificationEvents</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The different events for which you can receive notifications. Valid values: <code class="docutils literal notranslate"><span class="pre">All</span></code>, <code class="docutils literal notranslate"><span class="pre">InProgress</span></code>, <code class="docutils literal notranslate"><span class="pre">Success</span></code>, <code class="docutils literal notranslate"><span class="pre">TimedOut</span></code>, <code class="docutils literal notranslate"><span class="pre">Cancelled</span></code>, and <code class="docutils literal notranslate"><span class="pre">Failed</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notification_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When specified with <code class="docutils literal notranslate"><span class="pre">Command</span></code>, receive notification when the status of a command changes. When specified with <code class="docutils literal notranslate"><span class="pre">Invocation</span></code>, for commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. Valid values: <code class="docutils literal notranslate"><span class="pre">Command</span></code> and <code class="docutils literal notranslate"><span class="pre">Invocation</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">outputS3Bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Amazon S3 bucket.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">outputS3KeyPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon S3 bucket subfolder.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The parameters for the RUN_COMMAND task execution. Documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The parameter name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The array of strings.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IAM service role to assume during task execution.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeoutSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - If this time is reached and the command has not already started executing, it doesn’t run.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">stepFunctionsParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The parameters for a STEP_FUNCTIONS task type. Documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">input</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The inputs for the STEP_FUNCTION task.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the STEP_FUNCTION task.</p></li>
</ul>
</li>
</ul>
<p>The <strong>task_parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the maintenance window task.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the maintenance window task.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.logging_info">
<code class="sig-name descname">logging_info</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.logging_info" title="Permalink to this definition">¶</a></dt>
<dd><p>A structure containing information about an Amazon S3 bucket to write instance-level logs to. Use <code class="docutils literal notranslate"><span class="pre">task_invocation_parameters</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">run_command_parameters</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">output_s3_*</span></code> arguments instead. Conflicts with <code class="docutils literal notranslate"><span class="pre">task_invocation_parameters</span></code>. Documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">s3_bucket_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3BucketPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3_region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.max_concurrency">
<code class="sig-name descname">max_concurrency</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.max_concurrency" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of targets this task can be run for in parallel.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.max_errors">
<code class="sig-name descname">max_errors</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.max_errors" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of errors allowed before this task stops being scheduled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the maintenance window task.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.priority">
<code class="sig-name descname">priority</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the task in the Maintenance Window, the lower the number the higher the priority. Tasks in a Maintenance Window are scheduled in priority order with tasks that have the same priority scheduled in parallel.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.service_role_arn">
<code class="sig-name descname">service_role_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.service_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be assumed when executing the task.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.targets">
<code class="sig-name descname">targets</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.targets" title="Permalink to this definition">¶</a></dt>
<dd><p>The targets (either instances or window target ids). Instances are specified using Key=InstanceIds,Values=instanceid1,instanceid2. Window target ids are specified using Key=WindowTargetIds,Values=window target id1, window target id2.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.task_arn">
<code class="sig-name descname">task_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.task_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the task to execute.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.task_invocation_parameters">
<code class="sig-name descname">task_invocation_parameters</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.task_invocation_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>The parameters for task execution. This argument is conflict with <code class="docutils literal notranslate"><span class="pre">task_parameters</span></code> and <code class="docutils literal notranslate"><span class="pre">logging_info</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automationParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The parameters for an AUTOMATION task type. Documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">document_version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The version of an Automation document to use during task execution.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The parameters for the RUN_COMMAND task execution. Documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The parameter name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The array of strings.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">lambdaParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The parameters for a LAMBDA task type. Documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">clientContext</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Pass client-specific information to the Lambda function that you are invoking.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">payload</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - JSON to provide to your Lambda function as input.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">qualifier</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specify a Lambda function version or alias name.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">runCommandParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The parameters for a RUN_COMMAND task type. Documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Information about the command(s) to execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">documentHash</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">documentHashType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - SHA-256 or SHA-1. SHA-1 hashes have been deprecated. Valid values: <code class="docutils literal notranslate"><span class="pre">Sha256</span></code> and <code class="docutils literal notranslate"><span class="pre">Sha1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notificationConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Configurations for sending notifications about command status changes on a per-instance basis. Documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">notificationArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notificationEvents</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The different events for which you can receive notifications. Valid values: <code class="docutils literal notranslate"><span class="pre">All</span></code>, <code class="docutils literal notranslate"><span class="pre">InProgress</span></code>, <code class="docutils literal notranslate"><span class="pre">Success</span></code>, <code class="docutils literal notranslate"><span class="pre">TimedOut</span></code>, <code class="docutils literal notranslate"><span class="pre">Cancelled</span></code>, and <code class="docutils literal notranslate"><span class="pre">Failed</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notification_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - When specified with <code class="docutils literal notranslate"><span class="pre">Command</span></code>, receive notification when the status of a command changes. When specified with <code class="docutils literal notranslate"><span class="pre">Invocation</span></code>, for commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. Valid values: <code class="docutils literal notranslate"><span class="pre">Command</span></code> and <code class="docutils literal notranslate"><span class="pre">Invocation</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">outputS3Bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Amazon S3 bucket.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">outputS3KeyPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Amazon S3 bucket subfolder.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The parameters for the RUN_COMMAND task execution. Documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The parameter name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The array of strings.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The IAM service role to assume during task execution.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeoutSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - If this time is reached and the command has not already started executing, it doesn’t run.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">stepFunctionsParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The parameters for a STEP_FUNCTIONS task type. Documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">input</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The inputs for the STEP_FUNCTION task.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the STEP_FUNCTION task.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.task_parameters">
<code class="sig-name descname">task_parameters</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.task_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A structure containing information about parameters required by the particular <code class="docutils literal notranslate"><span class="pre">task_arn</span></code>. Use <code class="docutils literal notranslate"><span class="pre">parameter</span></code> configuration blocks under the <code class="docutils literal notranslate"><span class="pre">task_invocation_parameters</span></code> configuration block instead. Conflicts with <code class="docutils literal notranslate"><span class="pre">task_invocation_parameters</span></code>. Documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the maintenance window task.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.task_type">
<code class="sig-name descname">task_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.task_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of task being registered. The only allowed value is <code class="docutils literal notranslate"><span class="pre">RUN_COMMAND</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.window_id">
<code class="sig-name descname">window_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.window_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of the maintenance window to register the task with.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_info</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_concurrency</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_errors</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">targets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_invocation_parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">window_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MaintenanceWindowTask resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the maintenance window task.</p></li>
<li><p><strong>logging_info</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A structure containing information about an Amazon S3 bucket to write instance-level logs to. Use <code class="docutils literal notranslate"><span class="pre">task_invocation_parameters</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">run_command_parameters</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">output_s3_*</span></code> arguments instead. Conflicts with <code class="docutils literal notranslate"><span class="pre">task_invocation_parameters</span></code>. Documented below.</p></li>
<li><p><strong>max_concurrency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum number of targets this task can be run for in parallel.</p></li>
<li><p><strong>max_errors</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum number of errors allowed before this task stops being scheduled.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the maintenance window task.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the task in the Maintenance Window, the lower the number the higher the priority. Tasks in a Maintenance Window are scheduled in priority order with tasks that have the same priority scheduled in parallel.</p></li>
<li><p><strong>service_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be assumed when executing the task.</p></li>
<li><p><strong>targets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The targets (either instances or window target ids). Instances are specified using Key=InstanceIds,Values=instanceid1,instanceid2. Window target ids are specified using Key=WindowTargetIds,Values=window target id1, window target id2.</p></li>
<li><p><strong>task_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the task to execute.</p></li>
<li><p><strong>task_invocation_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The parameters for task execution. This argument is conflict with <code class="docutils literal notranslate"><span class="pre">task_parameters</span></code> and <code class="docutils literal notranslate"><span class="pre">logging_info</span></code>.</p></li>
<li><p><strong>task_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A structure containing information about parameters required by the particular <code class="docutils literal notranslate"><span class="pre">task_arn</span></code>. Use <code class="docutils literal notranslate"><span class="pre">parameter</span></code> configuration blocks under the <code class="docutils literal notranslate"><span class="pre">task_invocation_parameters</span></code> configuration block instead. Conflicts with <code class="docutils literal notranslate"><span class="pre">task_invocation_parameters</span></code>. Documented below.</p></li>
<li><p><strong>task_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of task being registered. The only allowed value is <code class="docutils literal notranslate"><span class="pre">RUN_COMMAND</span></code>.</p></li>
<li><p><strong>window_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of the maintenance window to register the task with.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>logging_info</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">s3_bucket_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3BucketPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3_region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>targets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>task_invocation_parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automationParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The parameters for an AUTOMATION task type. Documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">document_version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of an Automation document to use during task execution.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The parameters for the RUN_COMMAND task execution. Documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The parameter name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The array of strings.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">lambdaParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The parameters for a LAMBDA task type. Documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">clientContext</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Pass client-specific information to the Lambda function that you are invoking.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">payload</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - JSON to provide to your Lambda function as input.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">qualifier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specify a Lambda function version or alias name.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">runCommandParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The parameters for a RUN_COMMAND task type. Documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">comment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Information about the command(s) to execute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">documentHash</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">documentHashType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - SHA-256 or SHA-1. SHA-1 hashes have been deprecated. Valid values: <code class="docutils literal notranslate"><span class="pre">Sha256</span></code> and <code class="docutils literal notranslate"><span class="pre">Sha1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notificationConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configurations for sending notifications about command status changes on a per-instance basis. Documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">notificationArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notificationEvents</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The different events for which you can receive notifications. Valid values: <code class="docutils literal notranslate"><span class="pre">All</span></code>, <code class="docutils literal notranslate"><span class="pre">InProgress</span></code>, <code class="docutils literal notranslate"><span class="pre">Success</span></code>, <code class="docutils literal notranslate"><span class="pre">TimedOut</span></code>, <code class="docutils literal notranslate"><span class="pre">Cancelled</span></code>, and <code class="docutils literal notranslate"><span class="pre">Failed</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notification_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - When specified with <code class="docutils literal notranslate"><span class="pre">Command</span></code>, receive notification when the status of a command changes. When specified with <code class="docutils literal notranslate"><span class="pre">Invocation</span></code>, for commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. Valid values: <code class="docutils literal notranslate"><span class="pre">Command</span></code> and <code class="docutils literal notranslate"><span class="pre">Invocation</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">outputS3Bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Amazon S3 bucket.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">outputS3KeyPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon S3 bucket subfolder.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The parameters for the RUN_COMMAND task execution. Documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The parameter name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The array of strings.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IAM service role to assume during task execution.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeoutSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - If this time is reached and the command has not already started executing, it doesn’t run.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">stepFunctionsParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The parameters for a STEP_FUNCTIONS task type. Documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">input</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The inputs for the STEP_FUNCTION task.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the STEP_FUNCTION task.</p></li>
</ul>
</li>
</ul>
<p>The <strong>task_parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the maintenance window task.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ssm.Parameter">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ssm.</code><code class="sig-name descname">Parameter</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_pattern</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">overwrite</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Parameter" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SSM Parameter resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ssm</span><span class="o">.</span><span class="n">Parameter</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;String&quot;</span><span class="p">,</span>
    <span class="n">value</span><span class="o">=</span><span class="s2">&quot;bar&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression used to validate the parameter value.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the parameter.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the parameter.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The KMS key id or arn for encrypting a SecureString.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the parameter. If the name contains a path (e.g. any forward slashes (<code class="docutils literal notranslate"><span class="pre">/</span></code>)), it must be fully qualified with a leading forward slash (<code class="docutils literal notranslate"><span class="pre">/</span></code>). For additional requirements and constraints, see the <a class="reference external" href="https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-parameter-name-constraints.html">AWS SSM User Guide</a>.</p></li>
<li><p><strong>overwrite</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Overwrite an existing parameter. If not specified, will default to <code class="docutils literal notranslate"><span class="pre">false</span></code> if the resource has not been created by this provider to avoid overwrite of existing resource and will default to <code class="docutils literal notranslate"><span class="pre">true</span></code> otherwise (lifecycle rules should then be used to manage the update behavior).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the object.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The tier of the parameter. If not specified, will default to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Valid tiers are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Advanced</span></code>. For more information on parameter tiers, see the <a class="reference external" href="https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html">AWS SSM Parameter tier comparison and guide</a>.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the parameter. Valid types are <code class="docutils literal notranslate"><span class="pre">String</span></code>, <code class="docutils literal notranslate"><span class="pre">StringList</span></code> and <code class="docutils literal notranslate"><span class="pre">SecureString</span></code>.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the parameter.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.ssm.Parameter.allowed_pattern">
<code class="sig-name descname">allowed_pattern</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Parameter.allowed_pattern" title="Permalink to this definition">¶</a></dt>
<dd><p>A regular expression used to validate the parameter value.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Parameter.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Parameter.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the parameter.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Parameter.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Parameter.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the parameter.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Parameter.key_id">
<code class="sig-name descname">key_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Parameter.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The KMS key id or arn for encrypting a SecureString.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Parameter.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Parameter.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the parameter. If the name contains a path (e.g. any forward slashes (<code class="docutils literal notranslate"><span class="pre">/</span></code>)), it must be fully qualified with a leading forward slash (<code class="docutils literal notranslate"><span class="pre">/</span></code>). For additional requirements and constraints, see the <a class="reference external" href="https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-parameter-name-constraints.html">AWS SSM User Guide</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Parameter.overwrite">
<code class="sig-name descname">overwrite</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Parameter.overwrite" title="Permalink to this definition">¶</a></dt>
<dd><p>Overwrite an existing parameter. If not specified, will default to <code class="docutils literal notranslate"><span class="pre">false</span></code> if the resource has not been created by this provider to avoid overwrite of existing resource and will default to <code class="docutils literal notranslate"><span class="pre">true</span></code> otherwise (lifecycle rules should then be used to manage the update behavior).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Parameter.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Parameter.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the object.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Parameter.tier">
<code class="sig-name descname">tier</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Parameter.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>The tier of the parameter. If not specified, will default to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Valid tiers are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Advanced</span></code>. For more information on parameter tiers, see the <a class="reference external" href="https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html">AWS SSM Parameter tier comparison and guide</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Parameter.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Parameter.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the parameter. Valid types are <code class="docutils literal notranslate"><span class="pre">String</span></code>, <code class="docutils literal notranslate"><span class="pre">StringList</span></code> and <code class="docutils literal notranslate"><span class="pre">SecureString</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Parameter.value">
<code class="sig-name descname">value</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Parameter.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the parameter.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.Parameter.version">
<code class="sig-name descname">version</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Parameter.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the parameter.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ssm.Parameter.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_pattern</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">overwrite</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tier</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Parameter.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Parameter resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression used to validate the parameter value.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the parameter.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the parameter.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The KMS key id or arn for encrypting a SecureString.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of the parameter. If the name contains a path (e.g. any forward slashes (<code class="docutils literal notranslate"><span class="pre">/</span></code>)), it must be fully qualified with a leading forward slash (<code class="docutils literal notranslate"><span class="pre">/</span></code>). For additional requirements and constraints, see the <a class="reference external" href="https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-parameter-name-constraints.html">AWS SSM User Guide</a>.</p>
</p></li>
<li><p><strong>overwrite</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Overwrite an existing parameter. If not specified, will default to <code class="docutils literal notranslate"><span class="pre">false</span></code> if the resource has not been created by this provider to avoid overwrite of existing resource and will default to <code class="docutils literal notranslate"><span class="pre">true</span></code> otherwise (lifecycle rules should then be used to manage the update behavior).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the object.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The tier of the parameter. If not specified, will default to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Valid tiers are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Advanced</span></code>. For more information on parameter tiers, see the <a class="reference external" href="https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html">AWS SSM Parameter tier comparison and guide</a>.</p>
</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the parameter. Valid types are <code class="docutils literal notranslate"><span class="pre">String</span></code>, <code class="docutils literal notranslate"><span class="pre">StringList</span></code> and <code class="docutils literal notranslate"><span class="pre">SecureString</span></code>.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the parameter.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The version of the parameter.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ssm.Parameter.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Parameter.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ssm.Parameter.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Parameter.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ssm.PatchBaseline">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ssm.</code><code class="sig-name descname">PatchBaseline</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">approval_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">approved_patches</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">approved_patches_compliance_level</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">global_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">operating_system</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rejected_patches</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.PatchBaseline" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SSM Patch Baseline resource</p>
<blockquote>
<div><p><strong>NOTE on Patch Baselines:</strong> The <code class="docutils literal notranslate"><span class="pre">approved_patches</span></code> and <code class="docutils literal notranslate"><span class="pre">approval_rule</span></code> are 
both marked as optional fields, but the Patch Baseline requires that at least one
of them is specified.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">production</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ssm</span><span class="o">.</span><span class="n">PatchBaseline</span><span class="p">(</span><span class="s2">&quot;production&quot;</span><span class="p">,</span> <span class="n">approved_patches</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;KB123456&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>approval_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of rules used to include patches in the baseline. up to 10 approval rules can be specified. Each approval_rule block requires the fields documented below.</p></li>
<li><p><strong>approved_patches</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of explicitly approved patches for the baseline.</p></li>
<li><p><strong>approved_patches_compliance_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the compliance level for approved patches. This means that if an approved patch is reported as missing, this is the severity of the compliance violation. Valid compliance levels include the following: <code class="docutils literal notranslate"><span class="pre">CRITICAL</span></code>, <code class="docutils literal notranslate"><span class="pre">HIGH</span></code>, <code class="docutils literal notranslate"><span class="pre">MEDIUM</span></code>, <code class="docutils literal notranslate"><span class="pre">LOW</span></code>, <code class="docutils literal notranslate"><span class="pre">INFORMATIONAL</span></code>, <code class="docutils literal notranslate"><span class="pre">UNSPECIFIED</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">UNSPECIFIED</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the patch baseline.</p></li>
<li><p><strong>global_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of global filters used to exclude patches from the baseline. Up to 4 global filters can be specified using Key/Value pairs. Valid Keys are <code class="docutils literal notranslate"><span class="pre">PRODUCT</span> <span class="pre">|</span> <span class="pre">CLASSIFICATION</span> <span class="pre">|</span> <span class="pre">MSRC_SEVERITY</span> <span class="pre">|</span> <span class="pre">PATCH_ID</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the patch baseline.</p></li>
<li><p><strong>operating_system</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the operating system the patch baseline applies to. Supported operating systems include <code class="docutils literal notranslate"><span class="pre">WINDOWS</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_LINUX</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_LINUX_2</span></code>, <code class="docutils literal notranslate"><span class="pre">SUSE</span></code>, <code class="docutils literal notranslate"><span class="pre">UBUNTU</span></code>, <code class="docutils literal notranslate"><span class="pre">CENTOS</span></code>, and <code class="docutils literal notranslate"><span class="pre">REDHAT_ENTERPRISE_LINUX</span></code>. The Default value is <code class="docutils literal notranslate"><span class="pre">WINDOWS</span></code>.</p></li>
<li><p><strong>rejected_patches</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of rejected patches.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>approval_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">approveAfterDays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days after the release date of each patch matched by the rule the patch is marked as approved in the patch baseline. Valid Range: 0 to 100.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">complianceLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Defines the compliance level for patches approved by this rule. Valid compliance levels include the following: <code class="docutils literal notranslate"><span class="pre">CRITICAL</span></code>, <code class="docutils literal notranslate"><span class="pre">HIGH</span></code>, <code class="docutils literal notranslate"><span class="pre">MEDIUM</span></code>, <code class="docutils literal notranslate"><span class="pre">LOW</span></code>, <code class="docutils literal notranslate"><span class="pre">INFORMATIONAL</span></code>, <code class="docutils literal notranslate"><span class="pre">UNSPECIFIED</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">UNSPECIFIED</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableNonSecurity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean enabling the application of non-security updates. The default value is ‘false’. Valid for Linux instances only.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">patchFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The patch filter group that defines the criteria for the rule. Up to 5 patch filters can be specified per approval rule using Key/Value pairs. Valid Keys are <code class="docutils literal notranslate"><span class="pre">PATCH_SET</span> <span class="pre">|</span> <span class="pre">PRODUCT</span> <span class="pre">|</span> <span class="pre">CLASSIFICATION</span> <span class="pre">|</span> <span class="pre">MSRC_SEVERITY</span> <span class="pre">|</span> <span class="pre">PATCH_ID</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>global_filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.ssm.PatchBaseline.approval_rules">
<code class="sig-name descname">approval_rules</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.PatchBaseline.approval_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of rules used to include patches in the baseline. up to 10 approval rules can be specified. Each approval_rule block requires the fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">approveAfterDays</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of days after the release date of each patch matched by the rule the patch is marked as approved in the patch baseline. Valid Range: 0 to 100.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">complianceLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Defines the compliance level for patches approved by this rule. Valid compliance levels include the following: <code class="docutils literal notranslate"><span class="pre">CRITICAL</span></code>, <code class="docutils literal notranslate"><span class="pre">HIGH</span></code>, <code class="docutils literal notranslate"><span class="pre">MEDIUM</span></code>, <code class="docutils literal notranslate"><span class="pre">LOW</span></code>, <code class="docutils literal notranslate"><span class="pre">INFORMATIONAL</span></code>, <code class="docutils literal notranslate"><span class="pre">UNSPECIFIED</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">UNSPECIFIED</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableNonSecurity</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean enabling the application of non-security updates. The default value is ‘false’. Valid for Linux instances only.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">patchFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The patch filter group that defines the criteria for the rule. Up to 5 patch filters can be specified per approval rule using Key/Value pairs. Valid Keys are <code class="docutils literal notranslate"><span class="pre">PATCH_SET</span> <span class="pre">|</span> <span class="pre">PRODUCT</span> <span class="pre">|</span> <span class="pre">CLASSIFICATION</span> <span class="pre">|</span> <span class="pre">MSRC_SEVERITY</span> <span class="pre">|</span> <span class="pre">PATCH_ID</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.PatchBaseline.approved_patches">
<code class="sig-name descname">approved_patches</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.PatchBaseline.approved_patches" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of explicitly approved patches for the baseline.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.PatchBaseline.approved_patches_compliance_level">
<code class="sig-name descname">approved_patches_compliance_level</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.PatchBaseline.approved_patches_compliance_level" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the compliance level for approved patches. This means that if an approved patch is reported as missing, this is the severity of the compliance violation. Valid compliance levels include the following: <code class="docutils literal notranslate"><span class="pre">CRITICAL</span></code>, <code class="docutils literal notranslate"><span class="pre">HIGH</span></code>, <code class="docutils literal notranslate"><span class="pre">MEDIUM</span></code>, <code class="docutils literal notranslate"><span class="pre">LOW</span></code>, <code class="docutils literal notranslate"><span class="pre">INFORMATIONAL</span></code>, <code class="docutils literal notranslate"><span class="pre">UNSPECIFIED</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">UNSPECIFIED</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.PatchBaseline.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.PatchBaseline.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the patch baseline.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.PatchBaseline.global_filters">
<code class="sig-name descname">global_filters</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.PatchBaseline.global_filters" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of global filters used to exclude patches from the baseline. Up to 4 global filters can be specified using Key/Value pairs. Valid Keys are <code class="docutils literal notranslate"><span class="pre">PRODUCT</span> <span class="pre">|</span> <span class="pre">CLASSIFICATION</span> <span class="pre">|</span> <span class="pre">MSRC_SEVERITY</span> <span class="pre">|</span> <span class="pre">PATCH_ID</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.PatchBaseline.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.PatchBaseline.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the patch baseline.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.PatchBaseline.operating_system">
<code class="sig-name descname">operating_system</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.PatchBaseline.operating_system" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the operating system the patch baseline applies to. Supported operating systems include <code class="docutils literal notranslate"><span class="pre">WINDOWS</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_LINUX</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_LINUX_2</span></code>, <code class="docutils literal notranslate"><span class="pre">SUSE</span></code>, <code class="docutils literal notranslate"><span class="pre">UBUNTU</span></code>, <code class="docutils literal notranslate"><span class="pre">CENTOS</span></code>, and <code class="docutils literal notranslate"><span class="pre">REDHAT_ENTERPRISE_LINUX</span></code>. The Default value is <code class="docutils literal notranslate"><span class="pre">WINDOWS</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.PatchBaseline.rejected_patches">
<code class="sig-name descname">rejected_patches</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.PatchBaseline.rejected_patches" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of rejected patches.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.PatchBaseline.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.PatchBaseline.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ssm.PatchBaseline.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">approval_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">approved_patches</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">approved_patches_compliance_level</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">global_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">operating_system</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rejected_patches</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.PatchBaseline.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PatchBaseline resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>approval_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of rules used to include patches in the baseline. up to 10 approval rules can be specified. Each approval_rule block requires the fields documented below.</p></li>
<li><p><strong>approved_patches</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of explicitly approved patches for the baseline.</p></li>
<li><p><strong>approved_patches_compliance_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the compliance level for approved patches. This means that if an approved patch is reported as missing, this is the severity of the compliance violation. Valid compliance levels include the following: <code class="docutils literal notranslate"><span class="pre">CRITICAL</span></code>, <code class="docutils literal notranslate"><span class="pre">HIGH</span></code>, <code class="docutils literal notranslate"><span class="pre">MEDIUM</span></code>, <code class="docutils literal notranslate"><span class="pre">LOW</span></code>, <code class="docutils literal notranslate"><span class="pre">INFORMATIONAL</span></code>, <code class="docutils literal notranslate"><span class="pre">UNSPECIFIED</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">UNSPECIFIED</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the patch baseline.</p></li>
<li><p><strong>global_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of global filters used to exclude patches from the baseline. Up to 4 global filters can be specified using Key/Value pairs. Valid Keys are <code class="docutils literal notranslate"><span class="pre">PRODUCT</span> <span class="pre">|</span> <span class="pre">CLASSIFICATION</span> <span class="pre">|</span> <span class="pre">MSRC_SEVERITY</span> <span class="pre">|</span> <span class="pre">PATCH_ID</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the patch baseline.</p></li>
<li><p><strong>operating_system</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the operating system the patch baseline applies to. Supported operating systems include <code class="docutils literal notranslate"><span class="pre">WINDOWS</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_LINUX</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_LINUX_2</span></code>, <code class="docutils literal notranslate"><span class="pre">SUSE</span></code>, <code class="docutils literal notranslate"><span class="pre">UBUNTU</span></code>, <code class="docutils literal notranslate"><span class="pre">CENTOS</span></code>, and <code class="docutils literal notranslate"><span class="pre">REDHAT_ENTERPRISE_LINUX</span></code>. The Default value is <code class="docutils literal notranslate"><span class="pre">WINDOWS</span></code>.</p></li>
<li><p><strong>rejected_patches</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of rejected patches.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>approval_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">approveAfterDays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days after the release date of each patch matched by the rule the patch is marked as approved in the patch baseline. Valid Range: 0 to 100.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">complianceLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Defines the compliance level for patches approved by this rule. Valid compliance levels include the following: <code class="docutils literal notranslate"><span class="pre">CRITICAL</span></code>, <code class="docutils literal notranslate"><span class="pre">HIGH</span></code>, <code class="docutils literal notranslate"><span class="pre">MEDIUM</span></code>, <code class="docutils literal notranslate"><span class="pre">LOW</span></code>, <code class="docutils literal notranslate"><span class="pre">INFORMATIONAL</span></code>, <code class="docutils literal notranslate"><span class="pre">UNSPECIFIED</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">UNSPECIFIED</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableNonSecurity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean enabling the application of non-security updates. The default value is ‘false’. Valid for Linux instances only.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">patchFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The patch filter group that defines the criteria for the rule. Up to 5 patch filters can be specified per approval rule using Key/Value pairs. Valid Keys are <code class="docutils literal notranslate"><span class="pre">PATCH_SET</span> <span class="pre">|</span> <span class="pre">PRODUCT</span> <span class="pre">|</span> <span class="pre">CLASSIFICATION</span> <span class="pre">|</span> <span class="pre">MSRC_SEVERITY</span> <span class="pre">|</span> <span class="pre">PATCH_ID</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>global_filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ssm.PatchBaseline.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.PatchBaseline.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ssm.PatchBaseline.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.PatchBaseline.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ssm.PatchGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ssm.</code><code class="sig-name descname">PatchGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">baseline_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">patch_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.PatchGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SSM Patch Group resource</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">production</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ssm</span><span class="o">.</span><span class="n">PatchBaseline</span><span class="p">(</span><span class="s2">&quot;production&quot;</span><span class="p">,</span> <span class="n">approved_patches</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;KB123456&quot;</span><span class="p">])</span>
<span class="n">patchgroup</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ssm</span><span class="o">.</span><span class="n">PatchGroup</span><span class="p">(</span><span class="s2">&quot;patchgroup&quot;</span><span class="p">,</span>
    <span class="n">baseline_id</span><span class="o">=</span><span class="n">production</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">patch_group</span><span class="o">=</span><span class="s2">&quot;patch-group-name&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>baseline_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the patch baseline to register the patch group with.</p></li>
<li><p><strong>patch_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the patch group that should be registered with the patch baseline.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.ssm.PatchGroup.baseline_id">
<code class="sig-name descname">baseline_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.PatchGroup.baseline_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the patch baseline to register the patch group with.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.PatchGroup.patch_group">
<code class="sig-name descname">patch_group</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.PatchGroup.patch_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the patch group that should be registered with the patch baseline.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ssm.PatchGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">baseline_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">patch_group</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.PatchGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PatchGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>baseline_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the patch baseline to register the patch group with.</p></li>
<li><p><strong>patch_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the patch group that should be registered with the patch baseline.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ssm.PatchGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.PatchGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ssm.PatchGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.PatchGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ssm.ResourceDataSync">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ssm.</code><code class="sig-name descname">ResourceDataSync</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">s3_destination</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.ResourceDataSync" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a SSM resource data sync.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">hoge_bucket</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">s3</span><span class="o">.</span><span class="n">Bucket</span><span class="p">(</span><span class="s2">&quot;hogeBucket&quot;</span><span class="p">,</span> <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-east-1&quot;</span><span class="p">)</span>
<span class="n">hoge_bucket_policy</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">s3</span><span class="o">.</span><span class="n">BucketPolicy</span><span class="p">(</span><span class="s2">&quot;hogeBucketPolicy&quot;</span><span class="p">,</span>
    <span class="n">bucket</span><span class="o">=</span><span class="n">hoge_bucket</span><span class="o">.</span><span class="n">bucket</span><span class="p">,</span>
    <span class="n">policy</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">    &quot;Version&quot;: &quot;2012-10-17&quot;,</span>
<span class="s2">    &quot;Statement&quot;: [</span>
<span class="s2">        {</span>
<span class="s2">            &quot;Sid&quot;: &quot;SSMBucketPermissionsCheck&quot;,</span>
<span class="s2">            &quot;Effect&quot;: &quot;Allow&quot;,</span>
<span class="s2">            &quot;Principal&quot;: {</span>
<span class="s2">                &quot;Service&quot;: &quot;ssm.amazonaws.com&quot;</span>
<span class="s2">            },</span>
<span class="s2">            &quot;Action&quot;: &quot;s3:GetBucketAcl&quot;,</span>
<span class="s2">            &quot;Resource&quot;: &quot;arn:aws:s3:::tf-test-bucket-1234&quot;</span>
<span class="s2">        },</span>
<span class="s2">        {</span>
<span class="s2">            &quot;Sid&quot;: &quot; SSMBucketDelivery&quot;,</span>
<span class="s2">            &quot;Effect&quot;: &quot;Allow&quot;,</span>
<span class="s2">            &quot;Principal&quot;: {</span>
<span class="s2">                &quot;Service&quot;: &quot;ssm.amazonaws.com&quot;</span>
<span class="s2">            },</span>
<span class="s2">            &quot;Action&quot;: &quot;s3:PutObject&quot;,</span>
<span class="s2">            &quot;Resource&quot;: [&quot;arn:aws:s3:::tf-test-bucket-1234/*&quot;],</span>
<span class="s2">            &quot;Condition&quot;: {</span>
<span class="s2">                &quot;StringEquals&quot;: {</span>
<span class="s2">                    &quot;s3:x-amz-acl&quot;: &quot;bucket-owner-full-control&quot;</span>
<span class="s2">                }</span>
<span class="s2">            }</span>
<span class="s2">        }</span>
<span class="s2">    ]</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
<span class="n">foo</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ssm</span><span class="o">.</span><span class="n">ResourceDataSync</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span> <span class="n">s3_destination</span><span class="o">=</span><span class="p">{</span>
    <span class="s2">&quot;bucketName&quot;</span><span class="p">:</span> <span class="n">hoge_bucket</span><span class="o">.</span><span class="n">bucket</span><span class="p">,</span>
    <span class="s2">&quot;region&quot;</span><span class="p">:</span> <span class="n">hoge_bucket</span><span class="o">.</span><span class="n">region</span><span class="p">,</span>
<span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name for the configuration.</p></li>
<li><p><strong>s3_destination</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Amazon S3 configuration details for the sync.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>s3_destination</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of S3 bucket where the aggregated data is stored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ARN of an encryption key for a destination in Amazon S3.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Prefix for the bucket.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Region with the bucket targeted by the Resource Data Sync.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">syncFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A supported sync format. Only JsonSerDe is currently supported. Defaults to JsonSerDe.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.ssm.ResourceDataSync.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.ResourceDataSync.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name for the configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ssm.ResourceDataSync.s3_destination">
<code class="sig-name descname">s3_destination</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.ResourceDataSync.s3_destination" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon S3 configuration details for the sync.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of S3 bucket where the aggregated data is stored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ARN of an encryption key for a destination in Amazon S3.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Prefix for the bucket.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Region with the bucket targeted by the Resource Data Sync.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">syncFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A supported sync format. Only JsonSerDe is currently supported. Defaults to JsonSerDe.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ssm.ResourceDataSync.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">s3_destination</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.ResourceDataSync.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ResourceDataSync resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name for the configuration.</p></li>
<li><p><strong>s3_destination</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Amazon S3 configuration details for the sync.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>s3_destination</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of S3 bucket where the aggregated data is stored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ARN of an encryption key for a destination in Amazon S3.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Prefix for the bucket.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Region with the bucket targeted by the Resource Data Sync.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">syncFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A supported sync format. Only JsonSerDe is currently supported. Defaults to JsonSerDe.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ssm.ResourceDataSync.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.ResourceDataSync.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ssm.ResourceDataSync.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.ResourceDataSync.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ssm.get_document">
<code class="sig-prename descclassname">pulumi_aws.ssm.</code><code class="sig-name descname">get_document</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">document_format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">document_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.get_document" title="Permalink to this definition">¶</a></dt>
<dd><p>Gets the contents of the specified Systems Manager document.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ssm</span><span class="o">.</span><span class="n">get_document</span><span class="p">(</span><span class="n">document_format</span><span class="o">=</span><span class="s2">&quot;YAML&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;AWS-GatherSoftwareInventory&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;content&quot;</span><span class="p">,</span> <span class="n">foo</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>document_format</strong> (<em>str</em>) – Returns the document in the specified format. The document format can be either JSON or YAML. JSON is the default format.</p></li>
<li><p><strong>document_version</strong> (<em>str</em>) – The document version for which you want information.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the Systems Manager document.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.ssm.get_parameter">
<code class="sig-prename descclassname">pulumi_aws.ssm.</code><code class="sig-name descname">get_parameter</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_decryption</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.get_parameter" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SSM Parameter data source.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ssm</span><span class="o">.</span><span class="n">get_parameter</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;foo&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the parameter.</p></li>
<li><p><strong>with_decryption</strong> (<em>bool</em>) – Whether to return decrypted <code class="docutils literal notranslate"><span class="pre">SecureString</span></code> value. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.ssm.get_patch_baseline">
<code class="sig-prename descclassname">pulumi_aws.ssm.</code><code class="sig-name descname">get_patch_baseline</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">default_baseline</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">operating_system</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.get_patch_baseline" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SSM Patch Baseline data source. Useful if you wish to reuse the default baselines provided.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">centos</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ssm</span><span class="o">.</span><span class="n">get_patch_baseline</span><span class="p">(</span><span class="n">name_prefix</span><span class="o">=</span><span class="s2">&quot;AWS-&quot;</span><span class="p">,</span>
    <span class="n">operating_system</span><span class="o">=</span><span class="s2">&quot;CENTOS&quot;</span><span class="p">,</span>
    <span class="n">owner</span><span class="o">=</span><span class="s2">&quot;AWS&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>default_baseline</strong> (<em>bool</em>) – Filters the results against the baselines default_baseline field.</p></li>
<li><p><strong>name_prefix</strong> (<em>str</em>) – Filter results by the baseline name prefix.</p></li>
<li><p><strong>operating_system</strong> (<em>str</em>) – The specified OS for the baseline.</p></li>
<li><p><strong>owner</strong> (<em>str</em>) – The owner of the baseline. Valid values: <code class="docutils literal notranslate"><span class="pre">All</span></code>, <code class="docutils literal notranslate"><span class="pre">AWS</span></code>, <code class="docutils literal notranslate"><span class="pre">Self</span></code> (the current account).</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
