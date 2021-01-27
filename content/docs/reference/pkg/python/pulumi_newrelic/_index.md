---
title: Package pulumi_newrelic
title_tag: Package pulumi_newrelic | Python SDK
linktitle: pulumi_newrelic
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "newrelic" >}}

<div class="section" id="pulumi-newrelic">
<h1>Pulumi NewRelic<a class="headerlink" href="#pulumi-newrelic" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-newrelic">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-newrelic/issues">pulumi/pulumi-newrelic repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-newrelic/issues">terraform-providers/terraform-provider-newrelic repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_newrelic"></span><dl class="py class">
<dt id="pulumi_newrelic.AlertChannel">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">AlertChannel</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>AlertChannelConfigArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>AlertChannelConfigArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AlertChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to create and manage New Relic alert channels.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannel</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannelConfigArgs</span><span class="p">(</span>
        <span class="n">include_json_attachment</span><span class="o">=</span><span class="s2">&quot;1&quot;</span><span class="p">,</span>
        <span class="n">recipients</span><span class="o">=</span><span class="s2">&quot;foo@example.com&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;email&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannel</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannelConfigArgs</span><span class="p">(</span>
        <span class="n">channel</span><span class="o">=</span><span class="s2">&quot;example-alerts-channel&quot;</span><span class="p">,</span>
        <span class="n">url</span><span class="o">=</span><span class="s2">&quot;https://hooks.slack.com/services/XXXXXXX/XXXXXXX/XXXXXXXXXX&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;slack&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannel</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannelConfigArgs</span><span class="p">(</span>
        <span class="n">api_key</span><span class="o">=</span><span class="s2">&quot;abc123&quot;</span><span class="p">,</span>
        <span class="n">recipients</span><span class="o">=</span><span class="s2">&quot;user1@domain.com, user2@domain.com&quot;</span><span class="p">,</span>
        <span class="n">tags</span><span class="o">=</span><span class="s2">&quot;tag1, tag2&quot;</span><span class="p">,</span>
        <span class="n">teams</span><span class="o">=</span><span class="s2">&quot;team1, team2&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;opsgenie&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannel</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannelConfigArgs</span><span class="p">(</span>
        <span class="n">service_key</span><span class="o">=</span><span class="s2">&quot;abc123&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;pagerduty&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannel</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannelConfigArgs</span><span class="p">(</span>
        <span class="n">key</span><span class="o">=</span><span class="s2">&quot;abc123&quot;</span><span class="p">,</span>
        <span class="n">route_key</span><span class="o">=</span><span class="s2">&quot;/example&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;victorops&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannel</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;webhook&quot;</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannelConfigArgs</span><span class="p">(</span>
        <span class="n">base_url</span><span class="o">=</span><span class="s2">&quot;http://www.test.com&quot;</span><span class="p">,</span>
        <span class="n">payload_type</span><span class="o">=</span><span class="s2">&quot;application/json&quot;</span><span class="p">,</span>
        <span class="n">payload</span><span class="o">=</span><span class="p">{</span>
            <span class="s2">&quot;condition_name&quot;</span><span class="p">:</span> <span class="s2">&quot;$CONDITION_NAME&quot;</span><span class="p">,</span>
            <span class="s2">&quot;policy_name&quot;</span><span class="p">:</span> <span class="s2">&quot;$POLICY_NAME&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="n">headers</span><span class="o">=</span><span class="p">{</span>
            <span class="s2">&quot;header1&quot;</span><span class="p">:</span> <span class="n">value1</span><span class="p">,</span>
            <span class="s2">&quot;header2&quot;</span><span class="p">:</span> <span class="n">value2</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">))</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannel</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannelConfigArgs</span><span class="p">(</span>
        <span class="n">base_url</span><span class="o">=</span><span class="s2">&quot;http://www.test.com&quot;</span><span class="p">,</span>
        <span class="n">payload_string</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">  &quot;my_custom_values&quot;: {</span>
<span class="s2">    &quot;condition_name&quot;: &quot;$CONDITION_NAME&quot;,</span>
<span class="s2">    &quot;policy_name&quot;: &quot;$POLICY_NAME&quot;</span>
<span class="s2">  }</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
        <span class="n">payload_type</span><span class="o">=</span><span class="s2">&quot;application/json&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;webhook&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Alert channels can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g. bash</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import newrelic:index/alertChannel:AlertChannel main &lt;id&gt;
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AlertChannelConfigArgs'</em><em>]</em><em>]</em>) – A nested block that describes an alert channel configuration.  Only one config block is permitted per alert channel definition.  See Nested config blocks below for details.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the channel.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of channel.  Accepted values are ‘email’, ‘slack’, ‘opsgenie’, ‘pagerduty’, ‘victorops’, or ‘webhook’.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_newrelic.AlertChannel.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>AlertChannelConfigArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>AlertChannelConfigArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_newrelic.AlertChannel" title="pulumi_newrelic.AlertChannel">AlertChannel</a><a class="headerlink" href="#pulumi_newrelic.AlertChannel.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AlertChannel resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AlertChannelConfigArgs'</em><em>]</em><em>]</em>) – A nested block that describes an alert channel configuration.  Only one config block is permitted per alert channel definition.  See Nested config blocks below for details.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the channel.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of channel.  Accepted values are ‘email’, ‘slack’, ‘opsgenie’, ‘pagerduty’, ‘victorops’, or ‘webhook’.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertChannel.config">
<em class="property">property </em><code class="sig-name descname">config</code><a class="headerlink" href="#pulumi_newrelic.AlertChannel.config" title="Permalink to this definition">¶</a></dt>
<dd><p>A nested block that describes an alert channel configuration.  Only one config block is permitted per alert channel definition.  See Nested config blocks below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertChannel.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_newrelic.AlertChannel.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the channel.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertChannel.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_newrelic.AlertChannel.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of channel.  Accepted values are ‘email’, ‘slack’, ‘opsgenie’, ‘pagerduty’, ‘victorops’, or ‘webhook’.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertChannel.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AlertChannel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.AlertChannel.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AlertChannel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.AlertCondition">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">AlertCondition</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition_scope</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entities</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gc_metric</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">runbook_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">terms</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>AlertConditionTermArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>AlertConditionTermArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>AlertConditionTermArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>AlertConditionTermArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_defined_metric</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_defined_value_function</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">violation_close_timer</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AlertCondition" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to create and manage alert conditions for APM, Browser, and Mobile in New Relic.</p>
<blockquote>
<div><p><strong>NOTE:</strong> The NrqlAlertCondition resource is preferred for configuring alerts conditions. In most cases feature parity can be achieved with a NRQL query. Other condition types may be deprecated in the future and receive fewer product updates.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">app</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">get_entity</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;my-app&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;APPLICATION&quot;</span><span class="p">,</span>
    <span class="n">domain</span><span class="o">=</span><span class="s2">&quot;APM&quot;</span><span class="p">)</span>
<span class="n">foo_alert_policy</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertPolicy</span><span class="p">(</span><span class="s2">&quot;fooAlertPolicy&quot;</span><span class="p">)</span>
<span class="n">foo_alert_condition</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertCondition</span><span class="p">(</span><span class="s2">&quot;fooAlertCondition&quot;</span><span class="p">,</span>
    <span class="n">policy_id</span><span class="o">=</span><span class="n">foo_alert_policy</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;apm_app_metric&quot;</span><span class="p">,</span>
    <span class="n">entities</span><span class="o">=</span><span class="p">[</span><span class="n">app</span><span class="o">.</span><span class="n">application_id</span><span class="p">],</span>
    <span class="n">metric</span><span class="o">=</span><span class="s2">&quot;apdex&quot;</span><span class="p">,</span>
    <span class="n">runbook_url</span><span class="o">=</span><span class="s2">&quot;https://www.example.com&quot;</span><span class="p">,</span>
    <span class="n">condition_scope</span><span class="o">=</span><span class="s2">&quot;application&quot;</span><span class="p">,</span>
    <span class="n">terms</span><span class="o">=</span><span class="p">[</span><span class="n">newrelic</span><span class="o">.</span><span class="n">AlertConditionTermArgs</span><span class="p">(</span>
        <span class="n">duration</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
        <span class="n">operator</span><span class="o">=</span><span class="s2">&quot;below&quot;</span><span class="p">,</span>
        <span class="n">priority</span><span class="o">=</span><span class="s2">&quot;critical&quot;</span><span class="p">,</span>
        <span class="n">threshold</span><span class="o">=</span><span class="mf">0.75</span><span class="p">,</span>
        <span class="n">time_function</span><span class="o">=</span><span class="s2">&quot;all&quot;</span><span class="p">,</span>
    <span class="p">)])</span>
</pre></div>
</div>
<p>The <code class="docutils literal notranslate"><span class="pre">term</span></code> mapping supports the following arguments:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> - (Required) In minutes, must be in the range of <code class="docutils literal notranslate"><span class="pre">5</span></code> to <code class="docutils literal notranslate"><span class="pre">120</span></code>, inclusive.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> - (Optional) <code class="docutils literal notranslate"><span class="pre">above</span></code>, <code class="docutils literal notranslate"><span class="pre">below</span></code>, or <code class="docutils literal notranslate"><span class="pre">equal</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">equal</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> - (Optional) <code class="docutils literal notranslate"><span class="pre">critical</span></code> or <code class="docutils literal notranslate"><span class="pre">warning</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">critical</span></code>. Terms must include at least one <code class="docutils literal notranslate"><span class="pre">critical</span></code> priority term</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> - (Required) Must be 0 or greater.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">time_function</span></code> - (Required) <code class="docutils literal notranslate"><span class="pre">all</span></code> or <code class="docutils literal notranslate"><span class="pre">any</span></code>.</p></li>
</ul>
<p>Alert conditions can be imported using notation <code class="docutils literal notranslate"><span class="pre">alert_policy_id:alert_condition_id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import newrelic:index/alertCondition:AlertCondition main <span class="m">123456</span>:6789012345
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>condition_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">application</span></code> or <code class="docutils literal notranslate"><span class="pre">instance</span></code>.  Choose <code class="docutils literal notranslate"><span class="pre">application</span></code> for most scenarios.  If you are using the JVM plugin in New Relic, the <code class="docutils literal notranslate"><span class="pre">instance</span></code> setting allows your condition to trigger <a class="reference external" href="https://docs.newrelic.com/docs/alerts/new-relic-alerts/defining-conditions/scope-alert-thresholds-specific-instances">for specific app instances</a>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the condition is enabled or not. Defaults to true.</p></li>
<li><p><strong>entities</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>int</em><em>]</em><em>]</em><em>]</em>) – The instance IDs associated with this condition.</p></li>
<li><p><strong>gc_metric</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A valid Garbage Collection metric e.g. <code class="docutils literal notranslate"><span class="pre">GC/G1</span> <span class="pre">Young</span> <span class="pre">Generation</span></code>.</p></li>
<li><p><strong>metric</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metric field accepts parameters based on the <code class="docutils literal notranslate"><span class="pre">type</span></code> set. One of these metrics based on <code class="docutils literal notranslate"><span class="pre">type</span></code>:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `apm_app_metric`
* `apdex`
* `error_percentage`
* `response_time_background`
* `response_time_web`
* `throughput_background`
* `throughput_web`
* `user_defined`
* `apm_jvm_metric`
* `cpu_utilization_time`
* `deadlocked_threads`
* `gc_cpu_time`
* `heap_memory_usage`
* `apm_kt_metric`
* `apdex`
* `error_count`
* `error_percentage`
* `response_time`
* `throughput`
* `browser_metric`
* `ajax_response_time`
* `ajax_throughput`
* `dom_processing`
* `end_user_apdex`
* `network`
* `page_rendering`
* `page_view_throughput`
* `page_views_with_js_errors`
* `request_queuing`
* `total_page_load`
* `user_defined`
* `web_application`
* `mobile_metric`
* `database`
* `images`
* `json`
* `mobile_crash_rate`
* `network_error_percentage`
* `network`
* `status_error_percentage`
* `user_defined`
* `view_loading`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of the condition. Must be between 1 and 64 characters, inclusive.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the policy where this condition should be used.</p></li>
<li><p><strong>runbook_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Runbook URL to display in notifications.</p></li>
<li><p><strong>terms</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AlertConditionTermArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A list of terms for this condition. See Terms below for details.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of condition. One of: <code class="docutils literal notranslate"><span class="pre">apm_app_metric</span></code>, <code class="docutils literal notranslate"><span class="pre">apm_jvm_metric</span></code>, <code class="docutils literal notranslate"><span class="pre">apm_kt_metric</span></code>, <code class="docutils literal notranslate"><span class="pre">browser_metric</span></code>, <code class="docutils literal notranslate"><span class="pre">mobile_metric</span></code></p></li>
<li><p><strong>user_defined_metric</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A custom metric to be evaluated.</p></li>
<li><p><strong>user_defined_value_function</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – One of: <code class="docutils literal notranslate"><span class="pre">average</span></code>, <code class="docutils literal notranslate"><span class="pre">min</span></code>, <code class="docutils literal notranslate"><span class="pre">max</span></code>, <code class="docutils literal notranslate"><span class="pre">total</span></code>, or <code class="docutils literal notranslate"><span class="pre">sample_size</span></code>.</p></li>
<li><p><strong>violation_close_timer</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Automatically close instance-based violations, including JVM health metric violations, after the number of hours specified. Must be: <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>, <code class="docutils literal notranslate"><span class="pre">4</span></code>, <code class="docutils literal notranslate"><span class="pre">8</span></code>, <code class="docutils literal notranslate"><span class="pre">12</span></code> or <code class="docutils literal notranslate"><span class="pre">24</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_newrelic.AlertCondition.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition_scope</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entities</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gc_metric</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">runbook_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">terms</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>AlertConditionTermArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>AlertConditionTermArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>AlertConditionTermArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>AlertConditionTermArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_defined_metric</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_defined_value_function</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">violation_close_timer</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_newrelic.AlertCondition" title="pulumi_newrelic.AlertCondition">AlertCondition</a><a class="headerlink" href="#pulumi_newrelic.AlertCondition.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AlertCondition resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>condition_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p><code class="docutils literal notranslate"><span class="pre">application</span></code> or <code class="docutils literal notranslate"><span class="pre">instance</span></code>.  Choose <code class="docutils literal notranslate"><span class="pre">application</span></code> for most scenarios.  If you are using the JVM plugin in New Relic, the <code class="docutils literal notranslate"><span class="pre">instance</span></code> setting allows your condition to trigger <a class="reference external" href="https://docs.newrelic.com/docs/alerts/new-relic-alerts/defining-conditions/scope-alert-thresholds-specific-instances">for specific app instances</a>.</p>
</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the condition is enabled or not. Defaults to true.</p></li>
<li><p><strong>entities</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>int</em><em>]</em><em>]</em><em>]</em>) – The instance IDs associated with this condition.</p></li>
<li><p><strong>gc_metric</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A valid Garbage Collection metric e.g. <code class="docutils literal notranslate"><span class="pre">GC/G1</span> <span class="pre">Young</span> <span class="pre">Generation</span></code>.</p></li>
<li><p><strong>metric</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metric field accepts parameters based on the <code class="docutils literal notranslate"><span class="pre">type</span></code> set. One of these metrics based on <code class="docutils literal notranslate"><span class="pre">type</span></code>:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `apm_app_metric`
* `apdex`
* `error_percentage`
* `response_time_background`
* `response_time_web`
* `throughput_background`
* `throughput_web`
* `user_defined`
* `apm_jvm_metric`
* `cpu_utilization_time`
* `deadlocked_threads`
* `gc_cpu_time`
* `heap_memory_usage`
* `apm_kt_metric`
* `apdex`
* `error_count`
* `error_percentage`
* `response_time`
* `throughput`
* `browser_metric`
* `ajax_response_time`
* `ajax_throughput`
* `dom_processing`
* `end_user_apdex`
* `network`
* `page_rendering`
* `page_view_throughput`
* `page_views_with_js_errors`
* `request_queuing`
* `total_page_load`
* `user_defined`
* `web_application`
* `mobile_metric`
* `database`
* `images`
* `json`
* `mobile_crash_rate`
* `network_error_percentage`
* `network`
* `status_error_percentage`
* `user_defined`
* `view_loading`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of the condition. Must be between 1 and 64 characters, inclusive.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the policy where this condition should be used.</p></li>
<li><p><strong>runbook_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Runbook URL to display in notifications.</p></li>
<li><p><strong>terms</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AlertConditionTermArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A list of terms for this condition. See Terms below for details.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of condition. One of: <code class="docutils literal notranslate"><span class="pre">apm_app_metric</span></code>, <code class="docutils literal notranslate"><span class="pre">apm_jvm_metric</span></code>, <code class="docutils literal notranslate"><span class="pre">apm_kt_metric</span></code>, <code class="docutils literal notranslate"><span class="pre">browser_metric</span></code>, <code class="docutils literal notranslate"><span class="pre">mobile_metric</span></code></p></li>
<li><p><strong>user_defined_metric</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A custom metric to be evaluated.</p></li>
<li><p><strong>user_defined_value_function</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – One of: <code class="docutils literal notranslate"><span class="pre">average</span></code>, <code class="docutils literal notranslate"><span class="pre">min</span></code>, <code class="docutils literal notranslate"><span class="pre">max</span></code>, <code class="docutils literal notranslate"><span class="pre">total</span></code>, or <code class="docutils literal notranslate"><span class="pre">sample_size</span></code>.</p></li>
<li><p><strong>violation_close_timer</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Automatically close instance-based violations, including JVM health metric violations, after the number of hours specified. Must be: <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>, <code class="docutils literal notranslate"><span class="pre">4</span></code>, <code class="docutils literal notranslate"><span class="pre">8</span></code>, <code class="docutils literal notranslate"><span class="pre">12</span></code> or <code class="docutils literal notranslate"><span class="pre">24</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertCondition.condition_scope">
<em class="property">property </em><code class="sig-name descname">condition_scope</code><a class="headerlink" href="#pulumi_newrelic.AlertCondition.condition_scope" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">application</span></code> or <code class="docutils literal notranslate"><span class="pre">instance</span></code>.  Choose <code class="docutils literal notranslate"><span class="pre">application</span></code> for most scenarios.  If you are using the JVM plugin in New Relic, the <code class="docutils literal notranslate"><span class="pre">instance</span></code> setting allows your condition to trigger <a class="reference external" href="https://docs.newrelic.com/docs/alerts/new-relic-alerts/defining-conditions/scope-alert-thresholds-specific-instances">for specific app instances</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertCondition.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_newrelic.AlertCondition.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the condition is enabled or not. Defaults to true.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertCondition.entities">
<em class="property">property </em><code class="sig-name descname">entities</code><a class="headerlink" href="#pulumi_newrelic.AlertCondition.entities" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance IDs associated with this condition.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertCondition.gc_metric">
<em class="property">property </em><code class="sig-name descname">gc_metric</code><a class="headerlink" href="#pulumi_newrelic.AlertCondition.gc_metric" title="Permalink to this definition">¶</a></dt>
<dd><p>A valid Garbage Collection metric e.g. <code class="docutils literal notranslate"><span class="pre">GC/G1</span> <span class="pre">Young</span> <span class="pre">Generation</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertCondition.metric">
<em class="property">property </em><code class="sig-name descname">metric</code><a class="headerlink" href="#pulumi_newrelic.AlertCondition.metric" title="Permalink to this definition">¶</a></dt>
<dd><p>The metric field accepts parameters based on the <code class="docutils literal notranslate"><span class="pre">type</span></code> set. One of these metrics based on <code class="docutils literal notranslate"><span class="pre">type</span></code>:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">apm_app_metric</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">apdex</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">error_percentage</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response_time_background</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response_time_web</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">throughput_background</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">throughput_web</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_defined</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">apm_jvm_metric</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cpu_utilization_time</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deadlocked_threads</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gc_cpu_time</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">heap_memory_usage</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">apm_kt_metric</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">apdex</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">error_count</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">error_percentage</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response_time</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">throughput</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browser_metric</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ajax_response_time</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ajax_throughput</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dom_processing</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">end_user_apdex</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">page_rendering</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">page_view_throughput</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">page_views_with_js_errors</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">request_queuing</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">total_page_load</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_defined</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">web_application</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mobile_metric</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">database</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">images</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">json</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mobile_crash_rate</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network_error_percentage</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status_error_percentage</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_defined</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">view_loading</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertCondition.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_newrelic.AlertCondition.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The title of the condition. Must be between 1 and 64 characters, inclusive.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertCondition.policy_id">
<em class="property">property </em><code class="sig-name descname">policy_id</code><a class="headerlink" href="#pulumi_newrelic.AlertCondition.policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the policy where this condition should be used.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertCondition.runbook_url">
<em class="property">property </em><code class="sig-name descname">runbook_url</code><a class="headerlink" href="#pulumi_newrelic.AlertCondition.runbook_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Runbook URL to display in notifications.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertCondition.terms">
<em class="property">property </em><code class="sig-name descname">terms</code><a class="headerlink" href="#pulumi_newrelic.AlertCondition.terms" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of terms for this condition. See Terms below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertCondition.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_newrelic.AlertCondition.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of condition. One of: <code class="docutils literal notranslate"><span class="pre">apm_app_metric</span></code>, <code class="docutils literal notranslate"><span class="pre">apm_jvm_metric</span></code>, <code class="docutils literal notranslate"><span class="pre">apm_kt_metric</span></code>, <code class="docutils literal notranslate"><span class="pre">browser_metric</span></code>, <code class="docutils literal notranslate"><span class="pre">mobile_metric</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertCondition.user_defined_metric">
<em class="property">property </em><code class="sig-name descname">user_defined_metric</code><a class="headerlink" href="#pulumi_newrelic.AlertCondition.user_defined_metric" title="Permalink to this definition">¶</a></dt>
<dd><p>A custom metric to be evaluated.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertCondition.user_defined_value_function">
<em class="property">property </em><code class="sig-name descname">user_defined_value_function</code><a class="headerlink" href="#pulumi_newrelic.AlertCondition.user_defined_value_function" title="Permalink to this definition">¶</a></dt>
<dd><p>One of: <code class="docutils literal notranslate"><span class="pre">average</span></code>, <code class="docutils literal notranslate"><span class="pre">min</span></code>, <code class="docutils literal notranslate"><span class="pre">max</span></code>, <code class="docutils literal notranslate"><span class="pre">total</span></code>, or <code class="docutils literal notranslate"><span class="pre">sample_size</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertCondition.violation_close_timer">
<em class="property">property </em><code class="sig-name descname">violation_close_timer</code><a class="headerlink" href="#pulumi_newrelic.AlertCondition.violation_close_timer" title="Permalink to this definition">¶</a></dt>
<dd><p>Automatically close instance-based violations, including JVM health metric violations, after the number of hours specified. Must be: <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>, <code class="docutils literal notranslate"><span class="pre">4</span></code>, <code class="docutils literal notranslate"><span class="pre">8</span></code>, <code class="docutils literal notranslate"><span class="pre">12</span></code> or <code class="docutils literal notranslate"><span class="pre">24</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertCondition.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AlertCondition.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.AlertCondition.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AlertCondition.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.AlertMutingRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">AlertMutingRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>AlertMutingRuleConditionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>AlertMutingRuleConditionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AlertMutingRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Alert conditions can be imported using a composite ID of <code class="docutils literal notranslate"><span class="pre">&lt;account_id&gt;:&lt;muting_rule_id&gt;</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import newrelic:index/alertMutingRule:AlertMutingRule foo <span class="m">538291</span>:6789035
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The account id of the MutingRule.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AlertMutingRuleConditionArgs'</em><em>]</em><em>]</em>) – The condition that defines which violations to target. See Nested condition blocks below for details.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the MutingRule.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the MutingRule is enabled.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the MutingRule.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_newrelic.AlertMutingRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>AlertMutingRuleConditionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>AlertMutingRuleConditionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_newrelic.AlertMutingRule" title="pulumi_newrelic.AlertMutingRule">AlertMutingRule</a><a class="headerlink" href="#pulumi_newrelic.AlertMutingRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AlertMutingRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The account id of the MutingRule.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AlertMutingRuleConditionArgs'</em><em>]</em><em>]</em>) – The condition that defines which violations to target. See Nested condition blocks below for details.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the MutingRule.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the MutingRule is enabled.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the MutingRule.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertMutingRule.account_id">
<em class="property">property </em><code class="sig-name descname">account_id</code><a class="headerlink" href="#pulumi_newrelic.AlertMutingRule.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The account id of the MutingRule.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertMutingRule.condition">
<em class="property">property </em><code class="sig-name descname">condition</code><a class="headerlink" href="#pulumi_newrelic.AlertMutingRule.condition" title="Permalink to this definition">¶</a></dt>
<dd><p>The condition that defines which violations to target. See Nested condition blocks below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertMutingRule.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_newrelic.AlertMutingRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the MutingRule.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertMutingRule.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_newrelic.AlertMutingRule.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the MutingRule is enabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertMutingRule.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_newrelic.AlertMutingRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the MutingRule.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertMutingRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AlertMutingRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.AlertMutingRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AlertMutingRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.AlertPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">AlertPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">channel_ids</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">incident_preference</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AlertPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to create and manage New Relic alert policies.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertPolicy</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span> <span class="n">incident_preference</span><span class="o">=</span><span class="s2">&quot;PER_POLICY&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="c1"># Provision a Slack notification channel.</span>
<span class="n">slack_channel</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannel</span><span class="p">(</span><span class="s2">&quot;slackChannel&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;slack&quot;</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannelConfigArgs</span><span class="p">(</span>
        <span class="n">url</span><span class="o">=</span><span class="s2">&quot;https://hooks.slack.com/services/xxxxxxx/yyyyyyyy&quot;</span><span class="p">,</span>
        <span class="n">channel</span><span class="o">=</span><span class="s2">&quot;example-alerts-channel&quot;</span><span class="p">,</span>
    <span class="p">))</span>
