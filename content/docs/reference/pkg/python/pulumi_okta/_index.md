---
title: Package pulumi_okta
title_tag: Package pulumi_okta | Python SDK
linktitle: pulumi_okta
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "okta" >}}

<div class="section" id="pulumi-okta">
<h1>Pulumi Okta<a class="headerlink" href="#pulumi-okta" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-okta/issues">pulumi/pulumi-okta repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta/issues">terraform-providers/terraform-provider-okta repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_okta"></span><dl class="py class">
<dt id="pulumi_okta.EventHook">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.</code><code class="sig-name descname">EventHook</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth</span><span class="p">:</span> <span class="n">Union[EventHookAuthArgs, Mapping[str, Any], Awaitable[Union[EventHookAuthArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">channel</span><span class="p">:</span> <span class="n">Union[EventHookChannelArgs, Mapping[str, Any], Awaitable[Union[EventHookChannelArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">events</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">headers</span><span class="p">:</span> <span class="n">Union[List[Union[EventHookHeaderArgs, Mapping[str, Any], Awaitable[Union[EventHookHeaderArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[EventHookHeaderArgs, Mapping[str, Any], Awaitable[Union[EventHookHeaderArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.EventHook" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an event hook.</p>
<p>This resource allows you to create and configure an event hook.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_okta</span> <span class="k">as</span> <span class="nn">okta</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">okta</span><span class="o">.</span><span class="n">EventHook</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">auth</span><span class="o">=</span><span class="n">okta</span><span class="o">.</span><span class="n">EventHookAuthArgs</span><span class="p">(</span>
        <span class="n">key</span><span class="o">=</span><span class="s2">&quot;Authorization&quot;</span><span class="p">,</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;HEADER&quot;</span><span class="p">,</span>
        <span class="n">value</span><span class="o">=</span><span class="s2">&quot;123&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">channel</span><span class="o">=</span><span class="n">okta</span><span class="o">.</span><span class="n">EventHookChannelArgs</span><span class="p">(</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;HTTP&quot;</span><span class="p">,</span>
        <span class="n">uri</span><span class="o">=</span><span class="s2">&quot;https://example.com/test&quot;</span><span class="p">,</span>
        <span class="n">version</span><span class="o">=</span><span class="s2">&quot;1.0.0&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">events</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;user.lifecycle.create&quot;</span><span class="p">,</span>
        <span class="s2">&quot;user.lifecycle.delete.initiated&quot;</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'EventHookAuthArgs'</em><em>]</em><em>]</em>) – Authentication required for event hook request.</p></li>
<li><p><strong>channel</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'EventHookChannelArgs'</em><em>]</em><em>]</em>) – Details of the endpoint the event hook will hit.</p></li>
<li><p><strong>events</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The events that will be delivered to this hook. <a class="reference external" href="https://developer.okta.com/docs/reference/api/event-types/?q=event-hook-eligible">See here for a list of supported events</a>.</p></li>
<li><p><strong>headers</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'EventHookHeaderArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Map of headers to send along in event hook request.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The event hook display name.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_okta.EventHook.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth</span><span class="p">:</span> <span class="n">Union[EventHookAuthArgs, Mapping[str, Any], Awaitable[Union[EventHookAuthArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">channel</span><span class="p">:</span> <span class="n">Union[EventHookChannelArgs, Mapping[str, Any], Awaitable[Union[EventHookChannelArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">events</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">headers</span><span class="p">:</span> <span class="n">Union[List[Union[EventHookHeaderArgs, Mapping[str, Any], Awaitable[Union[EventHookHeaderArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[EventHookHeaderArgs, Mapping[str, Any], Awaitable[Union[EventHookHeaderArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_okta.event_hook.EventHook<a class="headerlink" href="#pulumi_okta.EventHook.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EventHook resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'EventHookAuthArgs'</em><em>]</em><em>]</em>) – Authentication required for event hook request.</p></li>
<li><p><strong>channel</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'EventHookChannelArgs'</em><em>]</em><em>]</em>) – Details of the endpoint the event hook will hit.</p></li>
<li><p><strong>events</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – <p>The events that will be delivered to this hook. <a class="reference external" href="https://developer.okta.com/docs/reference/api/event-types/?q=event-hook-eligible">See here for a list of supported events</a>.</p>
</p></li>
<li><p><strong>headers</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'EventHookHeaderArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Map of headers to send along in event hook request.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The event hook display name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.EventHook.auth">
<em class="property">property </em><code class="sig-name descname">auth</code><a class="headerlink" href="#pulumi_okta.EventHook.auth" title="Permalink to this definition">¶</a></dt>
<dd><p>Authentication required for event hook request.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.EventHook.channel">
<em class="property">property </em><code class="sig-name descname">channel</code><a class="headerlink" href="#pulumi_okta.EventHook.channel" title="Permalink to this definition">¶</a></dt>
<dd><p>Details of the endpoint the event hook will hit.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.EventHook.events">
<em class="property">property </em><code class="sig-name descname">events</code><a class="headerlink" href="#pulumi_okta.EventHook.events" title="Permalink to this definition">¶</a></dt>
<dd><p>The events that will be delivered to this hook. <a class="reference external" href="https://developer.okta.com/docs/reference/api/event-types/?q=event-hook-eligible">See here for a list of supported events</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.EventHook.headers">
<em class="property">property </em><code class="sig-name descname">headers</code><a class="headerlink" href="#pulumi_okta.EventHook.headers" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of headers to send along in event hook request.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.EventHook.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_okta.EventHook.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The event hook display name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.EventHook.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.EventHook.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.EventHook.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.EventHook.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backoff</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">base_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_retries</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_wait_seconds</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_wait_seconds</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">org_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parallelism</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the okta package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – API Token granting privileges to Okta API.</p></li>
<li><p><strong>backoff</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Use exponential back off strategy for rate limits.</p></li>
<li><p><strong>base_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Okta url. (Use ‘oktapreview.com’ for Okta testing)</p></li>
<li><p><strong>max_retries</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – maximum number of retries to attempt before erroring out.</p></li>
<li><p><strong>max_wait_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – maximum seconds to wait when rate limit is hit. We use exponential backoffs when backoff is enabled.</p></li>
<li><p><strong>min_wait_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – minimum seconds to wait when rate limit is hit. We use exponential backoffs when backoff is enabled.</p></li>
<li><p><strong>org_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The organization to manage in Okta.</p></li>
<li><p><strong>parallelism</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of concurrent requests to make within a resource where bulk operations are not possible. Take note of
<a class="reference external" href="https://developer.okta.com/docs/api/getting_started/rate-limits">https://developer.okta.com/docs/api/getting_started/rate-limits</a>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_okta.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.TemplateSms">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.</code><code class="sig-name descname">TemplateSms</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">translations</span><span class="p">:</span> <span class="n">Union[List[Union[TemplateSmsTranslationArgs, Mapping[str, Any], Awaitable[Union[TemplateSmsTranslationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[TemplateSmsTranslationArgs, Mapping[str, Any], Awaitable[Union[TemplateSmsTranslationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.TemplateSms" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Okta SMS Template.</p>
<p>This resource allows you to create and configure an Okta SMS Template.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_okta</span> <span class="k">as</span> <span class="nn">okta</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">okta</span><span class="o">.</span><span class="n">TemplateSms</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">template</span><span class="o">=</span><span class="sa">f</span><span class="s2">&quot;Your </span><span class="si">{</span><span class="n">org</span><span class="p">[</span><span class="s1">&#39;name&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2"> code is: </span><span class="si">{</span><span class="n">code</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span>
    <span class="n">translations</span><span class="o">=</span><span class="p">[</span>
        <span class="n">okta</span><span class="o">.</span><span class="n">TemplateSmsTranslationArgs</span><span class="p">(</span>
            <span class="n">language</span><span class="o">=</span><span class="s2">&quot;en&quot;</span><span class="p">,</span>
            <span class="n">template</span><span class="o">=</span><span class="sa">f</span><span class="s2">&quot;Your </span><span class="si">{</span><span class="n">org</span><span class="p">[</span><span class="s1">&#39;name&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2"> code is: </span><span class="si">{</span><span class="n">code</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">okta</span><span class="o">.</span><span class="n">TemplateSmsTranslationArgs</span><span class="p">(</span>
            <span class="n">language</span><span class="o">=</span><span class="s2">&quot;es&quot;</span><span class="p">,</span>
            <span class="n">template</span><span class="o">=</span><span class="sa">f</span><span class="s2">&quot;Tu código de </span><span class="si">{</span><span class="n">org</span><span class="p">[</span><span class="s1">&#39;name&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2"> es: </span><span class="si">{</span><span class="n">code</span><span class="si">}</span><span class="s2">.&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;SMS_VERIFY_CODE&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SMS message.</p></li>
<li><p><strong>translations</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TemplateSmsTranslationArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Set of translations for particular template.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SMS template type</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_okta.TemplateSms.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">translations</span><span class="p">:</span> <span class="n">Union[List[Union[TemplateSmsTranslationArgs, Mapping[str, Any], Awaitable[Union[TemplateSmsTranslationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[TemplateSmsTranslationArgs, Mapping[str, Any], Awaitable[Union[TemplateSmsTranslationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_okta.template_sms.TemplateSms<a class="headerlink" href="#pulumi_okta.TemplateSms.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TemplateSms resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SMS message.</p></li>
<li><p><strong>translations</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TemplateSmsTranslationArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Set of translations for particular template.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SMS template type</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.TemplateSms.template">
<em class="property">property </em><code class="sig-name descname">template</code><a class="headerlink" href="#pulumi_okta.TemplateSms.template" title="Permalink to this definition">¶</a></dt>
<dd><p>The SMS message.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.TemplateSms.translations">
<em class="property">property </em><code class="sig-name descname">translations</code><a class="headerlink" href="#pulumi_okta.TemplateSms.translations" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of translations for particular template.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.TemplateSms.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_okta.TemplateSms.type" title="Permalink to this definition">¶</a></dt>
<dd><p>SMS template type</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_okta.TemplateSms.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.TemplateSms.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.TemplateSms.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.TemplateSms.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
