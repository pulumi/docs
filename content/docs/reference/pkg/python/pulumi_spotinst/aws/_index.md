---
title: Module aws
title_tag: Module aws | Package pulumi_spotinst | Python SDK
linktitle: aws
notitle: true
---

<div class="section" id="aws">
<h1>aws<a class="headerlink" href="#aws" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-spotinst/issues">pulumi/pulumi-spotinst repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst/issues">terraform-providers/terraform-provider-spotinst repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_spotinst.aws"></span><dl class="py class">
<dt id="pulumi_spotinst.aws.Beanstalk">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.aws.</code><code class="sig-name descname">Beanstalk</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">beanstalk_environment_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">beanstalk_environment_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deployment_preferences</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">desired_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types_spots</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">managed_actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_tasks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.aws.Beanstalk" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Spotinst AWS group resource using Elastic Beanstalk.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_spotinst</span> <span class="k">as</span> <span class="nn">spotinst</span>

<span class="n">elastigoup_aws_beanstalk</span> <span class="o">=</span> <span class="n">spotinst</span><span class="o">.</span><span class="n">aws</span><span class="o">.</span><span class="n">Beanstalk</span><span class="p">(</span><span class="s2">&quot;elastigoup-aws-beanstalk&quot;</span><span class="p">,</span>
    <span class="n">beanstalk_environment_id</span><span class="o">=</span><span class="s2">&quot;e-example&quot;</span><span class="p">,</span>
    <span class="n">beanstalk_environment_name</span><span class="o">=</span><span class="s2">&quot;example-env&quot;</span><span class="p">,</span>
    <span class="n">deployment_preferences</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;automaticRoll&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;batchSizePercentage&quot;</span><span class="p">:</span> <span class="mi">100</span><span class="p">,</span>
        <span class="s2">&quot;gracePeriod&quot;</span><span class="p">:</span> <span class="mi">90</span><span class="p">,</span>
        <span class="s2">&quot;strategy&quot;</span><span class="p">:</span> <span class="p">[{</span>
            <span class="s2">&quot;action&quot;</span><span class="p">:</span> <span class="s2">&quot;REPLACE_SERVER&quot;</span><span class="p">,</span>
            <span class="s2">&quot;shouldDrainInstances&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="p">}],</span>
    <span class="p">},</span>
    <span class="n">desired_capacity</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="n">instance_types_spots</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;t2.micro&quot;</span><span class="p">,</span>
        <span class="s2">&quot;t2.medium&quot;</span><span class="p">,</span>
        <span class="s2">&quot;t2.large&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">managed_actions</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;platformUpdate&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;performAt&quot;</span><span class="p">:</span> <span class="s2">&quot;timeWindow&quot;</span><span class="p">,</span>
            <span class="s2">&quot;timeWindow&quot;</span><span class="p">:</span> <span class="s2">&quot;Mon:23:50-Tue:00:20&quot;</span><span class="p">,</span>
            <span class="s2">&quot;updateLevel&quot;</span><span class="p">:</span> <span class="s2">&quot;minorAndPatch&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">},</span>
    <span class="n">max_size</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">min_size</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="n">product</span><span class="o">=</span><span class="s2">&quot;Linux/UNIX&quot;</span><span class="p">,</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-west-2&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Each <code class="docutils literal notranslate"><span class="pre">scheduled_task</span></code> supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">task_type</span></code> - (Required) The task type to run. Supported task types are: <code class="docutils literal notranslate"><span class="pre">&quot;scale&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;backup_ami&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;roll&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;scaleUp&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;percentageScaleUp&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;scaleDown&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;percentageScaleDown&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;statefulUpdateCapacity&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cron_expression</span></code> - (Optional; Required if not using <code class="docutils literal notranslate"><span class="pre">frequency</span></code>) A valid cron expression. The cron is running in UTC time zone and is in <a class="reference external" href="https://en.wikipedia.org/wiki/Cron">Unix cron format</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start_time</span></code> - (Optional; Format: ISO 8601) Set a start time for one time tasks.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frequency</span></code> - (Optional; Required if not using <code class="docutils literal notranslate"><span class="pre">cron_expression</span></code>) The recurrence frequency to run this task. Supported values are <code class="docutils literal notranslate"><span class="pre">&quot;hourly&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;daily&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;weekly&quot;</span></code> and <code class="docutils literal notranslate"><span class="pre">&quot;continuous&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scale_target_capacity</span></code> - (Optional) The desired number of instances the group should have.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scale_min_capacity</span></code> - (Optional) The minimum number of instances the group should have.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scale_max_capacity</span></code> - (Optional) The maximum number of instances the group should have.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">is_enabled</span></code> - (Optional, Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>) Setting the task to being enabled or disabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_capacity</span></code> - (Optional; Only valid for statefulUpdateCapacity) The desired number of instances the group should have.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_capacity</span></code> - (Optional; Only valid for statefulUpdateCapacity) The minimum number of instances the group should have.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_capacity</span></code> - (Optional; Only valid for statefulUpdateCapacity) The maximum number of instances the group should have.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">batch_size_percentage</span></code> - (Optional; Required when the <code class="docutils literal notranslate"><span class="pre">task_type</span></code> is <code class="docutils literal notranslate"><span class="pre">&quot;roll&quot;</span></code>.) The percentage size of each batch in the scheduled deployment roll.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grace_period</span></code> - (Optional) The period of time (seconds) to wait before checking a batch’s health after it’s deployment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> - (Optional; Min 1) The number of instances to add or remove.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment_percentage</span></code> - (Optional; Min 1) The percentage of instances to add or remove.</p></li>