<span class="c1"># Provision an email notification channel.</span>
<span class="n">email_channel</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannel</span><span class="p">(</span><span class="s2">&quot;emailChannel&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;email&quot;</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannelConfigArgs</span><span class="p">(</span>
        <span class="n">recipients</span><span class="o">=</span><span class="s2">&quot;example@testing.com&quot;</span><span class="p">,</span>
        <span class="n">include_json_attachment</span><span class="o">=</span><span class="s2">&quot;1&quot;</span><span class="p">,</span>
    <span class="p">))</span>
<span class="c1"># Provision the alert policy.</span>
<span class="n">policy_with_channels</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertPolicy</span><span class="p">(</span><span class="s2">&quot;policyWithChannels&quot;</span><span class="p">,</span>
    <span class="n">incident_preference</span><span class="o">=</span><span class="s2">&quot;PER_CONDITION&quot;</span><span class="p">,</span>
    <span class="n">channel_ids</span><span class="o">=</span><span class="p">[</span>
        <span class="n">slack_channel</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="n">email_channel</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">slack_channel</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">get_alert_channel</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;slack-channel-notification&quot;</span><span class="p">)</span>
<span class="n">email_channel</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">get_alert_channel</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;test@example.com&quot;</span><span class="p">)</span>
<span class="c1"># Provision the alert policy.</span>
<span class="n">policy_with_channels</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertPolicy</span><span class="p">(</span><span class="s2">&quot;policyWithChannels&quot;</span><span class="p">,</span>
    <span class="n">incident_preference</span><span class="o">=</span><span class="s2">&quot;PER_CONDITION&quot;</span><span class="p">,</span>
    <span class="n">channel_ids</span><span class="o">=</span><span class="p">[</span>
        <span class="n">slack_channel</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="n">email_channel</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<p>Alert policies can be imported using a composite ID of <code class="docutils literal notranslate"><span class="pre">&lt;id&gt;:&lt;account_id&gt;</span></code>, where <code class="docutils literal notranslate"><span class="pre">account_id</span></code> is the account number scoped to the alert policy resource. Example import</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import newrelic:index/alertPolicy:AlertPolicy foo <span class="m">23423556</span>:4593020

Please note that channel IDs <span class="o">(</span><span class="se">\ </span><span class="sb">``</span>channel_ids<span class="sb">``</span><span class="se">\ </span><span class="o">)</span> *cannot* be imported due channels being a separate resource. However, to add channels to an imported alert policy, you can import the policy, add the <span class="sb">``</span>channel_ids<span class="sb">``</span> attribute with the associated channel IDs, <span class="k">then</span> run <span class="sb">``</span>terraform apply<span class="sb">``</span>. This will result <span class="k">in</span> the original alert policy being destroyed and a new alert policy being created along with the channels being added to the policy.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The New Relic account ID to operate on.  This allows the user to override the <code class="docutils literal notranslate"><span class="pre">account_id</span></code> attribute set on the provider. Defaults to the environment variable <code class="docutils literal notranslate"><span class="pre">NEW_RELIC_ACCOUNT_ID</span></code>.</p></li>
<li><p><strong>channel_ids</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>int</em><em>]</em><em>]</em><em>]</em>) – An array of channel IDs (integers) to assign to the policy. Adding or removing channel IDs from this array will result in a new alert policy resource being created and the old one being destroyed. Also note that channel IDs <em>cannot</em> be imported.</p></li>
<li><p><strong>incident_preference</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The rollup strategy for the policy.  Options include: <code class="docutils literal notranslate"><span class="pre">PER_POLICY</span></code>, <code class="docutils literal notranslate"><span class="pre">PER_CONDITION</span></code>, or <code class="docutils literal notranslate"><span class="pre">PER_CONDITION_AND_TARGET</span></code>.  The default is <code class="docutils literal notranslate"><span class="pre">PER_POLICY</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_newrelic.AlertPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">channel_ids</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">incident_preference</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_newrelic.AlertPolicy" title="pulumi_newrelic.AlertPolicy">AlertPolicy</a><a class="headerlink" href="#pulumi_newrelic.AlertPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AlertPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The New Relic account ID to operate on.  This allows the user to override the <code class="docutils literal notranslate"><span class="pre">account_id</span></code> attribute set on the provider. Defaults to the environment variable <code class="docutils literal notranslate"><span class="pre">NEW_RELIC_ACCOUNT_ID</span></code>.</p></li>
<li><p><strong>channel_ids</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>int</em><em>]</em><em>]</em><em>]</em>) – An array of channel IDs (integers) to assign to the policy. Adding or removing channel IDs from this array will result in a new alert policy resource being created and the old one being destroyed. Also note that channel IDs <em>cannot</em> be imported.</p></li>
<li><p><strong>incident_preference</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The rollup strategy for the policy.  Options include: <code class="docutils literal notranslate"><span class="pre">PER_POLICY</span></code>, <code class="docutils literal notranslate"><span class="pre">PER_CONDITION</span></code>, or <code class="docutils literal notranslate"><span class="pre">PER_CONDITION_AND_TARGET</span></code>.  The default is <code class="docutils literal notranslate"><span class="pre">PER_POLICY</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertPolicy.account_id">
<em class="property">property </em><code class="sig-name descname">account_id</code><a class="headerlink" href="#pulumi_newrelic.AlertPolicy.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The New Relic account ID to operate on.  This allows the user to override the <code class="docutils literal notranslate"><span class="pre">account_id</span></code> attribute set on the provider. Defaults to the environment variable <code class="docutils literal notranslate"><span class="pre">NEW_RELIC_ACCOUNT_ID</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertPolicy.channel_ids">
<em class="property">property </em><code class="sig-name descname">channel_ids</code><a class="headerlink" href="#pulumi_newrelic.AlertPolicy.channel_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of channel IDs (integers) to assign to the policy. Adding or removing channel IDs from this array will result in a new alert policy resource being created and the old one being destroyed. Also note that channel IDs <em>cannot</em> be imported.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertPolicy.incident_preference">
<em class="property">property </em><code class="sig-name descname">incident_preference</code><a class="headerlink" href="#pulumi_newrelic.AlertPolicy.incident_preference" title="Permalink to this definition">¶</a></dt>
<dd><p>The rollup strategy for the policy.  Options include: <code class="docutils literal notranslate"><span class="pre">PER_POLICY</span></code>, <code class="docutils literal notranslate"><span class="pre">PER_CONDITION</span></code>, or <code class="docutils literal notranslate"><span class="pre">PER_CONDITION_AND_TARGET</span></code>.  The default is <code class="docutils literal notranslate"><span class="pre">PER_POLICY</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertPolicy.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_newrelic.AlertPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AlertPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.AlertPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AlertPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.AlertPolicyChannel">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">AlertPolicyChannel</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">channel_ids</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AlertPolicyChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to map alert policies to alert channels in New Relic.</p>
<p>The example below will apply multiple alert channels to an existing New Relic alert policy.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">example_policy</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">get_alert_policy</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;my-alert-policy&quot;</span><span class="p">)</span>
<span class="c1"># Creates an email alert channel.</span>
<span class="n">email_channel</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannel</span><span class="p">(</span><span class="s2">&quot;emailChannel&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;email&quot;</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannelConfigArgs</span><span class="p">(</span>
        <span class="n">recipients</span><span class="o">=</span><span class="s2">&quot;foo@example.com&quot;</span><span class="p">,</span>
        <span class="n">include_json_attachment</span><span class="o">=</span><span class="s2">&quot;1&quot;</span><span class="p">,</span>
    <span class="p">))</span>
