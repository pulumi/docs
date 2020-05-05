---
title: Module fc
title_tag: Module fc | Package pulumi_alicloud | Python SDK
linktitle: fc
notitle: true
---

<div class="section" id="fc">
<h1>fc<a class="headerlink" href="#fc" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.fc"></span><dl class="py class">
<dt id="pulumi_alicloud.fc.AwaitableGetFunctionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.fc.</code><code class="sig-name descname">AwaitableGetFunctionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">functions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.fc.AwaitableGetFunctionsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.fc.AwaitableGetServicesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.fc.</code><code class="sig-name descname">AwaitableGetServicesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.fc.AwaitableGetServicesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.fc.AwaitableGetTriggersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.fc.</code><code class="sig-name descname">AwaitableGetTriggersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">function_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">triggers</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.fc.AwaitableGetTriggersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.fc.AwaitableGetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.fc.</code><code class="sig-name descname">AwaitableGetZonesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zones</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.fc.AwaitableGetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.fc.Function">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.fc.</code><code class="sig-name descname">Function</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">code_checksum</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">environment_variables</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filename</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">handler</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">memory_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oss_bucket</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oss_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">runtime</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.fc.Function" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Function resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] code_checksum: The checksum (crc64) of the function code.
:param pulumi.Input[str] description: The Function Compute function description.
:param pulumi.Input[dict] environment<em>variables: A map that defines environment variables for the function.
:param pulumi.Input[str] filename: The path to the function’s deployment package within the local filesystem. It is conflict with the `oss</em><code class="docutils literal notranslate"><span class="pre">-prefixed</span> <span class="pre">options.</span>
<span class="pre">:param</span> <span class="pre">pulumi.Input[str]</span> <span class="pre">handler:</span> <span class="pre">The</span> <span class="pre">function</span> <span class="pre">[entry</span> <span class="pre">point](https://www.alibabacloud.com/help/doc-detail/62213.htm)</span> <span class="pre">in</span> <span class="pre">your</span> <span class="pre">code.</span>
<span class="pre">:param</span> <span class="pre">pulumi.Input[float]</span> <span class="pre">memory_size:</span> <span class="pre">Amount</span> <span class="pre">of</span> <span class="pre">memory</span> <span class="pre">in</span> <span class="pre">MB</span> <span class="pre">your</span> <span class="pre">Function</span> <span class="pre">can</span> <span class="pre">use</span> <span class="pre">at</span> <span class="pre">runtime.</span> <span class="pre">Defaults</span> <span class="pre">to</span></code>128<code class="docutils literal notranslate"><span class="pre">.</span> <span class="pre">Limits</span> <span class="pre">to</span> <span class="pre">[128,</span> <span class="pre">3072].</span>
<span class="pre">:param</span> <span class="pre">pulumi.Input[str]</span> <span class="pre">name:</span> <span class="pre">The</span> <span class="pre">Function</span> <span class="pre">Compute</span> <span class="pre">function</span> <span class="pre">name.</span> <span class="pre">It</span> <span class="pre">is</span> <span class="pre">the</span> <span class="pre">only</span> <span class="pre">in</span> <span class="pre">one</span> <span class="pre">service</span> <span class="pre">and</span> <span class="pre">is</span> <span class="pre">conflict</span> <span class="pre">with</span> <span class="pre">&quot;name_prefix&quot;.</span>
<span class="pre">:param</span> <span class="pre">pulumi.Input[str]</span> <span class="pre">name_prefix:</span> <span class="pre">Setting</span> <span class="pre">a</span> <span class="pre">prefix</span> <span class="pre">to</span> <span class="pre">get</span> <span class="pre">a</span> <span class="pre">only</span> <span class="pre">function</span> <span class="pre">name.</span> <span class="pre">It</span> <span class="pre">is</span> <span class="pre">conflict</span> <span class="pre">with</span> <span class="pre">&quot;name&quot;.</span>
<span class="pre">:param</span> <span class="pre">pulumi.Input[str]</span> <span class="pre">oss_bucket:</span> <span class="pre">The</span> <span class="pre">OSS</span> <span class="pre">bucket</span> <span class="pre">location</span> <span class="pre">containing</span> <span class="pre">the</span> <span class="pre">function's</span> <span class="pre">deployment</span> <span class="pre">package.</span> <span class="pre">Conflicts</span> <span class="pre">with</span></code>filename<code class="docutils literal notranslate"><span class="pre">.</span> <span class="pre">This</span> <span class="pre">bucket</span> <span class="pre">must</span> <span class="pre">reside</span> <span class="pre">in</span> <span class="pre">the</span> <span class="pre">same</span> <span class="pre">Alibaba</span> <span class="pre">Cloud</span> <span class="pre">region</span> <span class="pre">where</span> <span class="pre">you</span> <span class="pre">are</span> <span class="pre">creating</span> <span class="pre">the</span> <span class="pre">function.</span>
<span class="pre">:param</span> <span class="pre">pulumi.Input[str]</span> <span class="pre">oss_key:</span> <span class="pre">The</span> <span class="pre">OSS</span> <span class="pre">key</span> <span class="pre">of</span> <span class="pre">an</span> <span class="pre">object</span> <span class="pre">containing</span> <span class="pre">the</span> <span class="pre">function's</span> <span class="pre">deployment</span> <span class="pre">package.</span> <span class="pre">Conflicts</span> <span class="pre">with</span></code>filename`.
:param pulumi.Input[str] runtime: See [Runtimes][<a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/52077.htm">https://www.alibabacloud.com/help/doc-detail/52077.htm</a>] for valid values.
:param pulumi.Input[str] service: The Function Compute service name.
:param pulumi.Input[float] timeout: The amount of time your Function has to run in seconds.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Function.code_checksum">
<code class="sig-name descname">code_checksum</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Function.code_checksum" title="Permalink to this definition">¶</a></dt>
<dd><p>The checksum (crc64) of the function code.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Function.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Function.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The Function Compute function description.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Function.environment_variables">
<code class="sig-name descname">environment_variables</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Function.environment_variables" title="Permalink to this definition">¶</a></dt>
<dd><p>A map that defines environment variables for the function.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Function.filename">
<code class="sig-name descname">filename</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Function.filename" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to the function’s deployment package within the local filesystem. It is conflict with the <code class="docutils literal notranslate"><span class="pre">oss_</span></code>-prefixed options.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Function.function_id">
<code class="sig-name descname">function_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Function.function_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Function Compute service ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Function.handler">
<code class="sig-name descname">handler</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Function.handler" title="Permalink to this definition">¶</a></dt>
<dd><p>The function <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/62213.htm">entry point</a> in your code.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Function.last_modified">
<code class="sig-name descname">last_modified</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Function.last_modified" title="Permalink to this definition">¶</a></dt>
<dd><p>The date this resource was last modified.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Function.memory_size">
<code class="sig-name descname">memory_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Function.memory_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Amount of memory in MB your Function can use at runtime. Defaults to <code class="docutils literal notranslate"><span class="pre">128</span></code>. Limits to [128, 3072].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Function.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Function.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Function Compute function name. It is the only in one service and is conflict with “name_prefix”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Function.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Function.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Setting a prefix to get a only function name. It is conflict with “name”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Function.oss_bucket">
<code class="sig-name descname">oss_bucket</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Function.oss_bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The OSS bucket location containing the function’s deployment package. Conflicts with <code class="docutils literal notranslate"><span class="pre">filename</span></code>. This bucket must reside in the same Alibaba Cloud region where you are creating the function.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Function.oss_key">
<code class="sig-name descname">oss_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Function.oss_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The OSS key of an object containing the function’s deployment package. Conflicts with <code class="docutils literal notranslate"><span class="pre">filename</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Function.runtime">
<code class="sig-name descname">runtime</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Function.runtime" title="Permalink to this definition">¶</a></dt>
<dd><p>See [Runtimes][<a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/52077.htm">https://www.alibabacloud.com/help/doc-detail/52077.htm</a>] for valid values.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Function.service">
<code class="sig-name descname">service</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Function.service" title="Permalink to this definition">¶</a></dt>
<dd><p>The Function Compute service name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Function.timeout">
<code class="sig-name descname">timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Function.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time your Function has to run in seconds.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.fc.Function.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">code_checksum</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">environment_variables</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filename</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">function_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">handler</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_modified</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">memory_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oss_bucket</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oss_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">runtime</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.fc.Function.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Function resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>code_checksum</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The checksum (crc64) of the function code.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Function Compute function description.</p></li>
<li><p><strong>environment*variables</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>A map that defines environment variables for the function.</p>
</p></li>
<li><p><strong>filename</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path to the function’s deployment package within the local filesystem. It is conflict with the <cite>oss*`</cite>-prefixed options.</p></li>
<li><p><strong>function_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Function Compute service ID.</p></li>
<li><p><strong>handler</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The function [entry point](<a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/62213.htm">https://www.alibabacloud.com/help/doc-detail/62213.htm</a>) in your code.</p></li>
<li><p><strong>last_modified</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date this resource was last modified.</p></li>
<li><p><strong>memory_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Amount of memory in MB your Function can use at runtime. Defaults to``128<a href="#id3"><span class="problematic" id="id4">``</span></a>. Limits to [128, 3072].</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Function Compute function name. It is the only in one service and is conflict with “name_prefix”.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Setting a prefix to get a only function name. It is conflict with “name”.</p></li>
<li><p><strong>oss_bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The OSS bucket location containing the function’s deployment package. Conflicts with``filename<a href="#id5"><span class="problematic" id="id6">``</span></a>. This bucket must reside in the same Alibaba Cloud region where you are creating the function.</p></li>
<li><p><strong>oss_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The OSS key of an object containing the function’s deployment package. Conflicts with``filename`.</p></li>
<li><p><strong>runtime</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – See [Runtimes][<a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/52077.htm">https://www.alibabacloud.com/help/doc-detail/52077.htm</a>] for valid values.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Function Compute service name.</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time your Function has to run in seconds.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.fc.Function.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.fc.Function.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.fc.Function.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.fc.Function.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.fc.GetFunctionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.fc.</code><code class="sig-name descname">GetFunctionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">functions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.fc.GetFunctionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getFunctions.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.fc.GetFunctionsResult.functions">
<code class="sig-name descname">functions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.GetFunctionsResult.functions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of functions. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.GetFunctionsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.GetFunctionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.GetFunctionsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.GetFunctionsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of functions ids.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.GetFunctionsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.GetFunctionsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of functions names.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.fc.GetServicesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.fc.</code><code class="sig-name descname">GetServicesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.fc.GetServicesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServices.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.fc.GetServicesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.GetServicesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.GetServicesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.GetServicesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of FC services ids.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.GetServicesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.GetServicesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of FC services names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.GetServicesResult.services">
<code class="sig-name descname">services</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.GetServicesResult.services" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of FC services. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.fc.GetTriggersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.fc.</code><code class="sig-name descname">GetTriggersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">function_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">triggers</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.fc.GetTriggersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTriggers.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.fc.GetTriggersResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.GetTriggersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.GetTriggersResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.GetTriggersResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of FC triggers ids.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.GetTriggersResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.GetTriggersResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of FC triggers names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.GetTriggersResult.triggers">
<code class="sig-name descname">triggers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.GetTriggersResult.triggers" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of FC triggers. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.fc.GetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.fc.</code><code class="sig-name descname">GetZonesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zones</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.fc.GetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getZones.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.fc.GetZonesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.GetZonesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.GetZonesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.GetZonesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of zone IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.GetZonesResult.zones">
<code class="sig-name descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.GetZonesResult.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of availability zones. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.fc.Service">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.fc.</code><code class="sig-name descname">Service</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet_access</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.fc.Service" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Service resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] description: The function compute service description.
:param pulumi.Input[bool] internet_access: Whether to allow the service to access Internet. Default to “true”.
:param pulumi.Input[dict] log_config: Provide this to store your FC service logs. Fields documented below. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/51924.htm">Create a Service</a>.
:param pulumi.Input[str] name: The Function Compute service name. It is the only in one Alicloud account and is conflict with “name_prefix”.
:param pulumi.Input[str] name_prefix: Setting a prefix to get a only name. It is conflict with “name”.
:param pulumi.Input[str] role: RAM role arn attached to the Function Compute service. This governs both who / what can invoke your Function, as well as what resources our Function has access to. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/52885.htm">User Permissions</a> for more details.
:param pulumi.Input[dict] vpc_config: Provide this to allow your FC service to access your VPC. Fields documented below. See <a class="reference external" href="https://www.alibabacloud.com/help/faq-detail/72959.htm">Function Compute Service in VPC</a>.</p>
<p>The <strong>log_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">logstore</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The log store name of Logs service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The project name of Logs service.</p></li>
</ul>
<p>The <strong>vpc_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A security group ID associated with the FC service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vswitch_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of vswitch IDs associated with the FC service.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Service.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Service.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The function compute service description.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Service.internet_access">
<code class="sig-name descname">internet_access</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Service.internet_access" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to allow the service to access Internet. Default to “true”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Service.last_modified">
<code class="sig-name descname">last_modified</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Service.last_modified" title="Permalink to this definition">¶</a></dt>
<dd><p>The date this resource was last modified.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Service.log_config">
<code class="sig-name descname">log_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Service.log_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Provide this to store your FC service logs. Fields documented below. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/51924.htm">Create a Service</a>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">logstore</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The log store name of Logs service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The project name of Logs service.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Service.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Service.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Function Compute service name. It is the only in one Alicloud account and is conflict with “name_prefix”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Service.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Service.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Setting a prefix to get a only name. It is conflict with “name”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Service.role">
<code class="sig-name descname">role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Service.role" title="Permalink to this definition">¶</a></dt>
<dd><p>RAM role arn attached to the Function Compute service. This governs both who / what can invoke your Function, as well as what resources our Function has access to. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/52885.htm">User Permissions</a> for more details.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Service.service_id">
<code class="sig-name descname">service_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Service.service_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Function Compute service ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Service.vpc_config">
<code class="sig-name descname">vpc_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Service.vpc_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Provide this to allow your FC service to access your VPC. Fields documented below. See <a class="reference external" href="https://www.alibabacloud.com/help/faq-detail/72959.htm">Function Compute Service in VPC</a>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A security group ID associated with the FC service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vswitch_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of vswitch IDs associated with the FC service.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.fc.Service.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet_access</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_modified</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_config</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.fc.Service.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Service resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The function compute service description.</p></li>
<li><p><strong>internet_access</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to allow the service to access Internet. Default to “true”.</p></li>
<li><p><strong>last_modified</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date this resource was last modified.</p></li>
<li><p><strong>log_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Provide this to store your FC service logs. Fields documented below. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/51924.htm">Create a Service</a>.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Function Compute service name. It is the only in one Alicloud account and is conflict with “name_prefix”.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Setting a prefix to get a only name. It is conflict with “name”.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>RAM role arn attached to the Function Compute service. This governs both who / what can invoke your Function, as well as what resources our Function has access to. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/52885.htm">User Permissions</a> for more details.</p>
</p></li>
<li><p><strong>service_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Function Compute service ID.</p></li>
<li><p><strong>vpc_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Provide this to allow your FC service to access your VPC. Fields documented below. See <a class="reference external" href="https://www.alibabacloud.com/help/faq-detail/72959.htm">Function Compute Service in VPC</a>.</p>
</p></li>
</ul>
</dd>
</dl>
<p>The <strong>log_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">logstore</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The log store name of Logs service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The project name of Logs service.</p></li>
</ul>
<p>The <strong>vpc_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A security group ID associated with the FC service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vswitch_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of vswitch IDs associated with the FC service.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.fc.Service.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.fc.Service.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.fc.Service.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.fc.Service.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.fc.Trigger">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.fc.</code><code class="sig-name descname">Trigger</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_mns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">function</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.fc.Trigger" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Trigger resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] config: The config of Function Compute trigger.It is valid when <code class="docutils literal notranslate"><span class="pre">type</span></code> is not “mns_topic”.See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/70140.htm">Configure triggers and events</a> for more details.
:param pulumi.Input[str] config_mns: The config of Function Compute trigger when the type is “mns_topic”.It is conflict with <code class="docutils literal notranslate"><span class="pre">config</span></code>.
:param pulumi.Input[str] function: The Function Compute function name.
:param pulumi.Input[str] name: The Function Compute trigger name. It is the only in one service and is conflict with “name_prefix”.
:param pulumi.Input[str] name_prefix: Setting a prefix to get a only trigger name. It is conflict with “name”.
:param pulumi.Input[str] role: RAM role arn attached to the Function Compute trigger. Role used by the event source to call the function. The value format is “acs:ram::$account-id:role/$role-name”. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/53102.htm">Create a trigger</a> for more details.
:param pulumi.Input[str] service: The Function Compute service name.
:param pulumi.Input[str] source_arn: Event source resource address. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/53102.htm">Create a trigger</a> for more details.
:param pulumi.Input[str] type: The Type of the trigger. Valid values: [“oss”, “log”, “timer”, “http”, “mns_topic”, “cdn_events”].</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Trigger.config">
<code class="sig-name descname">config</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Trigger.config" title="Permalink to this definition">¶</a></dt>
<dd><p>The config of Function Compute trigger.It is valid when <code class="docutils literal notranslate"><span class="pre">type</span></code> is not “mns_topic”.See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/70140.htm">Configure triggers and events</a> for more details.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Trigger.config_mns">
<code class="sig-name descname">config_mns</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Trigger.config_mns" title="Permalink to this definition">¶</a></dt>
<dd><p>The config of Function Compute trigger when the type is “mns_topic”.It is conflict with <code class="docutils literal notranslate"><span class="pre">config</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Trigger.function">
<code class="sig-name descname">function</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Trigger.function" title="Permalink to this definition">¶</a></dt>
<dd><p>The Function Compute function name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Trigger.last_modified">
<code class="sig-name descname">last_modified</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Trigger.last_modified" title="Permalink to this definition">¶</a></dt>
<dd><p>The date this resource was last modified.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Trigger.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Trigger.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Function Compute trigger name. It is the only in one service and is conflict with “name_prefix”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Trigger.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Trigger.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Setting a prefix to get a only trigger name. It is conflict with “name”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Trigger.role">
<code class="sig-name descname">role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Trigger.role" title="Permalink to this definition">¶</a></dt>
<dd><p>RAM role arn attached to the Function Compute trigger. Role used by the event source to call the function. The value format is “acs:ram::$account-id:role/$role-name”. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/53102.htm">Create a trigger</a> for more details.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Trigger.service">
<code class="sig-name descname">service</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Trigger.service" title="Permalink to this definition">¶</a></dt>
<dd><p>The Function Compute service name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Trigger.source_arn">
<code class="sig-name descname">source_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Trigger.source_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Event source resource address. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/53102.htm">Create a trigger</a> for more details.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Trigger.trigger_id">
<code class="sig-name descname">trigger_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Trigger.trigger_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Function Compute trigger ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.fc.Trigger.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.fc.Trigger.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Type of the trigger. Valid values: [“oss”, “log”, “timer”, “http”, “mns_topic”, “cdn_events”].</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.fc.Trigger.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_mns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">function</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_modified</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">trigger_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.fc.Trigger.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Trigger resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The config of Function Compute trigger.It is valid when <code class="docutils literal notranslate"><span class="pre">type</span></code> is not “mns_topic”.See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/70140.htm">Configure triggers and events</a> for more details.</p>
</p></li>
<li><p><strong>config_mns</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The config of Function Compute trigger when the type is “mns_topic”.It is conflict with <code class="docutils literal notranslate"><span class="pre">config</span></code>.</p></li>
<li><p><strong>function</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Function Compute function name.</p></li>
<li><p><strong>last_modified</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date this resource was last modified.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Function Compute trigger name. It is the only in one service and is conflict with “name_prefix”.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Setting a prefix to get a only trigger name. It is conflict with “name”.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>RAM role arn attached to the Function Compute trigger. Role used by the event source to call the function. The value format is “acs:ram::$account-id:role/$role-name”. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/53102.htm">Create a trigger</a> for more details.</p>
</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Function Compute service name.</p></li>
<li><p><strong>source_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Event source resource address. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/53102.htm">Create a trigger</a> for more details.</p>
</p></li>
<li><p><strong>trigger_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Function Compute trigger ID.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Type of the trigger. Valid values: [“oss”, “log”, “timer”, “http”, “mns_topic”, “cdn_events”].</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.fc.Trigger.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.fc.Trigger.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.fc.Trigger.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.fc.Trigger.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.fc.get_functions">
<code class="sig-prename descclassname">pulumi_alicloud.fc.</code><code class="sig-name descname">get_functions</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.fc.get_functions" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the Function Compute functions of the current Alibaba Cloud user.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – <ul>
<li><p>A list of functions ids.</p></li>
</ul>
</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by function name.</p></li>
<li><p><strong>service_name</strong> (<em>str</em>) – Name of the service that contains the functions to find.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.fc.get_services">
<code class="sig-prename descclassname">pulumi_alicloud.fc.</code><code class="sig-name descname">get_services</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.fc.get_services" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the Function Compute services of the current Alibaba Cloud user.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – <ul>
<li><p>A list of FC services ids.</p></li>
</ul>
</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by FC service name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.fc.get_triggers">
<code class="sig-prename descclassname">pulumi_alicloud.fc.</code><code class="sig-name descname">get_triggers</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">function_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.fc.get_triggers" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the Function Compute triggers of the current Alibaba Cloud user.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>function_name</strong> (<em>str</em>) – FC function name.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – <ul>
<li><p>A list of FC triggers ids.</p></li>
</ul>
</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by FC trigger name.</p></li>
<li><p><strong>service_name</strong> (<em>str</em>) – FC service name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.fc.get_zones">
<code class="sig-prename descclassname">pulumi_alicloud.fc.</code><code class="sig-name descname">get_zones</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.fc.get_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides availability zones for FunctionCompute that can be accessed by an Alibaba Cloud account within the region configured in the provider.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.74.0+.</p>
</div></blockquote>
</dd></dl>

</div>