</ul>
<p>Usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>beanstalk_environment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of an existing Beanstalk environment.</p></li>
<li><p><strong>beanstalk_environment_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of an existing Beanstalk environment.</p></li>
<li><p><strong>deployment_preferences</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Preferences when performing a roll</p></li>
<li><p><strong>desired_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The desired number of instances the group should have at any time.</p></li>
<li><p><strong>instance_types_spots</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more instance types. To maximize the availability of Spot instances, select as many instance types as possible.</p></li>
<li><p><strong>managed_actions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Managed Actions parameters</p></li>
<li><p><strong>max_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of instances the group should have at any time.</p></li>
<li><p><strong>min_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum number of instances the group should have at any time.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The group name.</p></li>
<li><p><strong>product</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operation system type. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;Linux/UNIX&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SUSE</span> <span class="pre">Linux&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Windows&quot;</span></code>.
For EC2 Classic instances:  <code class="docutils literal notranslate"><span class="pre">&quot;Linux/UNIX</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SUSE</span> <span class="pre">Linux</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Windows</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS region your group will be created in. Cannot be changed after the group has been created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>deployment_preferences</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automaticRoll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should roll perform automatically</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">batchSizePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Percent size of each batch</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grace_period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Amount of time to wait between batches</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">strategies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Strategy parameters</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Action to take</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldDrainInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Bool value if to wait to drain instance</p></li>
</ul>
</li>
</ul>
<p>The <strong>managed_actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">platformUpdate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Platform Update parameters</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">performAt</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Actions to perform (options: timeWindow, never)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeWindow</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Time Window for when action occurs ex. Mon:23:50-Tue:00:20</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">updateLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - - Level to update</p></li>
</ul>
</li>
</ul>
<p>The <strong>scheduled_tasks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustmentPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">batchSizePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Percent size of each batch</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cronExpression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frequency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grace_period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amount of time to wait between batches</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleMaxCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleMinCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Beanstalk.beanstalk_environment_id">
<code class="sig-name descname">beanstalk_environment_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Beanstalk.beanstalk_environment_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of an existing Beanstalk environment.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Beanstalk.beanstalk_environment_name">
<code class="sig-name descname">beanstalk_environment_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Beanstalk.beanstalk_environment_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of an existing Beanstalk environment.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Beanstalk.deployment_preferences">
<code class="sig-name descname">deployment_preferences</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Beanstalk.deployment_preferences" title="Permalink to this definition">¶</a></dt>
<dd><p>Preferences when performing a roll</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automaticRoll</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should roll perform automatically</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">batchSizePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Percent size of each batch</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grace_period</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Amount of time to wait between batches</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">strategies</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Strategy parameters</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Action to take</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldDrainInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Bool value if to wait to drain instance</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Beanstalk.desired_capacity">
<code class="sig-name descname">desired_capacity</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Beanstalk.desired_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired number of instances the group should have at any time.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Beanstalk.instance_types_spots">
<code class="sig-name descname">instance_types_spots</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Beanstalk.instance_types_spots" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more instance types. To maximize the availability of Spot instances, select as many instance types as possible.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Beanstalk.managed_actions">
<code class="sig-name descname">managed_actions</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Beanstalk.managed_actions" title="Permalink to this definition">¶</a></dt>
<dd><p>Managed Actions parameters</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">platformUpdate</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Platform Update parameters</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">performAt</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Actions to perform (options: timeWindow, never)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeWindow</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Time Window for when action occurs ex. Mon:23:50-Tue:00:20</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">updateLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - - Level to update</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Beanstalk.max_size">
<code class="sig-name descname">max_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Beanstalk.max_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of instances the group should have at any time.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Beanstalk.min_size">
<code class="sig-name descname">min_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Beanstalk.min_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum number of instances the group should have at any time.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Beanstalk.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Beanstalk.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The group name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Beanstalk.product">
<code class="sig-name descname">product</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Beanstalk.product" title="Permalink to this definition">¶</a></dt>
<dd><p>Operation system type. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;Linux/UNIX&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SUSE</span> <span class="pre">Linux&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Windows&quot;</span></code>.
For EC2 Classic instances:  <code class="docutils literal notranslate"><span class="pre">&quot;Linux/UNIX</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SUSE</span> <span class="pre">Linux</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Windows</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Beanstalk.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Beanstalk.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS region your group will be created in. Cannot be changed after the group has been created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.aws.Beanstalk.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">beanstalk_environment_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">beanstalk_environment_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deployment_preferences</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">desired_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types_spots</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">managed_actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_tasks</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.aws.Beanstalk.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Beanstalk resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>beanstalk_environment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of an existing Beanstalk environment.</p></li>
<li><p><strong>beanstalk_environment_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of an existing Beanstalk environment.</p></li>
<li><p><strong>deployment_preferences</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Preferences when performing a roll</p></li>
<li><p><strong>desired_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The desired number of instances the group should have at any time.</p></li>
<li><p><strong>instance_types_spots</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more instance types. To maximize the availability of Spot instances, select as many instance types as possible.</p></li>
<li><p><strong>managed_actions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Managed Actions parameters</p></li>
<li><p><strong>max_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of instances the group should have at any time.</p></li>
<li><p><strong>min_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum number of instances the group should have at any time.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The group name.</p></li>
<li><p><strong>product</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operation system type. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;Linux/UNIX&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SUSE</span> <span class="pre">Linux&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Windows&quot;</span></code>.
For EC2 Classic instances:  <code class="docutils literal notranslate"><span class="pre">&quot;Linux/UNIX</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SUSE</span> <span class="pre">Linux</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Windows</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS region your group will be created in. Cannot be changed after the group has been created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>deployment_preferences</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automaticRoll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should roll perform automatically</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">batchSizePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Percent size of each batch</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grace_period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Amount of time to wait between batches</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">strategies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Strategy parameters</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Action to take</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldDrainInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Bool value if to wait to drain instance</p></li>
</ul>
</li>
</ul>
<p>The <strong>managed_actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">platformUpdate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Platform Update parameters</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">performAt</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Actions to perform (options: timeWindow, never)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeWindow</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Time Window for when action occurs ex. Mon:23:50-Tue:00:20</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">updateLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - - Level to update</p></li>
</ul>
</li>
</ul>
<p>The <strong>scheduled_tasks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustmentPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">batchSizePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Percent size of each batch</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cronExpression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frequency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grace_period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amount of time to wait between batches</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleMaxCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleMinCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.aws.Beanstalk.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.aws.Beanstalk.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.aws.Beanstalk.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.aws.Beanstalk.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.aws.Elastigroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.aws.</code><code class="sig-name descname">Elastigroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">block_devices_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">capacity_unit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cpu_credits</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">desired_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">draining_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_block_devices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_optimized</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_load_balancers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_monitoring</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ephemeral_block_devices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fallback_to_ondemand</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_grace_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_unhealthy_duration_before_replacement</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iam_instance_profile</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types_ondemand</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types_preferred_spots</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types_spots</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types_weights</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_beanstalk</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_codedeploy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_docker_swarm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_ecs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_gitlab</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_kubernetes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_mesosphere</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_multai_runtime</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_nomad</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_rancher</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_route53</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lifetime_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">multai_target_sets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_interfaces</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ondemand_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">orientation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">persist_block_devices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">persist_private_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">persist_root_device</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">placement_tenancy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preferred_availability_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">revert_to_spot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_down_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_strategies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_target_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_up_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_tasks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shutdown_script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">signals</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_percentage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stateful_deallocation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_group_arns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">utilize_reserved_instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_for_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_for_capacity_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Elastigroup resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] availability_zones: List of Strings of availability zones. When this parameter is set, <code class="docutils literal notranslate"><span class="pre">subnet_ids</span></code> should be left unused.</p>
<blockquote>
<div><p>Note: <code class="docutils literal notranslate"><span class="pre">availability_zones</span></code> naming syntax follows the convention <code class="docutils literal notranslate"><span class="pre">availability-zone:subnet:placement-group-name</span></code>. For example, to set an AZ in <code class="docutils literal notranslate"><span class="pre">us-east-1</span></code> with subnet <code class="docutils literal notranslate"><span class="pre">subnet-123456</span></code> and placement group <code class="docutils literal notranslate"><span class="pre">ClusterI03</span></code>, you would set:
<code class="docutils literal notranslate"><span class="pre">availability_zones</span> <span class="pre">=</span> <span class="pre">[&quot;us-east-1a:subnet-123456:ClusterI03&quot;]</span></code></p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>capacity_unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The capacity unit to launch instances by. If not specified, when choosing the weight unit, each instance will weight as the number of its vCPUs.</p></li>
<li><p><strong>cpu_credits</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Controls how T3 instances are launched. Valid values: <code class="docutils literal notranslate"><span class="pre">standard</span></code>, <code class="docutils literal notranslate"><span class="pre">unlimited</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The group description.</p></li>
<li><p><strong>desired_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The desired number of instances the group should have at any time.</p></li>
<li><p><strong>draining_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time in seconds, the instance is allowed to run while detached from the ELB. This is to allow the instance time to be drained from incoming TCP connections before terminating it, during a scale down operation.</p></li>
<li><p><strong>ebs_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable high bandwidth connectivity between instances and AWS’s Elastic Block Store (EBS). For instance types that are EBS-optimized by default this parameter will be ignored.</p></li>
<li><p><strong>elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of <a class="reference external" href="http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html">AWS Elastic IP</a> allocation IDs to associate to the group instances.</p></li>
<li><p><strong>enable_monitoring</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether monitoring is enabled for the instance.</p></li>
<li><p><strong>fallback_to_ondemand</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – In a case of no Spot instances available, Elastigroup will launch on-demand instances instead.</p></li>
<li><p><strong>health_check_grace_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time, in seconds, after the instance has launched to starts and check its health.</p></li>
<li><p><strong>health_check_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service that will perform health checks for the instance. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;ELB&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;HCS&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;TARGET_GROUP&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;MLB&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;EC2&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;MULTAI_TARGET_SET&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;MLB_RUNTIME&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;K8S_NODE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;NOMAD_NODE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ECS_CLUSTER_INSTANCE&quot;</span></code>.</p></li>
<li><p><strong>health_check_unhealthy_duration_before_replacement</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time, in seconds, that we will wait before replacing an instance that is running and became unhealthy (this is only applicable for instances that were once healthy).</p></li>
<li><p><strong>iam_instance_profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN or name of an IAM instance profile to associate with launched instances.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the AMI used to launch the instance.</p></li>
<li><p><strong>instance_types_ondemand</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of instance determines your instance’s CPU capacity, memory and storage (e.g., m1.small, c1.xlarge).</p></li>
<li><p><strong>instance_types_preferred_spots</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Prioritize a subset of spot instance types. Must be a subset of the selected spot instance types.</p></li>
<li><p><strong>instance_types_spots</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more instance types.</p></li>
<li><p><strong>instance_types_weights</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of weights per instance type for weighted groups. Each object in the list should have the following attributes:</p></li>
<li><p><strong>key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key name that should be used for the instance.</p></li>
<li><p><strong>max_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of instances the group should have at any time.</p></li>
<li><p><strong>min_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum number of instances the group should have at any time.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The group name.</p></li>
<li><p><strong>ondemand_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of on demand instances to launch in the group. All other instances will be spot instances. When this parameter is set the <code class="docutils literal notranslate"><span class="pre">spot_percentage</span></code> parameter is being ignored.</p></li>
<li><p><strong>orientation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Select a prediction strategy. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;balanced&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;costOriented&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;equalAzDistribution&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;availabilityOriented&quot;</span></code>.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>placement_tenancy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enable dedicated tenancy. Note: There is a flat hourly fee for each region in which dedicated tenancy is used.</p></li>
<li><p><strong>preferred_availability_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The AZs to prioritize when launching Spot instances. If no markets are available in the Preferred AZs, Spot instances are launched in the non-preferred AZs. 
Note: Must be a sublist of <code class="docutils literal notranslate"><span class="pre">availability_zones</span></code> and <code class="docutils literal notranslate"><span class="pre">orientation</span></code> value must not be <code class="docutils literal notranslate"><span class="pre">&quot;equalAzDistribution&quot;</span></code>.</p></li>
<li><p><strong>product</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operation system type. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;Linux/UNIX&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SUSE</span> <span class="pre">Linux&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Windows&quot;</span></code>. 
For EC2 Classic instances:  <code class="docutils literal notranslate"><span class="pre">&quot;Linux/UNIX</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SUSE</span> <span class="pre">Linux</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Windows</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS region your group will be created in.
Note: This parameter is required if you specify subnets (through subnet_ids). This parameter is optional if you specify Availability Zones (through availability_zones).</p></li>
<li><p><strong>revert_to_spot</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Hold settings for strategy correction – replacing On-Demand for Spot instances. Supported Values: <code class="docutils literal notranslate"><span class="pre">&quot;never&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;always&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;timeWindow&quot;</span></code></p></li>
<li><p><strong>scaling_strategies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set termination policy.</p></li>
<li><p><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of associated security group IDS.</p></li>
<li><p><strong>shutdown_script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Base64-encoded shutdown script that executes prior to instance termination, for more information please see: <a class="reference external" href="https://api.spotinst.com/integration-docs/elastigroup/concepts/compute-concepts/shutdown-scripts/">Shutdown Script</a></p></li>
<li><p><strong>spot_percentage</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The percentage of Spot instances that would spin up from the <code class="docutils literal notranslate"><span class="pre">desired_capacity</span></code> number.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Strings of subnet identifiers.
Note: When this parameter is set, <code class="docutils literal notranslate"><span class="pre">availability_zones</span></code> should be left unused.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A key/value mapping of tags to assign to the resource.</p></li>
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user data to provide when launching the instance.</p></li>
<li><p><strong>utilize_reserved_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – In a case of any available reserved instances, Elastigroup will utilize them first before purchasing Spot instances.</p></li>
<li><p><strong>wait_for_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum number of instances in a ‘HEALTHY’ status that is required before continuing. This is ignored when updating with blue/green deployment. Cannot exceed <code class="docutils literal notranslate"><span class="pre">desired_capacity</span></code>.</p></li>
<li><p><strong>wait_for_capacity_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time (seconds) to wait for instances to report a ‘HEALTHY’ status. Useful for plans with multiple dependencies that take some time to initialize. Leave undefined or set to <code class="docutils literal notranslate"><span class="pre">0</span></code> to indicate no wait. This is ignored when updating with blue/green deployment.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_block_devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deleteOnTermination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deviceName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeyId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshotId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>ephemeral_block_devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deviceName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>instance_types_weights</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instanceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of instance type (String).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Weight per instance type (Integer).</p></li>
</ul>
<p>The <strong>integration_beanstalk</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deployment_preferences</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">automaticRoll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">batchSizePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grace_period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">strategy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldDrainInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">environmentId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managed_actions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">platformUpdate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">performAt</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - In the event of a fallback to On-Demand instances, select the time period to revert back to Spot. Supported Arguments – always (default), timeWindow, never. For timeWindow or never to be valid the group must have availabilityOriented OR persistence defined.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeWindow</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">updateLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<p>The <strong>integration_codedeploy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cleanupOnFailure</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deploymentGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">applicationName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deploymentGroupName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">terminateInstanceOnFailure</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>integration_docker_swarm</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleCooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleDown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleHeadroom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numOfUnits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleIsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterHost</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>integration_ecs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleAttributes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleCooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleDown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxScaleDownPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleHeadroom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numOfUnits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleIsAutoConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleIsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleScaleDownNonServiceTasks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>integration_gitlab</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">runner</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>integration_kubernetes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">apiServer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleCooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleDown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleHeadroom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numOfUnits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleIsAutoConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleIsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleLabels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterIdentifier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">integrationMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>integration_mesosphere</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">apiServer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>integration_multai_runtime</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deployment_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>integration_nomad</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aclToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleConstraints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleCooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleDown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleHeadroom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numOfUnits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleIsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterHost</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>integration_rancher</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterHost</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>integration_route53</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">domains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">hostedZoneId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordSets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The group name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">usePublicIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">spotinstAcctId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>multai_target_sets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">balancer_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_set_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>network_interfaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">associateIpv6Address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">associate_public_ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deleteOnTermination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The group description.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deviceIndex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkInterfaceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateIpAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secondaryPrivateIpAddressCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>revert_to_spot</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">performAt</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - In the event of a fallback to On-Demand instances, select the time period to revert back to Spot. Supported Arguments – always (default), timeWindow, never. For timeWindow or never to be valid the group must have availabilityOriented OR persistence defined.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeWindows</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specify a list of time windows for to execute revertToSpot strategy. Time window format: <code class="docutils literal notranslate"><span class="pre">ddd:hh:mm-ddd:hh:mm</span></code>. Example: <code class="docutils literal notranslate"><span class="pre">Mon:03:00-Wed:02:30</span></code></p></li>
</ul>
<p>The <strong>scaling_down_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The group name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scaling_strategies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">terminateAtEndOfBillingHour</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specify whether to terminate instances at the end of each billing hour.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">terminationPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - - Determines whether to terminate the newest instances when performing a scaling action. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;default&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;newestInstance&quot;</span></code>.</p></li>
</ul>
<p>The <strong>scaling_target_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The group name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">predictiveMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scaling_up_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The group name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scheduled_tasks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustmentPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">batchSizePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cronExpression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frequency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grace_period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleMaxCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleMinCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>signals</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The group name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>stateful_deallocation</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">shouldDeleteImages</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldDeleteNetworkInterfaces</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldDeleteSnapshots</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldDeleteVolumes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>update_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoApplyTags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rollConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">batchSizePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grace_period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">health_check_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service that will perform health checks for the instance. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;ELB&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;HCS&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;TARGET_GROUP&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;MLB&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;EC2&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;MULTAI_TARGET_SET&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;MLB_RUNTIME&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;K8S_NODE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;NOMAD_NODE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ECS_CLUSTER_INSTANCE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">strategy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">batchMinHealthyPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">onFailure</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">batchNum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">draining_timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time in seconds, the instance is allowed to run while detached from the ELB. This is to allow the instance time to be drained from incoming TCP connections before terminating it, during a scale down operation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldDecrementTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldHandleAllBatches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldDrainInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitForRollPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitForRollTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldResumeStateful</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldRoll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.availability_zones">
<code class="sig-name descname">availability_zones</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Strings of availability zones. When this parameter is set, <code class="docutils literal notranslate"><span class="pre">subnet_ids</span></code> should be left unused.
Note: <code class="docutils literal notranslate"><span class="pre">availability_zones</span></code> naming syntax follows the convention <code class="docutils literal notranslate"><span class="pre">availability-zone:subnet:placement-group-name</span></code>. For example, to set an AZ in <code class="docutils literal notranslate"><span class="pre">us-east-1</span></code> with subnet <code class="docutils literal notranslate"><span class="pre">subnet-123456</span></code> and placement group <code class="docutils literal notranslate"><span class="pre">ClusterI03</span></code>, you would set:
<code class="docutils literal notranslate"><span class="pre">availability_zones</span> <span class="pre">=</span> <span class="pre">[&quot;us-east-1a:subnet-123456:ClusterI03&quot;]</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.capacity_unit">
<code class="sig-name descname">capacity_unit</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.capacity_unit" title="Permalink to this definition">¶</a></dt>
<dd><p>The capacity unit to launch instances by. If not specified, when choosing the weight unit, each instance will weight as the number of its vCPUs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.cpu_credits">
<code class="sig-name descname">cpu_credits</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.cpu_credits" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls how T3 instances are launched. Valid values: <code class="docutils literal notranslate"><span class="pre">standard</span></code>, <code class="docutils literal notranslate"><span class="pre">unlimited</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The group description.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.desired_capacity">
<code class="sig-name descname">desired_capacity</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.desired_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired number of instances the group should have at any time.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.draining_timeout">
<code class="sig-name descname">draining_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.draining_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time in seconds, the instance is allowed to run while detached from the ELB. This is to allow the instance time to be drained from incoming TCP connections before terminating it, during a scale down operation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.ebs_optimized">
<code class="sig-name descname">ebs_optimized</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.ebs_optimized" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable high bandwidth connectivity between instances and AWS’s Elastic Block Store (EBS). For instance types that are EBS-optimized by default this parameter will be ignored.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.elastic_ips">
<code class="sig-name descname">elastic_ips</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.elastic_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of <a class="reference external" href="http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html">AWS Elastic IP</a> allocation IDs to associate to the group instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.enable_monitoring">
<code class="sig-name descname">enable_monitoring</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.enable_monitoring" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether monitoring is enabled for the instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.fallback_to_ondemand">
<code class="sig-name descname">fallback_to_ondemand</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.fallback_to_ondemand" title="Permalink to this definition">¶</a></dt>
<dd><p>In a case of no Spot instances available, Elastigroup will launch on-demand instances instead.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.health_check_grace_period">
<code class="sig-name descname">health_check_grace_period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.health_check_grace_period" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time, in seconds, after the instance has launched to starts and check its health.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.health_check_type">
<code class="sig-name descname">health_check_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.health_check_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The service that will perform health checks for the instance. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;ELB&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;HCS&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;TARGET_GROUP&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;MLB&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;EC2&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;MULTAI_TARGET_SET&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;MLB_RUNTIME&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;K8S_NODE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;NOMAD_NODE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ECS_CLUSTER_INSTANCE&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.health_check_unhealthy_duration_before_replacement">
<code class="sig-name descname">health_check_unhealthy_duration_before_replacement</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.health_check_unhealthy_duration_before_replacement" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time, in seconds, that we will wait before replacing an instance that is running and became unhealthy (this is only applicable for instances that were once healthy).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.iam_instance_profile">
<code class="sig-name descname">iam_instance_profile</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.iam_instance_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN or name of an IAM instance profile to associate with launched instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.image_id">
<code class="sig-name descname">image_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AMI used to launch the instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.instance_types_ondemand">
<code class="sig-name descname">instance_types_ondemand</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.instance_types_ondemand" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of instance determines your instance’s CPU capacity, memory and storage (e.g., m1.small, c1.xlarge).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.instance_types_preferred_spots">
<code class="sig-name descname">instance_types_preferred_spots</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.instance_types_preferred_spots" title="Permalink to this definition">¶</a></dt>
<dd><p>Prioritize a subset of spot instance types. Must be a subset of the selected spot instance types.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.instance_types_spots">
<code class="sig-name descname">instance_types_spots</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.instance_types_spots" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more instance types.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.instance_types_weights">
<code class="sig-name descname">instance_types_weights</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.instance_types_weights" title="Permalink to this definition">¶</a></dt>
<dd><p>List of weights per instance type for weighted groups. Each object in the list should have the following attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instanceType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of instance type (String).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Weight per instance type (Integer).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.key_name">
<code class="sig-name descname">key_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The key name that should be used for the instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.max_size">
<code class="sig-name descname">max_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.max_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of instances the group should have at any time.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.min_size">
<code class="sig-name descname">min_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.min_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum number of instances the group should have at any time.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The group name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.ondemand_count">
<code class="sig-name descname">ondemand_count</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.ondemand_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of on demand instances to launch in the group. All other instances will be spot instances. When this parameter is set the <code class="docutils literal notranslate"><span class="pre">spot_percentage</span></code> parameter is being ignored.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.orientation">
<code class="sig-name descname">orientation</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.orientation" title="Permalink to this definition">¶</a></dt>
<dd><p>Select a prediction strategy. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;balanced&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;costOriented&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;equalAzDistribution&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;availabilityOriented&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.placement_tenancy">
<code class="sig-name descname">placement_tenancy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.placement_tenancy" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable dedicated tenancy. Note: There is a flat hourly fee for each region in which dedicated tenancy is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.preferred_availability_zones">
<code class="sig-name descname">preferred_availability_zones</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.preferred_availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>The AZs to prioritize when launching Spot instances. If no markets are available in the Preferred AZs, Spot instances are launched in the non-preferred AZs. 
Note: Must be a sublist of <code class="docutils literal notranslate"><span class="pre">availability_zones</span></code> and <code class="docutils literal notranslate"><span class="pre">orientation</span></code> value must not be <code class="docutils literal notranslate"><span class="pre">&quot;equalAzDistribution&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.product">
<code class="sig-name descname">product</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.product" title="Permalink to this definition">¶</a></dt>
<dd><p>Operation system type. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;Linux/UNIX&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SUSE</span> <span class="pre">Linux&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Windows&quot;</span></code>. 
For EC2 Classic instances:  <code class="docutils literal notranslate"><span class="pre">&quot;Linux/UNIX</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SUSE</span> <span class="pre">Linux</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Windows</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS region your group will be created in.
Note: This parameter is required if you specify subnets (through subnet_ids). This parameter is optional if you specify Availability Zones (through availability_zones).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.revert_to_spot">
<code class="sig-name descname">revert_to_spot</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.revert_to_spot" title="Permalink to this definition">¶</a></dt>
<dd><p>Hold settings for strategy correction – replacing On-Demand for Spot instances. Supported Values: <code class="docutils literal notranslate"><span class="pre">&quot;never&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;always&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;timeWindow&quot;</span></code></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">performAt</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - In the event of a fallback to On-Demand instances, select the time period to revert back to Spot. Supported Arguments – always (default), timeWindow, never. For timeWindow or never to be valid the group must have availabilityOriented OR persistence defined.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeWindows</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specify a list of time windows for to execute revertToSpot strategy. Time window format: <code class="docutils literal notranslate"><span class="pre">ddd:hh:mm-ddd:hh:mm</span></code>. Example: <code class="docutils literal notranslate"><span class="pre">Mon:03:00-Wed:02:30</span></code></p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.scaling_strategies">
<code class="sig-name descname">scaling_strategies</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.scaling_strategies" title="Permalink to this definition">¶</a></dt>
<dd><p>Set termination policy.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">terminateAtEndOfBillingHour</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specify whether to terminate instances at the end of each billing hour.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">terminationPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - - Determines whether to terminate the newest instances when performing a scaling action. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;default&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;newestInstance&quot;</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.security_groups">
<code class="sig-name descname">security_groups</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of associated security group IDS.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.shutdown_script">
<code class="sig-name descname">shutdown_script</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.shutdown_script" title="Permalink to this definition">¶</a></dt>
<dd><p>The Base64-encoded shutdown script that executes prior to instance termination, for more information please see: <a class="reference external" href="https://api.spotinst.com/integration-docs/elastigroup/concepts/compute-concepts/shutdown-scripts/">Shutdown Script</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.spot_percentage">
<code class="sig-name descname">spot_percentage</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.spot_percentage" title="Permalink to this definition">¶</a></dt>
<dd><p>The percentage of Spot instances that would spin up from the <code class="docutils literal notranslate"><span class="pre">desired_capacity</span></code> number.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.subnet_ids">
<code class="sig-name descname">subnet_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Strings of subnet identifiers.
Note: When this parameter is set, <code class="docutils literal notranslate"><span class="pre">availability_zones</span></code> should be left unused.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A key/value mapping of tags to assign to the resource.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.user_data">
<code class="sig-name descname">user_data</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The user data to provide when launching the instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.utilize_reserved_instances">
<code class="sig-name descname">utilize_reserved_instances</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.utilize_reserved_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>In a case of any available reserved instances, Elastigroup will utilize them first before purchasing Spot instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.wait_for_capacity">
<code class="sig-name descname">wait_for_capacity</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.wait_for_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>Minimum number of instances in a ‘HEALTHY’ status that is required before continuing. This is ignored when updating with blue/green deployment. Cannot exceed <code class="docutils literal notranslate"><span class="pre">desired_capacity</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Elastigroup.wait_for_capacity_timeout">
<code class="sig-name descname">wait_for_capacity_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.wait_for_capacity_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Time (seconds) to wait for instances to report a ‘HEALTHY’ status. Useful for plans with multiple dependencies that take some time to initialize. Leave undefined or set to <code class="docutils literal notranslate"><span class="pre">0</span></code> to indicate no wait. This is ignored when updating with blue/green deployment.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.aws.Elastigroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">block_devices_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">capacity_unit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cpu_credits</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">desired_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">draining_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_block_devices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_optimized</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_load_balancers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_monitoring</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ephemeral_block_devices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fallback_to_ondemand</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_grace_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_unhealthy_duration_before_replacement</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iam_instance_profile</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types_ondemand</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types_preferred_spots</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types_spots</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types_weights</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_beanstalk</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_codedeploy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_docker_swarm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_ecs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_gitlab</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_kubernetes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_mesosphere</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_multai_runtime</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_nomad</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_rancher</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_route53</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lifetime_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">multai_target_sets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_interfaces</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ondemand_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">orientation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">persist_block_devices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">persist_private_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">persist_root_device</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">placement_tenancy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preferred_availability_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">revert_to_spot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_down_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_strategies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_target_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_up_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_tasks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shutdown_script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">signals</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_percentage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stateful_deallocation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_group_arns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">utilize_reserved_instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_for_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_for_capacity_timeout</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Elastigroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>availability_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Strings of availability zones. When this parameter is set, <code class="docutils literal notranslate"><span class="pre">subnet_ids</span></code> should be left unused.
Note: <code class="docutils literal notranslate"><span class="pre">availability_zones</span></code> naming syntax follows the convention <code class="docutils literal notranslate"><span class="pre">availability-zone:subnet:placement-group-name</span></code>. For example, to set an AZ in <code class="docutils literal notranslate"><span class="pre">us-east-1</span></code> with subnet <code class="docutils literal notranslate"><span class="pre">subnet-123456</span></code> and placement group <code class="docutils literal notranslate"><span class="pre">ClusterI03</span></code>, you would set:
<code class="docutils literal notranslate"><span class="pre">availability_zones</span> <span class="pre">=</span> <span class="pre">[&quot;us-east-1a:subnet-123456:ClusterI03&quot;]</span></code></p></li>
<li><p><strong>capacity_unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The capacity unit to launch instances by. If not specified, when choosing the weight unit, each instance will weight as the number of its vCPUs.</p></li>
<li><p><strong>cpu_credits</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Controls how T3 instances are launched. Valid values: <code class="docutils literal notranslate"><span class="pre">standard</span></code>, <code class="docutils literal notranslate"><span class="pre">unlimited</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The group description.</p></li>
<li><p><strong>desired_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The desired number of instances the group should have at any time.</p></li>
<li><p><strong>draining_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time in seconds, the instance is allowed to run while detached from the ELB. This is to allow the instance time to be drained from incoming TCP connections before terminating it, during a scale down operation.</p></li>
<li><p><strong>ebs_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable high bandwidth connectivity between instances and AWS’s Elastic Block Store (EBS). For instance types that are EBS-optimized by default this parameter will be ignored.</p></li>
<li><p><strong>elastic_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A list of <a class="reference external" href="http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html">AWS Elastic IP</a> allocation IDs to associate to the group instances.</p>
</p></li>
<li><p><strong>enable_monitoring</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether monitoring is enabled for the instance.</p></li>
<li><p><strong>fallback_to_ondemand</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – In a case of no Spot instances available, Elastigroup will launch on-demand instances instead.</p></li>
<li><p><strong>health_check_grace_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time, in seconds, after the instance has launched to starts and check its health.</p></li>
<li><p><strong>health_check_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service that will perform health checks for the instance. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;ELB&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;HCS&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;TARGET_GROUP&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;MLB&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;EC2&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;MULTAI_TARGET_SET&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;MLB_RUNTIME&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;K8S_NODE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;NOMAD_NODE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ECS_CLUSTER_INSTANCE&quot;</span></code>.</p></li>
<li><p><strong>health_check_unhealthy_duration_before_replacement</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time, in seconds, that we will wait before replacing an instance that is running and became unhealthy (this is only applicable for instances that were once healthy).</p></li>
<li><p><strong>iam_instance_profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN or name of an IAM instance profile to associate with launched instances.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the AMI used to launch the instance.</p></li>
<li><p><strong>instance_types_ondemand</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of instance determines your instance’s CPU capacity, memory and storage (e.g., m1.small, c1.xlarge).</p></li>
<li><p><strong>instance_types_preferred_spots</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Prioritize a subset of spot instance types. Must be a subset of the selected spot instance types.</p></li>
<li><p><strong>instance_types_spots</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more instance types.</p></li>
<li><p><strong>instance_types_weights</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of weights per instance type for weighted groups. Each object in the list should have the following attributes:</p></li>
<li><p><strong>key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key name that should be used for the instance.</p></li>
<li><p><strong>max_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of instances the group should have at any time.</p></li>
<li><p><strong>min_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum number of instances the group should have at any time.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The group name.</p></li>
<li><p><strong>ondemand_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of on demand instances to launch in the group. All other instances will be spot instances. When this parameter is set the <code class="docutils literal notranslate"><span class="pre">spot_percentage</span></code> parameter is being ignored.</p></li>
<li><p><strong>orientation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Select a prediction strategy. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;balanced&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;costOriented&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;equalAzDistribution&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;availabilityOriented&quot;</span></code>.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>placement_tenancy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enable dedicated tenancy. Note: There is a flat hourly fee for each region in which dedicated tenancy is used.</p></li>
<li><p><strong>preferred_availability_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The AZs to prioritize when launching Spot instances. If no markets are available in the Preferred AZs, Spot instances are launched in the non-preferred AZs. 
Note: Must be a sublist of <code class="docutils literal notranslate"><span class="pre">availability_zones</span></code> and <code class="docutils literal notranslate"><span class="pre">orientation</span></code> value must not be <code class="docutils literal notranslate"><span class="pre">&quot;equalAzDistribution&quot;</span></code>.</p></li>
<li><p><strong>product</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operation system type. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;Linux/UNIX&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SUSE</span> <span class="pre">Linux&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Windows&quot;</span></code>. 
For EC2 Classic instances:  <code class="docutils literal notranslate"><span class="pre">&quot;Linux/UNIX</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SUSE</span> <span class="pre">Linux</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Windows</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS region your group will be created in.
Note: This parameter is required if you specify subnets (through subnet_ids). This parameter is optional if you specify Availability Zones (through availability_zones).</p></li>
<li><p><strong>revert_to_spot</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Hold settings for strategy correction – replacing On-Demand for Spot instances. Supported Values: <code class="docutils literal notranslate"><span class="pre">&quot;never&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;always&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;timeWindow&quot;</span></code></p></li>
<li><p><strong>scaling_strategies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set termination policy.</p></li>
<li><p><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of associated security group IDS.</p></li>
<li><p><strong>shutdown_script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The Base64-encoded shutdown script that executes prior to instance termination, for more information please see: <a class="reference external" href="https://api.spotinst.com/integration-docs/elastigroup/concepts/compute-concepts/shutdown-scripts/">Shutdown Script</a></p>
</p></li>
<li><p><strong>spot_percentage</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The percentage of Spot instances that would spin up from the <code class="docutils literal notranslate"><span class="pre">desired_capacity</span></code> number.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Strings of subnet identifiers.
Note: When this parameter is set, <code class="docutils literal notranslate"><span class="pre">availability_zones</span></code> should be left unused.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A key/value mapping of tags to assign to the resource.</p></li>
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user data to provide when launching the instance.</p></li>
<li><p><strong>utilize_reserved_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – In a case of any available reserved instances, Elastigroup will utilize them first before purchasing Spot instances.</p></li>
<li><p><strong>wait_for_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum number of instances in a ‘HEALTHY’ status that is required before continuing. This is ignored when updating with blue/green deployment. Cannot exceed <code class="docutils literal notranslate"><span class="pre">desired_capacity</span></code>.</p></li>
<li><p><strong>wait_for_capacity_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time (seconds) to wait for instances to report a ‘HEALTHY’ status. Useful for plans with multiple dependencies that take some time to initialize. Leave undefined or set to <code class="docutils literal notranslate"><span class="pre">0</span></code> to indicate no wait. This is ignored when updating with blue/green deployment.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_block_devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deleteOnTermination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deviceName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeyId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshotId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>ephemeral_block_devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deviceName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>instance_types_weights</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instanceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of instance type (String).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Weight per instance type (Integer).</p></li>
</ul>
<p>The <strong>integration_beanstalk</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deployment_preferences</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">automaticRoll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">batchSizePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grace_period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">strategy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldDrainInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">environmentId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managed_actions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">platformUpdate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">performAt</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - In the event of a fallback to On-Demand instances, select the time period to revert back to Spot. Supported Arguments – always (default), timeWindow, never. For timeWindow or never to be valid the group must have availabilityOriented OR persistence defined.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeWindow</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">updateLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<p>The <strong>integration_codedeploy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cleanupOnFailure</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deploymentGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">applicationName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deploymentGroupName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">terminateInstanceOnFailure</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>integration_docker_swarm</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleCooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleDown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleHeadroom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numOfUnits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleIsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterHost</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>integration_ecs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleAttributes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleCooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleDown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxScaleDownPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleHeadroom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numOfUnits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleIsAutoConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleIsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleScaleDownNonServiceTasks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>integration_gitlab</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">runner</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>integration_kubernetes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">apiServer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleCooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleDown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleHeadroom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numOfUnits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleIsAutoConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleIsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleLabels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterIdentifier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">integrationMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>integration_mesosphere</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">apiServer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>integration_multai_runtime</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deployment_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>integration_nomad</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aclToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleConstraints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleCooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleDown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleHeadroom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numOfUnits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleIsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterHost</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>integration_rancher</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterHost</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>integration_route53</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">domains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">hostedZoneId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordSets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The group name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">usePublicIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">spotinstAcctId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>multai_target_sets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">balancer_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_set_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>network_interfaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">associateIpv6Address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">associate_public_ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deleteOnTermination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The group description.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deviceIndex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkInterfaceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateIpAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secondaryPrivateIpAddressCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>revert_to_spot</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">performAt</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - In the event of a fallback to On-Demand instances, select the time period to revert back to Spot. Supported Arguments – always (default), timeWindow, never. For timeWindow or never to be valid the group must have availabilityOriented OR persistence defined.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeWindows</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specify a list of time windows for to execute revertToSpot strategy. Time window format: <code class="docutils literal notranslate"><span class="pre">ddd:hh:mm-ddd:hh:mm</span></code>. Example: <code class="docutils literal notranslate"><span class="pre">Mon:03:00-Wed:02:30</span></code></p></li>
</ul>
<p>The <strong>scaling_down_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The group name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scaling_strategies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">terminateAtEndOfBillingHour</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specify whether to terminate instances at the end of each billing hour.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">terminationPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - - Determines whether to terminate the newest instances when performing a scaling action. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;default&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;newestInstance&quot;</span></code>.</p></li>
</ul>
<p>The <strong>scaling_target_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The group name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">predictiveMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scaling_up_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The group name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scheduled_tasks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustmentPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">batchSizePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cronExpression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frequency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grace_period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleMaxCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleMinCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>signals</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The group name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>stateful_deallocation</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">shouldDeleteImages</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldDeleteNetworkInterfaces</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldDeleteSnapshots</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldDeleteVolumes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>update_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoApplyTags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rollConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">batchSizePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grace_period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">health_check_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service that will perform health checks for the instance. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;ELB&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;HCS&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;TARGET_GROUP&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;MLB&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;EC2&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;MULTAI_TARGET_SET&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;MLB_RUNTIME&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;K8S_NODE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;NOMAD_NODE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ECS_CLUSTER_INSTANCE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">strategy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">batchMinHealthyPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">onFailure</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">batchNum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">draining_timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time in seconds, the instance is allowed to run while detached from the ELB. This is to allow the instance time to be drained from incoming TCP connections before terminating it, during a scale down operation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldDecrementTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldHandleAllBatches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldDrainInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitForRollPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitForRollTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldResumeStateful</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldRoll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.aws.Elastigroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.aws.Elastigroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.aws.Elastigroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.aws.ManagedInstance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.aws.</code><code class="sig-name descname">ManagedInstance</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_healing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">block_devices_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cpu_credits</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">draining_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_optimized</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_monitoring</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fall_back_to_od</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grace_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iam_instance_profile</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_route53</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_pair</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">life_cycle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_interfaces</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">optimization_windows</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">orientation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">persist_block_devices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">persist_private_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">persist_root_device</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">placement_tenancy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preferred_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">revert_to_spot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_tasks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shutdown_script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unhealthy_duration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">utilize_reserved_instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ManagedInstance resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] auto_healing: Enable the auto healing which auto replaces the instance in case the health check fails, default: <code class="docutils literal notranslate"><span class="pre">“true”</span></code>. 
:param pulumi.Input[str] block_devices_mode: Determine the way we attach the data volumes to the data devices. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;reattach&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;onLaunch&quot;</span></code>.</p>
<blockquote>
<div><p>Default: <code class="docutils literal notranslate"><span class="pre">&quot;onLaunch&quot;</span></code>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cpu_credits</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – cpuCredits can have one of two values: “unlimited”, “standard”.
Default: unlimited</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ManagedInstance description.</p></li>
<li><p><strong>draining_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time in seconds to allow the instance be drained from incoming TCP connections and detached from ELB before terminating it, during a scale down operation.</p></li>
<li><p><strong>ebs_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable EBS optimization for supported instance which is not enabled by default. Note - additional charges will be applied.
Default: false</p></li>
<li><p><strong>elastic_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Elastic IP Allocation Id to associate to the instance.</p></li>
<li><p><strong>enable_monitoring</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Describes whether instance Enhanced Monitoring is enabled.
Default: false</p></li>
<li><p><strong>grace_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time, in seconds, after the instance has launched to starts and check its health, default <code class="docutils literal notranslate"><span class="pre">“120&quot;</span></code>.</p></li>
<li><p><strong>health_check_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service to use for the health check. Valid values: <code class="docutils literal notranslate"><span class="pre">“EC2”</span></code>, <code class="docutils literal notranslate"><span class="pre">“ELB”</span></code>, <code class="docutils literal notranslate"><span class="pre">“TARGET_GROUP”</span></code>, <code class="docutils literal notranslate"><span class="pre">“MULTAI_TARGET_SET”</span></code>.
Default: <code class="docutils literal notranslate"><span class="pre">“EC2”</span></code>.</p></li>
<li><p><strong>iam_instance_profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set IAM profile to instance. Set only one of ARN or Name.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the image used to launch the instance.</p></li>
<li><p><strong>instance_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Comma separated list of available instance types for instance.</p></li>
<li><p><strong>key_pair</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify a Key Pair to attach to the instances.</p></li>
<li><p><strong>life_cycle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set lifecycle, valid values: <code class="docutils literal notranslate"><span class="pre">“spot”</span></code>, <code class="docutils literal notranslate"><span class="pre">“on_demand”</span></code>.
Default <code class="docutils literal notranslate"><span class="pre">&quot;spot&quot;</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ManagedInstance name.</p></li>
<li><p><strong>optimization_windows</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – When performAt is ‘timeWindow’: must specify a list of ‘timeWindows’ with at least one time window Each string is in the format of - ddd:hh:mm-ddd:hh:mm ddd = day of week = Sun | Mon | Tue | Wed | Thu | Fri | Sat hh = hour 24 = 0 -23 mm = minute = 0 - 59.</p></li>
<li><p><strong>orientation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Select a prediction strategy. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;balanced&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;costOriented&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;availabilityOriented&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;cheapest&quot;</span></code>.
Default: <code class="docutils literal notranslate"><span class="pre">&quot;availabilityOriented&quot;</span></code>.</p></li>
<li><p><strong>persist_block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the instance maintain its Data volumes.</p></li>
<li><p><strong>persist_private_ip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the instance maintain its private IP.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>persist_root_device</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the instance maintain its root device volumes.</p></li>
<li><p><strong>placement_tenancy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values: “default”, “dedicated”
Default: default</p></li>
<li><p><strong>preferred_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Preferred instance types for the instance. We will automatically select optional similar instance types to ensure optimized cost efficiency</p></li>
<li><p><strong>private_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Private IP Allocation Id to associate to the instance.</p></li>
<li><p><strong>product</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operation system type. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;Linux/UNIX&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SUSE</span> <span class="pre">Linux&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Windows&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Red</span> <span class="pre">Hat</span> <span class="pre">Enterprise</span> <span class="pre">Linux&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Linux/UNIX</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SUSE</span> <span class="pre">Linux</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Windows</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>,  <code class="docutils literal notranslate"><span class="pre">&quot;Red</span> <span class="pre">Hat</span> <span class="pre">Enterprise</span> <span class="pre">Linux</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS region your group will be created in.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more security group IDs.</p></li>
<li><p><strong>shutdown_script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Base64-encoded shutdown script to execute prior to instance termination.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A comma-separated list of subnet identifiers for your instance.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set tags for the instance. Items should be unique.</p></li>
<li><p><strong>unhealthy_duration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time, in seconds, an existing instance should remain active after becoming unhealthy. After the set time out the instance will be replaced, default <code class="docutils literal notranslate"><span class="pre">“120&quot;</span></code>.</p></li>
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Base64-encoded MIME user data to make available to the instances.</p></li>
<li><p><strong>utilize_reserved_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – In case of any available Reserved Instances, Managed Instance will utilize them before purchasing Spot instances.
Default: <code class="docutils literal notranslate"><span class="pre">&quot;false&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>integration_route53</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">domains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">hostedZoneId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordSets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ManagedInstance name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">usePublicIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">spotinstAcctId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>load_balancers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoWeight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azAwareness</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">balancer_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ManagedInstance name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_set_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>network_interfaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">associateIpv6Address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">associate_public_ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deviceIndex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>revert_to_spot</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">performAt</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values: “always”, “never”, “timeWindow”.
Default <code class="docutils literal notranslate"><span class="pre">&quot;never&quot;</span></code>.</p></li>
</ul>
<p>The <strong>scheduled_tasks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cronExpression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frequency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Tag’s key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Tag’s name.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.auto_healing">
<code class="sig-name descname">auto_healing</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.auto_healing" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable the auto healing which auto replaces the instance in case the health check fails, default: <code class="docutils literal notranslate"><span class="pre">“true”</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.block_devices_mode">
<code class="sig-name descname">block_devices_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.block_devices_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Determine the way we attach the data volumes to the data devices. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;reattach&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;onLaunch&quot;</span></code>.
Default: <code class="docutils literal notranslate"><span class="pre">&quot;onLaunch&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.cpu_credits">
<code class="sig-name descname">cpu_credits</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.cpu_credits" title="Permalink to this definition">¶</a></dt>
<dd><p>cpuCredits can have one of two values: “unlimited”, “standard”.
Default: unlimited</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The ManagedInstance description.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.draining_timeout">
<code class="sig-name descname">draining_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.draining_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time in seconds to allow the instance be drained from incoming TCP connections and detached from ELB before terminating it, during a scale down operation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.ebs_optimized">
<code class="sig-name descname">ebs_optimized</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.ebs_optimized" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable EBS optimization for supported instance which is not enabled by default. Note - additional charges will be applied.
Default: false</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.elastic_ip">
<code class="sig-name descname">elastic_ip</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.elastic_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Elastic IP Allocation Id to associate to the instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.enable_monitoring">
<code class="sig-name descname">enable_monitoring</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.enable_monitoring" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes whether instance Enhanced Monitoring is enabled.
Default: false</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.grace_period">
<code class="sig-name descname">grace_period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.grace_period" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time, in seconds, after the instance has launched to starts and check its health, default <code class="docutils literal notranslate"><span class="pre">“120&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.health_check_type">
<code class="sig-name descname">health_check_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.health_check_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The service to use for the health check. Valid values: <code class="docutils literal notranslate"><span class="pre">“EC2”</span></code>, <code class="docutils literal notranslate"><span class="pre">“ELB”</span></code>, <code class="docutils literal notranslate"><span class="pre">“TARGET_GROUP”</span></code>, <code class="docutils literal notranslate"><span class="pre">“MULTAI_TARGET_SET”</span></code>.
Default: <code class="docutils literal notranslate"><span class="pre">“EC2”</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.iam_instance_profile">
<code class="sig-name descname">iam_instance_profile</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.iam_instance_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>Set IAM profile to instance. Set only one of ARN or Name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.image_id">
<code class="sig-name descname">image_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the image used to launch the instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.instance_types">
<code class="sig-name descname">instance_types</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.instance_types" title="Permalink to this definition">¶</a></dt>
<dd><p>Comma separated list of available instance types for instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.key_pair">
<code class="sig-name descname">key_pair</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.key_pair" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify a Key Pair to attach to the instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.life_cycle">
<code class="sig-name descname">life_cycle</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.life_cycle" title="Permalink to this definition">¶</a></dt>
<dd><p>Set lifecycle, valid values: <code class="docutils literal notranslate"><span class="pre">“spot”</span></code>, <code class="docutils literal notranslate"><span class="pre">“on_demand”</span></code>.
Default <code class="docutils literal notranslate"><span class="pre">&quot;spot&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The ManagedInstance name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.optimization_windows">
<code class="sig-name descname">optimization_windows</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.optimization_windows" title="Permalink to this definition">¶</a></dt>
<dd><p>When performAt is ‘timeWindow’: must specify a list of ‘timeWindows’ with at least one time window Each string is in the format of - ddd:hh:mm-ddd:hh:mm ddd = day of week = Sun | Mon | Tue | Wed | Thu | Fri | Sat hh = hour 24 = 0 -23 mm = minute = 0 - 59.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.orientation">
<code class="sig-name descname">orientation</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.orientation" title="Permalink to this definition">¶</a></dt>
<dd><p>Select a prediction strategy. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;balanced&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;costOriented&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;availabilityOriented&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;cheapest&quot;</span></code>.
Default: <code class="docutils literal notranslate"><span class="pre">&quot;availabilityOriented&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.persist_block_devices">
<code class="sig-name descname">persist_block_devices</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.persist_block_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the instance maintain its Data volumes.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.persist_private_ip">
<code class="sig-name descname">persist_private_ip</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.persist_private_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the instance maintain its private IP.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.persist_root_device">
<code class="sig-name descname">persist_root_device</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.persist_root_device" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the instance maintain its root device volumes.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.placement_tenancy">
<code class="sig-name descname">placement_tenancy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.placement_tenancy" title="Permalink to this definition">¶</a></dt>
<dd><p>Valid values: “default”, “dedicated”
Default: default</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.preferred_type">
<code class="sig-name descname">preferred_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.preferred_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Preferred instance types for the instance. We will automatically select optional similar instance types to ensure optimized cost efficiency</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.private_ip">
<code class="sig-name descname">private_ip</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.private_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Private IP Allocation Id to associate to the instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.product">
<code class="sig-name descname">product</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.product" title="Permalink to this definition">¶</a></dt>
<dd><p>Operation system type. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;Linux/UNIX&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SUSE</span> <span class="pre">Linux&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Windows&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Red</span> <span class="pre">Hat</span> <span class="pre">Enterprise</span> <span class="pre">Linux&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Linux/UNIX</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SUSE</span> <span class="pre">Linux</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Windows</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>,  <code class="docutils literal notranslate"><span class="pre">&quot;Red</span> <span class="pre">Hat</span> <span class="pre">Enterprise</span> <span class="pre">Linux</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS region your group will be created in.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.security_group_ids">
<code class="sig-name descname">security_group_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more security group IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.shutdown_script">
<code class="sig-name descname">shutdown_script</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.shutdown_script" title="Permalink to this definition">¶</a></dt>
<dd><p>The Base64-encoded shutdown script to execute prior to instance termination.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.subnet_ids">
<code class="sig-name descname">subnet_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma-separated list of subnet identifiers for your instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Set tags for the instance. Items should be unique.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Tag’s key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Tag’s name.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.unhealthy_duration">
<code class="sig-name descname">unhealthy_duration</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.unhealthy_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time, in seconds, an existing instance should remain active after becoming unhealthy. After the set time out the instance will be replaced, default <code class="docutils literal notranslate"><span class="pre">“120&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.user_data">
<code class="sig-name descname">user_data</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The Base64-encoded MIME user data to make available to the instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.ManagedInstance.utilize_reserved_instances">
<code class="sig-name descname">utilize_reserved_instances</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.utilize_reserved_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>In case of any available Reserved Instances, Managed Instance will utilize them before purchasing Spot instances.
Default: <code class="docutils literal notranslate"><span class="pre">&quot;false&quot;</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.aws.ManagedInstance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_healing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">block_devices_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cpu_credits</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">draining_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_optimized</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_monitoring</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fall_back_to_od</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grace_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iam_instance_profile</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_route53</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_pair</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">life_cycle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_interfaces</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">optimization_windows</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">orientation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">persist_block_devices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">persist_private_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">persist_root_device</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">placement_tenancy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preferred_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">revert_to_spot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_tasks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shutdown_script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unhealthy_duration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">utilize_reserved_instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ManagedInstance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_healing</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable the auto healing which auto replaces the instance in case the health check fails, default: <code class="docutils literal notranslate"><span class="pre">“true”</span></code>.</p></li>
<li><p><strong>block_devices_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determine the way we attach the data volumes to the data devices. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;reattach&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;onLaunch&quot;</span></code>.
Default: <code class="docutils literal notranslate"><span class="pre">&quot;onLaunch&quot;</span></code>.</p></li>
<li><p><strong>cpu_credits</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – cpuCredits can have one of two values: “unlimited”, “standard”.
Default: unlimited</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ManagedInstance description.</p></li>
<li><p><strong>draining_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time in seconds to allow the instance be drained from incoming TCP connections and detached from ELB before terminating it, during a scale down operation.</p></li>
<li><p><strong>ebs_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable EBS optimization for supported instance which is not enabled by default. Note - additional charges will be applied.
Default: false</p></li>
<li><p><strong>elastic_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Elastic IP Allocation Id to associate to the instance.</p></li>
<li><p><strong>enable_monitoring</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Describes whether instance Enhanced Monitoring is enabled.
Default: false</p></li>
<li><p><strong>grace_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time, in seconds, after the instance has launched to starts and check its health, default <code class="docutils literal notranslate"><span class="pre">“120&quot;</span></code>.</p></li>
<li><p><strong>health_check_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service to use for the health check. Valid values: <code class="docutils literal notranslate"><span class="pre">“EC2”</span></code>, <code class="docutils literal notranslate"><span class="pre">“ELB”</span></code>, <code class="docutils literal notranslate"><span class="pre">“TARGET_GROUP”</span></code>, <code class="docutils literal notranslate"><span class="pre">“MULTAI_TARGET_SET”</span></code>.
Default: <code class="docutils literal notranslate"><span class="pre">“EC2”</span></code>.</p></li>
<li><p><strong>iam_instance_profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set IAM profile to instance. Set only one of ARN or Name.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the image used to launch the instance.</p></li>
<li><p><strong>instance_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Comma separated list of available instance types for instance.</p></li>
<li><p><strong>key_pair</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify a Key Pair to attach to the instances.</p></li>
<li><p><strong>life_cycle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set lifecycle, valid values: <code class="docutils literal notranslate"><span class="pre">“spot”</span></code>, <code class="docutils literal notranslate"><span class="pre">“on_demand”</span></code>.
Default <code class="docutils literal notranslate"><span class="pre">&quot;spot&quot;</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ManagedInstance name.</p></li>
<li><p><strong>optimization_windows</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – When performAt is ‘timeWindow’: must specify a list of ‘timeWindows’ with at least one time window Each string is in the format of - ddd:hh:mm-ddd:hh:mm ddd = day of week = Sun | Mon | Tue | Wed | Thu | Fri | Sat hh = hour 24 = 0 -23 mm = minute = 0 - 59.</p></li>
<li><p><strong>orientation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Select a prediction strategy. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;balanced&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;costOriented&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;availabilityOriented&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;cheapest&quot;</span></code>.
Default: <code class="docutils literal notranslate"><span class="pre">&quot;availabilityOriented&quot;</span></code>.</p></li>
<li><p><strong>persist_block_devices</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the instance maintain its Data volumes.</p></li>
<li><p><strong>persist_private_ip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the instance maintain its private IP.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>persist_root_device</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the instance maintain its root device volumes.</p></li>
<li><p><strong>placement_tenancy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values: “default”, “dedicated”
Default: default</p></li>
<li><p><strong>preferred_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Preferred instance types for the instance. We will automatically select optional similar instance types to ensure optimized cost efficiency</p></li>
<li><p><strong>private_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Private IP Allocation Id to associate to the instance.</p></li>
<li><p><strong>product</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operation system type. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;Linux/UNIX&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SUSE</span> <span class="pre">Linux&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Windows&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Red</span> <span class="pre">Hat</span> <span class="pre">Enterprise</span> <span class="pre">Linux&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Linux/UNIX</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;SUSE</span> <span class="pre">Linux</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Windows</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>,  <code class="docutils literal notranslate"><span class="pre">&quot;Red</span> <span class="pre">Hat</span> <span class="pre">Enterprise</span> <span class="pre">Linux</span> <span class="pre">(Amazon</span> <span class="pre">VPC)&quot;</span></code>.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS region your group will be created in.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more security group IDs.</p></li>
<li><p><strong>shutdown_script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Base64-encoded shutdown script to execute prior to instance termination.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A comma-separated list of subnet identifiers for your instance.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set tags for the instance. Items should be unique.</p></li>
<li><p><strong>unhealthy_duration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time, in seconds, an existing instance should remain active after becoming unhealthy. After the set time out the instance will be replaced, default <code class="docutils literal notranslate"><span class="pre">“120&quot;</span></code>.</p></li>
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Base64-encoded MIME user data to make available to the instances.</p></li>
<li><p><strong>utilize_reserved_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – In case of any available Reserved Instances, Managed Instance will utilize them before purchasing Spot instances.
Default: <code class="docutils literal notranslate"><span class="pre">&quot;false&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>integration_route53</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">domains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">hostedZoneId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recordSets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ManagedInstance name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">usePublicIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">spotinstAcctId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>load_balancers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoWeight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azAwareness</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">balancer_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ManagedInstance name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_set_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>network_interfaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">associateIpv6Address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">associate_public_ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deviceIndex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>revert_to_spot</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">performAt</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values: “always”, “never”, “timeWindow”.
Default <code class="docutils literal notranslate"><span class="pre">&quot;never&quot;</span></code>.</p></li>
</ul>
<p>The <strong>scheduled_tasks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cronExpression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frequency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Tag’s key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Tag’s name.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.aws.ManagedInstance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.aws.ManagedInstance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.aws.ManagedInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.aws.MrScalar">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.aws.</code><code class="sig-name descname">MrScalar</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_info</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_primary_security_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_replica_security_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">applications</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bootstrap_actions_files</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configurations_files</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_desired_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_ebs_block_devices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_ebs_optimized</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_instance_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_lifecycle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_max_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_min_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_scaling_down_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_scaling_up_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_unit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_ami_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_root_volume_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ec2_key_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expose_cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_weights</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">job_flow_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keep_job_flow_alive</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">managed_primary_security_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">managed_replica_security_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_ebs_block_devices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_ebs_optimized</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_instance_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_lifecycle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provisioning_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">release_label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repo_upgrade_on_boot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_tasks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_access_security_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">steps_files</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_desired_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_ebs_block_devices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_ebs_optimized</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_instance_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_lifecycle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_max_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_min_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_scaling_down_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_scaling_up_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_unit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protected</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visible_to_all_users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.aws.MrScalar" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a MrScalar resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] cluster_id: The MrScaler cluster id.
:param pulumi.Input[str] description: The MrScaler description.
:param pulumi.Input[str] name: The MrScaler name.
:param pulumi.Input[str] region: The MrScaler region.
:param pulumi.Input[str] strategy: The MrScaler strategy. Allowed values are <code class="docutils literal notranslate"><span class="pre">new</span></code> <code class="docutils literal notranslate"><span class="pre">clone</span></code> and <code class="docutils literal notranslate"><span class="pre">wrap</span></code>.
:param pulumi.Input[list] termination_policies: Allows defining termination policies for EMR clusters based on CloudWatch Metrics.</p>
<p>The <strong>applications</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The MrScaler name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>bootstrap_actions_files</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>configurations_files</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>core_ebs_block_devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeInGb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>core_scaling_down_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of periods over which data is compared to the specified threshold.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the metric in CloudWatch which the statement will be based on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Must contain the value: <code class="docutils literal notranslate"><span class="pre">AWS/ElasticMapReduce</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The operator to use in order to determine if the policy is applicable. Valid values: <code class="docutils literal notranslate"><span class="pre">gt</span></code> | <code class="docutils literal notranslate"><span class="pre">gte</span></code> | <code class="docutils literal notranslate"><span class="pre">lt</span></code> | <code class="docutils literal notranslate"><span class="pre">lte</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time window in seconds over which the statistic is applied.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The aggregation method of the given metric. Valid Values: <code class="docutils literal notranslate"><span class="pre">average</span></code> | <code class="docutils literal notranslate"><span class="pre">sum</span></code> | <code class="docutils literal notranslate"><span class="pre">sampleCount</span></code> | <code class="docutils literal notranslate"><span class="pre">maximum</span></code> | <code class="docutils literal notranslate"><span class="pre">minimum</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The value that the specified statistic is compared to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unit for a given metric. Valid Values: <code class="docutils literal notranslate"><span class="pre">seconds</span></code> | <code class="docutils literal notranslate"><span class="pre">microseconds</span></code> | <code class="docutils literal notranslate"><span class="pre">milliseconds</span></code> | <code class="docutils literal notranslate"><span class="pre">bytes</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobytes</span></code> | <code class="docutils literal notranslate"><span class="pre">megabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">terabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">bits</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobits</span></code> | <code class="docutils literal notranslate"><span class="pre">megabits</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabits</span></code> | <code class="docutils literal notranslate"><span class="pre">terabits</span></code> | <code class="docutils literal notranslate"><span class="pre">percent</span></code> | <code class="docutils literal notranslate"><span class="pre">count</span></code> | <code class="docutils literal notranslate"><span class="pre">bytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">megabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">terabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">bits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">megabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">terabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">count/second</span></code> | <code class="docutils literal notranslate"><span class="pre">none</span></code></p></li>
</ul>
<p>The <strong>core_scaling_up_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of periods over which data is compared to the specified threshold.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the metric in CloudWatch which the statement will be based on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Must contain the value: <code class="docutils literal notranslate"><span class="pre">AWS/ElasticMapReduce</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The operator to use in order to determine if the policy is applicable. Valid values: <code class="docutils literal notranslate"><span class="pre">gt</span></code> | <code class="docutils literal notranslate"><span class="pre">gte</span></code> | <code class="docutils literal notranslate"><span class="pre">lt</span></code> | <code class="docutils literal notranslate"><span class="pre">lte</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time window in seconds over which the statistic is applied.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The aggregation method of the given metric. Valid Values: <code class="docutils literal notranslate"><span class="pre">average</span></code> | <code class="docutils literal notranslate"><span class="pre">sum</span></code> | <code class="docutils literal notranslate"><span class="pre">sampleCount</span></code> | <code class="docutils literal notranslate"><span class="pre">maximum</span></code> | <code class="docutils literal notranslate"><span class="pre">minimum</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The value that the specified statistic is compared to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unit for a given metric. Valid Values: <code class="docutils literal notranslate"><span class="pre">seconds</span></code> | <code class="docutils literal notranslate"><span class="pre">microseconds</span></code> | <code class="docutils literal notranslate"><span class="pre">milliseconds</span></code> | <code class="docutils literal notranslate"><span class="pre">bytes</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobytes</span></code> | <code class="docutils literal notranslate"><span class="pre">megabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">terabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">bits</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobits</span></code> | <code class="docutils literal notranslate"><span class="pre">megabits</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabits</span></code> | <code class="docutils literal notranslate"><span class="pre">terabits</span></code> | <code class="docutils literal notranslate"><span class="pre">percent</span></code> | <code class="docutils literal notranslate"><span class="pre">count</span></code> | <code class="docutils literal notranslate"><span class="pre">bytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">megabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">terabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">bits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">megabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">terabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">count/second</span></code> | <code class="docutils literal notranslate"><span class="pre">none</span></code></p></li>
</ul>
<p>The <strong>instance_weights</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instanceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weightedCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>master_ebs_block_devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeInGb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>provisioning_timeout</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeoutAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scheduled_tasks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cron</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">desired_capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceGroupType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>steps_files</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>task_ebs_block_devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeInGb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>task_scaling_down_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of periods over which data is compared to the specified threshold.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the metric in CloudWatch which the statement will be based on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Must contain the value: <code class="docutils literal notranslate"><span class="pre">AWS/ElasticMapReduce</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The operator to use in order to determine if the policy is applicable. Valid values: <code class="docutils literal notranslate"><span class="pre">gt</span></code> | <code class="docutils literal notranslate"><span class="pre">gte</span></code> | <code class="docutils literal notranslate"><span class="pre">lt</span></code> | <code class="docutils literal notranslate"><span class="pre">lte</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time window in seconds over which the statistic is applied.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The aggregation method of the given metric. Valid Values: <code class="docutils literal notranslate"><span class="pre">average</span></code> | <code class="docutils literal notranslate"><span class="pre">sum</span></code> | <code class="docutils literal notranslate"><span class="pre">sampleCount</span></code> | <code class="docutils literal notranslate"><span class="pre">maximum</span></code> | <code class="docutils literal notranslate"><span class="pre">minimum</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The value that the specified statistic is compared to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unit for a given metric. Valid Values: <code class="docutils literal notranslate"><span class="pre">seconds</span></code> | <code class="docutils literal notranslate"><span class="pre">microseconds</span></code> | <code class="docutils literal notranslate"><span class="pre">milliseconds</span></code> | <code class="docutils literal notranslate"><span class="pre">bytes</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobytes</span></code> | <code class="docutils literal notranslate"><span class="pre">megabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">terabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">bits</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobits</span></code> | <code class="docutils literal notranslate"><span class="pre">megabits</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabits</span></code> | <code class="docutils literal notranslate"><span class="pre">terabits</span></code> | <code class="docutils literal notranslate"><span class="pre">percent</span></code> | <code class="docutils literal notranslate"><span class="pre">count</span></code> | <code class="docutils literal notranslate"><span class="pre">bytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">megabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">terabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">bits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">megabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">terabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">count/second</span></code> | <code class="docutils literal notranslate"><span class="pre">none</span></code></p></li>
</ul>
<p>The <strong>task_scaling_up_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of periods over which data is compared to the specified threshold.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the metric in CloudWatch which the statement will be based on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Must contain the value: <code class="docutils literal notranslate"><span class="pre">AWS/ElasticMapReduce</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The operator to use in order to determine if the policy is applicable. Valid values: <code class="docutils literal notranslate"><span class="pre">gt</span></code> | <code class="docutils literal notranslate"><span class="pre">gte</span></code> | <code class="docutils literal notranslate"><span class="pre">lt</span></code> | <code class="docutils literal notranslate"><span class="pre">lte</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time window in seconds over which the statistic is applied.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The aggregation method of the given metric. Valid Values: <code class="docutils literal notranslate"><span class="pre">average</span></code> | <code class="docutils literal notranslate"><span class="pre">sum</span></code> | <code class="docutils literal notranslate"><span class="pre">sampleCount</span></code> | <code class="docutils literal notranslate"><span class="pre">maximum</span></code> | <code class="docutils literal notranslate"><span class="pre">minimum</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The value that the specified statistic is compared to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unit for a given metric. Valid Values: <code class="docutils literal notranslate"><span class="pre">seconds</span></code> | <code class="docutils literal notranslate"><span class="pre">microseconds</span></code> | <code class="docutils literal notranslate"><span class="pre">milliseconds</span></code> | <code class="docutils literal notranslate"><span class="pre">bytes</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobytes</span></code> | <code class="docutils literal notranslate"><span class="pre">megabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">terabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">bits</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobits</span></code> | <code class="docutils literal notranslate"><span class="pre">megabits</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabits</span></code> | <code class="docutils literal notranslate"><span class="pre">terabits</span></code> | <code class="docutils literal notranslate"><span class="pre">percent</span></code> | <code class="docutils literal notranslate"><span class="pre">count</span></code> | <code class="docutils literal notranslate"><span class="pre">bytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">megabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">terabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">bits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">megabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">terabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">count/second</span></code> | <code class="docutils literal notranslate"><span class="pre">none</span></code></p></li>
</ul>
<p>The <strong>termination_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">statements</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of periods over which data is compared to the specified threshold.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the metric in CloudWatch which the statement will be based on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Must contain the value: <code class="docutils literal notranslate"><span class="pre">AWS/ElasticMapReduce</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The operator to use in order to determine if the policy is applicable. Valid values: <code class="docutils literal notranslate"><span class="pre">gt</span></code> | <code class="docutils literal notranslate"><span class="pre">gte</span></code> | <code class="docutils literal notranslate"><span class="pre">lt</span></code> | <code class="docutils literal notranslate"><span class="pre">lte</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time window in seconds over which the statistic is applied.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The aggregation method of the given metric. Valid Values: <code class="docutils literal notranslate"><span class="pre">average</span></code> | <code class="docutils literal notranslate"><span class="pre">sum</span></code> | <code class="docutils literal notranslate"><span class="pre">sampleCount</span></code> | <code class="docutils literal notranslate"><span class="pre">maximum</span></code> | <code class="docutils literal notranslate"><span class="pre">minimum</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The value that the specified statistic is compared to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unit for a given metric. Valid Values: <code class="docutils literal notranslate"><span class="pre">seconds</span></code> | <code class="docutils literal notranslate"><span class="pre">microseconds</span></code> | <code class="docutils literal notranslate"><span class="pre">milliseconds</span></code> | <code class="docutils literal notranslate"><span class="pre">bytes</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobytes</span></code> | <code class="docutils literal notranslate"><span class="pre">megabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">terabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">bits</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobits</span></code> | <code class="docutils literal notranslate"><span class="pre">megabits</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabits</span></code> | <code class="docutils literal notranslate"><span class="pre">terabits</span></code> | <code class="docutils literal notranslate"><span class="pre">percent</span></code> | <code class="docutils literal notranslate"><span class="pre">count</span></code> | <code class="docutils literal notranslate"><span class="pre">bytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">megabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">terabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">bits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">megabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">terabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">count/second</span></code> | <code class="docutils literal notranslate"><span class="pre">none</span></code></p></li>
</ul>
</li>
</ul>
<dl class="py attribute">
<dt id="pulumi_spotinst.aws.MrScalar.cluster_id">
<code class="sig-name descname">cluster_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.MrScalar.cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The MrScaler cluster id.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.MrScalar.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.MrScalar.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The MrScaler description.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.MrScalar.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.MrScalar.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The MrScaler name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.MrScalar.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.MrScalar.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The MrScaler region.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.MrScalar.strategy">
<code class="sig-name descname">strategy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.MrScalar.strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>The MrScaler strategy. Allowed values are <code class="docutils literal notranslate"><span class="pre">new</span></code> <code class="docutils literal notranslate"><span class="pre">clone</span></code> and <code class="docutils literal notranslate"><span class="pre">wrap</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.MrScalar.termination_policies">
<code class="sig-name descname">termination_policies</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.MrScalar.termination_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows defining termination policies for EMR clusters based on CloudWatch Metrics.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">statements</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of periods over which data is compared to the specified threshold.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the metric in CloudWatch which the statement will be based on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Must contain the value: <code class="docutils literal notranslate"><span class="pre">AWS/ElasticMapReduce</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The operator to use in order to determine if the policy is applicable. Valid values: <code class="docutils literal notranslate"><span class="pre">gt</span></code> | <code class="docutils literal notranslate"><span class="pre">gte</span></code> | <code class="docutils literal notranslate"><span class="pre">lt</span></code> | <code class="docutils literal notranslate"><span class="pre">lte</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The time window in seconds over which the statistic is applied.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The aggregation method of the given metric. Valid Values: <code class="docutils literal notranslate"><span class="pre">average</span></code> | <code class="docutils literal notranslate"><span class="pre">sum</span></code> | <code class="docutils literal notranslate"><span class="pre">sampleCount</span></code> | <code class="docutils literal notranslate"><span class="pre">maximum</span></code> | <code class="docutils literal notranslate"><span class="pre">minimum</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The value that the specified statistic is compared to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unit for a given metric. Valid Values: <code class="docutils literal notranslate"><span class="pre">seconds</span></code> | <code class="docutils literal notranslate"><span class="pre">microseconds</span></code> | <code class="docutils literal notranslate"><span class="pre">milliseconds</span></code> | <code class="docutils literal notranslate"><span class="pre">bytes</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobytes</span></code> | <code class="docutils literal notranslate"><span class="pre">megabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">terabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">bits</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobits</span></code> | <code class="docutils literal notranslate"><span class="pre">megabits</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabits</span></code> | <code class="docutils literal notranslate"><span class="pre">terabits</span></code> | <code class="docutils literal notranslate"><span class="pre">percent</span></code> | <code class="docutils literal notranslate"><span class="pre">count</span></code> | <code class="docutils literal notranslate"><span class="pre">bytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">megabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">terabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">bits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">megabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">terabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">count/second</span></code> | <code class="docutils literal notranslate"><span class="pre">none</span></code></p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.aws.MrScalar.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_info</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_primary_security_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_replica_security_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">applications</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bootstrap_actions_files</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configurations_files</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_desired_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_ebs_block_devices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_ebs_optimized</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_instance_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_lifecycle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_max_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_min_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_scaling_down_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_scaling_up_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_unit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_ami_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_root_volume_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ec2_key_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expose_cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_weights</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">job_flow_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keep_job_flow_alive</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">managed_primary_security_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">managed_replica_security_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_ebs_block_devices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_ebs_optimized</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_instance_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_lifecycle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provisioning_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">release_label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repo_upgrade_on_boot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_tasks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_access_security_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">steps_files</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_desired_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_ebs_block_devices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_ebs_optimized</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_instance_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_lifecycle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_max_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_min_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_scaling_down_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_scaling_up_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_unit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protected</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visible_to_all_users</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.aws.MrScalar.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MrScalar resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The MrScaler cluster id.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The MrScaler description.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The MrScaler name.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The MrScaler region.</p></li>
<li><p><strong>strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The MrScaler strategy. Allowed values are <code class="docutils literal notranslate"><span class="pre">new</span></code> <code class="docutils literal notranslate"><span class="pre">clone</span></code> and <code class="docutils literal notranslate"><span class="pre">wrap</span></code>.</p></li>
<li><p><strong>termination_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Allows defining termination policies for EMR clusters based on CloudWatch Metrics.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>applications</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The MrScaler name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>bootstrap_actions_files</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>configurations_files</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>core_ebs_block_devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeInGb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>core_scaling_down_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of periods over which data is compared to the specified threshold.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the metric in CloudWatch which the statement will be based on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Must contain the value: <code class="docutils literal notranslate"><span class="pre">AWS/ElasticMapReduce</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The operator to use in order to determine if the policy is applicable. Valid values: <code class="docutils literal notranslate"><span class="pre">gt</span></code> | <code class="docutils literal notranslate"><span class="pre">gte</span></code> | <code class="docutils literal notranslate"><span class="pre">lt</span></code> | <code class="docutils literal notranslate"><span class="pre">lte</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time window in seconds over which the statistic is applied.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The aggregation method of the given metric. Valid Values: <code class="docutils literal notranslate"><span class="pre">average</span></code> | <code class="docutils literal notranslate"><span class="pre">sum</span></code> | <code class="docutils literal notranslate"><span class="pre">sampleCount</span></code> | <code class="docutils literal notranslate"><span class="pre">maximum</span></code> | <code class="docutils literal notranslate"><span class="pre">minimum</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The value that the specified statistic is compared to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unit for a given metric. Valid Values: <code class="docutils literal notranslate"><span class="pre">seconds</span></code> | <code class="docutils literal notranslate"><span class="pre">microseconds</span></code> | <code class="docutils literal notranslate"><span class="pre">milliseconds</span></code> | <code class="docutils literal notranslate"><span class="pre">bytes</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobytes</span></code> | <code class="docutils literal notranslate"><span class="pre">megabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">terabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">bits</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobits</span></code> | <code class="docutils literal notranslate"><span class="pre">megabits</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabits</span></code> | <code class="docutils literal notranslate"><span class="pre">terabits</span></code> | <code class="docutils literal notranslate"><span class="pre">percent</span></code> | <code class="docutils literal notranslate"><span class="pre">count</span></code> | <code class="docutils literal notranslate"><span class="pre">bytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">megabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">terabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">bits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">megabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">terabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">count/second</span></code> | <code class="docutils literal notranslate"><span class="pre">none</span></code></p></li>
</ul>
<p>The <strong>core_scaling_up_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of periods over which data is compared to the specified threshold.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the metric in CloudWatch which the statement will be based on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Must contain the value: <code class="docutils literal notranslate"><span class="pre">AWS/ElasticMapReduce</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The operator to use in order to determine if the policy is applicable. Valid values: <code class="docutils literal notranslate"><span class="pre">gt</span></code> | <code class="docutils literal notranslate"><span class="pre">gte</span></code> | <code class="docutils literal notranslate"><span class="pre">lt</span></code> | <code class="docutils literal notranslate"><span class="pre">lte</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time window in seconds over which the statistic is applied.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The aggregation method of the given metric. Valid Values: <code class="docutils literal notranslate"><span class="pre">average</span></code> | <code class="docutils literal notranslate"><span class="pre">sum</span></code> | <code class="docutils literal notranslate"><span class="pre">sampleCount</span></code> | <code class="docutils literal notranslate"><span class="pre">maximum</span></code> | <code class="docutils literal notranslate"><span class="pre">minimum</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The value that the specified statistic is compared to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unit for a given metric. Valid Values: <code class="docutils literal notranslate"><span class="pre">seconds</span></code> | <code class="docutils literal notranslate"><span class="pre">microseconds</span></code> | <code class="docutils literal notranslate"><span class="pre">milliseconds</span></code> | <code class="docutils literal notranslate"><span class="pre">bytes</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobytes</span></code> | <code class="docutils literal notranslate"><span class="pre">megabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">terabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">bits</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobits</span></code> | <code class="docutils literal notranslate"><span class="pre">megabits</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabits</span></code> | <code class="docutils literal notranslate"><span class="pre">terabits</span></code> | <code class="docutils literal notranslate"><span class="pre">percent</span></code> | <code class="docutils literal notranslate"><span class="pre">count</span></code> | <code class="docutils literal notranslate"><span class="pre">bytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">megabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">terabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">bits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">megabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">terabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">count/second</span></code> | <code class="docutils literal notranslate"><span class="pre">none</span></code></p></li>
</ul>
<p>The <strong>instance_weights</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instanceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weightedCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>master_ebs_block_devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeInGb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>provisioning_timeout</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeoutAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scheduled_tasks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cron</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">desired_capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceGroupType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>steps_files</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>task_ebs_block_devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeInGb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>task_scaling_down_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of periods over which data is compared to the specified threshold.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the metric in CloudWatch which the statement will be based on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Must contain the value: <code class="docutils literal notranslate"><span class="pre">AWS/ElasticMapReduce</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The operator to use in order to determine if the policy is applicable. Valid values: <code class="docutils literal notranslate"><span class="pre">gt</span></code> | <code class="docutils literal notranslate"><span class="pre">gte</span></code> | <code class="docutils literal notranslate"><span class="pre">lt</span></code> | <code class="docutils literal notranslate"><span class="pre">lte</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time window in seconds over which the statistic is applied.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The aggregation method of the given metric. Valid Values: <code class="docutils literal notranslate"><span class="pre">average</span></code> | <code class="docutils literal notranslate"><span class="pre">sum</span></code> | <code class="docutils literal notranslate"><span class="pre">sampleCount</span></code> | <code class="docutils literal notranslate"><span class="pre">maximum</span></code> | <code class="docutils literal notranslate"><span class="pre">minimum</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The value that the specified statistic is compared to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unit for a given metric. Valid Values: <code class="docutils literal notranslate"><span class="pre">seconds</span></code> | <code class="docutils literal notranslate"><span class="pre">microseconds</span></code> | <code class="docutils literal notranslate"><span class="pre">milliseconds</span></code> | <code class="docutils literal notranslate"><span class="pre">bytes</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobytes</span></code> | <code class="docutils literal notranslate"><span class="pre">megabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">terabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">bits</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobits</span></code> | <code class="docutils literal notranslate"><span class="pre">megabits</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabits</span></code> | <code class="docutils literal notranslate"><span class="pre">terabits</span></code> | <code class="docutils literal notranslate"><span class="pre">percent</span></code> | <code class="docutils literal notranslate"><span class="pre">count</span></code> | <code class="docutils literal notranslate"><span class="pre">bytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">megabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">terabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">bits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">megabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">terabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">count/second</span></code> | <code class="docutils literal notranslate"><span class="pre">none</span></code></p></li>
</ul>
<p>The <strong>task_scaling_up_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of periods over which data is compared to the specified threshold.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the metric in CloudWatch which the statement will be based on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Must contain the value: <code class="docutils literal notranslate"><span class="pre">AWS/ElasticMapReduce</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The operator to use in order to determine if the policy is applicable. Valid values: <code class="docutils literal notranslate"><span class="pre">gt</span></code> | <code class="docutils literal notranslate"><span class="pre">gte</span></code> | <code class="docutils literal notranslate"><span class="pre">lt</span></code> | <code class="docutils literal notranslate"><span class="pre">lte</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time window in seconds over which the statistic is applied.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The aggregation method of the given metric. Valid Values: <code class="docutils literal notranslate"><span class="pre">average</span></code> | <code class="docutils literal notranslate"><span class="pre">sum</span></code> | <code class="docutils literal notranslate"><span class="pre">sampleCount</span></code> | <code class="docutils literal notranslate"><span class="pre">maximum</span></code> | <code class="docutils literal notranslate"><span class="pre">minimum</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The value that the specified statistic is compared to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unit for a given metric. Valid Values: <code class="docutils literal notranslate"><span class="pre">seconds</span></code> | <code class="docutils literal notranslate"><span class="pre">microseconds</span></code> | <code class="docutils literal notranslate"><span class="pre">milliseconds</span></code> | <code class="docutils literal notranslate"><span class="pre">bytes</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobytes</span></code> | <code class="docutils literal notranslate"><span class="pre">megabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">terabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">bits</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobits</span></code> | <code class="docutils literal notranslate"><span class="pre">megabits</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabits</span></code> | <code class="docutils literal notranslate"><span class="pre">terabits</span></code> | <code class="docutils literal notranslate"><span class="pre">percent</span></code> | <code class="docutils literal notranslate"><span class="pre">count</span></code> | <code class="docutils literal notranslate"><span class="pre">bytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">megabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">terabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">bits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">megabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">terabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">count/second</span></code> | <code class="docutils literal notranslate"><span class="pre">none</span></code></p></li>
</ul>
<p>The <strong>termination_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">statements</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of periods over which data is compared to the specified threshold.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the metric in CloudWatch which the statement will be based on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Must contain the value: <code class="docutils literal notranslate"><span class="pre">AWS/ElasticMapReduce</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The operator to use in order to determine if the policy is applicable. Valid values: <code class="docutils literal notranslate"><span class="pre">gt</span></code> | <code class="docutils literal notranslate"><span class="pre">gte</span></code> | <code class="docutils literal notranslate"><span class="pre">lt</span></code> | <code class="docutils literal notranslate"><span class="pre">lte</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time window in seconds over which the statistic is applied.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The aggregation method of the given metric. Valid Values: <code class="docutils literal notranslate"><span class="pre">average</span></code> | <code class="docutils literal notranslate"><span class="pre">sum</span></code> | <code class="docutils literal notranslate"><span class="pre">sampleCount</span></code> | <code class="docutils literal notranslate"><span class="pre">maximum</span></code> | <code class="docutils literal notranslate"><span class="pre">minimum</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The value that the specified statistic is compared to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unit for a given metric. Valid Values: <code class="docutils literal notranslate"><span class="pre">seconds</span></code> | <code class="docutils literal notranslate"><span class="pre">microseconds</span></code> | <code class="docutils literal notranslate"><span class="pre">milliseconds</span></code> | <code class="docutils literal notranslate"><span class="pre">bytes</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobytes</span></code> | <code class="docutils literal notranslate"><span class="pre">megabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">terabytes</span></code> | <code class="docutils literal notranslate"><span class="pre">bits</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobits</span></code> | <code class="docutils literal notranslate"><span class="pre">megabits</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabits</span></code> | <code class="docutils literal notranslate"><span class="pre">terabits</span></code> | <code class="docutils literal notranslate"><span class="pre">percent</span></code> | <code class="docutils literal notranslate"><span class="pre">count</span></code> | <code class="docutils literal notranslate"><span class="pre">bytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">megabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">terabytes/second</span></code> | <code class="docutils literal notranslate"><span class="pre">bits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">kilobits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">megabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">gigabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">terabits/second</span></code> | <code class="docutils literal notranslate"><span class="pre">count/second</span></code> | <code class="docutils literal notranslate"><span class="pre">none</span></code></p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.aws.MrScalar.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.aws.MrScalar.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.aws.MrScalar.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.aws.MrScalar.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.aws.Ocean">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.aws.</code><code class="sig-name descname">Ocean</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">associate_public_ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">autoscaler</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blacklists</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">controller_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">desired_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">draining_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_optimized</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fallback_to_ondemand</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grace_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iam_instance_profile</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_volume_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_tasks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_percentage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">utilize_reserved_instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">whitelists</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.aws.Ocean" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Spotinst Ocean AWS resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_spotinst</span> <span class="k">as</span> <span class="nn">spotinst</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">spotinst</span><span class="o">.</span><span class="n">aws</span><span class="o">.</span><span class="n">Ocean</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">associate_public_ip_address</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">controller_id</span><span class="o">=</span><span class="s2">&quot;fakeClusterId&quot;</span><span class="p">,</span>
    <span class="n">desired_capacity</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">draining_timeout</span><span class="o">=</span><span class="mi">120</span><span class="p">,</span>
    <span class="n">ebs_optimized</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">fallback_to_ondemand</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">grace_period</span><span class="o">=</span><span class="mi">600</span><span class="p">,</span>
    <span class="n">iam_instance_profile</span><span class="o">=</span><span class="s2">&quot;iam-profile&quot;</span><span class="p">,</span>
    <span class="n">image_id</span><span class="o">=</span><span class="s2">&quot;ami-123456&quot;</span><span class="p">,</span>
    <span class="n">key_name</span><span class="o">=</span><span class="s2">&quot;fake key&quot;</span><span class="p">,</span>
    <span class="n">load_balancers</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;arn&quot;</span><span class="p">:</span> <span class="s2">&quot;arn:aws:elasticloadbalancing:us-west-2:fake-arn&quot;</span><span class="p">,</span>
            <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;TARGET_GROUP&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;AntonK&quot;</span><span class="p">,</span>
            <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;CLASSIC&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">],</span>
    <span class="n">max_size</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">min_size</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">monitoring</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-west-2&quot;</span><span class="p">,</span>
    <span class="n">root_volume_size</span><span class="o">=</span><span class="mi">20</span><span class="p">,</span>
    <span class="n">security_groups</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;sg-987654321&quot;</span><span class="p">],</span>
    <span class="n">subnet_ids</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;subnet-123456789&quot;</span><span class="p">],</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;fakeKey&quot;</span><span class="p">,</span>
        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;fakeValue&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">user_data</span><span class="o">=</span><span class="s2">&quot;echo hello world&quot;</span><span class="p">,</span>
    <span class="n">utilize_reserved_instances</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">whitelists</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;t1.micro&quot;</span><span class="p">,</span>
        <span class="s2">&quot;m1.small&quot;</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaler</span></code> - (Optional) Describes the Ocean Kubernetes autoscaler.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscale_is_enabled</span></code> - (Optional, Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>) Enable the Ocean Kubernetes autoscaler.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscale_is_auto_config</span></code> - (Optional, Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>) Automatically configure and optimize headroom resources.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscale_cooldown</span></code> - (Optional, Default: <code class="docutils literal notranslate"><span class="pre">null</span></code>) Cooldown period between scaling actions.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">auto_headroom_percentage</span></code> - (Optional) Set the auto headroom percentage (a number in the range [0, 200]) which controls the percentage of headroom from the cluster. Relevant only when <code class="docutils literal notranslate"><span class="pre">isAutoConfig</span></code> toggled on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscale_headroom</span></code> - (Optional) Spare resource capacity management enabling fast assignment of Pods without waiting for new resources to launch.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cpu_per_unit</span></code> - (Optional) Optionally configure the number of CPUs to allocate the headroom. CPUs are denoted in millicores, where 1000 millicores = 1 vCPU.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gpu_per_unit</span></code> - (Optional) Optionally configure the number of GPUS to allocate the headroom.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memory_per_unit</span></code> - (Optional) Optionally configure the amount of memory (MB) to allocate the headroom.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">num_of_units</span></code> - (Optional) The number of units to retain as headroom, where each unit has the defined headroom CPU and memory.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscale_down</span></code> - (Optional) Auto Scaling scale down operations.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_scale_down_percentage</span></code> - (Optional) Would represent the maximum % to scale-down. Number between 1-100.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_limits</span></code> - (Optional) Optionally set upper and lower bounds on the resource usage of the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_vcpu</span></code> - (Optional) The maximum cpu in vCPU units that can be allocated to the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_memory_gib</span></code> - (Optional) The maximum memory in GiB units that can be allocated to the cluster.</p></li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p><span class="raw-html-m2r"><a id="update-policy"></a></span></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">update_policy</span></code> - (Optional)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">should_roll</span></code> - (Required) Enables the roll.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">roll_config</span></code> - (Required) While used, you can control whether the group should perform a deployment after an update to the configuration.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">batch_size_percentage</span></code> - (Required) Sets the percentage of the instances to deploy in each batch.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p><span class="raw-html-m2r"><a id="scheduled-task"></a></span></p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">scheduled_task</span></code> - (Optional) Set scheduling object.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">shutdown_hours</span></code> - (Optional) Set shutdown hours for cluster object.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">is_enabled</span></code> - (Optional)  Flag to enable / disable the shutdown hours.