<span class="c1"># Creates a Slack alert channel.</span>
<span class="n">slack_channel</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannel</span><span class="p">(</span><span class="s2">&quot;slackChannel&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;slack&quot;</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannelConfigArgs</span><span class="p">(</span>
        <span class="n">channel</span><span class="o">=</span><span class="s2">&quot;#example-channel&quot;</span><span class="p">,</span>
        <span class="n">url</span><span class="o">=</span><span class="s2">&quot;http://example-org.slack.com&quot;</span><span class="p">,</span>
    <span class="p">))</span>
<span class="c1"># Applies the created channels above to the alert policy</span>
<span class="c1"># referenced at the top of the config.</span>
<span class="n">foo</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertPolicyChannel</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">policy_id</span><span class="o">=</span><span class="n">newrelic_alert_policy</span><span class="p">[</span><span class="s2">&quot;example_policy&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">channel_ids</span><span class="o">=</span><span class="p">[</span>
        <span class="n">email_channel</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="n">slack_channel</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<p>Alert policy channels can be imported using the following notation<code class="docutils literal notranslate"><span class="pre">&lt;policyID&gt;:&lt;channelID&gt;:&lt;channelID&gt;</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import newrelic:index/alertPolicyChannel:AlertPolicyChannel foo <span class="m">123456</span>:3462754:2938324

When importing <span class="sb">``</span>newrelic_alert_policy_channel<span class="sb">``</span> resource, the attribute <span class="sb">``</span>channel_ids<span class="sb">``</span><span class="se">\ </span>* will be <span class="nb">set</span> <span class="k">in</span> your Terraform state. You can import multiple channels as long as those channel IDs are included as part of the import ID hash.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>channel_ids</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>int</em><em>]</em><em>]</em><em>]</em>) – Array of channel IDs to apply to the specified policy. We recommended sorting channel IDs in ascending order to avoid drift in your state.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the policy.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_newrelic.AlertPolicyChannel.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">channel_ids</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_newrelic.AlertPolicyChannel" title="pulumi_newrelic.AlertPolicyChannel">AlertPolicyChannel</a><a class="headerlink" href="#pulumi_newrelic.AlertPolicyChannel.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AlertPolicyChannel resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>channel_ids</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>int</em><em>]</em><em>]</em><em>]</em>) – Array of channel IDs to apply to the specified policy. We recommended sorting channel IDs in ascending order to avoid drift in your state.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the policy.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertPolicyChannel.channel_ids">
<em class="property">property </em><code class="sig-name descname">channel_ids</code><a class="headerlink" href="#pulumi_newrelic.AlertPolicyChannel.channel_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of channel IDs to apply to the specified policy. We recommended sorting channel IDs in ascending order to avoid drift in your state.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertPolicyChannel.policy_id">
<em class="property">property </em><code class="sig-name descname">policy_id</code><a class="headerlink" href="#pulumi_newrelic.AlertPolicyChannel.policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the policy.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertPolicyChannel.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AlertPolicyChannel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.AlertPolicyChannel.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AlertPolicyChannel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.ApiAccessKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">ApiAccessKey</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ingest_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.ApiAccessKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to programmatically create and manage the following types of keys:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.newrelic.co/docs/apis/get-started/intro-apis/types-new-relic-api-keys#user-api-key">User API keys</a></p></li>
<li><p>License (or ingest) keys, including:</p>
<ul>
<li><p>General <a class="reference external" href="https://docs.newrelic.co/docs/accounts/install-new-relic/account-setup/license-key">license key</a> used for APM</p></li>
<li><p><a class="reference external" href="https://docs.newrelic.co/docs/browser/new-relic-browser/configuration/copy-browser-monitoring-license-key-app-id">Browser license key</a></p></li>
</ul>
</li>
</ul>
<p>Please visit the New Relic article <a class="reference external" href="https://docs.newrelic.com/docs/apis/nerdgraph/examples/use-nerdgraph-manage-license-keys-user-keys">‘Use NerdGraph to manage license keys and User API keys’</a>
for more information.</p>
<blockquote>
<div><p><strong>IMPORTANT!</strong>
Please be very careful when updating existing <code class="docutils literal notranslate"><span class="pre">ApiAccessKey</span></code> resources as only <code class="docutils literal notranslate"><span class="pre">newrelic_api_access_key.name</span></code>
and <code class="docutils literal notranslate"><span class="pre">newrelic_api_access_key.notes</span></code> are updatable. All other resource attributes will force a resource recreation which will
invalidate the previous API key(s).</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foobar</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">ApiAccessKey</span><span class="p">(</span><span class="s2">&quot;foobar&quot;</span><span class="p">,</span>
    <span class="n">account_id</span><span class="o">=</span><span class="mi">1234567</span><span class="p">,</span>
    <span class="n">ingest_type</span><span class="o">=</span><span class="s2">&quot;LICENSE&quot;</span><span class="p">,</span>
    <span class="n">key_type</span><span class="o">=</span><span class="s2">&quot;INGEST&quot;</span><span class="p">,</span>
    <span class="n">notes</span><span class="o">=</span><span class="s2">&quot;To be used with service X&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Existing API access keys can be imported using a composite ID of <code class="docutils literal notranslate"><span class="pre">&lt;api_access_key_id&gt;:&lt;key_type&gt;</span></code>. <code class="docutils literal notranslate"><span class="pre">&lt;key_type&gt;</span></code> will be either <code class="docutils literal notranslate"><span class="pre">INGEST</span></code> or <code class="docutils literal notranslate"><span class="pre">USER</span></code>. For example</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import newrelic:index/apiAccessKey:ApiAccessKey foobar <span class="s2">&quot;1234567:INGEST&quot;</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The New Relic account ID of the account you wish to create the API access key.</p></li>
<li><p><strong>ingest_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required if <code class="docutils literal notranslate"><span class="pre">key_type</span> <span class="pre">=</span> <span class="pre">INGEST</span></code>. Valid options are <code class="docutils literal notranslate"><span class="pre">BROWSER</span></code> or <code class="docutils literal notranslate"><span class="pre">LICENSE</span></code>, case-sensitive.</p></li>
<li><p><strong>key_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – What type of API key to create. Valid options are <code class="docutils literal notranslate"><span class="pre">INGEST</span></code> or <code class="docutils literal notranslate"><span class="pre">USER</span></code>, case-sensitive.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the key.</p></li>
<li><p><strong>notes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Any notes about this ingest key.</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Required if <code class="docutils literal notranslate"><span class="pre">key_type</span> <span class="pre">=</span> <span class="pre">USER</span></code>. The New Relic user ID yous wish to create the API access key for in an account.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_newrelic.ApiAccessKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ingest_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_newrelic.ApiAccessKey" title="pulumi_newrelic.ApiAccessKey">ApiAccessKey</a><a class="headerlink" href="#pulumi_newrelic.ApiAccessKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApiAccessKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The New Relic account ID of the account you wish to create the API access key.</p></li>
<li><p><strong>ingest_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required if <code class="docutils literal notranslate"><span class="pre">key_type</span> <span class="pre">=</span> <span class="pre">INGEST</span></code>. Valid options are <code class="docutils literal notranslate"><span class="pre">BROWSER</span></code> or <code class="docutils literal notranslate"><span class="pre">LICENSE</span></code>, case-sensitive.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The actual API key. This attribute is masked and not be visible in your terminal, CI, etc.</p></li>
<li><p><strong>key_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – What type of API key to create. Valid options are <code class="docutils literal notranslate"><span class="pre">INGEST</span></code> or <code class="docutils literal notranslate"><span class="pre">USER</span></code>, case-sensitive.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the key.</p></li>
<li><p><strong>notes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Any notes about this ingest key.</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Required if <code class="docutils literal notranslate"><span class="pre">key_type</span> <span class="pre">=</span> <span class="pre">USER</span></code>. The New Relic user ID yous wish to create the API access key for in an account.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.ApiAccessKey.account_id">
<em class="property">property </em><code class="sig-name descname">account_id</code><a class="headerlink" href="#pulumi_newrelic.ApiAccessKey.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The New Relic account ID of the account you wish to create the API access key.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.ApiAccessKey.ingest_type">
<em class="property">property </em><code class="sig-name descname">ingest_type</code><a class="headerlink" href="#pulumi_newrelic.ApiAccessKey.ingest_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Required if <code class="docutils literal notranslate"><span class="pre">key_type</span> <span class="pre">=</span> <span class="pre">INGEST</span></code>. Valid options are <code class="docutils literal notranslate"><span class="pre">BROWSER</span></code> or <code class="docutils literal notranslate"><span class="pre">LICENSE</span></code>, case-sensitive.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.ApiAccessKey.key">
<em class="property">property </em><code class="sig-name descname">key</code><a class="headerlink" href="#pulumi_newrelic.ApiAccessKey.key" title="Permalink to this definition">¶</a></dt>
<dd><p>The actual API key. This attribute is masked and not be visible in your terminal, CI, etc.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.ApiAccessKey.key_type">
<em class="property">property </em><code class="sig-name descname">key_type</code><a class="headerlink" href="#pulumi_newrelic.ApiAccessKey.key_type" title="Permalink to this definition">¶</a></dt>
<dd><p>What type of API key to create. Valid options are <code class="docutils literal notranslate"><span class="pre">INGEST</span></code> or <code class="docutils literal notranslate"><span class="pre">USER</span></code>, case-sensitive.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.ApiAccessKey.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_newrelic.ApiAccessKey.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the key.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.ApiAccessKey.notes">
<em class="property">property </em><code class="sig-name descname">notes</code><a class="headerlink" href="#pulumi_newrelic.ApiAccessKey.notes" title="Permalink to this definition">¶</a></dt>
<dd><p>Any notes about this ingest key.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.ApiAccessKey.user_id">
<em class="property">property </em><code class="sig-name descname">user_id</code><a class="headerlink" href="#pulumi_newrelic.ApiAccessKey.user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Required if <code class="docutils literal notranslate"><span class="pre">key_type</span> <span class="pre">=</span> <span class="pre">USER</span></code>. The New Relic user ID yous wish to create the API access key for in an account.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.ApiAccessKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.ApiAccessKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.ApiAccessKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.ApiAccessKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.AwaitableGetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">AwaitableGetAccountResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AwaitableGetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_newrelic.AwaitableGetAlertChannelResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">AwaitableGetAlertChannelResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AwaitableGetAlertChannelResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_newrelic.AwaitableGetAlertPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">AwaitableGetAlertPolicyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">incident_preference</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated_at</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AwaitableGetAlertPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_newrelic.AwaitableGetApplicationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">AwaitableGetApplicationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">host_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AwaitableGetApplicationResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_newrelic.AwaitableGetEntityResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">AwaitableGetEntityResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">guid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">serving_apm_application_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AwaitableGetEntityResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_newrelic.AwaitableGetKeyTransactionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">AwaitableGetKeyTransactionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AwaitableGetKeyTransactionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_newrelic.Dashboard">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">Dashboard</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">editable</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>DashboardFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>DashboardFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grid_column_count</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">icon</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">widgets</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>DashboardWidgetArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>DashboardWidgetArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>DashboardWidgetArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>DashboardWidgetArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.Dashboard" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to create and manage New Relic dashboards.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">my_application</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">get_entity</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;My Application&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;APPLICATION&quot;</span><span class="p">,</span>
    <span class="n">domain</span><span class="o">=</span><span class="s2">&quot;APM&quot;</span><span class="p">)</span>
<span class="n">exampledash</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">Dashboard</span><span class="p">(</span><span class="s2">&quot;exampledash&quot;</span><span class="p">,</span>
    <span class="n">title</span><span class="o">=</span><span class="s2">&quot;New Relic Terraform Example&quot;</span><span class="p">,</span>
    <span class="nb">filter</span><span class="o">=</span><span class="n">newrelic</span><span class="o">.</span><span class="n">DashboardFilterArgs</span><span class="p">(</span>
        <span class="n">event_types</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;Transaction&quot;</span><span class="p">],</span>
        <span class="n">attributes</span><span class="o">=</span><span class="p">[</span>
            <span class="s2">&quot;appName&quot;</span><span class="p">,</span>
            <span class="s2">&quot;name&quot;</span><span class="p">,</span>
        <span class="p">],</span>
    <span class="p">),</span>
    <span class="n">widgets</span><span class="o">=</span><span class="p">[</span>
        <span class="n">newrelic</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Requests per minute&quot;</span><span class="p">,</span>
            <span class="n">visualization</span><span class="o">=</span><span class="s2">&quot;billboard&quot;</span><span class="p">,</span>
            <span class="n">nrql</span><span class="o">=</span><span class="s2">&quot;SELECT rate(count(*), 1 minute) FROM Transaction&quot;</span><span class="p">,</span>
            <span class="n">row</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
            <span class="n">column</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">newrelic</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Error rate&quot;</span><span class="p">,</span>
            <span class="n">visualization</span><span class="o">=</span><span class="s2">&quot;gauge&quot;</span><span class="p">,</span>
            <span class="n">nrql</span><span class="o">=</span><span class="s2">&quot;SELECT percentage(count(*), WHERE error IS True) FROM Transaction&quot;</span><span class="p">,</span>
            <span class="n">threshold_red</span><span class="o">=</span><span class="mf">2.5</span><span class="p">,</span>
            <span class="n">row</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
            <span class="n">column</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">newrelic</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Average transaction duration, by application&quot;</span><span class="p">,</span>
            <span class="n">visualization</span><span class="o">=</span><span class="s2">&quot;facet_bar_chart&quot;</span><span class="p">,</span>
            <span class="n">nrql</span><span class="o">=</span><span class="s2">&quot;SELECT average(duration) FROM Transaction FACET appName&quot;</span><span class="p">,</span>
            <span class="n">row</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
            <span class="n">column</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">newrelic</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Apdex, top 5 by host&quot;</span><span class="p">,</span>
            <span class="n">duration</span><span class="o">=</span><span class="mi">1800000</span><span class="p">,</span>
            <span class="n">visualization</span><span class="o">=</span><span class="s2">&quot;metric_line_chart&quot;</span><span class="p">,</span>
            <span class="n">entity_ids</span><span class="o">=</span><span class="p">[</span><span class="n">my_application</span><span class="o">.</span><span class="n">application_id</span><span class="p">],</span>
            <span class="n">metrics</span><span class="o">=</span><span class="p">[</span><span class="n">newrelic</span><span class="o">.</span><span class="n">DashboardWidgetMetricArgs</span><span class="p">(</span>
                <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Apdex&quot;</span><span class="p">,</span>
                <span class="n">values</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;score&quot;</span><span class="p">],</span>
            <span class="p">)],</span>
            <span class="n">facet</span><span class="o">=</span><span class="s2">&quot;host&quot;</span><span class="p">,</span>
            <span class="n">limit</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
            <span class="n">order_by</span><span class="o">=</span><span class="s2">&quot;score&quot;</span><span class="p">,</span>
            <span class="n">row</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
            <span class="n">column</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">newrelic</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Requests per minute, by transaction&quot;</span><span class="p">,</span>
            <span class="n">visualization</span><span class="o">=</span><span class="s2">&quot;facet_table&quot;</span><span class="p">,</span>
            <span class="n">nrql</span><span class="o">=</span><span class="s2">&quot;SELECT rate(count(*), 1 minute) FROM Transaction FACET name&quot;</span><span class="p">,</span>
            <span class="n">row</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
            <span class="n">column</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">newrelic</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Dashboard Note&quot;</span><span class="p">,</span>
            <span class="n">visualization</span><span class="o">=</span><span class="s2">&quot;markdown&quot;</span><span class="p">,</span>
            <span class="n">source</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;### Helpful Links</span>

<span class="s2">* [New Relic One](https://one.newrelic.com)</span>
<span class="s2">* [Developer Portal](https://developer.newrelic.com)&quot;&quot;&quot;</span><span class="p">,</span>
            <span class="n">row</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
            <span class="n">column</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">])</span>
</pre></div>
</div>
<p>See additional examples.</p>
<p>The example below shows how you can display data for an application from a primary account and an application from a subaccount. In order to create cross-account widgets, you must use an API key from a user with admin permissions in the primary account. Please see the <code class="docutils literal notranslate"><span class="pre">widget</span></code> attribute documentation for more details.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">primary_account_application</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">get_entity</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Main Account Application Name&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;APPLICATION&quot;</span><span class="p">,</span>
    <span class="n">domain</span><span class="o">=</span><span class="s2">&quot;APM&quot;</span><span class="p">)</span>
<span class="n">subaccount_application</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">get_entity</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Subaccount Application Name&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;APPLICATION&quot;</span><span class="p">,</span>
    <span class="n">domain</span><span class="o">=</span><span class="s2">&quot;APM&quot;</span><span class="p">)</span>
