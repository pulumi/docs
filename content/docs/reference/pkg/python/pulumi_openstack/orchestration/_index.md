---
title: Module orchestration
title_tag: Module orchestration | Package pulumi_openstack | Python SDK
linktitle: orchestration
notitle: true
---

<div class="section" id="orchestration">
<h1>orchestration<a class="headerlink" href="#orchestration" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-openstack/issues">pulumi/pulumi-openstack repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/issues">terraform-providers/terraform-provider-openstack repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_openstack.orchestration"></span><dl class="py class">
<dt id="pulumi_openstack.orchestration.StackV1">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.orchestration.</code><code class="sig-name descname">StackV1</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">capabilities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creation_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable_rollback</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">environment_opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_topics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">outputs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status_reason</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.orchestration.StackV1" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>Manages a V1 stack resource within OpenStack.

## Example Usage



```python
import pulumi
import pulumi_openstack as openstack

stack1 = openstack.orchestration.StackV1(&quot;stack1&quot;,
    disable_rollback=True,
    environment_opts={
        &quot;Bin&quot;: &quot;
</pre></div>
</div>
<dl>
<dt>“,</dt><dd><blockquote>
<div><p>},
parameters={</p>
<blockquote>
<div><p>“length”: 4,</p>
</div></blockquote>
<p>},
template_opts={</p>
<blockquote>
<div><p>“Bin”: “””heat_template_version: 2013-05-23</p>
</div></blockquote>
</div></blockquote>
<dl>
<dt>parameters:</dt><dd><dl class="simple">
<dt>length:</dt><dd><p>type: number</p>
</dd>
</dl>
</dd>
<dt>resources:</dt><dd><dl>
<dt>test_res:</dt><dd><p>type: OS::Heat::TestResource</p>
</dd>
<dt>random:</dt><dd><p>type: OS::Heat::RandomString
properties:</p>
<blockquote>
<div><p>length: {get_param: length}</p>
</div></blockquote>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="s2">&quot;&quot;&quot;,</span>
<span class="s2">    },</span>
<span class="s2">    timeout=30)</span>
<span class="s2">```</span>


<span class="s2">:param str resource_name: The name of the resource.</span>
<span class="s2">:param pulumi.ResourceOptions opts: Options for the resource.</span>
<span class="s2">:param pulumi.Input[list] capabilities: List of stack capabilities for stack.</span>
<span class="s2">:param pulumi.Input[str] creation_time: The date and time when the resource was created. The date</span>
<span class="s2">       and time stamp format is ISO 8601: CCYY-MM-DDThh:mm:ss±hh:mm</span>
<span class="s2">       For example, 2015-08-27T09:49:58-05:00. The ±hh:mm value, if included,</span>
<span class="s2">       is the time zone as an offset from UTC.</span>
<span class="s2">:param pulumi.Input[str] description: The description of the stack resource.</span>
<span class="s2">:param pulumi.Input[bool] disable_rollback: Enables or disables deletion of all stack</span>
<span class="s2">       resources when a stack creation fails. Default is true, meaning all</span>
<span class="s2">       resources are not deleted when stack creation fails.</span>
<span class="s2">:param pulumi.Input[dict] environment_opts: Environment key/value pairs to associate with</span>
<span class="s2">       the stack which contains details for the environment of the stack.</span>
<span class="s2">       Allowed keys: Bin, URL, Files. Changing this updates the existing stack</span>
<span class="s2">       Environment Opts.</span>
<span class="s2">:param pulumi.Input[str] name: A unique name for the stack. It must start with an</span>
<span class="s2">       alphabetic character. Changing this updates the stack&#39;s name.</span>
<span class="s2">:param pulumi.Input[list] notification_topics: List of notification topics for stack.</span>
<span class="s2">:param pulumi.Input[list] outputs: A list of stack outputs.</span>
<span class="s2">:param pulumi.Input[dict] parameters: User-defined key/value pairs as parameters to pass</span>
<span class="s2">       to the template. Changing this updates the existing stack parameters.</span>
<span class="s2">:param pulumi.Input[str] region: The region in which to create the stack. If</span>
<span class="s2">       omitted, the `region` argument of the provider is used. Changing this</span>
<span class="s2">       creates a new stack.</span>
<span class="s2">:param pulumi.Input[str] status: The status of the stack.</span>
<span class="s2">:param pulumi.Input[str] status_reason: The reason for the current status of the stack.</span>
<span class="s2">:param pulumi.Input[list] tags: A list of tags to assosciate with the Stack</span>
<span class="s2">:param pulumi.Input[str] template_description: The description of the stack template.</span>
<span class="s2">:param pulumi.Input[dict] template_opts: Template key/value pairs to associate with the</span>
<span class="s2">       stack which contains either the template file or url.</span>
<span class="s2">       Allowed keys: Bin, URL, Files. Changing this updates the existing stack</span>
<span class="s2">       Template Opts.</span>
<span class="s2">:param pulumi.Input[float] timeout: The timeout for stack action in minutes.</span>
<span class="s2">:param pulumi.Input[str] updated_time: The date and time when the resource was updated. The date</span>
<span class="s2">       and time stamp format is ISO 8601: CCYY-MM-DDThh:mm:ss±hh:mm</span>
<span class="s2">       For example, 2015-08-27T09:49:58-05:00. The ±hh:mm value, if included,</span>
<span class="s2">       is the time zone as an offset from UTC.</span>

<span class="s2">The **outputs** object supports the following:</span>