.. code-block:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">Example</span><span class="p">:</span> <span class="kc">True</span>
</pre></div>
</div>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">time_windows</span></code> - (Required) Set time windows for shutdown hours. specify a list of ‘timeWindows’ with at least one time window Each string is in the format of - ddd:hh:mm-ddd:hh:mm ddd = day of week = Sun | Mon | Tue | Wed | Thu | Fri | Sat hh = hour 24 = 0 -23 mm = minute = 0 - 59. Time windows should not overlap. required on cluster.scheduling.isEnabled = True. API Times are in UTC
.. code-block:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">Example</span><span class="p">:</span> <span class="n">Fri</span><span class="p">:</span><span class="mi">15</span><span class="p">:</span><span class="mi">30</span><span class="o">-</span><span class="n">Wed</span><span class="p">:</span><span class="mi">14</span><span class="p">:</span><span class="mi">30</span>
</pre></div>
</div>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tasks</span></code> - (Optional) The scheduling tasks for the cluster.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">is_enabled</span></code> - (Required)  Describes whether the task is enabled. When true the task should run when false it should not run. Required for cluster.scheduling.tasks object.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cron_expression</span></code> - (Required) A valid cron expression. For example : ” * * * * * “.The cron is running in UTC time zone and is in Unix cron format Cron Expression Validator Script. Only one of ‘frequency’ or ‘cronExpression’ should be used at a time. Required for cluster.scheduling.tasks object
.. code-block:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">Example</span><span class="p">:</span> <span class="mi">0</span> <span class="mi">1</span> <span class="o">*</span> <span class="o">*</span> <span class="o">*</span>
</pre></div>
</div>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">task_type</span></code> - (Required) Valid values: “clusterRoll”. Required for cluster.scheduling.tasks object
.. code-block:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">Example</span><span class="p">:</span> <span class="n">clusterRoll</span>
</pre></div>
</div>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>associate_public_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Configure public IP address allocation.</p></li>
<li><p><strong>blacklists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Instance types not allowed in the Ocean cluster. Cannot be configured if <code class="docutils literal notranslate"><span class="pre">whitelist</span></code> is configured.</p></li>
<li><p><strong>controller_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ocean cluster identifier. Example: <code class="docutils literal notranslate"><span class="pre">ocean.k8s</span></code></p></li>
<li><p><strong>desired_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of instances to launch and maintain in the cluster.</p></li>
<li><p><strong>draining_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time in seconds, the instance is allowed to run while detached from the ELB. This is to allow the instance time to be drained from incoming TCP connections before terminating it, during a scale down operation.</p></li>
<li><p><strong>ebs_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable EBS optimized for cluster. Flag will enable optimized capacity for high bandwidth connectivity to the EB service for non EBS optimized instance types. For instances that are EBS optimized this flag will be ignored.</p></li>
<li><p><strong>fallback_to_ondemand</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If not Spot instance markets are available, enable Ocean to launch On-Demand instances instead.</p></li>
<li><p><strong>grace_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time, in seconds, after the instance has launched to start checking its health.</p></li>
<li><p><strong>iam_instance_profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance profile iam role.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the image used to launch the instances.</p></li>
<li><p><strong>key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key pair to attach the instances.</p></li>
<li><p><strong>load_balancers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <ul>
<li><p>Array of load balancer objects to add to ocean cluster</p></li>
</ul>
</p></li>
<li><p><strong>max_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The upper limit of instances the cluster can scale up to.</p></li>
<li><p><strong>min_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The lower limit of instances the cluster can scale down to.</p></li>
<li><p><strong>monitoring</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable detailed monitoring for cluster. Flag will enable Cloud Watch detailed detailed monitoring (one minute increments). Note: there are additional hourly costs for this service based on the region used.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required if type is set to CLASSIC</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region the cluster will run in.</p></li>
<li><p><strong>root_volume_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size (in Gb) to allocate for the root volume. Minimum <code class="docutils literal notranslate"><span class="pre">20</span></code>.</p></li>
<li><p><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more security group ids.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A comma-separated list of subnet identifiers for the Ocean cluster. Subnet IDs should be configured with auto assign public ip.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Optionally adds tags to instances launched in an Ocean cluster.</p></li>
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base64-encoded MIME user data to make available to the instances.</p></li>
<li><p><strong>utilize_reserved_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If Reserved instances exist, Ocean will utilize them before launching Spot instances.</p></li>
<li><p><strong>whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Instance types allowed in the Ocean cluster. Cannot be configured if <code class="docutils literal notranslate"><span class="pre">blacklist</span></code> is configured.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>autoscaler</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoHeadroomPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleCooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleDown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxScaleDownPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleHeadroom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numOfUnits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleIsAutoConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleIsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceLimits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxMemoryGib</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxVcpu</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>load_balancers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Required if type is set to TARGET_GROUP</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Required if type is set to CLASSIC</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Can be set to CLASSIC or TARGET_GROUP</p></li>
</ul>
<p>The <strong>scheduled_tasks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">shutdownHours</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeWindows</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tasks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cronExpression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag value.</p></li>
</ul>
<p>The <strong>update_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rollConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">batchSizePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldRoll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Ocean.associate_public_ip_address">
<code class="sig-name descname">associate_public_ip_address</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.associate_public_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Configure public IP address allocation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Ocean.blacklists">
<code class="sig-name descname">blacklists</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.blacklists" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance types not allowed in the Ocean cluster. Cannot be configured if <code class="docutils literal notranslate"><span class="pre">whitelist</span></code> is configured.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Ocean.controller_id">
<code class="sig-name descname">controller_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.controller_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ocean cluster identifier. Example: <code class="docutils literal notranslate"><span class="pre">ocean.k8s</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Ocean.desired_capacity">
<code class="sig-name descname">desired_capacity</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.desired_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of instances to launch and maintain in the cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Ocean.draining_timeout">
<code class="sig-name descname">draining_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.draining_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time in seconds, the instance is allowed to run while detached from the ELB. This is to allow the instance time to be drained from incoming TCP connections before terminating it, during a scale down operation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Ocean.ebs_optimized">
<code class="sig-name descname">ebs_optimized</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.ebs_optimized" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable EBS optimized for cluster. Flag will enable optimized capacity for high bandwidth connectivity to the EB service for non EBS optimized instance types. For instances that are EBS optimized this flag will be ignored.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Ocean.fallback_to_ondemand">
<code class="sig-name descname">fallback_to_ondemand</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.fallback_to_ondemand" title="Permalink to this definition">¶</a></dt>
<dd><p>If not Spot instance markets are available, enable Ocean to launch On-Demand instances instead.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Ocean.grace_period">
<code class="sig-name descname">grace_period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.grace_period" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time, in seconds, after the instance has launched to start checking its health.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Ocean.iam_instance_profile">
<code class="sig-name descname">iam_instance_profile</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.iam_instance_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance profile iam role.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Ocean.image_id">
<code class="sig-name descname">image_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the image used to launch the instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Ocean.key_name">
<code class="sig-name descname">key_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The key pair to attach the instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Ocean.load_balancers">
<code class="sig-name descname">load_balancers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.load_balancers" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li><p>Array of load balancer objects to add to ocean cluster</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Required if type is set to TARGET_GROUP</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Required if type is set to CLASSIC</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Can be set to CLASSIC or TARGET_GROUP</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Ocean.max_size">
<code class="sig-name descname">max_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.max_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The upper limit of instances the cluster can scale up to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Ocean.min_size">
<code class="sig-name descname">min_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.min_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The lower limit of instances the cluster can scale down to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Ocean.monitoring">
<code class="sig-name descname">monitoring</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.monitoring" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable detailed monitoring for cluster. Flag will enable Cloud Watch detailed detailed monitoring (one minute increments). Note: there are additional hourly costs for this service based on the region used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Ocean.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Required if type is set to CLASSIC</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Ocean.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region the cluster will run in.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Ocean.root_volume_size">
<code class="sig-name descname">root_volume_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.root_volume_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size (in Gb) to allocate for the root volume. Minimum <code class="docutils literal notranslate"><span class="pre">20</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Ocean.security_groups">
<code class="sig-name descname">security_groups</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more security group ids.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Ocean.subnet_ids">
<code class="sig-name descname">subnet_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma-separated list of subnet identifiers for the Ocean cluster. Subnet IDs should be configured with auto assign public ip.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Ocean.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Optionally adds tags to instances launched in an Ocean cluster.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tag key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tag value.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Ocean.user_data">
<code class="sig-name descname">user_data</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64-encoded MIME user data to make available to the instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Ocean.utilize_reserved_instances">
<code class="sig-name descname">utilize_reserved_instances</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.utilize_reserved_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>If Reserved instances exist, Ocean will utilize them before launching Spot instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.Ocean.whitelists">
<code class="sig-name descname">whitelists</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.whitelists" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance types allowed in the Ocean cluster. Cannot be configured if <code class="docutils literal notranslate"><span class="pre">blacklist</span></code> is configured.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.aws.Ocean.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">associate_public_ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">autoscaler</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blacklists</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">controller_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">desired_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">draining_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_optimized</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fallback_to_ondemand</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grace_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iam_instance_profile</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_volume_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_tasks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_percentage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">utilize_reserved_instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">whitelists</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Ocean resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>associate_public_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Configure public IP address allocation.</p></li>
<li><p><strong>blacklists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Instance types not allowed in the Ocean cluster. Cannot be configured if <code class="docutils literal notranslate"><span class="pre">whitelist</span></code> is configured.</p></li>
<li><p><strong>controller_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ocean cluster identifier. Example: <code class="docutils literal notranslate"><span class="pre">ocean.k8s</span></code></p></li>
<li><p><strong>desired_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of instances to launch and maintain in the cluster.</p></li>
<li><p><strong>draining_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time in seconds, the instance is allowed to run while detached from the ELB. This is to allow the instance time to be drained from incoming TCP connections before terminating it, during a scale down operation.</p></li>
<li><p><strong>ebs_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable EBS optimized for cluster. Flag will enable optimized capacity for high bandwidth connectivity to the EB service for non EBS optimized instance types. For instances that are EBS optimized this flag will be ignored.</p></li>
<li><p><strong>fallback_to_ondemand</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If not Spot instance markets are available, enable Ocean to launch On-Demand instances instead.</p></li>
<li><p><strong>grace_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time, in seconds, after the instance has launched to start checking its health.</p></li>
<li><p><strong>iam_instance_profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance profile iam role.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the image used to launch the instances.</p></li>
<li><p><strong>key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key pair to attach the instances.</p></li>
<li><p><strong>load_balancers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <ul>
<li><p>Array of load balancer objects to add to ocean cluster</p></li>
</ul>
</p></li>
<li><p><strong>max_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The upper limit of instances the cluster can scale up to.</p></li>
<li><p><strong>min_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The lower limit of instances the cluster can scale down to.</p></li>
<li><p><strong>monitoring</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable detailed monitoring for cluster. Flag will enable Cloud Watch detailed detailed monitoring (one minute increments). Note: there are additional hourly costs for this service based on the region used.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required if type is set to CLASSIC</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region the cluster will run in.</p></li>
<li><p><strong>root_volume_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size (in Gb) to allocate for the root volume. Minimum <code class="docutils literal notranslate"><span class="pre">20</span></code>.</p></li>
<li><p><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more security group ids.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A comma-separated list of subnet identifiers for the Ocean cluster. Subnet IDs should be configured with auto assign public ip.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Optionally adds tags to instances launched in an Ocean cluster.</p></li>
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base64-encoded MIME user data to make available to the instances.</p></li>
<li><p><strong>utilize_reserved_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If Reserved instances exist, Ocean will utilize them before launching Spot instances.</p></li>
<li><p><strong>whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Instance types allowed in the Ocean cluster. Cannot be configured if <code class="docutils literal notranslate"><span class="pre">blacklist</span></code> is configured.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>autoscaler</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoHeadroomPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleCooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleDown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxScaleDownPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleHeadroom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numOfUnits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleIsAutoConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleIsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceLimits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxMemoryGib</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxVcpu</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>load_balancers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Required if type is set to TARGET_GROUP</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Required if type is set to CLASSIC</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Can be set to CLASSIC or TARGET_GROUP</p></li>
</ul>
<p>The <strong>scheduled_tasks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">shutdownHours</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeWindows</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tasks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cronExpression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag value.</p></li>
</ul>
<p>The <strong>update_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rollConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">batchSizePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldRoll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.aws.Ocean.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.aws.Ocean.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.aws.Ocean.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.aws.OceanLaunchSpec">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.aws.</code><code class="sig-name descname">OceanLaunchSpec</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">autoscale_headrooms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iam_instance_profile</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ocean_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_volume_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">taints</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.aws.OceanLaunchSpec" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a custom Spotinst Ocean AWS Launch Spec resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_spotinst</span> <span class="k">as</span> <span class="nn">spotinst</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">spotinst</span><span class="o">.</span><span class="n">aws</span><span class="o">.</span><span class="n">OceanLaunchSpec</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">autoscale_headrooms</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;cpuPerUnit&quot;</span><span class="p">:</span> <span class="mi">1000</span><span class="p">,</span>
        <span class="s2">&quot;gpuPerUnit&quot;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span>
        <span class="s2">&quot;memoryPerUnit&quot;</span><span class="p">:</span> <span class="mi">2048</span><span class="p">,</span>
        <span class="s2">&quot;numOfUnits&quot;</span><span class="p">:</span> <span class="mi">5</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">iam_instance_profile</span><span class="o">=</span><span class="s2">&quot;iam-profile&quot;</span><span class="p">,</span>
    <span class="n">image_id</span><span class="o">=</span><span class="s2">&quot;ami-123456&quot;</span><span class="p">,</span>
    <span class="n">labels</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;fakeKey&quot;</span><span class="p">,</span>
        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;fakeValue&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">ocean_id</span><span class="o">=</span><span class="s2">&quot;o-123456&quot;</span><span class="p">,</span>
    <span class="n">root_volume_size</span><span class="o">=</span><span class="mi">30</span><span class="p">,</span>
    <span class="n">security_groups</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;sg-987654321&quot;</span><span class="p">],</span>
    <span class="n">subnet_ids</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;subnet-1234&quot;</span><span class="p">],</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;Env&quot;</span><span class="p">,</span>
        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;production&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">taints</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;effect&quot;</span><span class="p">:</span> <span class="s2">&quot;NoExecute&quot;</span><span class="p">,</span>
        <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;taint key updated&quot;</span><span class="p">,</span>
        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;taint value updated&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">user_data</span><span class="o">=</span><span class="s2">&quot;echo hello world&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>autoscale_headrooms</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set custom headroom per launch spec. provide list of headrooms object.</p></li>