<span class="n">cross_account_widget_example</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">Dashboard</span><span class="p">(</span><span class="s2">&quot;crossAccountWidgetExample&quot;</span><span class="p">,</span>
    <span class="n">title</span><span class="o">=</span><span class="s2">&quot;tf-test-cross-account-widget-dashboard&quot;</span><span class="p">,</span>
    <span class="nb">filter</span><span class="o">=</span><span class="n">newrelic</span><span class="o">.</span><span class="n">DashboardFilterArgs</span><span class="p">(</span>
        <span class="n">event_types</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;Transaction&quot;</span><span class="p">],</span>
        <span class="n">attributes</span><span class="o">=</span><span class="p">[</span>
            <span class="s2">&quot;appName&quot;</span><span class="p">,</span>
            <span class="s2">&quot;envName&quot;</span><span class="p">,</span>
        <span class="p">],</span>
    <span class="p">),</span>
    <span class="n">grid_column_count</span><span class="o">=</span><span class="mi">12</span><span class="p">,</span>
    <span class="n">widgets</span><span class="o">=</span><span class="p">[</span>
        <span class="n">newrelic</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Apdex (primary account)&quot;</span><span class="p">,</span>
            <span class="n">row</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
            <span class="n">column</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
            <span class="n">width</span><span class="o">=</span><span class="mi">6</span><span class="p">,</span>
            <span class="n">height</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
            <span class="n">visualization</span><span class="o">=</span><span class="s2">&quot;metric_line_chart&quot;</span><span class="p">,</span>
            <span class="n">duration</span><span class="o">=</span><span class="mi">1800000</span><span class="p">,</span>
            <span class="n">metrics</span><span class="o">=</span><span class="p">[</span><span class="n">newrelic</span><span class="o">.</span><span class="n">DashboardWidgetMetricArgs</span><span class="p">(</span>
                <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Apdex&quot;</span><span class="p">,</span>
                <span class="n">values</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;score&quot;</span><span class="p">],</span>
            <span class="p">)],</span>
            <span class="n">entity_ids</span><span class="o">=</span><span class="p">[</span><span class="n">primary_account_application</span><span class="o">.</span><span class="n">application_id</span><span class="p">],</span>
        <span class="p">),</span>
        <span class="n">newrelic</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">account_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;subaccount_id&quot;</span><span class="p">],</span>
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Apdex (subaccount)&quot;</span><span class="p">,</span>
            <span class="n">row</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
            <span class="n">column</span><span class="o">=</span><span class="mi">7</span><span class="p">,</span>
            <span class="n">width</span><span class="o">=</span><span class="mi">6</span><span class="p">,</span>
            <span class="n">height</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
            <span class="n">visualization</span><span class="o">=</span><span class="s2">&quot;metric_line_chart&quot;</span><span class="p">,</span>
            <span class="n">duration</span><span class="o">=</span><span class="mi">1800000</span><span class="p">,</span>
            <span class="n">metrics</span><span class="o">=</span><span class="p">[</span><span class="n">newrelic</span><span class="o">.</span><span class="n">DashboardWidgetMetricArgs</span><span class="p">(</span>
                <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Apdex&quot;</span><span class="p">,</span>
                <span class="n">values</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;score&quot;</span><span class="p">],</span>
            <span class="p">)],</span>
            <span class="n">entity_ids</span><span class="o">=</span><span class="p">[</span><span class="n">subaccount_application</span><span class="o">.</span><span class="n">application_id</span><span class="p">],</span>
        <span class="p">),</span>
    <span class="p">])</span>
</pre></div>
</div>
<p>New Relic dashboards can be imported using their ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import newrelic:index/dashboard:Dashboard my_dashboard <span class="m">8675309</span>

~&gt; **NOTE** Due to API restrictions, importing a dashboard resource will <span class="nb">set</span> the <span class="sb">``</span>grid_column_count<span class="sb">``</span> attribute to <span class="sb">``</span><span class="m">3</span><span class="sb">``</span>. If your dashboard is a New Relic One dashboard *and* uses a <span class="m">12</span> column grid, you will need to make sure <span class="sb">``</span>grid_column_count<span class="sb">``</span> is <span class="nb">set</span> to <span class="sb">``</span><span class="m">12</span><span class="sb">``</span> <span class="k">in</span> your configuration, <span class="k">then</span> run <span class="sb">``</span>terraform apply<span class="sb">``</span> after importing to sync remote state with Terraform state. Also note, cross-account widgets cannot be imported due to API restrictions.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>editable</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determines who can edit the dashboard in an account. Valid values are <code class="docutils literal notranslate"><span class="pre">all</span></code>,  <code class="docutils literal notranslate"><span class="pre">editable_by_all</span></code>, <code class="docutils literal notranslate"><span class="pre">editable_by_owner</span></code>, or <code class="docutils literal notranslate"><span class="pre">read_only</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">editable_by_all</span></code>.</p></li>
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardFilterArgs'</em><em>]</em><em>]</em>) – A nested block that describes a dashboard filter.  Exactly one nested <code class="docutils literal notranslate"><span class="pre">filter</span></code> block is allowed. See Nested filter block below for details.</p></li>
<li><p><strong>grid_column_count</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of columns to use when organizing and displaying widgets. New Relic One supports a 3 column grid and a 12 column grid. New Relic Insights supports a 3 column grid.</p></li>
<li><p><strong>icon</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The icon for the dashboard.  Valid values are <code class="docutils literal notranslate"><span class="pre">adjust</span></code>, <code class="docutils literal notranslate"><span class="pre">archive</span></code>, <code class="docutils literal notranslate"><span class="pre">bar-chart</span></code>, <code class="docutils literal notranslate"><span class="pre">bell</span></code>, <code class="docutils literal notranslate"><span class="pre">bolt</span></code>, <code class="docutils literal notranslate"><span class="pre">bug</span></code>, <code class="docutils literal notranslate"><span class="pre">bullhorn</span></code>, <code class="docutils literal notranslate"><span class="pre">bullseye</span></code>, <code class="docutils literal notranslate"><span class="pre">clock-o</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud</span></code>, <code class="docutils literal notranslate"><span class="pre">cog</span></code>, <code class="docutils literal notranslate"><span class="pre">comments-o</span></code>, <code class="docutils literal notranslate"><span class="pre">crosshairs</span></code>, <code class="docutils literal notranslate"><span class="pre">dashboard</span></code>, <code class="docutils literal notranslate"><span class="pre">envelope</span></code>, <code class="docutils literal notranslate"><span class="pre">fire</span></code>, <code class="docutils literal notranslate"><span class="pre">flag</span></code>, <code class="docutils literal notranslate"><span class="pre">flask</span></code>, <code class="docutils literal notranslate"><span class="pre">globe</span></code>, <code class="docutils literal notranslate"><span class="pre">heart</span></code>, <code class="docutils literal notranslate"><span class="pre">leaf</span></code>, <code class="docutils literal notranslate"><span class="pre">legal</span></code>, <code class="docutils literal notranslate"><span class="pre">life-ring</span></code>, <code class="docutils literal notranslate"><span class="pre">line-chart</span></code>, <code class="docutils literal notranslate"><span class="pre">magic</span></code>, <code class="docutils literal notranslate"><span class="pre">mobile</span></code>, <code class="docutils literal notranslate"><span class="pre">money</span></code>, <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">paper-plane</span></code>, <code class="docutils literal notranslate"><span class="pre">pie-chart</span></code>, <code class="docutils literal notranslate"><span class="pre">puzzle-piece</span></code>, <code class="docutils literal notranslate"><span class="pre">road</span></code>, <code class="docutils literal notranslate"><span class="pre">rocket</span></code>, <code class="docutils literal notranslate"><span class="pre">shopping-cart</span></code>, <code class="docutils literal notranslate"><span class="pre">sitemap</span></code>, <code class="docutils literal notranslate"><span class="pre">sliders</span></code>, <code class="docutils literal notranslate"><span class="pre">tablet</span></code>, <code class="docutils literal notranslate"><span class="pre">thumbs-down</span></code>, <code class="docutils literal notranslate"><span class="pre">thumbs-up</span></code>, <code class="docutils literal notranslate"><span class="pre">trophy</span></code>, <code class="docutils literal notranslate"><span class="pre">usd</span></code>, <code class="docutils literal notranslate"><span class="pre">user</span></code>, and <code class="docutils literal notranslate"><span class="pre">users</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">bar-chart</span></code>.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of the dashboard.</p></li>
<li><p><strong>visibility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determines who can see the dashboard in an account. Valid values are <code class="docutils literal notranslate"><span class="pre">all</span></code> or <code class="docutils literal notranslate"><span class="pre">owner</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">all</span></code>.</p></li>
<li><p><strong>widgets</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardWidgetArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A nested block that describes a visualization.  Up to 300 <code class="docutils literal notranslate"><span class="pre">widget</span></code> blocks are allowed in a dashboard definition. See Nested widget blocks below for details.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_newrelic.Dashboard.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dashboard_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">editable</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>DashboardFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>DashboardFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grid_column_count</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">icon</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">widgets</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>DashboardWidgetArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>DashboardWidgetArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>DashboardWidgetArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>DashboardWidgetArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_newrelic.Dashboard" title="pulumi_newrelic.Dashboard">Dashboard</a><a class="headerlink" href="#pulumi_newrelic.Dashboard.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Dashboard resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dashboard_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL for viewing the dashboard.</p></li>
<li><p><strong>editable</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determines who can edit the dashboard in an account. Valid values are <code class="docutils literal notranslate"><span class="pre">all</span></code>,  <code class="docutils literal notranslate"><span class="pre">editable_by_all</span></code>, <code class="docutils literal notranslate"><span class="pre">editable_by_owner</span></code>, or <code class="docutils literal notranslate"><span class="pre">read_only</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">editable_by_all</span></code>.</p></li>
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardFilterArgs'</em><em>]</em><em>]</em>) – A nested block that describes a dashboard filter.  Exactly one nested <code class="docutils literal notranslate"><span class="pre">filter</span></code> block is allowed. See Nested filter block below for details.</p></li>
<li><p><strong>grid_column_count</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of columns to use when organizing and displaying widgets. New Relic One supports a 3 column grid and a 12 column grid. New Relic Insights supports a 3 column grid.</p></li>
<li><p><strong>icon</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The icon for the dashboard.  Valid values are <code class="docutils literal notranslate"><span class="pre">adjust</span></code>, <code class="docutils literal notranslate"><span class="pre">archive</span></code>, <code class="docutils literal notranslate"><span class="pre">bar-chart</span></code>, <code class="docutils literal notranslate"><span class="pre">bell</span></code>, <code class="docutils literal notranslate"><span class="pre">bolt</span></code>, <code class="docutils literal notranslate"><span class="pre">bug</span></code>, <code class="docutils literal notranslate"><span class="pre">bullhorn</span></code>, <code class="docutils literal notranslate"><span class="pre">bullseye</span></code>, <code class="docutils literal notranslate"><span class="pre">clock-o</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud</span></code>, <code class="docutils literal notranslate"><span class="pre">cog</span></code>, <code class="docutils literal notranslate"><span class="pre">comments-o</span></code>, <code class="docutils literal notranslate"><span class="pre">crosshairs</span></code>, <code class="docutils literal notranslate"><span class="pre">dashboard</span></code>, <code class="docutils literal notranslate"><span class="pre">envelope</span></code>, <code class="docutils literal notranslate"><span class="pre">fire</span></code>, <code class="docutils literal notranslate"><span class="pre">flag</span></code>, <code class="docutils literal notranslate"><span class="pre">flask</span></code>, <code class="docutils literal notranslate"><span class="pre">globe</span></code>, <code class="docutils literal notranslate"><span class="pre">heart</span></code>, <code class="docutils literal notranslate"><span class="pre">leaf</span></code>, <code class="docutils literal notranslate"><span class="pre">legal</span></code>, <code class="docutils literal notranslate"><span class="pre">life-ring</span></code>, <code class="docutils literal notranslate"><span class="pre">line-chart</span></code>, <code class="docutils literal notranslate"><span class="pre">magic</span></code>, <code class="docutils literal notranslate"><span class="pre">mobile</span></code>, <code class="docutils literal notranslate"><span class="pre">money</span></code>, <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">paper-plane</span></code>, <code class="docutils literal notranslate"><span class="pre">pie-chart</span></code>, <code class="docutils literal notranslate"><span class="pre">puzzle-piece</span></code>, <code class="docutils literal notranslate"><span class="pre">road</span></code>, <code class="docutils literal notranslate"><span class="pre">rocket</span></code>, <code class="docutils literal notranslate"><span class="pre">shopping-cart</span></code>, <code class="docutils literal notranslate"><span class="pre">sitemap</span></code>, <code class="docutils literal notranslate"><span class="pre">sliders</span></code>, <code class="docutils literal notranslate"><span class="pre">tablet</span></code>, <code class="docutils literal notranslate"><span class="pre">thumbs-down</span></code>, <code class="docutils literal notranslate"><span class="pre">thumbs-up</span></code>, <code class="docutils literal notranslate"><span class="pre">trophy</span></code>, <code class="docutils literal notranslate"><span class="pre">usd</span></code>, <code class="docutils literal notranslate"><span class="pre">user</span></code>, and <code class="docutils literal notranslate"><span class="pre">users</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">bar-chart</span></code>.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of the dashboard.</p></li>
<li><p><strong>visibility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determines who can see the dashboard in an account. Valid values are <code class="docutils literal notranslate"><span class="pre">all</span></code> or <code class="docutils literal notranslate"><span class="pre">owner</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">all</span></code>.</p></li>
<li><p><strong>widgets</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardWidgetArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A nested block that describes a visualization.  Up to 300 <code class="docutils literal notranslate"><span class="pre">widget</span></code> blocks are allowed in a dashboard definition. See Nested widget blocks below for details.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.Dashboard.dashboard_url">
<em class="property">property </em><code class="sig-name descname">dashboard_url</code><a class="headerlink" href="#pulumi_newrelic.Dashboard.dashboard_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL for viewing the dashboard.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.Dashboard.editable">
<em class="property">property </em><code class="sig-name descname">editable</code><a class="headerlink" href="#pulumi_newrelic.Dashboard.editable" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines who can edit the dashboard in an account. Valid values are <code class="docutils literal notranslate"><span class="pre">all</span></code>,  <code class="docutils literal notranslate"><span class="pre">editable_by_all</span></code>, <code class="docutils literal notranslate"><span class="pre">editable_by_owner</span></code>, or <code class="docutils literal notranslate"><span class="pre">read_only</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">editable_by_all</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.Dashboard.filter">
<em class="property">property </em><code class="sig-name descname">filter</code><a class="headerlink" href="#pulumi_newrelic.Dashboard.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>A nested block that describes a dashboard filter.  Exactly one nested <code class="docutils literal notranslate"><span class="pre">filter</span></code> block is allowed. See Nested filter block below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.Dashboard.grid_column_count">
<em class="property">property </em><code class="sig-name descname">grid_column_count</code><a class="headerlink" href="#pulumi_newrelic.Dashboard.grid_column_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of columns to use when organizing and displaying widgets. New Relic One supports a 3 column grid and a 12 column grid. New Relic Insights supports a 3 column grid.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.Dashboard.icon">
<em class="property">property </em><code class="sig-name descname">icon</code><a class="headerlink" href="#pulumi_newrelic.Dashboard.icon" title="Permalink to this definition">¶</a></dt>
<dd><p>The icon for the dashboard.  Valid values are <code class="docutils literal notranslate"><span class="pre">adjust</span></code>, <code class="docutils literal notranslate"><span class="pre">archive</span></code>, <code class="docutils literal notranslate"><span class="pre">bar-chart</span></code>, <code class="docutils literal notranslate"><span class="pre">bell</span></code>, <code class="docutils literal notranslate"><span class="pre">bolt</span></code>, <code class="docutils literal notranslate"><span class="pre">bug</span></code>, <code class="docutils literal notranslate"><span class="pre">bullhorn</span></code>, <code class="docutils literal notranslate"><span class="pre">bullseye</span></code>, <code class="docutils literal notranslate"><span class="pre">clock-o</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud</span></code>, <code class="docutils literal notranslate"><span class="pre">cog</span></code>, <code class="docutils literal notranslate"><span class="pre">comments-o</span></code>, <code class="docutils literal notranslate"><span class="pre">crosshairs</span></code>, <code class="docutils literal notranslate"><span class="pre">dashboard</span></code>, <code class="docutils literal notranslate"><span class="pre">envelope</span></code>, <code class="docutils literal notranslate"><span class="pre">fire</span></code>, <code class="docutils literal notranslate"><span class="pre">flag</span></code>, <code class="docutils literal notranslate"><span class="pre">flask</span></code>, <code class="docutils literal notranslate"><span class="pre">globe</span></code>, <code class="docutils literal notranslate"><span class="pre">heart</span></code>, <code class="docutils literal notranslate"><span class="pre">leaf</span></code>, <code class="docutils literal notranslate"><span class="pre">legal</span></code>, <code class="docutils literal notranslate"><span class="pre">life-ring</span></code>, <code class="docutils literal notranslate"><span class="pre">line-chart</span></code>, <code class="docutils literal notranslate"><span class="pre">magic</span></code>, <code class="docutils literal notranslate"><span class="pre">mobile</span></code>, <code class="docutils literal notranslate"><span class="pre">money</span></code>, <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">paper-plane</span></code>, <code class="docutils literal notranslate"><span class="pre">pie-chart</span></code>, <code class="docutils literal notranslate"><span class="pre">puzzle-piece</span></code>, <code class="docutils literal notranslate"><span class="pre">road</span></code>, <code class="docutils literal notranslate"><span class="pre">rocket</span></code>, <code class="docutils literal notranslate"><span class="pre">shopping-cart</span></code>, <code class="docutils literal notranslate"><span class="pre">sitemap</span></code>, <code class="docutils literal notranslate"><span class="pre">sliders</span></code>, <code class="docutils literal notranslate"><span class="pre">tablet</span></code>, <code class="docutils literal notranslate"><span class="pre">thumbs-down</span></code>, <code class="docutils literal notranslate"><span class="pre">thumbs-up</span></code>, <code class="docutils literal notranslate"><span class="pre">trophy</span></code>, <code class="docutils literal notranslate"><span class="pre">usd</span></code>, <code class="docutils literal notranslate"><span class="pre">user</span></code>, and <code class="docutils literal notranslate"><span class="pre">users</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">bar-chart</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.Dashboard.title">
<em class="property">property </em><code class="sig-name descname">title</code><a class="headerlink" href="#pulumi_newrelic.Dashboard.title" title="Permalink to this definition">¶</a></dt>
<dd><p>The title of the dashboard.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.Dashboard.visibility">
<em class="property">property </em><code class="sig-name descname">visibility</code><a class="headerlink" href="#pulumi_newrelic.Dashboard.visibility" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines who can see the dashboard in an account. Valid values are <code class="docutils literal notranslate"><span class="pre">all</span></code> or <code class="docutils literal notranslate"><span class="pre">owner</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">all</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.Dashboard.widgets">
<em class="property">property </em><code class="sig-name descname">widgets</code><a class="headerlink" href="#pulumi_newrelic.Dashboard.widgets" title="Permalink to this definition">¶</a></dt>
<dd><p>A nested block that describes a visualization.  Up to 300 <code class="docutils literal notranslate"><span class="pre">widget</span></code> blocks are allowed in a dashboard definition. See Nested widget blocks below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.Dashboard.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.Dashboard.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.Dashboard.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.Dashboard.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.EntityTags">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">EntityTags</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">guid</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>EntityTagsTagArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>EntityTagsTagArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>EntityTagsTagArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>EntityTagsTagArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.EntityTags" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to create, update, and delete tags for a New Relic One entity.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foo_entity</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">get_entity</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Example application&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;APPLICATION&quot;</span><span class="p">,</span>
    <span class="n">domain</span><span class="o">=</span><span class="s2">&quot;APM&quot;</span><span class="p">)</span>