<span class="s2">  * `description` (`pulumi.Input[str]`) - The description of the stack resource.</span>
<span class="s2">  * `outputKey` (`pulumi.Input[str]`)</span>
<span class="s2">  * `outputValue` (`pulumi.Input[str]`)</span>
</pre></div>
</div>
<dl class="py attribute">
<dt id="pulumi_openstack.orchestration.StackV1.capabilities">
<code class="sig-name descname">capabilities</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.orchestration.StackV1.capabilities" title="Permalink to this definition">¶</a></dt>
<dd><p>List of stack capabilities for stack.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.orchestration.StackV1.creation_time">
<code class="sig-name descname">creation_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.orchestration.StackV1.creation_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time when the resource was created. The date
and time stamp format is ISO 8601: CCYY-MM-DDThh:mm:ss±hh:mm
For example, 2015-08-27T09:49:58-05:00. The ±hh:mm value, if included,
is the time zone as an offset from UTC.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.orchestration.StackV1.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.orchestration.StackV1.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the stack resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.orchestration.StackV1.disable_rollback">
<code class="sig-name descname">disable_rollback</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.orchestration.StackV1.disable_rollback" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables or disables deletion of all stack
resources when a stack creation fails. Default is true, meaning all
resources are not deleted when stack creation fails.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.orchestration.StackV1.environment_opts">
<code class="sig-name descname">environment_opts</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.orchestration.StackV1.environment_opts" title="Permalink to this definition">¶</a></dt>
<dd><p>Environment key/value pairs to associate with
the stack which contains details for the environment of the stack.
Allowed keys: Bin, URL, Files. Changing this updates the existing stack
Environment Opts.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.orchestration.StackV1.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.orchestration.StackV1.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the stack. It must start with an
alphabetic character. Changing this updates the stack’s name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.orchestration.StackV1.notification_topics">
<code class="sig-name descname">notification_topics</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.orchestration.StackV1.notification_topics" title="Permalink to this definition">¶</a></dt>
<dd><p>List of notification topics for stack.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.orchestration.StackV1.outputs">
<code class="sig-name descname">outputs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.orchestration.StackV1.outputs" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of stack outputs.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The description of the stack resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">outputKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">outputValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.orchestration.StackV1.parameters">
<code class="sig-name descname">parameters</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.orchestration.StackV1.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>User-defined key/value pairs as parameters to pass
to the template. Changing this updates the existing stack parameters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.orchestration.StackV1.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.orchestration.StackV1.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to create the stack. If
omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new stack.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.orchestration.StackV1.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.orchestration.StackV1.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the stack.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.orchestration.StackV1.status_reason">
<code class="sig-name descname">status_reason</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.orchestration.StackV1.status_reason" title="Permalink to this definition">¶</a></dt>
<dd><p>The reason for the current status of the stack.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.orchestration.StackV1.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.orchestration.StackV1.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags to assosciate with the Stack</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.orchestration.StackV1.template_description">
<code class="sig-name descname">template_description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.orchestration.StackV1.template_description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the stack template.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.orchestration.StackV1.template_opts">
<code class="sig-name descname">template_opts</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.orchestration.StackV1.template_opts" title="Permalink to this definition">¶</a></dt>
<dd><p>Template key/value pairs to associate with the
stack which contains either the template file or url.
Allowed keys: Bin, URL, Files. Changing this updates the existing stack
Template Opts.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.orchestration.StackV1.timeout">
<code class="sig-name descname">timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.orchestration.StackV1.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The timeout for stack action in minutes.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.orchestration.StackV1.updated_time">
<code class="sig-name descname">updated_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.orchestration.StackV1.updated_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time when the resource was updated. The date
and time stamp format is ISO 8601: CCYY-MM-DDThh:mm:ss±hh:mm
For example, 2015-08-27T09:49:58-05:00. The ±hh:mm value, if included,
is the time zone as an offset from UTC.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.orchestration.StackV1.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">capabilities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creation_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable_rollback</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">environment_opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_topics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">outputs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status_reason</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated_time</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.orchestration.StackV1.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing StackV1 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>capabilities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of stack capabilities for stack.</p></li>
<li><p><strong>creation_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date and time when the resource was created. The date
and time stamp format is ISO 8601: CCYY-MM-DDThh:mm:ss±hh:mm
For example, 2015-08-27T09:49:58-05:00. The ±hh:mm value, if included,
is the time zone as an offset from UTC.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the stack resource.</p></li>
<li><p><strong>disable_rollback</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables or disables deletion of all stack
resources when a stack creation fails. Default is true, meaning all
resources are not deleted when stack creation fails.</p></li>
<li><p><strong>environment_opts</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Environment key/value pairs to associate with
the stack which contains details for the environment of the stack.
Allowed keys: Bin, URL, Files. Changing this updates the existing stack
Environment Opts.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the stack. It must start with an
alphabetic character. Changing this updates the stack’s name.</p></li>
<li><p><strong>notification_topics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of notification topics for stack.</p></li>
<li><p><strong>outputs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of stack outputs.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – User-defined key/value pairs as parameters to pass
to the template. Changing this updates the existing stack parameters.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to create the stack. If
omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new stack.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the stack.</p></li>
<li><p><strong>status_reason</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The reason for the current status of the stack.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tags to assosciate with the Stack</p></li>
<li><p><strong>template_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the stack template.</p></li>
<li><p><strong>template_opts</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Template key/value pairs to associate with the
stack which contains either the template file or url.
Allowed keys: Bin, URL, Files. Changing this updates the existing stack
Template Opts.</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The timeout for stack action in minutes.</p></li>
<li><p><strong>updated_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date and time when the resource was updated. The date
and time stamp format is ISO 8601: CCYY-MM-DDThh:mm:ss±hh:mm
For example, 2015-08-27T09:49:58-05:00. The ±hh:mm value, if included,
is the time zone as an offset from UTC.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>outputs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of the stack resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">outputKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">outputValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.orchestration.StackV1.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.orchestration.StackV1.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.orchestration.StackV1.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.orchestration.StackV1.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