<li><p><strong>iam_instance_profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN or name of an IAM instance profile to associate with launched instances.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the image used to launch the instances.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Optionally adds labels to instances launched in an Ocean cluster.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set Launch Specification name</p></li>
<li><p><strong>ocean_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ocean cluster you wish to</p></li>
<li><p><strong>root_volume_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Set root volume size (in GB).</p></li>
<li><p><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Optionally adds security group IDs.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set subnets in launchSpec. Each element in array should be subnet ID.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A key/value mapping of tags to assign to the resource.</p></li>
<li><p><strong>taints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Optionally adds labels to instances launched in an Ocean cluster.</p></li>
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base64-encoded MIME user data to make available to the instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>autoscale_headrooms</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Optionally configure the number of CPUs to allocate for each headroom unit. CPUs are denoted in millicores, where 1000 millicores = 1 vCPU.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Optionally configure the number of GPUS to allocate for each headroom unit.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Optionally configure the amount of memory (MiB) to allocate for each headroom unit.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numOfUnits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of units to retain as headroom, where each unit has the defined headroom CPU, memory and GPU.</p></li>
</ul>
<p>The <strong>labels</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag value.</p></li>
</ul>
<p>The <strong>tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag value.</p></li>
</ul>
<p>The <strong>taints</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">effect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The effect of the taint. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;NoSchedule&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;PreferNoSchedule&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;NoExecute&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag value.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_spotinst.aws.OceanLaunchSpec.autoscale_headrooms">
<code class="sig-name descname">autoscale_headrooms</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.OceanLaunchSpec.autoscale_headrooms" title="Permalink to this definition">¶</a></dt>
<dd><p>Set custom headroom per launch spec. provide list of headrooms object.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Optionally configure the number of CPUs to allocate for each headroom unit. CPUs are denoted in millicores, where 1000 millicores = 1 vCPU.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Optionally configure the number of GPUS to allocate for each headroom unit.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Optionally configure the amount of memory (MiB) to allocate for each headroom unit.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numOfUnits</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of units to retain as headroom, where each unit has the defined headroom CPU, memory and GPU.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.OceanLaunchSpec.iam_instance_profile">
<code class="sig-name descname">iam_instance_profile</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.OceanLaunchSpec.iam_instance_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN or name of an IAM instance profile to associate with launched instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.OceanLaunchSpec.image_id">
<code class="sig-name descname">image_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.OceanLaunchSpec.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the image used to launch the instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.OceanLaunchSpec.labels">
<code class="sig-name descname">labels</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.OceanLaunchSpec.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>Optionally adds labels to instances launched in an Ocean cluster.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tag key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tag value.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.OceanLaunchSpec.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.OceanLaunchSpec.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Set Launch Specification name</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.OceanLaunchSpec.ocean_id">
<code class="sig-name descname">ocean_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.OceanLaunchSpec.ocean_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ocean cluster you wish to</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.OceanLaunchSpec.root_volume_size">
<code class="sig-name descname">root_volume_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.OceanLaunchSpec.root_volume_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Set root volume size (in GB).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.OceanLaunchSpec.security_groups">
<code class="sig-name descname">security_groups</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.OceanLaunchSpec.security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Optionally adds security group IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.OceanLaunchSpec.subnet_ids">
<code class="sig-name descname">subnet_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.OceanLaunchSpec.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Set subnets in launchSpec. Each element in array should be subnet ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.OceanLaunchSpec.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.OceanLaunchSpec.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A key/value mapping of tags to assign to the resource.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tag key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tag value.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.OceanLaunchSpec.taints">
<code class="sig-name descname">taints</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.OceanLaunchSpec.taints" title="Permalink to this definition">¶</a></dt>
<dd><p>Optionally adds labels to instances launched in an Ocean cluster.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">effect</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The effect of the taint. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;NoSchedule&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;PreferNoSchedule&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;NoExecute&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tag key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tag value.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.aws.OceanLaunchSpec.user_data">
<code class="sig-name descname">user_data</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.aws.OceanLaunchSpec.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64-encoded MIME user data to make available to the instances.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.aws.OceanLaunchSpec.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">autoscale_headrooms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iam_instance_profile</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ocean_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_volume_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">taints</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_data</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.aws.OceanLaunchSpec.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OceanLaunchSpec resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>autoscale_headrooms</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set custom headroom per launch spec. provide list of headrooms object.</p></li>
<li><p><strong>iam_instance_profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN or name of an IAM instance profile to associate with launched instances.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the image used to launch the instances.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Optionally adds labels to instances launched in an Ocean cluster.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set Launch Specification name</p></li>
<li><p><strong>ocean_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ocean cluster you wish to</p></li>
<li><p><strong>root_volume_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Set root volume size (in GB).</p></li>
<li><p><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Optionally adds security group IDs.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set subnets in launchSpec. Each element in array should be subnet ID.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A key/value mapping of tags to assign to the resource.</p></li>
<li><p><strong>taints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Optionally adds labels to instances launched in an Ocean cluster.</p></li>
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base64-encoded MIME user data to make available to the instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>autoscale_headrooms</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Optionally configure the number of CPUs to allocate for each headroom unit. CPUs are denoted in millicores, where 1000 millicores = 1 vCPU.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Optionally configure the number of GPUS to allocate for each headroom unit.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Optionally configure the amount of memory (MiB) to allocate for each headroom unit.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numOfUnits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of units to retain as headroom, where each unit has the defined headroom CPU, memory and GPU.</p></li>
</ul>
<p>The <strong>labels</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag value.</p></li>
</ul>
<p>The <strong>tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag value.</p></li>
</ul>
<p>The <strong>taints</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">effect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The effect of the taint. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;NoSchedule&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;PreferNoSchedule&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;NoExecute&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag value.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.aws.OceanLaunchSpec.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.aws.OceanLaunchSpec.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.aws.OceanLaunchSpec.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.aws.OceanLaunchSpec.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