<span class="n">foo_entity_tags</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">EntityTags</span><span class="p">(</span><span class="s2">&quot;fooEntityTags&quot;</span><span class="p">,</span>
    <span class="n">guid</span><span class="o">=</span><span class="n">foo_entity</span><span class="o">.</span><span class="n">guid</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span>
        <span class="n">newrelic</span><span class="o">.</span><span class="n">EntityTagsTagArgs</span><span class="p">(</span>
            <span class="n">key</span><span class="o">=</span><span class="s2">&quot;my-key&quot;</span><span class="p">,</span>
            <span class="n">values</span><span class="o">=</span><span class="p">[</span>
                <span class="s2">&quot;my-value&quot;</span><span class="p">,</span>
                <span class="s2">&quot;my-other-value&quot;</span><span class="p">,</span>
            <span class="p">],</span>
        <span class="p">),</span>
        <span class="n">newrelic</span><span class="o">.</span><span class="n">EntityTagsTagArgs</span><span class="p">(</span>
            <span class="n">key</span><span class="o">=</span><span class="s2">&quot;my-key-2&quot;</span><span class="p">,</span>
            <span class="n">values</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;my-value-2&quot;</span><span class="p">],</span>
        <span class="p">),</span>
    <span class="p">])</span>
</pre></div>
</div>
<p>New Relic One entity tags can be imported using a concatenated string of the format</p>
<p><code class="docutils literal notranslate"><span class="pre">&lt;guid&gt;</span></code>, e.g. bash</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import newrelic:index/entityTags:EntityTags foo MjUyMDUyOHxBUE18QVBRTElDQVRJT058MjE1MDM3Nzk1
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>guid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The guid of the entity to tag.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'EntityTagsTagArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A nested block that describes an entity tag. See Nested tag blocks below for details.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_newrelic.EntityTags.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">guid</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>EntityTagsTagArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>EntityTagsTagArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>EntityTagsTagArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>EntityTagsTagArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_newrelic.EntityTags" title="pulumi_newrelic.EntityTags">EntityTags</a><a class="headerlink" href="#pulumi_newrelic.EntityTags.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EntityTags resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>guid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The guid of the entity to tag.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'EntityTagsTagArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A nested block that describes an entity tag. See Nested tag blocks below for details.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.EntityTags.guid">
<em class="property">property </em><code class="sig-name descname">guid</code><a class="headerlink" href="#pulumi_newrelic.EntityTags.guid" title="Permalink to this definition">¶</a></dt>
<dd><p>The guid of the entity to tag.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.EntityTags.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_newrelic.EntityTags.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A nested block that describes an entity tag. See Nested tag blocks below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.EntityTags.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.EntityTags.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.EntityTags.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.EntityTags.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.EventsToMetricsRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">EventsToMetricsRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nrql</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.EventsToMetricsRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to create, update, and delete New Relic Events to Metrics rules.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">EventsToMetricsRule</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">account_id</span><span class="o">=</span><span class="mi">12345</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Example description&quot;</span><span class="p">,</span>
    <span class="n">nrql</span><span class="o">=</span><span class="s2">&quot;SELECT uniqueCount(account_id) AS ``Transaction.account_id`` FROM Transaction FACET appName, name&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>New Relic Events to Metrics rules can be imported using a concatenated string of the format</p>
<p><code class="docutils literal notranslate"><span class="pre">&lt;account_id&gt;:&lt;rule_id&gt;</span></code>, e.g. bash</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import newrelic:index/eventsToMetricsRule:EventsToMetricsRule foo <span class="m">12345</span>:34567
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Account with the event and where the metrics will be put.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Provides additional information about the rule.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – True means this rule is enabled. False means the rule is currently not creating metrics.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule. This must be unique within an account.</p></li>
<li><p><strong>nrql</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Explains how to create metrics from events.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_newrelic.EventsToMetricsRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nrql</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rule_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_newrelic.EventsToMetricsRule" title="pulumi_newrelic.EventsToMetricsRule">EventsToMetricsRule</a><a class="headerlink" href="#pulumi_newrelic.EventsToMetricsRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EventsToMetricsRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Account with the event and where the metrics will be put.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Provides additional information about the rule.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – True means this rule is enabled. False means the rule is currently not creating metrics.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule. This must be unique within an account.</p></li>
<li><p><strong>nrql</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Explains how to create metrics from events.</p></li>
<li><p><strong>rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id, uniquely identifying the rule.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.EventsToMetricsRule.account_id">
<em class="property">property </em><code class="sig-name descname">account_id</code><a class="headerlink" href="#pulumi_newrelic.EventsToMetricsRule.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account with the event and where the metrics will be put.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.EventsToMetricsRule.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_newrelic.EventsToMetricsRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides additional information about the rule.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.EventsToMetricsRule.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_newrelic.EventsToMetricsRule.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>True means this rule is enabled. False means the rule is currently not creating metrics.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.EventsToMetricsRule.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_newrelic.EventsToMetricsRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the rule. This must be unique within an account.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.EventsToMetricsRule.nrql">
<em class="property">property </em><code class="sig-name descname">nrql</code><a class="headerlink" href="#pulumi_newrelic.EventsToMetricsRule.nrql" title="Permalink to this definition">¶</a></dt>
<dd><p>Explains how to create metrics from events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.EventsToMetricsRule.rule_id">
<em class="property">property </em><code class="sig-name descname">rule_id</code><a class="headerlink" href="#pulumi_newrelic.EventsToMetricsRule.rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id, uniquely identifying the rule.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.EventsToMetricsRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.EventsToMetricsRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.EventsToMetricsRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.EventsToMetricsRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.GetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">GetAccountResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.GetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccount.</p>
<dl class="py method">
<dt id="pulumi_newrelic.GetAccountResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_newrelic.GetAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_newrelic.GetAlertChannelResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">GetAlertChannelResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.GetAlertChannelResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAlertChannel.</p>
<dl class="py method">
<dt id="pulumi_newrelic.GetAlertChannelResult.config">
<em class="property">property </em><code class="sig-name descname">config</code><a class="headerlink" href="#pulumi_newrelic.GetAlertChannelResult.config" title="Permalink to this definition">¶</a></dt>
<dd><p>Alert channel configuration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.GetAlertChannelResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_newrelic.GetAlertChannelResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.GetAlertChannelResult.policy_ids">
<em class="property">property </em><code class="sig-name descname">policy_ids</code><a class="headerlink" href="#pulumi_newrelic.GetAlertChannelResult.policy_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of policy IDs associated with the alert channel.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.GetAlertChannelResult.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_newrelic.GetAlertChannelResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Alert channel type, either: <code class="docutils literal notranslate"><span class="pre">email</span></code>, <code class="docutils literal notranslate"><span class="pre">opsgenie</span></code>, <code class="docutils literal notranslate"><span class="pre">pagerduty</span></code>, <code class="docutils literal notranslate"><span class="pre">slack</span></code>, <code class="docutils literal notranslate"><span class="pre">victorops</span></code>, or <code class="docutils literal notranslate"><span class="pre">webhook</span></code>.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_newrelic.GetAlertPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">GetAlertPolicyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">incident_preference</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated_at</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.GetAlertPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAlertPolicy.</p>
<dl class="py method">
<dt id="pulumi_newrelic.GetAlertPolicyResult.created_at">
<em class="property">property </em><code class="sig-name descname">created_at</code><a class="headerlink" href="#pulumi_newrelic.GetAlertPolicyResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time the policy was created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.GetAlertPolicyResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_newrelic.GetAlertPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.GetAlertPolicyResult.incident_preference">
<em class="property">property </em><code class="sig-name descname">incident_preference</code><a class="headerlink" href="#pulumi_newrelic.GetAlertPolicyResult.incident_preference" title="Permalink to this definition">¶</a></dt>
<dd><p>The rollup strategy for the policy. Options include: PER_POLICY, PER_CONDITION, or PER_CONDITION_AND_TARGET. The default is PER_POLICY.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.GetAlertPolicyResult.updated_at">
<em class="property">property </em><code class="sig-name descname">updated_at</code><a class="headerlink" href="#pulumi_newrelic.GetAlertPolicyResult.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time the policy was last updated.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_newrelic.GetApplicationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">GetApplicationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">host_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.GetApplicationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getApplication.</p>
<dl class="py method">
<dt id="pulumi_newrelic.GetApplicationResult.host_ids">
<em class="property">property </em><code class="sig-name descname">host_ids</code><a class="headerlink" href="#pulumi_newrelic.GetApplicationResult.host_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of host IDs associated with the application.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.GetApplicationResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_newrelic.GetApplicationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.GetApplicationResult.instance_ids">
<em class="property">property </em><code class="sig-name descname">instance_ids</code><a class="headerlink" href="#pulumi_newrelic.GetApplicationResult.instance_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of instance IDs associated with the application.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_newrelic.GetEntityResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">GetEntityResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">guid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">serving_apm_application_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.GetEntityResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getEntity.</p>
<dl class="py method">
<dt id="pulumi_newrelic.GetEntityResult.account_id">
<em class="property">property </em><code class="sig-name descname">account_id</code><a class="headerlink" href="#pulumi_newrelic.GetEntityResult.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The New Relic account ID associated with this entity.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.GetEntityResult.application_id">
<em class="property">property </em><code class="sig-name descname">application_id</code><a class="headerlink" href="#pulumi_newrelic.GetEntityResult.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain-specific application ID of the entity. Only returned for APM and Browser applications.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.GetEntityResult.guid">
<em class="property">property </em><code class="sig-name descname">guid</code><a class="headerlink" href="#pulumi_newrelic.GetEntityResult.guid" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique GUID of the entity.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.GetEntityResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_newrelic.GetEntityResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_newrelic.GetKeyTransactionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">GetKeyTransactionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.GetKeyTransactionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKeyTransaction.</p>
<dl class="py method">
<dt id="pulumi_newrelic.GetKeyTransactionResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_newrelic.GetKeyTransactionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_newrelic.InfraAlertCondition">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">InfraAlertCondition</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comparison</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">critical</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>InfraAlertConditionCriticalArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>InfraAlertConditionCriticalArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_provider</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">process_where</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">runbook_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">select</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">violation_close_timer</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">warning</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>InfraAlertConditionWarningArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>InfraAlertConditionWarningArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">where</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to create and manage Infrastructure alert conditions in New Relic.</p>
<blockquote>
<div><p><strong>NOTE:</strong> The NrqlAlertCondition resource is preferred for configuring alerts conditions. In most cases feature parity can be achieved with a NRQL query. Other condition types may be deprecated in the future and receive fewer product updates.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertPolicy</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">)</span>
<span class="n">high_disk_usage</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">InfraAlertCondition</span><span class="p">(</span><span class="s2">&quot;highDiskUsage&quot;</span><span class="p">,</span>
    <span class="n">policy_id</span><span class="o">=</span><span class="n">foo</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;infra_metric&quot;</span><span class="p">,</span>
    <span class="n">event</span><span class="o">=</span><span class="s2">&quot;StorageSample&quot;</span><span class="p">,</span>
    <span class="n">select</span><span class="o">=</span><span class="s2">&quot;diskUsedPercent&quot;</span><span class="p">,</span>
    <span class="n">comparison</span><span class="o">=</span><span class="s2">&quot;above&quot;</span><span class="p">,</span>
    <span class="n">where</span><span class="o">=</span><span class="s2">&quot;(hostname LIKE &#39;</span><span class="si">%f</span><span class="s2">rontend%&#39;)&quot;</span><span class="p">,</span>
    <span class="n">critical</span><span class="o">=</span><span class="n">newrelic</span><span class="o">.</span><span class="n">InfraAlertConditionCriticalArgs</span><span class="p">(</span>
        <span class="n">duration</span><span class="o">=</span><span class="mi">25</span><span class="p">,</span>
        <span class="n">value</span><span class="o">=</span><span class="mi">90</span><span class="p">,</span>
        <span class="n">time_function</span><span class="o">=</span><span class="s2">&quot;all&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">warning</span><span class="o">=</span><span class="n">newrelic</span><span class="o">.</span><span class="n">InfraAlertConditionWarningArgs</span><span class="p">(</span>
        <span class="n">duration</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
        <span class="n">value</span><span class="o">=</span><span class="mi">80</span><span class="p">,</span>
        <span class="n">time_function</span><span class="o">=</span><span class="s2">&quot;all&quot;</span><span class="p">,</span>
    <span class="p">))</span>
<span class="n">high_db_conn_count</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">InfraAlertCondition</span><span class="p">(</span><span class="s2">&quot;highDbConnCount&quot;</span><span class="p">,</span>
    <span class="n">policy_id</span><span class="o">=</span><span class="n">foo</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;infra_metric&quot;</span><span class="p">,</span>
    <span class="n">event</span><span class="o">=</span><span class="s2">&quot;DatastoreSample&quot;</span><span class="p">,</span>
    <span class="n">select</span><span class="o">=</span><span class="s2">&quot;provider.databaseConnections.Average&quot;</span><span class="p">,</span>
    <span class="n">comparison</span><span class="o">=</span><span class="s2">&quot;above&quot;</span><span class="p">,</span>
    <span class="n">where</span><span class="o">=</span><span class="s2">&quot;(hostname LIKE &#39;</span><span class="si">%d</span><span class="s2">b%&#39;)&quot;</span><span class="p">,</span>
    <span class="n">integration_provider</span><span class="o">=</span><span class="s2">&quot;RdsDbInstance&quot;</span><span class="p">,</span>
    <span class="n">critical</span><span class="o">=</span><span class="n">newrelic</span><span class="o">.</span><span class="n">InfraAlertConditionCriticalArgs</span><span class="p">(</span>
        <span class="n">duration</span><span class="o">=</span><span class="mi">25</span><span class="p">,</span>
        <span class="n">value</span><span class="o">=</span><span class="mi">90</span><span class="p">,</span>
        <span class="n">time_function</span><span class="o">=</span><span class="s2">&quot;all&quot;</span><span class="p">,</span>
    <span class="p">))</span>
<span class="n">process_not_running</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">InfraAlertCondition</span><span class="p">(</span><span class="s2">&quot;processNotRunning&quot;</span><span class="p">,</span>
    <span class="n">policy_id</span><span class="o">=</span><span class="n">foo</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;infra_process_running&quot;</span><span class="p">,</span>
    <span class="n">comparison</span><span class="o">=</span><span class="s2">&quot;equal&quot;</span><span class="p">,</span>
    <span class="n">where</span><span class="o">=</span><span class="s2">&quot;hostname = &#39;web01&#39;&quot;</span><span class="p">,</span>
    <span class="n">process_where</span><span class="o">=</span><span class="s2">&quot;commandName = &#39;/usr/bin/ruby&#39;&quot;</span><span class="p">,</span>
    <span class="n">critical</span><span class="o">=</span><span class="n">newrelic</span><span class="o">.</span><span class="n">InfraAlertConditionCriticalArgs</span><span class="p">(</span>
        <span class="n">duration</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
        <span class="n">value</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="p">))</span>
<span class="n">host_not_reporting</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">InfraAlertCondition</span><span class="p">(</span><span class="s2">&quot;hostNotReporting&quot;</span><span class="p">,</span>
    <span class="n">policy_id</span><span class="o">=</span><span class="n">foo</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;infra_host_not_reporting&quot;</span><span class="p">,</span>
    <span class="n">where</span><span class="o">=</span><span class="s2">&quot;(hostname LIKE &#39;</span><span class="si">%f</span><span class="s2">rontend%&#39;)&quot;</span><span class="p">,</span>
    <span class="n">critical</span><span class="o">=</span><span class="n">newrelic</span><span class="o">.</span><span class="n">InfraAlertConditionCriticalArgs</span><span class="p">(</span>
        <span class="n">duration</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
    <span class="p">))</span>
</pre></div>
</div>
<p>The <code class="docutils literal notranslate"><span class="pre">critical</span></code> and <code class="docutils literal notranslate"><span class="pre">warning</span></code> threshold mapping supports the following arguments:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> - (Required) Identifies the number of minutes the threshold must be passed or met for the alert to trigger. Threshold durations must be between 1 and 60 minutes (inclusive).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> - (Optional) Threshold value, computed against the <code class="docutils literal notranslate"><span class="pre">comparison</span></code> operator. Supported by <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> and <code class="docutils literal notranslate"><span class="pre">infra_process_running</span></code> alert condition types.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">time_function</span></code> - (Optional) Indicates if the condition needs to be sustained or to just break the threshold once; <code class="docutils literal notranslate"><span class="pre">all</span></code> or <code class="docutils literal notranslate"><span class="pre">any</span></code>. Supported by the <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> alert condition type.</p></li>
</ul>
<p>Infrastructure alert conditions can be imported using a composite ID of <code class="docutils literal notranslate"><span class="pre">&lt;policy_id&gt;:&lt;condition_id&gt;</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import newrelic:index/infraAlertCondition:InfraAlertCondition main <span class="m">12345</span>:67890
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>comparison</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The operator used to evaluate the threshold value.  Valid values are <code class="docutils literal notranslate"><span class="pre">above</span></code>, <code class="docutils literal notranslate"><span class="pre">below</span></code>, and <code class="docutils literal notranslate"><span class="pre">equal</span></code>.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> and <code class="docutils literal notranslate"><span class="pre">infra_process_running</span></code> condition types.</p></li>
<li><p><strong>critical</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'InfraAlertConditionCriticalArgs'</em><em>]</em><em>]</em>) – Identifies the threshold parameters for opening a critical alert violation. See Thresholds below for details.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Infrastructure alert condition.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the condition is turned on or off.  Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>event</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metric event; for example, <code class="docutils literal notranslate"><span class="pre">SystemSample</span></code> or <code class="docutils literal notranslate"><span class="pre">StorageSample</span></code>.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> condition type.</p></li>
<li><p><strong>integration_provider</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – For alerts on integrations, use this instead of <code class="docutils literal notranslate"><span class="pre">event</span></code>.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> condition type.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Infrastructure alert condition’s name.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the alert policy where this condition should be used.</p></li>
<li><p><strong>process_where</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Any filters applied to processes; for example: <code class="docutils literal notranslate"><span class="pre">commandName</span> <span class="pre">=</span> <span class="pre">'java'</span></code>.  Required by the <code class="docutils literal notranslate"><span class="pre">infra_process_running</span></code> condition type.</p></li>
<li><p><strong>runbook_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Runbook URL to display in notifications.</p></li>
<li><p><strong>select</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The attribute name to identify the metric being targeted; for example, <code class="docutils literal notranslate"><span class="pre">cpuPercent</span></code>, <code class="docutils literal notranslate"><span class="pre">diskFreePercent</span></code>, or <code class="docutils literal notranslate"><span class="pre">memoryResidentSizeBytes</span></code>.  The underlying API will automatically populate this value for Infrastructure integrations (for example <code class="docutils literal notranslate"><span class="pre">diskFreePercent</span></code>), so make sure to explicitly include this value to avoid diff issues.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> condition type.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of Infrastructure alert condition.  Valid values are  <code class="docutils literal notranslate"><span class="pre">infra_process_running</span></code>, <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code>, and <code class="docutils literal notranslate"><span class="pre">infra_host_not_reporting</span></code>.</p></li>
<li><p><strong>violation_close_timer</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Determines how much time will pass before a violation is automatically closed. Setting the time limit to 0 prevents a violation from being force-closed.</p></li>
<li><p><strong>warning</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'InfraAlertConditionWarningArgs'</em><em>]</em><em>]</em>) – Identifies the threshold parameters for opening a warning alert violation. See Thresholds below for details.</p></li>
<li><p><strong>where</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If applicable, this identifies any Infrastructure host filters used; for example: <code class="docutils literal notranslate"><span class="pre">hostname</span> <span class="pre">LIKE</span> <span class="pre">'%cassandra%'</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_newrelic.InfraAlertCondition.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comparison</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">critical</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>InfraAlertConditionCriticalArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>InfraAlertConditionCriticalArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_provider</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">process_where</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">runbook_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">select</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated_at</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">violation_close_timer</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">warning</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>InfraAlertConditionWarningArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>InfraAlertConditionWarningArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">where</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_newrelic.InfraAlertCondition" title="pulumi_newrelic.InfraAlertCondition">InfraAlertCondition</a><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing InfraAlertCondition resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>comparison</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The operator used to evaluate the threshold value.  Valid values are <code class="docutils literal notranslate"><span class="pre">above</span></code>, <code class="docutils literal notranslate"><span class="pre">below</span></code>, and <code class="docutils literal notranslate"><span class="pre">equal</span></code>.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> and <code class="docutils literal notranslate"><span class="pre">infra_process_running</span></code> condition types.</p></li>
<li><p><strong>created_at</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The timestamp the alert condition was created.</p></li>
<li><p><strong>critical</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'InfraAlertConditionCriticalArgs'</em><em>]</em><em>]</em>) – Identifies the threshold parameters for opening a critical alert violation. See Thresholds below for details.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Infrastructure alert condition.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the condition is turned on or off.  Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>event</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metric event; for example, <code class="docutils literal notranslate"><span class="pre">SystemSample</span></code> or <code class="docutils literal notranslate"><span class="pre">StorageSample</span></code>.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> condition type.</p></li>
<li><p><strong>integration_provider</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – For alerts on integrations, use this instead of <code class="docutils literal notranslate"><span class="pre">event</span></code>.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> condition type.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Infrastructure alert condition’s name.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the alert policy where this condition should be used.</p></li>
<li><p><strong>process_where</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Any filters applied to processes; for example: <code class="docutils literal notranslate"><span class="pre">commandName</span> <span class="pre">=</span> <span class="pre">'java'</span></code>.  Required by the <code class="docutils literal notranslate"><span class="pre">infra_process_running</span></code> condition type.</p></li>
<li><p><strong>runbook_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Runbook URL to display in notifications.</p></li>
<li><p><strong>select</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The attribute name to identify the metric being targeted; for example, <code class="docutils literal notranslate"><span class="pre">cpuPercent</span></code>, <code class="docutils literal notranslate"><span class="pre">diskFreePercent</span></code>, or <code class="docutils literal notranslate"><span class="pre">memoryResidentSizeBytes</span></code>.  The underlying API will automatically populate this value for Infrastructure integrations (for example <code class="docutils literal notranslate"><span class="pre">diskFreePercent</span></code>), so make sure to explicitly include this value to avoid diff issues.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> condition type.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of Infrastructure alert condition.  Valid values are  <code class="docutils literal notranslate"><span class="pre">infra_process_running</span></code>, <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code>, and <code class="docutils literal notranslate"><span class="pre">infra_host_not_reporting</span></code>.</p></li>
<li><p><strong>updated_at</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The timestamp the alert condition was last updated.</p></li>
<li><p><strong>violation_close_timer</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Determines how much time will pass before a violation is automatically closed. Setting the time limit to 0 prevents a violation from being force-closed.</p></li>
<li><p><strong>warning</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'InfraAlertConditionWarningArgs'</em><em>]</em><em>]</em>) – Identifies the threshold parameters for opening a warning alert violation. See Thresholds below for details.</p></li>
<li><p><strong>where</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If applicable, this identifies any Infrastructure host filters used; for example: <code class="docutils literal notranslate"><span class="pre">hostname</span> <span class="pre">LIKE</span> <span class="pre">'%cassandra%'</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.InfraAlertCondition.comparison">
<em class="property">property </em><code class="sig-name descname">comparison</code><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.comparison" title="Permalink to this definition">¶</a></dt>
<dd><p>The operator used to evaluate the threshold value.  Valid values are <code class="docutils literal notranslate"><span class="pre">above</span></code>, <code class="docutils literal notranslate"><span class="pre">below</span></code>, and <code class="docutils literal notranslate"><span class="pre">equal</span></code>.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> and <code class="docutils literal notranslate"><span class="pre">infra_process_running</span></code> condition types.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.InfraAlertCondition.created_at">
<em class="property">property </em><code class="sig-name descname">created_at</code><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp the alert condition was created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.InfraAlertCondition.critical">
<em class="property">property </em><code class="sig-name descname">critical</code><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.critical" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifies the threshold parameters for opening a critical alert violation. See Thresholds below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.InfraAlertCondition.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Infrastructure alert condition.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.InfraAlertCondition.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the condition is turned on or off.  Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.InfraAlertCondition.event">
<em class="property">property </em><code class="sig-name descname">event</code><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.event" title="Permalink to this definition">¶</a></dt>
<dd><p>The metric event; for example, <code class="docutils literal notranslate"><span class="pre">SystemSample</span></code> or <code class="docutils literal notranslate"><span class="pre">StorageSample</span></code>.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> condition type.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.InfraAlertCondition.integration_provider">
<em class="property">property </em><code class="sig-name descname">integration_provider</code><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.integration_provider" title="Permalink to this definition">¶</a></dt>
<dd><p>For alerts on integrations, use this instead of <code class="docutils literal notranslate"><span class="pre">event</span></code>.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> condition type.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.InfraAlertCondition.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Infrastructure alert condition’s name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.InfraAlertCondition.policy_id">
<em class="property">property </em><code class="sig-name descname">policy_id</code><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the alert policy where this condition should be used.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.InfraAlertCondition.process_where">
<em class="property">property </em><code class="sig-name descname">process_where</code><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.process_where" title="Permalink to this definition">¶</a></dt>
<dd><p>Any filters applied to processes; for example: <code class="docutils literal notranslate"><span class="pre">commandName</span> <span class="pre">=</span> <span class="pre">'java'</span></code>.  Required by the <code class="docutils literal notranslate"><span class="pre">infra_process_running</span></code> condition type.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.InfraAlertCondition.runbook_url">
<em class="property">property </em><code class="sig-name descname">runbook_url</code><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.runbook_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Runbook URL to display in notifications.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.InfraAlertCondition.select">
<em class="property">property </em><code class="sig-name descname">select</code><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.select" title="Permalink to this definition">¶</a></dt>
<dd><p>The attribute name to identify the metric being targeted; for example, <code class="docutils literal notranslate"><span class="pre">cpuPercent</span></code>, <code class="docutils literal notranslate"><span class="pre">diskFreePercent</span></code>, or <code class="docutils literal notranslate"><span class="pre">memoryResidentSizeBytes</span></code>.  The underlying API will automatically populate this value for Infrastructure integrations (for example <code class="docutils literal notranslate"><span class="pre">diskFreePercent</span></code>), so make sure to explicitly include this value to avoid diff issues.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> condition type.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.InfraAlertCondition.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of Infrastructure alert condition.  Valid values are  <code class="docutils literal notranslate"><span class="pre">infra_process_running</span></code>, <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code>, and <code class="docutils literal notranslate"><span class="pre">infra_host_not_reporting</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.InfraAlertCondition.updated_at">
<em class="property">property </em><code class="sig-name descname">updated_at</code><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp the alert condition was last updated.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.InfraAlertCondition.violation_close_timer">
<em class="property">property </em><code class="sig-name descname">violation_close_timer</code><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.violation_close_timer" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines how much time will pass before a violation is automatically closed. Setting the time limit to 0 prevents a violation from being force-closed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.InfraAlertCondition.warning">
<em class="property">property </em><code class="sig-name descname">warning</code><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.warning" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifies the threshold parameters for opening a warning alert violation. See Thresholds below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.InfraAlertCondition.where">
<em class="property">property </em><code class="sig-name descname">where</code><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.where" title="Permalink to this definition">¶</a></dt>
<dd><p>If applicable, this identifies any Infrastructure host filters used; for example: <code class="docutils literal notranslate"><span class="pre">hostname</span> <span class="pre">LIKE</span> <span class="pre">'%cassandra%'</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.InfraAlertCondition.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.InfraAlertCondition.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.NrqlAlertCondition">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">NrqlAlertCondition</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aggregation_window</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">baseline_direction</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">close_violations_on_expiration</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">critical</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>NrqlAlertConditionCriticalArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NrqlAlertConditionCriticalArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expected_groups</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiration_duration</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fill_option</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fill_value</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>float<span class="p">, </span>Awaitable<span class="p">[</span>float<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_overlap</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nrql</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>NrqlAlertConditionNrqlArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NrqlAlertConditionNrqlArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">open_violation_on_expiration</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">open_violation_on_group_overlap</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">runbook_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">terms</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NrqlAlertConditionTermArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NrqlAlertConditionTermArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NrqlAlertConditionTermArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NrqlAlertConditionTermArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value_function</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">violation_time_limit</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">violation_time_limit_seconds</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">warning</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>NrqlAlertConditionWarningArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NrqlAlertConditionWarningArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to create and manage NRQL alert conditions in New Relic.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">nrql</span></code> block supports the following arguments:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> - (Required) The NRQL query to execute for the condition.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluation_offset</span></code> - (Optional<em>) Represented in minutes and must be within 1-20 minutes (inclusive). NRQL queries are evaluated in one-minute time windows. The start time depends on this value. It’s recommended to set this to 3 minutes. An offset of less than 3 minutes will trigger violations sooner, but you may see more false positives and negatives due to data latency. With ``evaluation_offset`` set to 3 minutes, the NRQL time window applied to your query will be: ``SINCE 3 minutes ago UNTIL 2 minutes ago``.:raw-html-m2r:`&lt;br&gt;`
:raw-html-m2r:`&lt;small&gt;`**</em>Note**: One of <code class="docutils literal notranslate"><span class="pre">evaluation_offset</span></code> <em>or</em> <code class="docutils literal notranslate"><span class="pre">since_value</span></code> must be set, but not both.&lt;/small&gt;</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">since_value</span></code> - (Optional<em>)  **DEPRECATED:*</em> Use <code class="docutils literal notranslate"><span class="pre">evaluation_offset</span></code> instead. The value to be used in the <code class="docutils literal notranslate"><span class="pre">SINCE</span> <span class="pre">&lt;X&gt;</span> <span class="pre">minutes</span> <span class="pre">ago</span></code> clause for the NRQL query. Must be between 1-20 (inclusive). <span class="raw-html-m2r"><br></span>
<span class="raw-html-m2r"><small></span><strong>*Note</strong>: One of <code class="docutils literal notranslate"><span class="pre">evaluation_offset</span></code> <em>or</em> <code class="docutils literal notranslate"><span class="pre">since_value</span></code> must be set, but not both.&lt;/small&gt;</p></li>
</ul>
<blockquote>
<div><p><strong>NOTE:</strong> The direct use of the <code class="docutils literal notranslate"><span class="pre">term</span></code> has been deprecated, and users should use <code class="docutils literal notranslate"><span class="pre">critical</span></code> and <code class="docutils literal notranslate"><span class="pre">warning</span></code> instead.  What follows now applies to the named priority attributes for <code class="docutils literal notranslate"><span class="pre">critical</span></code> and <code class="docutils literal notranslate"><span class="pre">warning</span></code>, but for those attributes the priority is not allowed.</p>
</div></blockquote>
<p>NRQL alert conditions support up to two terms. At least one <code class="docutils literal notranslate"><span class="pre">term</span></code> must have <code class="docutils literal notranslate"><span class="pre">priority</span></code> set to <code class="docutils literal notranslate"><span class="pre">critical</span></code> and the second optional <code class="docutils literal notranslate"><span class="pre">term</span></code> must have <code class="docutils literal notranslate"><span class="pre">priority</span></code> set to <code class="docutils literal notranslate"><span class="pre">warning</span></code>.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">term</span></code> block the following arguments:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> - (Optional) Valid values are <code class="docutils literal notranslate"><span class="pre">above</span></code>, <code class="docutils literal notranslate"><span class="pre">below</span></code>, or <code class="docutils literal notranslate"><span class="pre">equals</span></code> (case insensitive). Defaults to <code class="docutils literal notranslate"><span class="pre">equals</span></code>. Note that when using a <code class="docutils literal notranslate"><span class="pre">type</span></code> of <code class="docutils literal notranslate"><span class="pre">outlier</span></code>, the only valid option here is <code class="docutils literal notranslate"><span class="pre">above</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> - (Optional) <code class="docutils literal notranslate"><span class="pre">critical</span></code> or <code class="docutils literal notranslate"><span class="pre">warning</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">critical</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> - (Required) The value which will trigger a violation. Must be <code class="docutils literal notranslate"><span class="pre">0</span></code> or greater.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold_duration</span></code> - (Optional) The duration of time, in seconds, that the threshold must violate for in order to create a violation. Value must be a multiple of 60.
<span class="raw-html-m2r"><br></span>For <em>baseline</em> NRQL alert conditions, the value must be within 120-3600 seconds (inclusive).
<span class="raw-html-m2r"><br></span>For <em>static</em> NRQL alert conditions, the value must be within 120-7200 seconds (inclusive).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold_occurrences</span></code> - (Optional) The criteria for how many data points must be in violation for the specified threshold duration. Valid values are: <code class="docutils literal notranslate"><span class="pre">all</span></code> or <code class="docutils literal notranslate"><span class="pre">at_least_once</span></code> (case insensitive).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> - (Optional) <strong>DEPRECATED:</strong> Use <code class="docutils literal notranslate"><span class="pre">threshold_duration</span></code> instead. The duration of time, in <em>minutes</em>, that the threshold must violate for in order to create a violation. Must be within 1-120 (inclusive).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">time_function</span></code> - (Optional) <strong>DEPRECATED:</strong> Use <code class="docutils literal notranslate"><span class="pre">threshold_occurrences</span></code> instead. The criteria for how many data points must be in violation for the specified threshold duration. Valid values are: <code class="docutils literal notranslate"><span class="pre">all</span></code> or <code class="docutils literal notranslate"><span class="pre">any</span></code>.</p></li>
</ul>
<p>Alert conditions can be imported using a composite ID of <code class="docutils literal notranslate"><span class="pre">&lt;policy_id&gt;:&lt;condition_id&gt;:&lt;conditionType&gt;</span></code>, e.g. // For <code class="docutils literal notranslate"><span class="pre">baseline</span></code> conditions</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import newrelic:index/nrqlAlertCondition:NrqlAlertCondition foo <span class="m">538291</span>:6789035:baseline

// For <span class="sb">``</span>static<span class="sb">``</span> conditions
</pre></div>
</div>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import newrelic:index/nrqlAlertCondition:NrqlAlertCondition foo <span class="m">538291</span>:6789035:static

// For <span class="sb">``</span>outlier<span class="sb">``</span> conditions
</pre></div>
</div>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import newrelic:index/nrqlAlertCondition:NrqlAlertCondition foo <span class="m">538291</span>:6789035:outlier

The actual values <span class="k">for</span> <span class="sb">``</span>policy_id<span class="sb">``</span> and <span class="sb">``</span>condition_id<span class="sb">``</span> can be retrieved from the following New Relic URL when viewing the NRQL alert condition you want to import<span class="se">\ </span>:raw-html-m2r:<span class="sb">`</span>&lt;small&gt;alerts.newrelic.com/accounts/**<span class="se">\&lt;</span>account_id<span class="se">\&gt;</span>**/policies/**<span class="se">\&lt;</span>policy_id<span class="se">\&gt;</span>**/conditions/**<span class="se">\&lt;</span>condition_id<span class="se">\&gt;</span>**/edit&lt;/small&gt;<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The New Relic account ID of the account you wish to create the condition. Defaults to the account ID set in your environment variable <code class="docutils literal notranslate"><span class="pre">NEW_RELIC_ACCOUNT_ID</span></code>.</p></li>
<li><p><strong>aggregation_window</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The duration of the time window used to evaluate the NRQL query, in seconds. The value must be at least 30 seconds, and no more than 15 minutes (900 seconds). Default is 60 seconds.</p></li>
<li><p><strong>baseline_direction</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The baseline direction of a <em>baseline</em> NRQL alert condition. Valid values are: <code class="docutils literal notranslate"><span class="pre">lower_only</span></code>, <code class="docutils literal notranslate"><span class="pre">upper_and_lower</span></code>, <code class="docutils literal notranslate"><span class="pre">upper_only</span></code> (case insensitive).</p></li>
<li><p><strong>close_violations_on_expiration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to close all open violations when the signal expires.</p></li>
<li><p><strong>critical</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NrqlAlertConditionCriticalArgs'</em><em>]</em><em>]</em>) – A list containing the <code class="docutils literal notranslate"><span class="pre">critical</span></code> threshold values. See Terms below for details.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the NRQL alert condition.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable the alert condition. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>expected_groups</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Number of expected groups when using <code class="docutils literal notranslate"><span class="pre">outlier</span></code> detection.</p></li>
<li><p><strong>expiration_duration</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The amount of time (in seconds) to wait before considering the signal expired.</p></li>
<li><p><strong>fill_option</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which strategy to use when filling gaps in the signal. Possible values are <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">last_value</span></code> or <code class="docutils literal notranslate"><span class="pre">static</span></code>. If <code class="docutils literal notranslate"><span class="pre">static</span></code>, the <code class="docutils literal notranslate"><span class="pre">fill_value</span></code> field will be used for filling gaps in the signal.</p></li>
<li><p><strong>fill_value</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – This value will be used for filling gaps in the signal.</p></li>
<li><p><strong>ignore_overlap</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <strong>DEPRECATED:</strong> Use <code class="docutils literal notranslate"><span class="pre">open_violation_on_group_overlap</span></code> instead, but use the inverse value of your boolean - e.g. if <code class="docutils literal notranslate"><span class="pre">ignore_overlap</span> <span class="pre">=</span> <span class="pre">false</span></code>, use <code class="docutils literal notranslate"><span class="pre">open_violation_on_group_overlap</span> <span class="pre">=</span> <span class="pre">true</span></code>. This argument sets whether to trigger a violation when groups overlap. If set to <code class="docutils literal notranslate"><span class="pre">true</span></code> overlapping groups will not trigger a violation. This argument is only applicable in <code class="docutils literal notranslate"><span class="pre">outlier</span></code> conditions.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of the condition.</p></li>
<li><p><strong>nrql</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NrqlAlertConditionNrqlArgs'</em><em>]</em><em>]</em>) – A NRQL query. See NRQL below for details.</p></li>
<li><p><strong>open_violation_on_expiration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to create a new violation to capture that the signal expired.</p></li>
<li><p><strong>open_violation_on_group_overlap</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to trigger a violation when groups overlap. Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want to trigger a violation when groups overlap. This argument is only applicable in <code class="docutils literal notranslate"><span class="pre">outlier</span></code> conditions.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the policy where this condition should be used.</p></li>
<li><p><strong>runbook_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Runbook URL to display in notifications.</p></li>
<li><p><strong>terms</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NrqlAlertConditionTermArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <strong>DEPRECATED</strong> Use <code class="docutils literal notranslate"><span class="pre">critical</span></code>, and <code class="docutils literal notranslate"><span class="pre">warning</span></code> instead.  A list of terms for this condition. See Terms below for details.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the condition. Valid values are <code class="docutils literal notranslate"><span class="pre">static</span></code>, <code class="docutils literal notranslate"><span class="pre">baseline</span></code>, or <code class="docutils literal notranslate"><span class="pre">outlier</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">static</span></code>.</p></li>
<li><p><strong>value_function</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Possible values are <code class="docutils literal notranslate"><span class="pre">single_value</span></code>, <code class="docutils literal notranslate"><span class="pre">sum</span></code> (case insensitive).</p></li>
<li><p><strong>violation_time_limit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <strong>DEPRECATED:</strong> Use <code class="docutils literal notranslate"><span class="pre">violation_time_limit_seconds</span></code> instead. Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are <code class="docutils literal notranslate"><span class="pre">ONE_HOUR</span></code>, <code class="docutils literal notranslate"><span class="pre">TWO_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">FOUR_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">EIGHT_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">TWELVE_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">TWENTY_FOUR_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">THIRTY_DAYS</span></code> (case insensitive).<span class="raw-html-m2r"><br></span>
<span class="raw-html-m2r"><small>\***Note**: One of `violation_time_limit</span> _or_ <cite>violation_time_limit_seconds</cite> must be set, but not both.&lt;/small&gt;`</p></li>
<li><p><strong>violation_time_limit_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select. The value must be between 300 seconds (5 minutes) to 2592000 seconds (30 days) (inclusive). <span class="raw-html-m2r"><br></span>
<span class="raw-html-m2r"><small>\***Note**: One of `violation_time_limit</span> _or_ <cite>violation_time_limit_seconds</cite> must be set, but not both.&lt;/small&gt;`</p></li>
<li><p><strong>warning</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NrqlAlertConditionWarningArgs'</em><em>]</em><em>]</em>) – A list containing the <code class="docutils literal notranslate"><span class="pre">warning</span></code> threshold values. See Terms below for details.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aggregation_window</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">baseline_direction</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">close_violations_on_expiration</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">critical</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>NrqlAlertConditionCriticalArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NrqlAlertConditionCriticalArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expected_groups</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiration_duration</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fill_option</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fill_value</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>float<span class="p">, </span>Awaitable<span class="p">[</span>float<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_overlap</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nrql</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>NrqlAlertConditionNrqlArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NrqlAlertConditionNrqlArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">open_violation_on_expiration</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">open_violation_on_group_overlap</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">runbook_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">terms</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NrqlAlertConditionTermArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NrqlAlertConditionTermArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NrqlAlertConditionTermArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NrqlAlertConditionTermArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value_function</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">violation_time_limit</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">violation_time_limit_seconds</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">warning</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>NrqlAlertConditionWarningArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NrqlAlertConditionWarningArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_newrelic.NrqlAlertCondition" title="pulumi_newrelic.NrqlAlertCondition">NrqlAlertCondition</a><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NrqlAlertCondition resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The New Relic account ID of the account you wish to create the condition. Defaults to the account ID set in your environment variable <code class="docutils literal notranslate"><span class="pre">NEW_RELIC_ACCOUNT_ID</span></code>.</p></li>
<li><p><strong>aggregation_window</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The duration of the time window used to evaluate the NRQL query, in seconds. The value must be at least 30 seconds, and no more than 15 minutes (900 seconds). Default is 60 seconds.</p></li>
<li><p><strong>baseline_direction</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The baseline direction of a <em>baseline</em> NRQL alert condition. Valid values are: <code class="docutils literal notranslate"><span class="pre">lower_only</span></code>, <code class="docutils literal notranslate"><span class="pre">upper_and_lower</span></code>, <code class="docutils literal notranslate"><span class="pre">upper_only</span></code> (case insensitive).</p></li>
<li><p><strong>close_violations_on_expiration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to close all open violations when the signal expires.</p></li>
<li><p><strong>critical</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NrqlAlertConditionCriticalArgs'</em><em>]</em><em>]</em>) – A list containing the <code class="docutils literal notranslate"><span class="pre">critical</span></code> threshold values. See Terms below for details.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the NRQL alert condition.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable the alert condition. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>expected_groups</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Number of expected groups when using <code class="docutils literal notranslate"><span class="pre">outlier</span></code> detection.</p></li>
<li><p><strong>expiration_duration</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The amount of time (in seconds) to wait before considering the signal expired.</p></li>
<li><p><strong>fill_option</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which strategy to use when filling gaps in the signal. Possible values are <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">last_value</span></code> or <code class="docutils literal notranslate"><span class="pre">static</span></code>. If <code class="docutils literal notranslate"><span class="pre">static</span></code>, the <code class="docutils literal notranslate"><span class="pre">fill_value</span></code> field will be used for filling gaps in the signal.</p></li>
<li><p><strong>fill_value</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – This value will be used for filling gaps in the signal.</p></li>
<li><p><strong>ignore_overlap</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <strong>DEPRECATED:</strong> Use <code class="docutils literal notranslate"><span class="pre">open_violation_on_group_overlap</span></code> instead, but use the inverse value of your boolean - e.g. if <code class="docutils literal notranslate"><span class="pre">ignore_overlap</span> <span class="pre">=</span> <span class="pre">false</span></code>, use <code class="docutils literal notranslate"><span class="pre">open_violation_on_group_overlap</span> <span class="pre">=</span> <span class="pre">true</span></code>. This argument sets whether to trigger a violation when groups overlap. If set to <code class="docutils literal notranslate"><span class="pre">true</span></code> overlapping groups will not trigger a violation. This argument is only applicable in <code class="docutils literal notranslate"><span class="pre">outlier</span></code> conditions.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of the condition.</p></li>
<li><p><strong>nrql</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NrqlAlertConditionNrqlArgs'</em><em>]</em><em>]</em>) – A NRQL query. See NRQL below for details.</p></li>
<li><p><strong>open_violation_on_expiration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to create a new violation to capture that the signal expired.</p></li>
<li><p><strong>open_violation_on_group_overlap</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to trigger a violation when groups overlap. Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want to trigger a violation when groups overlap. This argument is only applicable in <code class="docutils literal notranslate"><span class="pre">outlier</span></code> conditions.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the policy where this condition should be used.</p></li>
<li><p><strong>runbook_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Runbook URL to display in notifications.</p></li>
<li><p><strong>terms</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NrqlAlertConditionTermArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <strong>DEPRECATED</strong> Use <code class="docutils literal notranslate"><span class="pre">critical</span></code>, and <code class="docutils literal notranslate"><span class="pre">warning</span></code> instead.  A list of terms for this condition. See Terms below for details.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the condition. Valid values are <code class="docutils literal notranslate"><span class="pre">static</span></code>, <code class="docutils literal notranslate"><span class="pre">baseline</span></code>, or <code class="docutils literal notranslate"><span class="pre">outlier</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">static</span></code>.</p></li>
<li><p><strong>value_function</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Possible values are <code class="docutils literal notranslate"><span class="pre">single_value</span></code>, <code class="docutils literal notranslate"><span class="pre">sum</span></code> (case insensitive).</p></li>
<li><p><strong>violation_time_limit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <strong>DEPRECATED:</strong> Use <code class="docutils literal notranslate"><span class="pre">violation_time_limit_seconds</span></code> instead. Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are <code class="docutils literal notranslate"><span class="pre">ONE_HOUR</span></code>, <code class="docutils literal notranslate"><span class="pre">TWO_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">FOUR_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">EIGHT_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">TWELVE_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">TWENTY_FOUR_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">THIRTY_DAYS</span></code> (case insensitive).<span class="raw-html-m2r"><br></span>
<span class="raw-html-m2r"><small>\***Note**: One of `violation_time_limit</span> _or_ <cite>violation_time_limit_seconds</cite> must be set, but not both.&lt;/small&gt;`</p></li>
<li><p><strong>violation_time_limit_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select. The value must be between 300 seconds (5 minutes) to 2592000 seconds (30 days) (inclusive). <span class="raw-html-m2r"><br></span>
<span class="raw-html-m2r"><small>\***Note**: One of `violation_time_limit</span> _or_ <cite>violation_time_limit_seconds</cite> must be set, but not both.&lt;/small&gt;`</p></li>
<li><p><strong>warning</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NrqlAlertConditionWarningArgs'</em><em>]</em><em>]</em>) – A list containing the <code class="docutils literal notranslate"><span class="pre">warning</span></code> threshold values. See Terms below for details.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.account_id">
<em class="property">property </em><code class="sig-name descname">account_id</code><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The New Relic account ID of the account you wish to create the condition. Defaults to the account ID set in your environment variable <code class="docutils literal notranslate"><span class="pre">NEW_RELIC_ACCOUNT_ID</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.aggregation_window">
<em class="property">property </em><code class="sig-name descname">aggregation_window</code><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.aggregation_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The duration of the time window used to evaluate the NRQL query, in seconds. The value must be at least 30 seconds, and no more than 15 minutes (900 seconds). Default is 60 seconds.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.baseline_direction">
<em class="property">property </em><code class="sig-name descname">baseline_direction</code><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.baseline_direction" title="Permalink to this definition">¶</a></dt>
<dd><p>The baseline direction of a <em>baseline</em> NRQL alert condition. Valid values are: <code class="docutils literal notranslate"><span class="pre">lower_only</span></code>, <code class="docutils literal notranslate"><span class="pre">upper_and_lower</span></code>, <code class="docutils literal notranslate"><span class="pre">upper_only</span></code> (case insensitive).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.close_violations_on_expiration">
<em class="property">property </em><code class="sig-name descname">close_violations_on_expiration</code><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.close_violations_on_expiration" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to close all open violations when the signal expires.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.critical">
<em class="property">property </em><code class="sig-name descname">critical</code><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.critical" title="Permalink to this definition">¶</a></dt>
<dd><p>A list containing the <code class="docutils literal notranslate"><span class="pre">critical</span></code> threshold values. See Terms below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the NRQL alert condition.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable the alert condition. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.expected_groups">
<em class="property">property </em><code class="sig-name descname">expected_groups</code><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.expected_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of expected groups when using <code class="docutils literal notranslate"><span class="pre">outlier</span></code> detection.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.expiration_duration">
<em class="property">property </em><code class="sig-name descname">expiration_duration</code><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.expiration_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time (in seconds) to wait before considering the signal expired.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.fill_option">
<em class="property">property </em><code class="sig-name descname">fill_option</code><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.fill_option" title="Permalink to this definition">¶</a></dt>
<dd><p>Which strategy to use when filling gaps in the signal. Possible values are <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">last_value</span></code> or <code class="docutils literal notranslate"><span class="pre">static</span></code>. If <code class="docutils literal notranslate"><span class="pre">static</span></code>, the <code class="docutils literal notranslate"><span class="pre">fill_value</span></code> field will be used for filling gaps in the signal.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.fill_value">
<em class="property">property </em><code class="sig-name descname">fill_value</code><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.fill_value" title="Permalink to this definition">¶</a></dt>
<dd><p>This value will be used for filling gaps in the signal.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.ignore_overlap">
<em class="property">property </em><code class="sig-name descname">ignore_overlap</code><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.ignore_overlap" title="Permalink to this definition">¶</a></dt>
<dd><p><strong>DEPRECATED:</strong> Use <code class="docutils literal notranslate"><span class="pre">open_violation_on_group_overlap</span></code> instead, but use the inverse value of your boolean - e.g. if <code class="docutils literal notranslate"><span class="pre">ignore_overlap</span> <span class="pre">=</span> <span class="pre">false</span></code>, use <code class="docutils literal notranslate"><span class="pre">open_violation_on_group_overlap</span> <span class="pre">=</span> <span class="pre">true</span></code>. This argument sets whether to trigger a violation when groups overlap. If set to <code class="docutils literal notranslate"><span class="pre">true</span></code> overlapping groups will not trigger a violation. This argument is only applicable in <code class="docutils literal notranslate"><span class="pre">outlier</span></code> conditions.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The title of the condition.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.nrql">
<em class="property">property </em><code class="sig-name descname">nrql</code><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.nrql" title="Permalink to this definition">¶</a></dt>
<dd><p>A NRQL query. See NRQL below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.open_violation_on_expiration">
<em class="property">property </em><code class="sig-name descname">open_violation_on_expiration</code><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.open_violation_on_expiration" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to create a new violation to capture that the signal expired.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.open_violation_on_group_overlap">
<em class="property">property </em><code class="sig-name descname">open_violation_on_group_overlap</code><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.open_violation_on_group_overlap" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not to trigger a violation when groups overlap. Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want to trigger a violation when groups overlap. This argument is only applicable in <code class="docutils literal notranslate"><span class="pre">outlier</span></code> conditions.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.policy_id">
<em class="property">property </em><code class="sig-name descname">policy_id</code><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the policy where this condition should be used.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.runbook_url">
<em class="property">property </em><code class="sig-name descname">runbook_url</code><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.runbook_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Runbook URL to display in notifications.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.terms">
<em class="property">property </em><code class="sig-name descname">terms</code><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.terms" title="Permalink to this definition">¶</a></dt>
<dd><p><strong>DEPRECATED</strong> Use <code class="docutils literal notranslate"><span class="pre">critical</span></code>, and <code class="docutils literal notranslate"><span class="pre">warning</span></code> instead.  A list of terms for this condition. See Terms below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the condition. Valid values are <code class="docutils literal notranslate"><span class="pre">static</span></code>, <code class="docutils literal notranslate"><span class="pre">baseline</span></code>, or <code class="docutils literal notranslate"><span class="pre">outlier</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">static</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.value_function">
<em class="property">property </em><code class="sig-name descname">value_function</code><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.value_function" title="Permalink to this definition">¶</a></dt>
<dd><p>Possible values are <code class="docutils literal notranslate"><span class="pre">single_value</span></code>, <code class="docutils literal notranslate"><span class="pre">sum</span></code> (case insensitive).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.violation_time_limit">
<em class="property">property </em><code class="sig-name descname">violation_time_limit</code><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.violation_time_limit" title="Permalink to this definition">¶</a></dt>
<dd><p><strong>DEPRECATED:</strong> Use <code class="docutils literal notranslate"><span class="pre">violation_time_limit_seconds</span></code> instead. Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are <code class="docutils literal notranslate"><span class="pre">ONE_HOUR</span></code>, <code class="docutils literal notranslate"><span class="pre">TWO_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">FOUR_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">EIGHT_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">TWELVE_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">TWENTY_FOUR_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">THIRTY_DAYS</span></code> (case insensitive).<span class="raw-html-m2r"><br></span>
<span class="raw-html-m2r"><small>\***Note**: One of `violation_time_limit</span> _or_ <cite>violation_time_limit_seconds</cite> must be set, but not both.&lt;/small&gt;`</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.violation_time_limit_seconds">
<em class="property">property </em><code class="sig-name descname">violation_time_limit_seconds</code><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.violation_time_limit_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select. The value must be between 300 seconds (5 minutes) to 2592000 seconds (30 days) (inclusive). <span class="raw-html-m2r"><br></span>
<span class="raw-html-m2r"><small>\***Note**: One of `violation_time_limit</span> _or_ <cite>violation_time_limit_seconds</cite> must be set, but not both.&lt;/small&gt;`</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.warning">
<em class="property">property </em><code class="sig-name descname">warning</code><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.warning" title="Permalink to this definition">¶</a></dt>
<dd><p>A list containing the <code class="docutils literal notranslate"><span class="pre">warning</span></code> threshold values. See Terms below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.NrqlAlertCondition.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.OneDashboard">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">OneDashboard</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pages</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>OneDashboardPageArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>OneDashboardPageArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>OneDashboardPageArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>OneDashboardPageArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.OneDashboard" title="Permalink to this definition">¶</a></dt>
<dd><p><strong>NOTE:</strong> This feature is currently in <strong>CLOSED BETA</strong>, and will <strong>NOT WORK</strong> for most New Relic customers and is subject to <strong>BREAKING CHANGES</strong>.</p>
<p>Use this resource to create and manage New Relic One dashboards.</p>
<p>New Relic dashboards can be imported using their GUID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import newrelic:index/oneDashboard:OneDashboard my_dashboard &lt;Dashboard GUID&gt;
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Brief text describing the dashboard.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of the dashboard.</p></li>
<li><p><strong>pages</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'OneDashboardPageArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A nested block that describes a page. See Nested page blocks below for details.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determines who can see the dashboard in an account. Valid values are <code class="docutils literal notranslate"><span class="pre">private</span></code>, <code class="docutils literal notranslate"><span class="pre">public_read_only</span></code>, or <code class="docutils literal notranslate"><span class="pre">public_read_write</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">public_read_only</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_newrelic.OneDashboard.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">guid</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pages</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>OneDashboardPageArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>OneDashboardPageArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>OneDashboardPageArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>OneDashboardPageArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permalink</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_newrelic.OneDashboard" title="pulumi_newrelic.OneDashboard">OneDashboard</a><a class="headerlink" href="#pulumi_newrelic.OneDashboard.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OneDashboard resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Brief text describing the dashboard.</p></li>
<li><p><strong>guid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique entity identifier of the dashboard page in New Relic.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of the dashboard.</p></li>
<li><p><strong>pages</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'OneDashboardPageArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A nested block that describes a page. See Nested page blocks below for details.</p></li>
<li><p><strong>permalink</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL for viewing the dashboard.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determines who can see the dashboard in an account. Valid values are <code class="docutils literal notranslate"><span class="pre">private</span></code>, <code class="docutils literal notranslate"><span class="pre">public_read_only</span></code>, or <code class="docutils literal notranslate"><span class="pre">public_read_write</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">public_read_only</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.OneDashboard.account_id">
<em class="property">property </em><code class="sig-name descname">account_id</code><a class="headerlink" href="#pulumi_newrelic.OneDashboard.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.OneDashboard.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_newrelic.OneDashboard.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Brief text describing the dashboard.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.OneDashboard.guid">
<em class="property">property </em><code class="sig-name descname">guid</code><a class="headerlink" href="#pulumi_newrelic.OneDashboard.guid" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique entity identifier of the dashboard page in New Relic.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.OneDashboard.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_newrelic.OneDashboard.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The title of the dashboard.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.OneDashboard.pages">
<em class="property">property </em><code class="sig-name descname">pages</code><a class="headerlink" href="#pulumi_newrelic.OneDashboard.pages" title="Permalink to this definition">¶</a></dt>
<dd><p>A nested block that describes a page. See Nested page blocks below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.OneDashboard.permalink">
<em class="property">property </em><code class="sig-name descname">permalink</code><a class="headerlink" href="#pulumi_newrelic.OneDashboard.permalink" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL for viewing the dashboard.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.OneDashboard.permissions">
<em class="property">property </em><code class="sig-name descname">permissions</code><a class="headerlink" href="#pulumi_newrelic.OneDashboard.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines who can see the dashboard in an account. Valid values are <code class="docutils literal notranslate"><span class="pre">private</span></code>, <code class="docutils literal notranslate"><span class="pre">public_read_only</span></code>, or <code class="docutils literal notranslate"><span class="pre">public_read_write</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">public_read_only</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.OneDashboard.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.OneDashboard.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.OneDashboard.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.OneDashboard.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_api_key</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cacert_file</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">infrastructure_api_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">insecure_skip_verify</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">insights_insert_key</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">insights_insert_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">insights_query_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nerdgraph_api_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">synthetics_api_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the newrelic package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data center for which your New Relic account is configured. Only one region per provider block is permitted.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_newrelic.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.get_account">
<code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">get_account</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_newrelic.get_account.AwaitableGetAccountResult<a class="headerlink" href="#pulumi_newrelic.get_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a specific account in New Relic.
Accounts can be located by ID or name.  Exactly one of the two attributes is
required.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">acc</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">get_account</span><span class="p">(</span><span class="n">scope</span><span class="o">=</span><span class="s2">&quot;global&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>account_id</strong> (<em>int</em>) – The account ID in New Relic.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The account name in New Relic.</p></li>
<li><p><strong>scope</strong> (<em>str</em>) – The scope of the account in New Relic.  Valid values are “global” and “in_region”.  Defaults to “in_region”.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_newrelic.get_alert_channel">
<code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">get_alert_channel</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_newrelic.get_alert_channel.AwaitableGetAlertChannelResult<a class="headerlink" href="#pulumi_newrelic.get_alert_channel" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a specific alert channel in New Relic that already exists.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the alert channel in New Relic.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_newrelic.get_alert_policy">
<code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">get_alert_policy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">incident_preference</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_newrelic.get_alert_policy.AwaitableGetAlertPolicyResult<a class="headerlink" href="#pulumi_newrelic.get_alert_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a specific alert policy in New Relic that already exists.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>incident_preference</strong> (<em>str</em>) – The rollup strategy for the policy. Options include: PER_POLICY, PER_CONDITION, or PER_CONDITION_AND_TARGET. The default is PER_POLICY.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the alert policy in New Relic.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_newrelic.get_application">
<code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">get_application</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_newrelic.get_application.AwaitableGetApplicationResult<a class="headerlink" href="#pulumi_newrelic.get_application" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a specific application in New Relic that already exists.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">app</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">get_application</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;my-app&quot;</span><span class="p">)</span>
<span class="n">foo_alert_policy</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertPolicy</span><span class="p">(</span><span class="s2">&quot;fooAlertPolicy&quot;</span><span class="p">)</span>
<span class="n">foo_alert_condition</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertCondition</span><span class="p">(</span><span class="s2">&quot;fooAlertCondition&quot;</span><span class="p">,</span>
    <span class="n">policy_id</span><span class="o">=</span><span class="n">foo_alert_policy</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;apm_app_metric&quot;</span><span class="p">,</span>
    <span class="n">entities</span><span class="o">=</span><span class="p">[</span><span class="n">app</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
    <span class="n">metric</span><span class="o">=</span><span class="s2">&quot;apdex&quot;</span><span class="p">,</span>
    <span class="n">runbook_url</span><span class="o">=</span><span class="s2">&quot;https://www.example.com&quot;</span><span class="p">,</span>
    <span class="n">terms</span><span class="o">=</span><span class="p">[</span><span class="n">newrelic</span><span class="o">.</span><span class="n">AlertConditionTermArgs</span><span class="p">(</span>
        <span class="n">duration</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
        <span class="n">operator</span><span class="o">=</span><span class="s2">&quot;below&quot;</span><span class="p">,</span>
        <span class="n">priority</span><span class="o">=</span><span class="s2">&quot;critical&quot;</span><span class="p">,</span>
        <span class="n">threshold</span><span class="o">=</span><span class="mf">0.75</span><span class="p">,</span>
        <span class="n">time_function</span><span class="o">=</span><span class="s2">&quot;all&quot;</span><span class="p">,</span>
    <span class="p">)])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the application in New Relic.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_newrelic.get_entity">
<code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">get_entity</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>pulumi_newrelic._inputs.GetEntityTagArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_newrelic.get_entity.AwaitableGetEntityResult<a class="headerlink" href="#pulumi_newrelic.get_entity" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a specific entity in New Relic One that already exists.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>domain</strong> (<em>str</em>) – The entity’s domain. Valid values are APM, BROWSER, INFRA, MOBILE, SYNTH, and VIZ. If not specified, all domains are searched.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the entity in New Relic One.  The first entity matching this name for the given search parameters will be returned.</p></li>
<li><p><strong>type</strong> (<em>str</em>) – The entity’s type. Valid values are APPLICATION, DASHBOARD, HOST, MONITOR, and WORKLOAD.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_newrelic.get_key_transaction">
<code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">get_key_transaction</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_newrelic.get_key_transaction.AwaitableGetKeyTransactionResult<a class="headerlink" href="#pulumi_newrelic.get_key_transaction" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a specific key transaction in New Relic that already exists.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">txn</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">get_key_transaction</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;txn&quot;</span><span class="p">)</span>
<span class="n">foo_alert_policy</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertPolicy</span><span class="p">(</span><span class="s2">&quot;fooAlertPolicy&quot;</span><span class="p">)</span>
<span class="n">foo_alert_condition</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertCondition</span><span class="p">(</span><span class="s2">&quot;fooAlertCondition&quot;</span><span class="p">,</span>
    <span class="n">policy_id</span><span class="o">=</span><span class="n">foo_alert_policy</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;apm_kt_metric&quot;</span><span class="p">,</span>
    <span class="n">entities</span><span class="o">=</span><span class="p">[</span><span class="n">txn</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
    <span class="n">metric</span><span class="o">=</span><span class="s2">&quot;error_percentage&quot;</span><span class="p">,</span>
    <span class="n">runbook_url</span><span class="o">=</span><span class="s2">&quot;https://www.example.com&quot;</span><span class="p">,</span>
    <span class="n">terms</span><span class="o">=</span><span class="p">[</span><span class="n">newrelic</span><span class="o">.</span><span class="n">AlertConditionTermArgs</span><span class="p">(</span>
        <span class="n">duration</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
        <span class="n">operator</span><span class="o">=</span><span class="s2">&quot;below&quot;</span><span class="p">,</span>
        <span class="n">priority</span><span class="o">=</span><span class="s2">&quot;critical&quot;</span><span class="p">,</span>
        <span class="n">threshold</span><span class="o">=</span><span class="mf">0.75</span><span class="p">,</span>
        <span class="n">time_function</span><span class="o">=</span><span class="s2">&quot;all&quot;</span><span class="p">,</span>
    <span class="p">)])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the key transaction in New Relic.</p>
</dd>
</dl>
</dd></dl>

</div>
