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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">AlertChannel</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AlertChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to create and manage New Relic alert policies.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannel</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;includeJsonAttachment&quot;</span><span class="p">:</span> <span class="s2">&quot;1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;recipients&quot;</span><span class="p">:</span> <span class="s2">&quot;foo@example.com&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;email&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>See additional examples.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannel</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;channel&quot;</span><span class="p">:</span> <span class="s2">&quot;example-alerts-channel&quot;</span><span class="p">,</span>
        <span class="s2">&quot;url&quot;</span><span class="p">:</span> <span class="s2">&quot;https://&lt;YourOrganization&gt;.slack.com&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;slack&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannel</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;apiKey&quot;</span><span class="p">:</span> <span class="s2">&quot;abc123&quot;</span><span class="p">,</span>
        <span class="s2">&quot;recipients&quot;</span><span class="p">:</span> <span class="s2">&quot;user1@domain.com, user2@domain.com&quot;</span><span class="p">,</span>
        <span class="s2">&quot;tags&quot;</span><span class="p">:</span> <span class="s2">&quot;tag1, tag2&quot;</span><span class="p">,</span>
        <span class="s2">&quot;teams&quot;</span><span class="p">:</span> <span class="s2">&quot;team1, team2&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;opsgenie&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannel</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;serviceKey&quot;</span><span class="p">:</span> <span class="s2">&quot;abc123&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;pagerduty&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannel</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;abc123&quot;</span><span class="p">,</span>
        <span class="s2">&quot;routeKey&quot;</span><span class="p">:</span> <span class="s2">&quot;/example&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;victorops&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannel</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;webhook&quot;</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;baseUrl&quot;</span><span class="p">:</span> <span class="s2">&quot;http://www.test.com&quot;</span><span class="p">,</span>
        <span class="s2">&quot;payloadType&quot;</span><span class="p">:</span> <span class="s2">&quot;application/json&quot;</span><span class="p">,</span>
        <span class="s2">&quot;payload&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;condition_name&quot;</span><span class="p">:</span> <span class="s2">&quot;$CONDITION_NAME&quot;</span><span class="p">,</span>
            <span class="s2">&quot;policy_name&quot;</span><span class="p">:</span> <span class="s2">&quot;$POLICY_NAME&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="s2">&quot;headers&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;header1&quot;</span><span class="p">:</span> <span class="n">value1</span><span class="p">,</span>
            <span class="s2">&quot;header2&quot;</span><span class="p">:</span> <span class="n">value2</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">})</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannel</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;baseUrl&quot;</span><span class="p">:</span> <span class="s2">&quot;http://www.test.com&quot;</span><span class="p">,</span>
        <span class="s2">&quot;payloadString&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">  &quot;my_custom_values&quot;: {</span>
<span class="s2">    &quot;condition_name&quot;: &quot;$CONDITION_NAME&quot;,</span>
<span class="s2">    &quot;policy_name&quot;: &quot;$POLICY_NAME&quot;</span>
<span class="s2">  }</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
        <span class="s2">&quot;payloadType&quot;</span><span class="p">:</span> <span class="s2">&quot;application/json&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;webhook&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested block that describes an alert channel configuration.  Only one config block is permitted per alert channel definition.  See Nested config blocks below for details.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the channel.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of channel.  One of: <code class="docutils literal notranslate"><span class="pre">email</span></code>, <code class="docutils literal notranslate"><span class="pre">slack</span></code>, <code class="docutils literal notranslate"><span class="pre">opsgenie</span></code>, <code class="docutils literal notranslate"><span class="pre">pagerduty</span></code>, <code class="docutils literal notranslate"><span class="pre">victorops</span></code>, or <code class="docutils literal notranslate"><span class="pre">webhook</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">apiKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The API key for integrating with OpsGenie.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies an authentication password for use with a channel.  Supported by the <code class="docutils literal notranslate"><span class="pre">webhook</span></code> channel type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies an authentication method for use with a channel.  Supported by the <code class="docutils literal notranslate"><span class="pre">webhook</span></code> channel type.  Only HTTP basic authentication is currently supported via the value <code class="docutils literal notranslate"><span class="pre">BASIC</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authUsername</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies an authentication username for use with a channel.  Supported by the <code class="docutils literal notranslate"><span class="pre">webhook</span></code> channel type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">baseUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The base URL of the webhook destination.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">channel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Slack channel to send notifications to.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">opsgenie</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A map of key/value pairs that represents extra HTTP headers to be sent along with the webhook payload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headersString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Use instead of <code class="docutils literal notranslate"><span class="pre">headers</span></code> if the desired payload is more complex than a list of key/value pairs (e.g. a set of headers that makes use of nested objects).  The value provided should be a valid JSON string with escaped double quotes. Conflicts with <code class="docutils literal notranslate"><span class="pre">headers</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeJsonAttachment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - <code class="docutils literal notranslate"><span class="pre">0</span></code> or <code class="docutils literal notranslate"><span class="pre">1</span></code>. Flag for whether or not to attach a JSON document containing information about the associated alert to the email that is sent to recipients.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">webhook</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The key for integrating with VictorOps.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">payload</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A map of key/value pairs that represents the webhook payload.  Must provide <code class="docutils literal notranslate"><span class="pre">payload_type</span></code> if setting this argument.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">payloadString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Use instead of <code class="docutils literal notranslate"><span class="pre">payload</span></code> if the desired payload is more complex than a list of key/value pairs (e.g. a payload that makes use of nested objects).  The value provided should be a valid JSON string with escaped double quotes. Conflicts with <code class="docutils literal notranslate"><span class="pre">payload</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">payloadType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Can either be <code class="docutils literal notranslate"><span class="pre">application/json</span></code> or <code class="docutils literal notranslate"><span class="pre">application/x-www-form-urlencoded</span></code>. The <code class="docutils literal notranslate"><span class="pre">payload_type</span></code> argument is <em>required</em> if <code class="docutils literal notranslate"><span class="pre">payload</span></code> is set.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">pagerduty</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recipients</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A set of recipients for targeting notifications.  Multiple values are comma separated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data center region to store your data.  Valid values are <code class="docutils literal notranslate"><span class="pre">US</span></code> and <code class="docutils literal notranslate"><span class="pre">EU</span></code>.  Default is <code class="docutils literal notranslate"><span class="pre">US</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">routeKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The route key for integrating with VictorOps.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">slack</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the service key for integrating with Pagerduty.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">victorops</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A set of tags for targeting notifications. Multiple values are comma separated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">teams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A set of teams for targeting notifications. Multiple values are comma separated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your organization’s Slack URL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_newrelic.AlertChannel.config">
<code class="sig-name descname">config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.AlertChannel.config" title="Permalink to this definition">¶</a></dt>
<dd><p>A nested block that describes an alert channel configuration.  Only one config block is permitted per alert channel definition.  See Nested config blocks below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">apiKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The API key for integrating with OpsGenie.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies an authentication password for use with a channel.  Supported by the <code class="docutils literal notranslate"><span class="pre">webhook</span></code> channel type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies an authentication method for use with a channel.  Supported by the <code class="docutils literal notranslate"><span class="pre">webhook</span></code> channel type.  Only HTTP basic authentication is currently supported via the value <code class="docutils literal notranslate"><span class="pre">BASIC</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authUsername</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies an authentication username for use with a channel.  Supported by the <code class="docutils literal notranslate"><span class="pre">webhook</span></code> channel type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">baseUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The base URL of the webhook destination.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">channel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Slack channel to send notifications to.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">opsgenie</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A map of key/value pairs that represents extra HTTP headers to be sent along with the webhook payload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headersString</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Use instead of <code class="docutils literal notranslate"><span class="pre">headers</span></code> if the desired payload is more complex than a list of key/value pairs (e.g. a set of headers that makes use of nested objects).  The value provided should be a valid JSON string with escaped double quotes. Conflicts with <code class="docutils literal notranslate"><span class="pre">headers</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeJsonAttachment</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - <code class="docutils literal notranslate"><span class="pre">0</span></code> or <code class="docutils literal notranslate"><span class="pre">1</span></code>. Flag for whether or not to attach a JSON document containing information about the associated alert to the email that is sent to recipients.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">webhook</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The key for integrating with VictorOps.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">payload</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A map of key/value pairs that represents the webhook payload.  Must provide <code class="docutils literal notranslate"><span class="pre">payload_type</span></code> if setting this argument.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">payloadString</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Use instead of <code class="docutils literal notranslate"><span class="pre">payload</span></code> if the desired payload is more complex than a list of key/value pairs (e.g. a payload that makes use of nested objects).  The value provided should be a valid JSON string with escaped double quotes. Conflicts with <code class="docutils literal notranslate"><span class="pre">payload</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">payloadType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Can either be <code class="docutils literal notranslate"><span class="pre">application/json</span></code> or <code class="docutils literal notranslate"><span class="pre">application/x-www-form-urlencoded</span></code>. The <code class="docutils literal notranslate"><span class="pre">payload_type</span></code> argument is <em>required</em> if <code class="docutils literal notranslate"><span class="pre">payload</span></code> is set.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">pagerduty</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recipients</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A set of recipients for targeting notifications.  Multiple values are comma separated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The data center region to store your data.  Valid values are <code class="docutils literal notranslate"><span class="pre">US</span></code> and <code class="docutils literal notranslate"><span class="pre">EU</span></code>.  Default is <code class="docutils literal notranslate"><span class="pre">US</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">routeKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The route key for integrating with VictorOps.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">slack</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the service key for integrating with Pagerduty.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">victorops</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A set of tags for targeting notifications. Multiple values are comma separated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">teams</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A set of teams for targeting notifications. Multiple values are comma separated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Your organization’s Slack URL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.AlertChannel.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.AlertChannel.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the channel.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.AlertChannel.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.AlertChannel.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of channel.  One of: <code class="docutils literal notranslate"><span class="pre">email</span></code>, <code class="docutils literal notranslate"><span class="pre">slack</span></code>, <code class="docutils literal notranslate"><span class="pre">opsgenie</span></code>, <code class="docutils literal notranslate"><span class="pre">pagerduty</span></code>, <code class="docutils literal notranslate"><span class="pre">victorops</span></code>, or <code class="docutils literal notranslate"><span class="pre">webhook</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertChannel.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AlertChannel.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AlertChannel resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested block that describes an alert channel configuration.  Only one config block is permitted per alert channel definition.  See Nested config blocks below for details.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the channel.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of channel.  One of: <code class="docutils literal notranslate"><span class="pre">email</span></code>, <code class="docutils literal notranslate"><span class="pre">slack</span></code>, <code class="docutils literal notranslate"><span class="pre">opsgenie</span></code>, <code class="docutils literal notranslate"><span class="pre">pagerduty</span></code>, <code class="docutils literal notranslate"><span class="pre">victorops</span></code>, or <code class="docutils literal notranslate"><span class="pre">webhook</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">apiKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The API key for integrating with OpsGenie.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies an authentication password for use with a channel.  Supported by the <code class="docutils literal notranslate"><span class="pre">webhook</span></code> channel type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies an authentication method for use with a channel.  Supported by the <code class="docutils literal notranslate"><span class="pre">webhook</span></code> channel type.  Only HTTP basic authentication is currently supported via the value <code class="docutils literal notranslate"><span class="pre">BASIC</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authUsername</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies an authentication username for use with a channel.  Supported by the <code class="docutils literal notranslate"><span class="pre">webhook</span></code> channel type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">baseUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The base URL of the webhook destination.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">channel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Slack channel to send notifications to.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">opsgenie</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A map of key/value pairs that represents extra HTTP headers to be sent along with the webhook payload.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headersString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Use instead of <code class="docutils literal notranslate"><span class="pre">headers</span></code> if the desired payload is more complex than a list of key/value pairs (e.g. a set of headers that makes use of nested objects).  The value provided should be a valid JSON string with escaped double quotes. Conflicts with <code class="docutils literal notranslate"><span class="pre">headers</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeJsonAttachment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - <code class="docutils literal notranslate"><span class="pre">0</span></code> or <code class="docutils literal notranslate"><span class="pre">1</span></code>. Flag for whether or not to attach a JSON document containing information about the associated alert to the email that is sent to recipients.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">webhook</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The key for integrating with VictorOps.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">payload</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A map of key/value pairs that represents the webhook payload.  Must provide <code class="docutils literal notranslate"><span class="pre">payload_type</span></code> if setting this argument.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">payloadString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Use instead of <code class="docutils literal notranslate"><span class="pre">payload</span></code> if the desired payload is more complex than a list of key/value pairs (e.g. a payload that makes use of nested objects).  The value provided should be a valid JSON string with escaped double quotes. Conflicts with <code class="docutils literal notranslate"><span class="pre">payload</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">payloadType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Can either be <code class="docutils literal notranslate"><span class="pre">application/json</span></code> or <code class="docutils literal notranslate"><span class="pre">application/x-www-form-urlencoded</span></code>. The <code class="docutils literal notranslate"><span class="pre">payload_type</span></code> argument is <em>required</em> if <code class="docutils literal notranslate"><span class="pre">payload</span></code> is set.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">pagerduty</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recipients</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A set of recipients for targeting notifications.  Multiple values are comma separated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The data center region to store your data.  Valid values are <code class="docutils literal notranslate"><span class="pre">US</span></code> and <code class="docutils literal notranslate"><span class="pre">EU</span></code>.  Default is <code class="docutils literal notranslate"><span class="pre">US</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">routeKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The route key for integrating with VictorOps.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">slack</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the service key for integrating with Pagerduty.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">victorops</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A set of tags for targeting notifications. Multiple values are comma separated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">teams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A set of teams for targeting notifications. Multiple values are comma separated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Your organization’s Slack URL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">AlertCondition</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition_scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gc_metric</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">runbook_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">terms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_defined_metric</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_defined_value_function</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">violation_close_timer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AlertCondition" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to create and manage alert conditions for APM, Browser, and Mobile in New Relic.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">app</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">get_entity</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;my-app&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;APPLICATION&quot;</span><span class="p">,</span>
    <span class="n">domain</span><span class="o">=</span><span class="s2">&quot;APM&quot;</span><span class="p">)</span>
<span class="n">foo_alert_policy</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertPolicy</span><span class="p">(</span><span class="s2">&quot;fooAlertPolicy&quot;</span><span class="p">)</span>
<span class="n">foo_alert_condition</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertCondition</span><span class="p">(</span><span class="s2">&quot;fooAlertCondition&quot;</span><span class="p">,</span>
    <span class="n">policy_id</span><span class="o">=</span><span class="n">foo_alert_policy</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;apm_app_metric&quot;</span><span class="p">,</span>
    <span class="n">entities</span><span class="o">=</span><span class="p">[</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;newrelic_application&quot;</span><span class="p">][</span><span class="s2">&quot;app&quot;</span><span class="p">][</span><span class="s2">&quot;application_id&quot;</span><span class="p">]],</span>
    <span class="n">metric</span><span class="o">=</span><span class="s2">&quot;apdex&quot;</span><span class="p">,</span>
    <span class="n">runbook_url</span><span class="o">=</span><span class="s2">&quot;https://www.example.com&quot;</span><span class="p">,</span>
    <span class="n">condition_scope</span><span class="o">=</span><span class="s2">&quot;application&quot;</span><span class="p">,</span>
    <span class="n">terms</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;duration&quot;</span><span class="p">:</span> <span class="mi">5</span><span class="p">,</span>
        <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;below&quot;</span><span class="p">,</span>
        <span class="s2">&quot;priority&quot;</span><span class="p">:</span> <span class="s2">&quot;critical&quot;</span><span class="p">,</span>
        <span class="s2">&quot;threshold&quot;</span><span class="p">:</span> <span class="s2">&quot;0.75&quot;</span><span class="p">,</span>
        <span class="s2">&quot;timeFunction&quot;</span><span class="p">:</span> <span class="s2">&quot;all&quot;</span><span class="p">,</span>
    <span class="p">}])</span>
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
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>condition_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">application</span></code> or <code class="docutils literal notranslate"><span class="pre">instance</span></code>.  Choose <code class="docutils literal notranslate"><span class="pre">application</span></code> for most scenarios.  If you are using the JVM plugin in New Relic, the <code class="docutils literal notranslate"><span class="pre">instance</span></code> setting allows your condition to trigger <a class="reference external" href="https://docs.newrelic.com/docs/alerts/new-relic-alerts/defining-conditions/scope-alert-thresholds-specific-instances">for specific app instances</a>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the condition is enabled or not. Defaults to true.</p></li>
<li><p><strong>entities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The instance IDs associated with this condition.</p></li>
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
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the policy where this condition should be used.</p></li>
<li><p><strong>runbook_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Runbook URL to display in notifications.</p></li>
<li><p><strong>terms</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of terms for this condition. See Terms below for details.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of condition. One of: <code class="docutils literal notranslate"><span class="pre">apm_app_metric</span></code>, <code class="docutils literal notranslate"><span class="pre">apm_kt_metric</span></code>, <code class="docutils literal notranslate"><span class="pre">browser_metric</span></code>, <code class="docutils literal notranslate"><span class="pre">mobile_metric</span></code></p></li>
<li><p><strong>user_defined_metric</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A custom metric to be evaluated.</p></li>
<li><p><strong>user_defined_value_function</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – One of: <code class="docutils literal notranslate"><span class="pre">average</span></code>, <code class="docutils literal notranslate"><span class="pre">min</span></code>, <code class="docutils literal notranslate"><span class="pre">max</span></code>, <code class="docutils literal notranslate"><span class="pre">total</span></code>, or <code class="docutils literal notranslate"><span class="pre">sample_size</span></code>.</p></li>
<li><p><strong>violation_close_timer</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Automatically close instance-based violations, including JVM health metric violations, after the number of hours specified. Must be: <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>, <code class="docutils literal notranslate"><span class="pre">4</span></code>, <code class="docutils literal notranslate"><span class="pre">8</span></code>, <code class="docutils literal notranslate"><span class="pre">12</span></code> or <code class="docutils literal notranslate"><span class="pre">24</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>terms</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_newrelic.AlertCondition.condition_scope">
<code class="sig-name descname">condition_scope</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.AlertCondition.condition_scope" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">application</span></code> or <code class="docutils literal notranslate"><span class="pre">instance</span></code>.  Choose <code class="docutils literal notranslate"><span class="pre">application</span></code> for most scenarios.  If you are using the JVM plugin in New Relic, the <code class="docutils literal notranslate"><span class="pre">instance</span></code> setting allows your condition to trigger <a class="reference external" href="https://docs.newrelic.com/docs/alerts/new-relic-alerts/defining-conditions/scope-alert-thresholds-specific-instances">for specific app instances</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.AlertCondition.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.AlertCondition.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the condition is enabled or not. Defaults to true.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.AlertCondition.entities">
<code class="sig-name descname">entities</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.AlertCondition.entities" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance IDs associated with this condition.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.AlertCondition.gc_metric">
<code class="sig-name descname">gc_metric</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.AlertCondition.gc_metric" title="Permalink to this definition">¶</a></dt>
<dd><p>A valid Garbage Collection metric e.g. <code class="docutils literal notranslate"><span class="pre">GC/G1</span> <span class="pre">Young</span> <span class="pre">Generation</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.AlertCondition.metric">
<code class="sig-name descname">metric</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.AlertCondition.metric" title="Permalink to this definition">¶</a></dt>
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

<dl class="py attribute">
<dt id="pulumi_newrelic.AlertCondition.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.AlertCondition.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The title of the condition. Must be between 1 and 64 characters, inclusive.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.AlertCondition.policy_id">
<code class="sig-name descname">policy_id</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.AlertCondition.policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the policy where this condition should be used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.AlertCondition.runbook_url">
<code class="sig-name descname">runbook_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.AlertCondition.runbook_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Runbook URL to display in notifications.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.AlertCondition.terms">
<code class="sig-name descname">terms</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.AlertCondition.terms" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of terms for this condition. See Terms below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.AlertCondition.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.AlertCondition.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of condition. One of: <code class="docutils literal notranslate"><span class="pre">apm_app_metric</span></code>, <code class="docutils literal notranslate"><span class="pre">apm_kt_metric</span></code>, <code class="docutils literal notranslate"><span class="pre">browser_metric</span></code>, <code class="docutils literal notranslate"><span class="pre">mobile_metric</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.AlertCondition.user_defined_metric">
<code class="sig-name descname">user_defined_metric</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.AlertCondition.user_defined_metric" title="Permalink to this definition">¶</a></dt>
<dd><p>A custom metric to be evaluated.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.AlertCondition.user_defined_value_function">
<code class="sig-name descname">user_defined_value_function</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.AlertCondition.user_defined_value_function" title="Permalink to this definition">¶</a></dt>
<dd><p>One of: <code class="docutils literal notranslate"><span class="pre">average</span></code>, <code class="docutils literal notranslate"><span class="pre">min</span></code>, <code class="docutils literal notranslate"><span class="pre">max</span></code>, <code class="docutils literal notranslate"><span class="pre">total</span></code>, or <code class="docutils literal notranslate"><span class="pre">sample_size</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.AlertCondition.violation_close_timer">
<code class="sig-name descname">violation_close_timer</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.AlertCondition.violation_close_timer" title="Permalink to this definition">¶</a></dt>
<dd><p>Automatically close instance-based violations, including JVM health metric violations, after the number of hours specified. Must be: <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>, <code class="docutils literal notranslate"><span class="pre">4</span></code>, <code class="docutils literal notranslate"><span class="pre">8</span></code>, <code class="docutils literal notranslate"><span class="pre">12</span></code> or <code class="docutils literal notranslate"><span class="pre">24</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertCondition.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition_scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gc_metric</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">runbook_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">terms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_defined_metric</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_defined_value_function</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">violation_close_timer</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AlertCondition.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AlertCondition resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>condition_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p><code class="docutils literal notranslate"><span class="pre">application</span></code> or <code class="docutils literal notranslate"><span class="pre">instance</span></code>.  Choose <code class="docutils literal notranslate"><span class="pre">application</span></code> for most scenarios.  If you are using the JVM plugin in New Relic, the <code class="docutils literal notranslate"><span class="pre">instance</span></code> setting allows your condition to trigger <a class="reference external" href="https://docs.newrelic.com/docs/alerts/new-relic-alerts/defining-conditions/scope-alert-thresholds-specific-instances">for specific app instances</a>.</p>
</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the condition is enabled or not. Defaults to true.</p></li>
<li><p><strong>entities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The instance IDs associated with this condition.</p></li>
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
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the policy where this condition should be used.</p></li>
<li><p><strong>runbook_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Runbook URL to display in notifications.</p></li>
<li><p><strong>terms</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of terms for this condition. See Terms below for details.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of condition. One of: <code class="docutils literal notranslate"><span class="pre">apm_app_metric</span></code>, <code class="docutils literal notranslate"><span class="pre">apm_kt_metric</span></code>, <code class="docutils literal notranslate"><span class="pre">browser_metric</span></code>, <code class="docutils literal notranslate"><span class="pre">mobile_metric</span></code></p></li>
<li><p><strong>user_defined_metric</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A custom metric to be evaluated.</p></li>
<li><p><strong>user_defined_value_function</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – One of: <code class="docutils literal notranslate"><span class="pre">average</span></code>, <code class="docutils literal notranslate"><span class="pre">min</span></code>, <code class="docutils literal notranslate"><span class="pre">max</span></code>, <code class="docutils literal notranslate"><span class="pre">total</span></code>, or <code class="docutils literal notranslate"><span class="pre">sample_size</span></code>.</p></li>
<li><p><strong>violation_close_timer</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Automatically close instance-based violations, including JVM health metric violations, after the number of hours specified. Must be: <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>, <code class="docutils literal notranslate"><span class="pre">4</span></code>, <code class="docutils literal notranslate"><span class="pre">8</span></code>, <code class="docutils literal notranslate"><span class="pre">12</span></code> or <code class="docutils literal notranslate"><span class="pre">24</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>terms</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
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
<dt id="pulumi_newrelic.AlertPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">AlertPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">channel_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">incident_preference</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AlertPolicy" title="Permalink to this definition">¶</a></dt>
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
    <span class="n">config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;url&quot;</span><span class="p">:</span> <span class="s2">&quot;https://hooks.slack.com/services/&lt;*****&gt;/&lt;*****&gt;&quot;</span><span class="p">,</span>
        <span class="s2">&quot;channel&quot;</span><span class="p">:</span> <span class="s2">&quot;example-alerts-channel&quot;</span><span class="p">,</span>
    <span class="p">})</span>
<span class="c1"># Provision an email notification channel.</span>
<span class="n">email_channel</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannel</span><span class="p">(</span><span class="s2">&quot;emailChannel&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;email&quot;</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;recipients&quot;</span><span class="p">:</span> <span class="s2">&quot;example@testing.com&quot;</span><span class="p">,</span>
        <span class="s2">&quot;includeJsonAttachment&quot;</span><span class="p">:</span> <span class="s2">&quot;1&quot;</span><span class="p">,</span>
    <span class="p">})</span>
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
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The New Relic account ID to operate on.  This allows the user to override the <code class="docutils literal notranslate"><span class="pre">account_id</span></code> attribute set on the provider. Defaults to the environment variable <code class="docutils literal notranslate"><span class="pre">NEW_RELIC_ACCOUNT_ID</span></code>.</p></li>
<li><p><strong>channel_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of channel IDs (integers) to assign to the policy. Adding or removing channel IDs from this array will result
in a new alert policy resource being created and the old one being destroyed. Also note that channel IDs cannot be
imported via terraform import.</p></li>
<li><p><strong>incident_preference</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The rollup strategy for the policy.  Options include: <code class="docutils literal notranslate"><span class="pre">PER_POLICY</span></code>, <code class="docutils literal notranslate"><span class="pre">PER_CONDITION</span></code>, or <code class="docutils literal notranslate"><span class="pre">PER_CONDITION_AND_TARGET</span></code>.  The default is <code class="docutils literal notranslate"><span class="pre">PER_POLICY</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_newrelic.AlertPolicy.account_id">
<code class="sig-name descname">account_id</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.AlertPolicy.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The New Relic account ID to operate on.  This allows the user to override the <code class="docutils literal notranslate"><span class="pre">account_id</span></code> attribute set on the provider. Defaults to the environment variable <code class="docutils literal notranslate"><span class="pre">NEW_RELIC_ACCOUNT_ID</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.AlertPolicy.channel_ids">
<code class="sig-name descname">channel_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.AlertPolicy.channel_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of channel IDs (integers) to assign to the policy. Adding or removing channel IDs from this array will result
in a new alert policy resource being created and the old one being destroyed. Also note that channel IDs cannot be
imported via terraform import.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.AlertPolicy.incident_preference">
<code class="sig-name descname">incident_preference</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.AlertPolicy.incident_preference" title="Permalink to this definition">¶</a></dt>
<dd><p>The rollup strategy for the policy.  Options include: <code class="docutils literal notranslate"><span class="pre">PER_POLICY</span></code>, <code class="docutils literal notranslate"><span class="pre">PER_CONDITION</span></code>, or <code class="docutils literal notranslate"><span class="pre">PER_CONDITION_AND_TARGET</span></code>.  The default is <code class="docutils literal notranslate"><span class="pre">PER_POLICY</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.AlertPolicy.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.AlertPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">channel_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">incident_preference</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AlertPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AlertPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The New Relic account ID to operate on.  This allows the user to override the <code class="docutils literal notranslate"><span class="pre">account_id</span></code> attribute set on the provider. Defaults to the environment variable <code class="docutils literal notranslate"><span class="pre">NEW_RELIC_ACCOUNT_ID</span></code>.</p></li>
<li><p><strong>channel_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of channel IDs (integers) to assign to the policy. Adding or removing channel IDs from this array will result
in a new alert policy resource being created and the old one being destroyed. Also note that channel IDs cannot be
imported via terraform import.</p></li>
<li><p><strong>incident_preference</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The rollup strategy for the policy.  Options include: <code class="docutils literal notranslate"><span class="pre">PER_POLICY</span></code>, <code class="docutils literal notranslate"><span class="pre">PER_CONDITION</span></code>, or <code class="docutils literal notranslate"><span class="pre">PER_CONDITION_AND_TARGET</span></code>.  The default is <code class="docutils literal notranslate"><span class="pre">PER_POLICY</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy.</p></li>
</ul>
</dd>
</dl>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">AlertPolicyChannel</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">channel_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AlertPolicyChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to map alert policies to alert channels in New Relic.</p>
<p>The example below will apply multiple alert channels to an existing New Relic alert policy.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">example_policy</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">get_alert_policy</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;my-alert-policy&quot;</span><span class="p">)</span>
<span class="c1"># Creates an email alert channel.</span>
<span class="n">email_channel</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannel</span><span class="p">(</span><span class="s2">&quot;emailChannel&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;email&quot;</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;recipients&quot;</span><span class="p">:</span> <span class="s2">&quot;foo@example.com&quot;</span><span class="p">,</span>
        <span class="s2">&quot;includeJsonAttachment&quot;</span><span class="p">:</span> <span class="s2">&quot;1&quot;</span><span class="p">,</span>
    <span class="p">})</span>
<span class="c1"># Creates a Slack alert channel.</span>
<span class="n">slack_channel</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertChannel</span><span class="p">(</span><span class="s2">&quot;slackChannel&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;slack&quot;</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;channel&quot;</span><span class="p">:</span> <span class="s2">&quot;#example-channel&quot;</span><span class="p">,</span>
        <span class="s2">&quot;url&quot;</span><span class="p">:</span> <span class="s2">&quot;http://example-org.slack.com&quot;</span><span class="p">,</span>
    <span class="p">})</span>
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
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>channel_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of channel IDs to apply to the specified policy. We recommended sorting channel IDs in ascending order to avoid
drift your Terraform state.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the policy.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_newrelic.AlertPolicyChannel.channel_ids">
<code class="sig-name descname">channel_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.AlertPolicyChannel.channel_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of channel IDs to apply to the specified policy. We recommended sorting channel IDs in ascending order to avoid
drift your Terraform state.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.AlertPolicyChannel.policy_id">
<code class="sig-name descname">policy_id</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.AlertPolicyChannel.policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the policy.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.AlertPolicyChannel.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">channel_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AlertPolicyChannel.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AlertPolicyChannel resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>channel_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of channel IDs to apply to the specified policy. We recommended sorting channel IDs in ascending order to avoid
drift your Terraform state.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the policy.</p></li>
</ul>
</dd>
</dl>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">AwaitableGetEntityResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">guid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AwaitableGetEntityResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_newrelic.AwaitableGetKeyTransactionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">AwaitableGetKeyTransactionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.AwaitableGetKeyTransactionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_newrelic.Dashboard">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">Dashboard</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">editable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grid_column_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">icon</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">widgets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.Dashboard" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to create and manage New Relic dashboards.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">my_application</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">get_entity</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;My Application&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;APPLICATION&quot;</span><span class="p">,</span>
    <span class="n">domain</span><span class="o">=</span><span class="s2">&quot;APM&quot;</span><span class="p">)</span>
<span class="n">exampledash</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">Dashboard</span><span class="p">(</span><span class="s2">&quot;exampledash&quot;</span><span class="p">,</span>
    <span class="n">title</span><span class="o">=</span><span class="s2">&quot;New Relic Terraform Example&quot;</span><span class="p">,</span>
    <span class="nb">filter</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;eventTypes&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;Transaction&quot;</span><span class="p">],</span>
        <span class="s2">&quot;attributes&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="s2">&quot;appName&quot;</span><span class="p">,</span>
            <span class="s2">&quot;name&quot;</span><span class="p">,</span>
        <span class="p">],</span>
    <span class="p">},</span>
    <span class="n">widgets</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;title&quot;</span><span class="p">:</span> <span class="s2">&quot;Requests per minute&quot;</span><span class="p">,</span>
            <span class="s2">&quot;visualization&quot;</span><span class="p">:</span> <span class="s2">&quot;billboard&quot;</span><span class="p">,</span>
            <span class="s2">&quot;nrql&quot;</span><span class="p">:</span> <span class="s2">&quot;SELECT rate(count(*), 1 minute) FROM Transaction&quot;</span><span class="p">,</span>
            <span class="s2">&quot;row&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
            <span class="s2">&quot;column&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;title&quot;</span><span class="p">:</span> <span class="s2">&quot;Error rate&quot;</span><span class="p">,</span>
            <span class="s2">&quot;visualization&quot;</span><span class="p">:</span> <span class="s2">&quot;gauge&quot;</span><span class="p">,</span>
            <span class="s2">&quot;nrql&quot;</span><span class="p">:</span> <span class="s2">&quot;SELECT percentage(count(*), WHERE error IS True) FROM Transaction&quot;</span><span class="p">,</span>
            <span class="s2">&quot;thresholdRed&quot;</span><span class="p">:</span> <span class="mf">2.5</span><span class="p">,</span>
            <span class="s2">&quot;row&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
            <span class="s2">&quot;column&quot;</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;title&quot;</span><span class="p">:</span> <span class="s2">&quot;Average transaction duration, by application&quot;</span><span class="p">,</span>
            <span class="s2">&quot;visualization&quot;</span><span class="p">:</span> <span class="s2">&quot;facet_bar_chart&quot;</span><span class="p">,</span>
            <span class="s2">&quot;nrql&quot;</span><span class="p">:</span> <span class="s2">&quot;SELECT average(duration) FROM Transaction FACET appName&quot;</span><span class="p">,</span>
            <span class="s2">&quot;row&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
            <span class="s2">&quot;column&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;title&quot;</span><span class="p">:</span> <span class="s2">&quot;Apdex, top 5 by host&quot;</span><span class="p">,</span>
            <span class="s2">&quot;duration&quot;</span><span class="p">:</span> <span class="mi">1800000</span><span class="p">,</span>
            <span class="s2">&quot;visualization&quot;</span><span class="p">:</span> <span class="s2">&quot;metric_line_chart&quot;</span><span class="p">,</span>
            <span class="s2">&quot;entityIds&quot;</span><span class="p">:</span> <span class="p">[</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;newrelic_application&quot;</span><span class="p">][</span><span class="s2">&quot;my_application&quot;</span><span class="p">][</span><span class="s2">&quot;application_id&quot;</span><span class="p">]],</span>
            <span class="s2">&quot;metrics&quot;</span><span class="p">:</span> <span class="p">[{</span>
                <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;Apdex&quot;</span><span class="p">,</span>
                <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;score&quot;</span><span class="p">],</span>
            <span class="p">}],</span>
            <span class="s2">&quot;facet&quot;</span><span class="p">:</span> <span class="s2">&quot;host&quot;</span><span class="p">,</span>
            <span class="s2">&quot;limit&quot;</span><span class="p">:</span> <span class="mi">5</span><span class="p">,</span>
            <span class="s2">&quot;row&quot;</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span>
            <span class="s2">&quot;column&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;title&quot;</span><span class="p">:</span> <span class="s2">&quot;Requests per minute, by transaction&quot;</span><span class="p">,</span>
            <span class="s2">&quot;visualization&quot;</span><span class="p">:</span> <span class="s2">&quot;facet_table&quot;</span><span class="p">,</span>
            <span class="s2">&quot;nrql&quot;</span><span class="p">:</span> <span class="s2">&quot;SELECT rate(count(*), 1 minute) FROM Transaction FACET name&quot;</span><span class="p">,</span>
            <span class="s2">&quot;row&quot;</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span>
            <span class="s2">&quot;column&quot;</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;title&quot;</span><span class="p">:</span> <span class="s2">&quot;Dashboard Note&quot;</span><span class="p">,</span>
            <span class="s2">&quot;visualization&quot;</span><span class="p">:</span> <span class="s2">&quot;markdown&quot;</span><span class="p">,</span>
            <span class="s2">&quot;source&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;&quot;### Helpful Links</span>

<span class="s2">* [New Relic One](https://one.newrelic.com)</span>
<span class="s2">* [Developer Portal](https://developer.newrelic.com)&quot;&quot;&quot;</span><span class="p">,</span>
            <span class="s2">&quot;row&quot;</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span>
            <span class="s2">&quot;column&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">])</span>
</pre></div>
</div>
<p>In addition to all arguments above, the following attributes are exported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dashboard_url</span></code> - The URL for viewing the dashboard.</p></li>
</ul>
<p>All nested <code class="docutils literal notranslate"><span class="pre">widget</span></code> blocks support the following common arguments:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> - (Required) A title for the widget.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">visualization</span></code> - (Required) How the widget visualizes data.  Valid values are <code class="docutils literal notranslate"><span class="pre">billboard</span></code>, <code class="docutils literal notranslate"><span class="pre">gauge</span></code>, <code class="docutils literal notranslate"><span class="pre">billboard_comparison</span></code>, <code class="docutils literal notranslate"><span class="pre">facet_bar_chart</span></code>, <code class="docutils literal notranslate"><span class="pre">faceted_line_chart</span></code>, <code class="docutils literal notranslate"><span class="pre">facet_pie_chart</span></code>, <code class="docutils literal notranslate"><span class="pre">facet_table</span></code>, <code class="docutils literal notranslate"><span class="pre">faceted_area_chart</span></code>, <code class="docutils literal notranslate"><span class="pre">heatmap</span></code>, <code class="docutils literal notranslate"><span class="pre">attribute_sheet</span></code>, <code class="docutils literal notranslate"><span class="pre">single_event</span></code>, <code class="docutils literal notranslate"><span class="pre">histogram</span></code>, <code class="docutils literal notranslate"><span class="pre">funnel</span></code>, <code class="docutils literal notranslate"><span class="pre">raw_json</span></code>, <code class="docutils literal notranslate"><span class="pre">event_feed</span></code>, <code class="docutils literal notranslate"><span class="pre">event_table</span></code>, <code class="docutils literal notranslate"><span class="pre">uniques_list</span></code>, <code class="docutils literal notranslate"><span class="pre">line_chart</span></code>, <code class="docutils literal notranslate"><span class="pre">comparison_line_chart</span></code>, <code class="docutils literal notranslate"><span class="pre">markdown</span></code>, and <code class="docutils literal notranslate"><span class="pre">metric_line_chart</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">row</span></code> - (Required) Row position of widget from top left, starting at <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">column</span></code> - (Required) Column position of widget from top left, starting at <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">width</span></code> - (Optional) Width of the widget.  Valid values are <code class="docutils literal notranslate"><span class="pre">1</span></code> to <code class="docutils literal notranslate"><span class="pre">3</span></code> inclusive.  Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">height</span></code> - (Optional) Height of the widget.  Valid values are <code class="docutils literal notranslate"><span class="pre">1</span></code> to <code class="docutils literal notranslate"><span class="pre">3</span></code> inclusive.  Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notes</span></code> - (Optional) Description of the widget.</p></li>
</ul>
<p>Each <code class="docutils literal notranslate"><span class="pre">visualization</span></code> type supports an additional set of arguments:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">billboard</span></code>, <code class="docutils literal notranslate"><span class="pre">billboard_comparison</span></code>:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">nrql</span></code> - (Required) Valid NRQL query string. See <a class="reference external" href="https://docs.newrelic.com/docs/insights/nrql-new-relic-query-language/using-nrql/introduction-nrql">Writing NRQL Queries</a> for help.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold_red</span></code> - (Optional) Threshold above which the displayed value will be styled with a red color.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold_yellow</span></code> - (Optional) Threshold above which the displayed value will be styled with a yellow color.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">gauge</span></code>:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">nrql</span></code> - (Required) Valid NRQL query string. See <a class="reference external" href="https://docs.newrelic.com/docs/insights/nrql-new-relic-query-language/using-nrql/introduction-nrql">Writing NRQL Queries</a> for help.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold_red</span></code> - (Required) Threshold above which the displayed value will be styled with a red color.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold_yellow</span></code> - (Optional) Threshold above which the displayed value will be styled with a yellow color.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">facet_bar_chart</span></code>, <code class="docutils literal notranslate"><span class="pre">facet_pie_chart</span></code>, <code class="docutils literal notranslate"><span class="pre">facet_table</span></code>, <code class="docutils literal notranslate"><span class="pre">faceted_area_chart</span></code>, <code class="docutils literal notranslate"><span class="pre">faceted_line_chart</span></code>, or <code class="docutils literal notranslate"><span class="pre">heatmap</span></code>:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">nrql</span></code> - (Required) Valid NRQL query string. See <a class="reference external" href="https://docs.newrelic.com/docs/insights/nrql-new-relic-query-language/using-nrql/introduction-nrql">Writing NRQL Queries</a> for help.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">drilldown_dashboard_id</span></code> - (Optional) The ID of a dashboard to link to from the widget’s facets.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">attribute_sheet</span></code>, <code class="docutils literal notranslate"><span class="pre">comparison_line_chart</span></code>, <code class="docutils literal notranslate"><span class="pre">event_feed</span></code>, <code class="docutils literal notranslate"><span class="pre">event_table</span></code>, <code class="docutils literal notranslate"><span class="pre">funnel</span></code>, <code class="docutils literal notranslate"><span class="pre">histogram</span></code>, <code class="docutils literal notranslate"><span class="pre">line_chart</span></code>, <code class="docutils literal notranslate"><span class="pre">raw_json</span></code>, <code class="docutils literal notranslate"><span class="pre">single_event</span></code>, or <code class="docutils literal notranslate"><span class="pre">uniques_list</span></code>:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">nrql</span></code> - (Required) Valid NRQL query string. See <a class="reference external" href="https://docs.newrelic.com/docs/insights/nrql-new-relic-query-language/using-nrql/introduction-nrql">Writing NRQL Queries</a> for help.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">markdown</span></code>:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> - (Required) The markdown source to be rendered in the widget.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">metric_line_chart</span></code>:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">entity_ids</span></code> - (Required) A collection of entity ids to display data for.  These are typically application IDs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metric</span></code> - (Required) A nested block that describes a metric.  Nested <code class="docutils literal notranslate"><span class="pre">metric</span></code> blocks support the following arguments:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) The metric name to display.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> - (Required) The metric values to display.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> - (Required) The duration, in ms, of the time window represented in the chart.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">end_time</span></code> - (Optional) The end time of the time window represented in the chart in epoch time.  When not set, the time window will end at the current time.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">facet</span></code> - (Optional) Can be set to “host” to facet the metric data by host.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">limit</span></code> - (Optional) The limit of distinct data series to display.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">application_breakdown</span></code>:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">entity_ids</span></code> - (Required) A collection of entity IDs to display data. These are typically application IDs.</p></li>
</ul>
</li>
</ul>
<p>The optional filter block supports the following arguments:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">event_types</span></code> - (Optional) A list of event types to enable filtering for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attributes</span></code> - (Optional) A list of attributes belonging to the specified event types to enable filtering for.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>editable</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determines who can edit the dashboard in an account. Valid values are <code class="docutils literal notranslate"><span class="pre">all</span></code>,  <code class="docutils literal notranslate"><span class="pre">editable_by_all</span></code>, <code class="docutils literal notranslate"><span class="pre">editable_by_owner</span></code>, or <code class="docutils literal notranslate"><span class="pre">read_only</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">editable_by_all</span></code>.</p></li>
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested block that describes a dashboard filter.  Exactly one nested <code class="docutils literal notranslate"><span class="pre">filter</span></code> block is allowed. See Nested filter block below for details.</p></li>
<li><p><strong>grid_column_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of columns to use when organizing and displaying widgets. New Relic One supports a 3 column grid and a 12 column grid. New Relic Insights supports a 3 column grid.</p></li>
<li><p><strong>icon</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The icon for the dashboard.  Valid values are <code class="docutils literal notranslate"><span class="pre">adjust</span></code>, <code class="docutils literal notranslate"><span class="pre">archive</span></code>, <code class="docutils literal notranslate"><span class="pre">bar-chart</span></code>, <code class="docutils literal notranslate"><span class="pre">bell</span></code>, <code class="docutils literal notranslate"><span class="pre">bolt</span></code>, <code class="docutils literal notranslate"><span class="pre">bug</span></code>, <code class="docutils literal notranslate"><span class="pre">bullhorn</span></code>, <code class="docutils literal notranslate"><span class="pre">bullseye</span></code>, <code class="docutils literal notranslate"><span class="pre">clock-o</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud</span></code>, <code class="docutils literal notranslate"><span class="pre">cog</span></code>, <code class="docutils literal notranslate"><span class="pre">comments-o</span></code>, <code class="docutils literal notranslate"><span class="pre">crosshairs</span></code>, <code class="docutils literal notranslate"><span class="pre">dashboard</span></code>, <code class="docutils literal notranslate"><span class="pre">envelope</span></code>, <code class="docutils literal notranslate"><span class="pre">fire</span></code>, <code class="docutils literal notranslate"><span class="pre">flag</span></code>, <code class="docutils literal notranslate"><span class="pre">flask</span></code>, <code class="docutils literal notranslate"><span class="pre">globe</span></code>, <code class="docutils literal notranslate"><span class="pre">heart</span></code>, <code class="docutils literal notranslate"><span class="pre">leaf</span></code>, <code class="docutils literal notranslate"><span class="pre">legal</span></code>, <code class="docutils literal notranslate"><span class="pre">life-ring</span></code>, <code class="docutils literal notranslate"><span class="pre">line-chart</span></code>, <code class="docutils literal notranslate"><span class="pre">magic</span></code>, <code class="docutils literal notranslate"><span class="pre">mobile</span></code>, <code class="docutils literal notranslate"><span class="pre">money</span></code>, <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">paper-plane</span></code>, <code class="docutils literal notranslate"><span class="pre">pie-chart</span></code>, <code class="docutils literal notranslate"><span class="pre">puzzle-piece</span></code>, <code class="docutils literal notranslate"><span class="pre">road</span></code>, <code class="docutils literal notranslate"><span class="pre">rocket</span></code>, <code class="docutils literal notranslate"><span class="pre">shopping-cart</span></code>, <code class="docutils literal notranslate"><span class="pre">sitemap</span></code>, <code class="docutils literal notranslate"><span class="pre">sliders</span></code>, <code class="docutils literal notranslate"><span class="pre">tablet</span></code>, <code class="docutils literal notranslate"><span class="pre">thumbs-down</span></code>, <code class="docutils literal notranslate"><span class="pre">thumbs-up</span></code>, <code class="docutils literal notranslate"><span class="pre">trophy</span></code>, <code class="docutils literal notranslate"><span class="pre">usd</span></code>, <code class="docutils literal notranslate"><span class="pre">user</span></code>, and <code class="docutils literal notranslate"><span class="pre">users</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">bar-chart</span></code>.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of the dashboard.</p></li>
<li><p><strong>visibility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determines who can see the dashboard in an account. Valid values are <code class="docutils literal notranslate"><span class="pre">all</span></code> or <code class="docutils literal notranslate"><span class="pre">owner</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">all</span></code>.</p></li>
<li><p><strong>widgets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A nested block that describes a visualization.  Up to 300 <code class="docutils literal notranslate"><span class="pre">widget</span></code> blocks are allowed in a dashboard definition.  See Nested widget blocks below for details.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filter</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attributes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eventTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>widgets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">column</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compareWiths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">offsetDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">presentation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">color</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">drilldownDashboardId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">entityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">facet</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">height</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">limit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metrics</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">units</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">notes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nrql</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">orderBy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rawMetricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">row</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdRed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdYellow</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The title of the dashboard.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">visualization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">widgetId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">width</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_newrelic.Dashboard.dashboard_url">
<code class="sig-name descname">dashboard_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.Dashboard.dashboard_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL for viewing the dashboard.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.Dashboard.editable">
<code class="sig-name descname">editable</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.Dashboard.editable" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines who can edit the dashboard in an account. Valid values are <code class="docutils literal notranslate"><span class="pre">all</span></code>,  <code class="docutils literal notranslate"><span class="pre">editable_by_all</span></code>, <code class="docutils literal notranslate"><span class="pre">editable_by_owner</span></code>, or <code class="docutils literal notranslate"><span class="pre">read_only</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">editable_by_all</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.Dashboard.filter">
<code class="sig-name descname">filter</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.Dashboard.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>A nested block that describes a dashboard filter.  Exactly one nested <code class="docutils literal notranslate"><span class="pre">filter</span></code> block is allowed. See Nested filter block below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attributes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eventTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.Dashboard.grid_column_count">
<code class="sig-name descname">grid_column_count</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.Dashboard.grid_column_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of columns to use when organizing and displaying widgets. New Relic One supports a 3 column grid and a 12 column grid. New Relic Insights supports a 3 column grid.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.Dashboard.icon">
<code class="sig-name descname">icon</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.Dashboard.icon" title="Permalink to this definition">¶</a></dt>
<dd><p>The icon for the dashboard.  Valid values are <code class="docutils literal notranslate"><span class="pre">adjust</span></code>, <code class="docutils literal notranslate"><span class="pre">archive</span></code>, <code class="docutils literal notranslate"><span class="pre">bar-chart</span></code>, <code class="docutils literal notranslate"><span class="pre">bell</span></code>, <code class="docutils literal notranslate"><span class="pre">bolt</span></code>, <code class="docutils literal notranslate"><span class="pre">bug</span></code>, <code class="docutils literal notranslate"><span class="pre">bullhorn</span></code>, <code class="docutils literal notranslate"><span class="pre">bullseye</span></code>, <code class="docutils literal notranslate"><span class="pre">clock-o</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud</span></code>, <code class="docutils literal notranslate"><span class="pre">cog</span></code>, <code class="docutils literal notranslate"><span class="pre">comments-o</span></code>, <code class="docutils literal notranslate"><span class="pre">crosshairs</span></code>, <code class="docutils literal notranslate"><span class="pre">dashboard</span></code>, <code class="docutils literal notranslate"><span class="pre">envelope</span></code>, <code class="docutils literal notranslate"><span class="pre">fire</span></code>, <code class="docutils literal notranslate"><span class="pre">flag</span></code>, <code class="docutils literal notranslate"><span class="pre">flask</span></code>, <code class="docutils literal notranslate"><span class="pre">globe</span></code>, <code class="docutils literal notranslate"><span class="pre">heart</span></code>, <code class="docutils literal notranslate"><span class="pre">leaf</span></code>, <code class="docutils literal notranslate"><span class="pre">legal</span></code>, <code class="docutils literal notranslate"><span class="pre">life-ring</span></code>, <code class="docutils literal notranslate"><span class="pre">line-chart</span></code>, <code class="docutils literal notranslate"><span class="pre">magic</span></code>, <code class="docutils literal notranslate"><span class="pre">mobile</span></code>, <code class="docutils literal notranslate"><span class="pre">money</span></code>, <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">paper-plane</span></code>, <code class="docutils literal notranslate"><span class="pre">pie-chart</span></code>, <code class="docutils literal notranslate"><span class="pre">puzzle-piece</span></code>, <code class="docutils literal notranslate"><span class="pre">road</span></code>, <code class="docutils literal notranslate"><span class="pre">rocket</span></code>, <code class="docutils literal notranslate"><span class="pre">shopping-cart</span></code>, <code class="docutils literal notranslate"><span class="pre">sitemap</span></code>, <code class="docutils literal notranslate"><span class="pre">sliders</span></code>, <code class="docutils literal notranslate"><span class="pre">tablet</span></code>, <code class="docutils literal notranslate"><span class="pre">thumbs-down</span></code>, <code class="docutils literal notranslate"><span class="pre">thumbs-up</span></code>, <code class="docutils literal notranslate"><span class="pre">trophy</span></code>, <code class="docutils literal notranslate"><span class="pre">usd</span></code>, <code class="docutils literal notranslate"><span class="pre">user</span></code>, and <code class="docutils literal notranslate"><span class="pre">users</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">bar-chart</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.Dashboard.title">
<code class="sig-name descname">title</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.Dashboard.title" title="Permalink to this definition">¶</a></dt>
<dd><p>The title of the dashboard.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.Dashboard.visibility">
<code class="sig-name descname">visibility</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.Dashboard.visibility" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines who can see the dashboard in an account. Valid values are <code class="docutils literal notranslate"><span class="pre">all</span></code> or <code class="docutils literal notranslate"><span class="pre">owner</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">all</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.Dashboard.widgets">
<code class="sig-name descname">widgets</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.Dashboard.widgets" title="Permalink to this definition">¶</a></dt>
<dd><p>A nested block that describes a visualization.  Up to 300 <code class="docutils literal notranslate"><span class="pre">widget</span></code> blocks are allowed in a dashboard definition.  See Nested widget blocks below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">column</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compareWiths</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">offsetDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">presentation</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">color</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">drilldownDashboardId</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endTime</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">entityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">facet</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">height</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">limit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metrics</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">units</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">notes</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nrql</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">orderBy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rawMetricName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">row</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdRed</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdYellow</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The title of the dashboard.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">visualization</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">widgetId</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">width</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.Dashboard.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dashboard_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">editable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grid_column_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">icon</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">widgets</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.Dashboard.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Dashboard resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dashboard_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL for viewing the dashboard.</p></li>
<li><p><strong>editable</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determines who can edit the dashboard in an account. Valid values are <code class="docutils literal notranslate"><span class="pre">all</span></code>,  <code class="docutils literal notranslate"><span class="pre">editable_by_all</span></code>, <code class="docutils literal notranslate"><span class="pre">editable_by_owner</span></code>, or <code class="docutils literal notranslate"><span class="pre">read_only</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">editable_by_all</span></code>.</p></li>
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested block that describes a dashboard filter.  Exactly one nested <code class="docutils literal notranslate"><span class="pre">filter</span></code> block is allowed. See Nested filter block below for details.</p></li>
<li><p><strong>grid_column_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of columns to use when organizing and displaying widgets. New Relic One supports a 3 column grid and a 12 column grid. New Relic Insights supports a 3 column grid.</p></li>
<li><p><strong>icon</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The icon for the dashboard.  Valid values are <code class="docutils literal notranslate"><span class="pre">adjust</span></code>, <code class="docutils literal notranslate"><span class="pre">archive</span></code>, <code class="docutils literal notranslate"><span class="pre">bar-chart</span></code>, <code class="docutils literal notranslate"><span class="pre">bell</span></code>, <code class="docutils literal notranslate"><span class="pre">bolt</span></code>, <code class="docutils literal notranslate"><span class="pre">bug</span></code>, <code class="docutils literal notranslate"><span class="pre">bullhorn</span></code>, <code class="docutils literal notranslate"><span class="pre">bullseye</span></code>, <code class="docutils literal notranslate"><span class="pre">clock-o</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud</span></code>, <code class="docutils literal notranslate"><span class="pre">cog</span></code>, <code class="docutils literal notranslate"><span class="pre">comments-o</span></code>, <code class="docutils literal notranslate"><span class="pre">crosshairs</span></code>, <code class="docutils literal notranslate"><span class="pre">dashboard</span></code>, <code class="docutils literal notranslate"><span class="pre">envelope</span></code>, <code class="docutils literal notranslate"><span class="pre">fire</span></code>, <code class="docutils literal notranslate"><span class="pre">flag</span></code>, <code class="docutils literal notranslate"><span class="pre">flask</span></code>, <code class="docutils literal notranslate"><span class="pre">globe</span></code>, <code class="docutils literal notranslate"><span class="pre">heart</span></code>, <code class="docutils literal notranslate"><span class="pre">leaf</span></code>, <code class="docutils literal notranslate"><span class="pre">legal</span></code>, <code class="docutils literal notranslate"><span class="pre">life-ring</span></code>, <code class="docutils literal notranslate"><span class="pre">line-chart</span></code>, <code class="docutils literal notranslate"><span class="pre">magic</span></code>, <code class="docutils literal notranslate"><span class="pre">mobile</span></code>, <code class="docutils literal notranslate"><span class="pre">money</span></code>, <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">paper-plane</span></code>, <code class="docutils literal notranslate"><span class="pre">pie-chart</span></code>, <code class="docutils literal notranslate"><span class="pre">puzzle-piece</span></code>, <code class="docutils literal notranslate"><span class="pre">road</span></code>, <code class="docutils literal notranslate"><span class="pre">rocket</span></code>, <code class="docutils literal notranslate"><span class="pre">shopping-cart</span></code>, <code class="docutils literal notranslate"><span class="pre">sitemap</span></code>, <code class="docutils literal notranslate"><span class="pre">sliders</span></code>, <code class="docutils literal notranslate"><span class="pre">tablet</span></code>, <code class="docutils literal notranslate"><span class="pre">thumbs-down</span></code>, <code class="docutils literal notranslate"><span class="pre">thumbs-up</span></code>, <code class="docutils literal notranslate"><span class="pre">trophy</span></code>, <code class="docutils literal notranslate"><span class="pre">usd</span></code>, <code class="docutils literal notranslate"><span class="pre">user</span></code>, and <code class="docutils literal notranslate"><span class="pre">users</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">bar-chart</span></code>.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of the dashboard.</p></li>
<li><p><strong>visibility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determines who can see the dashboard in an account. Valid values are <code class="docutils literal notranslate"><span class="pre">all</span></code> or <code class="docutils literal notranslate"><span class="pre">owner</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">all</span></code>.</p></li>
<li><p><strong>widgets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A nested block that describes a visualization.  Up to 300 <code class="docutils literal notranslate"><span class="pre">widget</span></code> blocks are allowed in a dashboard definition.  See Nested widget blocks below for details.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filter</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attributes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eventTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>widgets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">column</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compareWiths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">offsetDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">presentation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">color</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">drilldownDashboardId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">entityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">facet</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">height</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">limit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metrics</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">units</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">notes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nrql</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">orderBy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rawMetricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">row</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdRed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdYellow</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The title of the dashboard.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">visualization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">widgetId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">width</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">EntityTags</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">guid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.EntityTags" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to create, update, and delete tags for a New Relic One entity.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foo_entity</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">get_entity</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Example application&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;APPLICATION&quot;</span><span class="p">,</span>
    <span class="n">domain</span><span class="o">=</span><span class="s2">&quot;APM&quot;</span><span class="p">)</span>
<span class="n">foo_entity_tags</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">EntityTags</span><span class="p">(</span><span class="s2">&quot;fooEntityTags&quot;</span><span class="p">,</span>
    <span class="n">guid</span><span class="o">=</span><span class="n">foo_entity</span><span class="o">.</span><span class="n">guid</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;my-key&quot;</span><span class="p">,</span>
            <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span>
                <span class="s2">&quot;my-value&quot;</span><span class="p">,</span>
                <span class="s2">&quot;my-other-value&quot;</span><span class="p">,</span>
            <span class="p">],</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;my-key-2&quot;</span><span class="p">,</span>
            <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;my-value-2&quot;</span><span class="p">],</span>
        <span class="p">},</span>
    <span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>guid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The guid of the entity to tag.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A nested block that describes an entity tag. See Nested tag blocks below for details.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The tag values.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_newrelic.EntityTags.guid">
<code class="sig-name descname">guid</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.EntityTags.guid" title="Permalink to this definition">¶</a></dt>
<dd><p>The guid of the entity to tag.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.EntityTags.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.EntityTags.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A nested block that describes an entity tag. See Nested tag blocks below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tag key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The tag values.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.EntityTags.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">guid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.EntityTags.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EntityTags resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>guid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The guid of the entity to tag.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A nested block that describes an entity tag. See Nested tag blocks below for details.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The tag values.</p></li>
</ul>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">EventsToMetricsRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nrql</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.EventsToMetricsRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to create, update, and delete New Relic Events to Metrics rules.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">EventsToMetricsRule</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">account_id</span><span class="o">=</span><span class="mi">12345</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Example description&quot;</span><span class="p">,</span>
    <span class="n">nrql</span><span class="o">=</span><span class="s2">&quot;SELECT uniqueCount(account_id) AS ``Transaction.account_id`` FROM Transaction FACET appName, name&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Account with the event and where the metrics will be put.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Provides additional information about the rule.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – True means this rule is enabled. False means the rule is currently not creating metrics.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule. This must be unique within an account.</p></li>
<li><p><strong>nrql</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Explains how to create metrics from events.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_newrelic.EventsToMetricsRule.account_id">
<code class="sig-name descname">account_id</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.EventsToMetricsRule.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account with the event and where the metrics will be put.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.EventsToMetricsRule.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.EventsToMetricsRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides additional information about the rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.EventsToMetricsRule.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.EventsToMetricsRule.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>True means this rule is enabled. False means the rule is currently not creating metrics.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.EventsToMetricsRule.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.EventsToMetricsRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the rule. This must be unique within an account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.EventsToMetricsRule.nrql">
<code class="sig-name descname">nrql</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.EventsToMetricsRule.nrql" title="Permalink to this definition">¶</a></dt>
<dd><p>Explains how to create metrics from events.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.EventsToMetricsRule.rule_id">
<code class="sig-name descname">rule_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.EventsToMetricsRule.rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id, uniquely identifying the rule.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.EventsToMetricsRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nrql</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rule_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.EventsToMetricsRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EventsToMetricsRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Account with the event and where the metrics will be put.</p></li>
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
<dl class="py attribute">
<dt id="pulumi_newrelic.GetAccountResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.GetAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_newrelic.GetAlertChannelResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">GetAlertChannelResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.GetAlertChannelResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAlertChannel.</p>
<dl class="py attribute">
<dt id="pulumi_newrelic.GetAlertChannelResult.config">
<code class="sig-name descname">config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.GetAlertChannelResult.config" title="Permalink to this definition">¶</a></dt>
<dd><p>Alert channel configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.GetAlertChannelResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.GetAlertChannelResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.GetAlertChannelResult.policy_ids">
<code class="sig-name descname">policy_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.GetAlertChannelResult.policy_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of policy IDs associated with the alert channel.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.GetAlertChannelResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.GetAlertChannelResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Alert channel type, either: <code class="docutils literal notranslate"><span class="pre">email</span></code>, <code class="docutils literal notranslate"><span class="pre">opsgenie</span></code>, <code class="docutils literal notranslate"><span class="pre">pagerduty</span></code>, <code class="docutils literal notranslate"><span class="pre">slack</span></code>, <code class="docutils literal notranslate"><span class="pre">victorops</span></code>, or <code class="docutils literal notranslate"><span class="pre">webhook</span></code>.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_newrelic.GetAlertPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">GetAlertPolicyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">incident_preference</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated_at</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.GetAlertPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAlertPolicy.</p>
<dl class="py attribute">
<dt id="pulumi_newrelic.GetAlertPolicyResult.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.GetAlertPolicyResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time the policy was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.GetAlertPolicyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.GetAlertPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.GetAlertPolicyResult.incident_preference">
<code class="sig-name descname">incident_preference</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.GetAlertPolicyResult.incident_preference" title="Permalink to this definition">¶</a></dt>
<dd><p>The rollup strategy for the policy. Options include: PER_POLICY, PER_CONDITION, or PER_CONDITION_AND_TARGET. The default is PER_POLICY.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.GetAlertPolicyResult.updated_at">
<code class="sig-name descname">updated_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.GetAlertPolicyResult.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time the policy was last updated.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_newrelic.GetApplicationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">GetApplicationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">host_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.GetApplicationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getApplication.</p>
<dl class="py attribute">
<dt id="pulumi_newrelic.GetApplicationResult.host_ids">
<code class="sig-name descname">host_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.GetApplicationResult.host_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of host IDs associated with the application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.GetApplicationResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.GetApplicationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.GetApplicationResult.instance_ids">
<code class="sig-name descname">instance_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.GetApplicationResult.instance_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of instance IDs associated with the application.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_newrelic.GetEntityResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">GetEntityResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">guid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.GetEntityResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getEntity.</p>
<dl class="py attribute">
<dt id="pulumi_newrelic.GetEntityResult.account_id">
<code class="sig-name descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.GetEntityResult.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The New Relic account ID associated with this entity.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.GetEntityResult.application_id">
<code class="sig-name descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.GetEntityResult.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain-specific application ID of the entity. Only returned for APM and Browser applications.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.GetEntityResult.guid">
<code class="sig-name descname">guid</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.GetEntityResult.guid" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique GUID of the entity.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.GetEntityResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.GetEntityResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_newrelic.GetKeyTransactionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">GetKeyTransactionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.GetKeyTransactionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKeyTransaction.</p>
<dl class="py attribute">
<dt id="pulumi_newrelic.GetKeyTransactionResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.GetKeyTransactionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_newrelic.InfraAlertCondition">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">InfraAlertCondition</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comparison</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">critical</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_provider</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">process_where</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">runbook_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">select</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">violation_close_timer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">warning</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">where</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to create and manage Infrastructure alert conditions in New Relic.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertPolicy</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">)</span>
<span class="n">high_disk_usage</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">InfraAlertCondition</span><span class="p">(</span><span class="s2">&quot;highDiskUsage&quot;</span><span class="p">,</span>
    <span class="n">policy_id</span><span class="o">=</span><span class="n">foo</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;infra_metric&quot;</span><span class="p">,</span>
    <span class="n">event</span><span class="o">=</span><span class="s2">&quot;StorageSample&quot;</span><span class="p">,</span>
    <span class="n">select</span><span class="o">=</span><span class="s2">&quot;diskUsedPercent&quot;</span><span class="p">,</span>
    <span class="n">comparison</span><span class="o">=</span><span class="s2">&quot;above&quot;</span><span class="p">,</span>
    <span class="n">where</span><span class="o">=</span><span class="s2">&quot;(`hostname` LIKE &#39;</span><span class="si">%f</span><span class="s2">rontend%&#39;)&quot;</span><span class="p">,</span>
    <span class="n">critical</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;duration&quot;</span><span class="p">:</span> <span class="mi">25</span><span class="p">,</span>
        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="mi">90</span><span class="p">,</span>
        <span class="s2">&quot;timeFunction&quot;</span><span class="p">:</span> <span class="s2">&quot;all&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">warning</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;duration&quot;</span><span class="p">:</span> <span class="mi">10</span><span class="p">,</span>
        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="mi">80</span><span class="p">,</span>
        <span class="s2">&quot;timeFunction&quot;</span><span class="p">:</span> <span class="s2">&quot;all&quot;</span><span class="p">,</span>
    <span class="p">})</span>
<span class="n">high_db_conn_count</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">InfraAlertCondition</span><span class="p">(</span><span class="s2">&quot;highDbConnCount&quot;</span><span class="p">,</span>
    <span class="n">policy_id</span><span class="o">=</span><span class="n">foo</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;infra_metric&quot;</span><span class="p">,</span>
    <span class="n">event</span><span class="o">=</span><span class="s2">&quot;DatastoreSample&quot;</span><span class="p">,</span>
    <span class="n">select</span><span class="o">=</span><span class="s2">&quot;provider.databaseConnections.Average&quot;</span><span class="p">,</span>
    <span class="n">comparison</span><span class="o">=</span><span class="s2">&quot;above&quot;</span><span class="p">,</span>
    <span class="n">where</span><span class="o">=</span><span class="s2">&quot;(`hostname` LIKE &#39;</span><span class="si">%d</span><span class="s2">b%&#39;)&quot;</span><span class="p">,</span>
    <span class="n">integration_provider</span><span class="o">=</span><span class="s2">&quot;RdsDbInstance&quot;</span><span class="p">,</span>
    <span class="n">critical</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;duration&quot;</span><span class="p">:</span> <span class="mi">25</span><span class="p">,</span>
        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="mi">90</span><span class="p">,</span>
        <span class="s2">&quot;timeFunction&quot;</span><span class="p">:</span> <span class="s2">&quot;all&quot;</span><span class="p">,</span>
    <span class="p">})</span>
<span class="n">process_not_running</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">InfraAlertCondition</span><span class="p">(</span><span class="s2">&quot;processNotRunning&quot;</span><span class="p">,</span>
    <span class="n">policy_id</span><span class="o">=</span><span class="n">foo</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;infra_process_running&quot;</span><span class="p">,</span>
    <span class="n">comparison</span><span class="o">=</span><span class="s2">&quot;equal&quot;</span><span class="p">,</span>
    <span class="n">process_where</span><span class="o">=</span><span class="s2">&quot;`commandName` = &#39;/usr/bin/ruby&#39;&quot;</span><span class="p">,</span>
    <span class="n">critical</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;duration&quot;</span><span class="p">:</span> <span class="mi">5</span><span class="p">,</span>
        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span>
    <span class="p">})</span>
<span class="n">host_not_reporting</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">InfraAlertCondition</span><span class="p">(</span><span class="s2">&quot;hostNotReporting&quot;</span><span class="p">,</span>
    <span class="n">policy_id</span><span class="o">=</span><span class="n">foo</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;infra_host_not_reporting&quot;</span><span class="p">,</span>
    <span class="n">where</span><span class="o">=</span><span class="s2">&quot;(`hostname` LIKE &#39;</span><span class="si">%f</span><span class="s2">rontend%&#39;)&quot;</span><span class="p">,</span>
    <span class="n">critical</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;duration&quot;</span><span class="p">:</span> <span class="mi">5</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<p>The <code class="docutils literal notranslate"><span class="pre">critical</span></code> and <code class="docutils literal notranslate"><span class="pre">warning</span></code> threshold mapping supports the following arguments:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> - (Required) Identifies the number of minutes the threshold must be passed or met for the alert to trigger. Threshold durations must be between 1 and 60 minutes (inclusive).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> - (Optional) Threshold value, computed against the <code class="docutils literal notranslate"><span class="pre">comparison</span></code> operator. Supported by <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> and <code class="docutils literal notranslate"><span class="pre">infra_process_running</span></code> alert condition types.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">time_function</span></code> - (Optional) Indicates if the condition needs to be sustained or to just break the threshold once; <code class="docutils literal notranslate"><span class="pre">all</span></code> or <code class="docutils literal notranslate"><span class="pre">any</span></code>. Supported by the <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> alert condition type.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>comparison</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The operator used to evaluate the threshold value.  Valid values are <code class="docutils literal notranslate"><span class="pre">above</span></code>, <code class="docutils literal notranslate"><span class="pre">below</span></code>, and <code class="docutils literal notranslate"><span class="pre">equal</span></code>.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> and <code class="docutils literal notranslate"><span class="pre">infra_process_running</span></code> condition types.</p></li>
<li><p><strong>critical</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Identifies the threshold parameters for opening a critical alert violation. See Thresholds below for details.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Infrastructure alert condition.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the condition is turned on or off.  Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>event</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metric event; for example, <code class="docutils literal notranslate"><span class="pre">SystemSample</span></code> or <code class="docutils literal notranslate"><span class="pre">StorageSample</span></code>.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> condition type.</p></li>
<li><p><strong>integration_provider</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – For alerts on integrations, use this instead of <code class="docutils literal notranslate"><span class="pre">event</span></code>.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> condition type.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Infrastructure alert condition’s name.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the alert policy where this condition should be used.</p></li>
<li><p><strong>process_where</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Any filters applied to processes; for example: <code class="docutils literal notranslate"><span class="pre">commandName</span> <span class="pre">=</span> <span class="pre">'java'</span></code>.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_process_running</span></code> condition type.</p></li>
<li><p><strong>runbook_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Runbook URL to display in notifications.</p></li>
<li><p><strong>select</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The attribute name to identify the metric being targeted; for example, <code class="docutils literal notranslate"><span class="pre">cpuPercent</span></code>, <code class="docutils literal notranslate"><span class="pre">diskFreePercent</span></code>, or <code class="docutils literal notranslate"><span class="pre">memoryResidentSizeBytes</span></code>.  The underlying API will automatically populate this value for Infrastructure integrations (for example <code class="docutils literal notranslate"><span class="pre">diskFreePercent</span></code>), so make sure to explicitly include this value to avoid diff issues.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> condition type.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of Infrastructure alert condition.  Valid values are  <code class="docutils literal notranslate"><span class="pre">infra_process_running</span></code>, <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code>, and <code class="docutils literal notranslate"><span class="pre">infra_host_not_reporting</span></code>.</p></li>
<li><p><strong>violation_close_timer</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Determines how much time will pass before a violation is automatically closed. Setting the time limit to 0 prevents a violation from being force-closed.</p></li>
<li><p><strong>warning</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Identifies the threshold parameters for opening a warning alert violation. See Thresholds below for details.</p></li>
<li><p><strong>where</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If applicable, this identifies any Infrastructure host filters used; for example: <code class="docutils literal notranslate"><span class="pre">hostname</span> <span class="pre">LIKE</span> <span class="pre">'%cassandra%'</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>critical</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>warning</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_newrelic.InfraAlertCondition.comparison">
<code class="sig-name descname">comparison</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.comparison" title="Permalink to this definition">¶</a></dt>
<dd><p>The operator used to evaluate the threshold value.  Valid values are <code class="docutils literal notranslate"><span class="pre">above</span></code>, <code class="docutils literal notranslate"><span class="pre">below</span></code>, and <code class="docutils literal notranslate"><span class="pre">equal</span></code>.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> and <code class="docutils literal notranslate"><span class="pre">infra_process_running</span></code> condition types.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.InfraAlertCondition.created_at">
<code class="sig-name descname">created_at</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp the alert condition was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.InfraAlertCondition.critical">
<code class="sig-name descname">critical</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.critical" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifies the threshold parameters for opening a critical alert violation. See Thresholds below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.InfraAlertCondition.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Infrastructure alert condition.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.InfraAlertCondition.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the condition is turned on or off.  Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.InfraAlertCondition.event">
<code class="sig-name descname">event</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.event" title="Permalink to this definition">¶</a></dt>
<dd><p>The metric event; for example, <code class="docutils literal notranslate"><span class="pre">SystemSample</span></code> or <code class="docutils literal notranslate"><span class="pre">StorageSample</span></code>.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> condition type.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.InfraAlertCondition.integration_provider">
<code class="sig-name descname">integration_provider</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.integration_provider" title="Permalink to this definition">¶</a></dt>
<dd><p>For alerts on integrations, use this instead of <code class="docutils literal notranslate"><span class="pre">event</span></code>.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> condition type.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.InfraAlertCondition.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Infrastructure alert condition’s name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.InfraAlertCondition.policy_id">
<code class="sig-name descname">policy_id</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the alert policy where this condition should be used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.InfraAlertCondition.process_where">
<code class="sig-name descname">process_where</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.process_where" title="Permalink to this definition">¶</a></dt>
<dd><p>Any filters applied to processes; for example: <code class="docutils literal notranslate"><span class="pre">commandName</span> <span class="pre">=</span> <span class="pre">'java'</span></code>.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_process_running</span></code> condition type.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.InfraAlertCondition.runbook_url">
<code class="sig-name descname">runbook_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.runbook_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Runbook URL to display in notifications.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.InfraAlertCondition.select">
<code class="sig-name descname">select</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.select" title="Permalink to this definition">¶</a></dt>
<dd><p>The attribute name to identify the metric being targeted; for example, <code class="docutils literal notranslate"><span class="pre">cpuPercent</span></code>, <code class="docutils literal notranslate"><span class="pre">diskFreePercent</span></code>, or <code class="docutils literal notranslate"><span class="pre">memoryResidentSizeBytes</span></code>.  The underlying API will automatically populate this value for Infrastructure integrations (for example <code class="docutils literal notranslate"><span class="pre">diskFreePercent</span></code>), so make sure to explicitly include this value to avoid diff issues.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> condition type.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.InfraAlertCondition.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of Infrastructure alert condition.  Valid values are  <code class="docutils literal notranslate"><span class="pre">infra_process_running</span></code>, <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code>, and <code class="docutils literal notranslate"><span class="pre">infra_host_not_reporting</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.InfraAlertCondition.updated_at">
<code class="sig-name descname">updated_at</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp the alert condition was last updated.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.InfraAlertCondition.violation_close_timer">
<code class="sig-name descname">violation_close_timer</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.violation_close_timer" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines how much time will pass before a violation is automatically closed. Setting the time limit to 0 prevents a violation from being force-closed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.InfraAlertCondition.warning">
<code class="sig-name descname">warning</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.warning" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifies the threshold parameters for opening a warning alert violation. See Thresholds below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.InfraAlertCondition.where">
<code class="sig-name descname">where</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.where" title="Permalink to this definition">¶</a></dt>
<dd><p>If applicable, this identifies any Infrastructure host filters used; for example: <code class="docutils literal notranslate"><span class="pre">hostname</span> <span class="pre">LIKE</span> <span class="pre">'%cassandra%'</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.InfraAlertCondition.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comparison</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">critical</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_provider</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">process_where</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">runbook_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">select</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">violation_close_timer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">warning</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">where</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.InfraAlertCondition.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing InfraAlertCondition resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>comparison</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The operator used to evaluate the threshold value.  Valid values are <code class="docutils literal notranslate"><span class="pre">above</span></code>, <code class="docutils literal notranslate"><span class="pre">below</span></code>, and <code class="docutils literal notranslate"><span class="pre">equal</span></code>.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> and <code class="docutils literal notranslate"><span class="pre">infra_process_running</span></code> condition types.</p></li>
<li><p><strong>created_at</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The timestamp the alert condition was created.</p></li>
<li><p><strong>critical</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Identifies the threshold parameters for opening a critical alert violation. See Thresholds below for details.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Infrastructure alert condition.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the condition is turned on or off.  Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>event</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metric event; for example, <code class="docutils literal notranslate"><span class="pre">SystemSample</span></code> or <code class="docutils literal notranslate"><span class="pre">StorageSample</span></code>.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> condition type.</p></li>
<li><p><strong>integration_provider</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – For alerts on integrations, use this instead of <code class="docutils literal notranslate"><span class="pre">event</span></code>.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> condition type.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Infrastructure alert condition’s name.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the alert policy where this condition should be used.</p></li>
<li><p><strong>process_where</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Any filters applied to processes; for example: <code class="docutils literal notranslate"><span class="pre">commandName</span> <span class="pre">=</span> <span class="pre">'java'</span></code>.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_process_running</span></code> condition type.</p></li>
<li><p><strong>runbook_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Runbook URL to display in notifications.</p></li>
<li><p><strong>select</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The attribute name to identify the metric being targeted; for example, <code class="docutils literal notranslate"><span class="pre">cpuPercent</span></code>, <code class="docutils literal notranslate"><span class="pre">diskFreePercent</span></code>, or <code class="docutils literal notranslate"><span class="pre">memoryResidentSizeBytes</span></code>.  The underlying API will automatically populate this value for Infrastructure integrations (for example <code class="docutils literal notranslate"><span class="pre">diskFreePercent</span></code>), so make sure to explicitly include this value to avoid diff issues.  Supported by the <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code> condition type.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of Infrastructure alert condition.  Valid values are  <code class="docutils literal notranslate"><span class="pre">infra_process_running</span></code>, <code class="docutils literal notranslate"><span class="pre">infra_metric</span></code>, and <code class="docutils literal notranslate"><span class="pre">infra_host_not_reporting</span></code>.</p></li>
<li><p><strong>updated_at</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The timestamp the alert condition was last updated.</p></li>
<li><p><strong>violation_close_timer</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Determines how much time will pass before a violation is automatically closed. Setting the time limit to 0 prevents a violation from being force-closed.</p></li>
<li><p><strong>warning</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Identifies the threshold parameters for opening a warning alert violation. See Thresholds below for details.</p></li>
<li><p><strong>where</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If applicable, this identifies any Infrastructure host filters used; for example: <code class="docutils literal notranslate"><span class="pre">hostname</span> <span class="pre">LIKE</span> <span class="pre">'%cassandra%'</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>critical</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>warning</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">NrqlAlertCondition</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">baseline_direction</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">critical</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expected_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_overlap</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nrql</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">open_violation_on_group_overlap</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">runbook_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">terms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value_function</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">violation_time_limit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">violation_time_limit_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">warning</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to create and manage NRQL alert conditions in New Relic.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">nrql</span></code> block supports the following arguments:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> - (Required) The NRQL query to execute for the condition.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluation_offset</span></code> - (Optional) Represented in minutes and must be within 1-20 minutes (inclusive). NRQL queries are evaluated in one-minute time windows. The start time depends on this value. It’s recommended to set this to 3 minutes. An offset of less than 3 minutes will trigger violations sooner, but you may see more false positives and negatives due to data latency. With <code class="docutils literal notranslate"><span class="pre">evaluation_offset</span></code> set to 3 minutes, the NRQL time window applied to your query will be: <code class="docutils literal notranslate"><span class="pre">SINCE</span> <span class="pre">3</span> <span class="pre">minutes</span> <span class="pre">ago</span> <span class="pre">UNTIL</span> <span class="pre">2</span> <span class="pre">minutes</span> <span class="pre">ago</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">since_value</span></code> - (Optional)  <strong>DEPRECATED:</strong> Use <code class="docutils literal notranslate"><span class="pre">evaluation_offset</span></code> instead. The value to be used in the <code class="docutils literal notranslate"><span class="pre">SINCE</span> <span class="pre">&lt;X&gt;</span> <span class="pre">minutes</span> <span class="pre">ago</span></code> clause for the NRQL query. Must be between 1-20 (inclusive).</p></li>
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
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The New Relic account ID of the account you wish to create the condition. Defaults to the account ID set in your environment variable <code class="docutils literal notranslate"><span class="pre">NEW_RELIC_ACCOUNT_ID</span></code>.</p></li>
<li><p><strong>baseline_direction</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The baseline direction of a <em>baseline</em> NRQL alert condition. Valid values are: <code class="docutils literal notranslate"><span class="pre">lower_only</span></code>, <code class="docutils literal notranslate"><span class="pre">upper_and_lower</span></code>, <code class="docutils literal notranslate"><span class="pre">upper_only</span></code> (case insensitive).</p></li>
<li><p><strong>critical</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list containing the <code class="docutils literal notranslate"><span class="pre">critical</span></code> threshold values. See Terms below for details.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the NRQL alert condition.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable the alert condition. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>expected_groups</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of expected groups when using <code class="docutils literal notranslate"><span class="pre">outlier</span></code> detection.</p></li>
<li><p><strong>ignore_overlap</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <strong>DEPRECATED:</strong> Use <code class="docutils literal notranslate"><span class="pre">open_violation_on_group_overlap</span></code> instead, but use the inverse value of your boolean - e.g. if <code class="docutils literal notranslate"><span class="pre">ignore_overlap</span> <span class="pre">=</span> <span class="pre">false</span></code>, use <code class="docutils literal notranslate"><span class="pre">open_violation_on_group_overlap</span> <span class="pre">=</span> <span class="pre">true</span></code>. This argument sets whether to trigger a violation when groups overlap. If set to <code class="docutils literal notranslate"><span class="pre">true</span></code> overlapping groups will not trigger a violation. This argument is only applicable in <code class="docutils literal notranslate"><span class="pre">outlier</span></code> conditions.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of the condition.</p></li>
<li><p><strong>nrql</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A NRQL query. See NRQL below for details.</p></li>
<li><p><strong>open_violation_on_group_overlap</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to trigger a violation when groups overlap. Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want to trigger a violation when groups overlap. This argument is only applicable in <code class="docutils literal notranslate"><span class="pre">outlier</span></code> conditions.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the policy where this condition should be used.</p></li>
<li><p><strong>runbook_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Runbook URL to display in notifications.</p></li>
<li><p><strong>terms</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <strong>DEPRECATED</strong> Use <code class="docutils literal notranslate"><span class="pre">critical</span></code>, and <code class="docutils literal notranslate"><span class="pre">warning</span></code> instead.  A list of terms for this condition. See Terms below for details.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the condition. Valid values are <code class="docutils literal notranslate"><span class="pre">static</span></code>, <code class="docutils literal notranslate"><span class="pre">baseline</span></code>, or <code class="docutils literal notranslate"><span class="pre">outlier</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">static</span></code>.</p></li>
<li><p><strong>value_function</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Possible values are <code class="docutils literal notranslate"><span class="pre">single_value</span></code>, <code class="docutils literal notranslate"><span class="pre">sum</span></code> (case insensitive). Defaults to <code class="docutils literal notranslate"><span class="pre">single_value</span></code>.</p></li>
<li><p><strong>violation_time_limit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are <code class="docutils literal notranslate"><span class="pre">ONE_HOUR</span></code>, <code class="docutils literal notranslate"><span class="pre">TWO_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">FOUR_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">EIGHT_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">TWELVE_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">TWENTY_FOUR_HOURS</span></code> (case insensitive).</p></li>
<li><p><strong>violation_time_limit_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <strong>DEPRECATED:</strong> Use <code class="docutils literal notranslate"><span class="pre">violation_time_limit</span></code> instead. Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are <code class="docutils literal notranslate"><span class="pre">3600</span></code>, <code class="docutils literal notranslate"><span class="pre">7200</span></code>, <code class="docutils literal notranslate"><span class="pre">14400</span></code>, <code class="docutils literal notranslate"><span class="pre">28800</span></code>, <code class="docutils literal notranslate"><span class="pre">43200</span></code>, and <code class="docutils literal notranslate"><span class="pre">86400</span></code>.</p></li>
<li><p><strong>warning</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list containing the <code class="docutils literal notranslate"><span class="pre">warning</span></code> threshold values. See Terms below for details.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>critical</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdOccurrences</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>nrql</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationOffset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sinceValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>terms</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdOccurrences</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>warning</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdOccurrences</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_newrelic.NrqlAlertCondition.account_id">
<code class="sig-name descname">account_id</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The New Relic account ID of the account you wish to create the condition. Defaults to the account ID set in your environment variable <code class="docutils literal notranslate"><span class="pre">NEW_RELIC_ACCOUNT_ID</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.NrqlAlertCondition.baseline_direction">
<code class="sig-name descname">baseline_direction</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.baseline_direction" title="Permalink to this definition">¶</a></dt>
<dd><p>The baseline direction of a <em>baseline</em> NRQL alert condition. Valid values are: <code class="docutils literal notranslate"><span class="pre">lower_only</span></code>, <code class="docutils literal notranslate"><span class="pre">upper_and_lower</span></code>, <code class="docutils literal notranslate"><span class="pre">upper_only</span></code> (case insensitive).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.NrqlAlertCondition.critical">
<code class="sig-name descname">critical</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.critical" title="Permalink to this definition">¶</a></dt>
<dd><p>A list containing the <code class="docutils literal notranslate"><span class="pre">critical</span></code> threshold values. See Terms below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdOccurrences</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.NrqlAlertCondition.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the NRQL alert condition.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.NrqlAlertCondition.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable the alert condition. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.NrqlAlertCondition.expected_groups">
<code class="sig-name descname">expected_groups</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.expected_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of expected groups when using <code class="docutils literal notranslate"><span class="pre">outlier</span></code> detection.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.NrqlAlertCondition.ignore_overlap">
<code class="sig-name descname">ignore_overlap</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.ignore_overlap" title="Permalink to this definition">¶</a></dt>
<dd><p><strong>DEPRECATED:</strong> Use <code class="docutils literal notranslate"><span class="pre">open_violation_on_group_overlap</span></code> instead, but use the inverse value of your boolean - e.g. if <code class="docutils literal notranslate"><span class="pre">ignore_overlap</span> <span class="pre">=</span> <span class="pre">false</span></code>, use <code class="docutils literal notranslate"><span class="pre">open_violation_on_group_overlap</span> <span class="pre">=</span> <span class="pre">true</span></code>. This argument sets whether to trigger a violation when groups overlap. If set to <code class="docutils literal notranslate"><span class="pre">true</span></code> overlapping groups will not trigger a violation. This argument is only applicable in <code class="docutils literal notranslate"><span class="pre">outlier</span></code> conditions.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.NrqlAlertCondition.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The title of the condition.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.NrqlAlertCondition.nrql">
<code class="sig-name descname">nrql</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.nrql" title="Permalink to this definition">¶</a></dt>
<dd><p>A NRQL query. See NRQL below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationOffset</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sinceValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.NrqlAlertCondition.open_violation_on_group_overlap">
<code class="sig-name descname">open_violation_on_group_overlap</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.open_violation_on_group_overlap" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not to trigger a violation when groups overlap. Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want to trigger a violation when groups overlap. This argument is only applicable in <code class="docutils literal notranslate"><span class="pre">outlier</span></code> conditions.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.NrqlAlertCondition.policy_id">
<code class="sig-name descname">policy_id</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the policy where this condition should be used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.NrqlAlertCondition.runbook_url">
<code class="sig-name descname">runbook_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.runbook_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Runbook URL to display in notifications.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.NrqlAlertCondition.terms">
<code class="sig-name descname">terms</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.terms" title="Permalink to this definition">¶</a></dt>
<dd><p><strong>DEPRECATED</strong> Use <code class="docutils literal notranslate"><span class="pre">critical</span></code>, and <code class="docutils literal notranslate"><span class="pre">warning</span></code> instead.  A list of terms for this condition. See Terms below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdOccurrences</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.NrqlAlertCondition.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the condition. Valid values are <code class="docutils literal notranslate"><span class="pre">static</span></code>, <code class="docutils literal notranslate"><span class="pre">baseline</span></code>, or <code class="docutils literal notranslate"><span class="pre">outlier</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">static</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.NrqlAlertCondition.value_function">
<code class="sig-name descname">value_function</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.value_function" title="Permalink to this definition">¶</a></dt>
<dd><p>Possible values are <code class="docutils literal notranslate"><span class="pre">single_value</span></code>, <code class="docutils literal notranslate"><span class="pre">sum</span></code> (case insensitive). Defaults to <code class="docutils literal notranslate"><span class="pre">single_value</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.NrqlAlertCondition.violation_time_limit">
<code class="sig-name descname">violation_time_limit</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.violation_time_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are <code class="docutils literal notranslate"><span class="pre">ONE_HOUR</span></code>, <code class="docutils literal notranslate"><span class="pre">TWO_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">FOUR_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">EIGHT_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">TWELVE_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">TWENTY_FOUR_HOURS</span></code> (case insensitive).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.NrqlAlertCondition.violation_time_limit_seconds">
<code class="sig-name descname">violation_time_limit_seconds</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.violation_time_limit_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p><strong>DEPRECATED:</strong> Use <code class="docutils literal notranslate"><span class="pre">violation_time_limit</span></code> instead. Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are <code class="docutils literal notranslate"><span class="pre">3600</span></code>, <code class="docutils literal notranslate"><span class="pre">7200</span></code>, <code class="docutils literal notranslate"><span class="pre">14400</span></code>, <code class="docutils literal notranslate"><span class="pre">28800</span></code>, <code class="docutils literal notranslate"><span class="pre">43200</span></code>, and <code class="docutils literal notranslate"><span class="pre">86400</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.NrqlAlertCondition.warning">
<code class="sig-name descname">warning</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.warning" title="Permalink to this definition">¶</a></dt>
<dd><p>A list containing the <code class="docutils literal notranslate"><span class="pre">warning</span></code> threshold values. See Terms below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdOccurrences</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.NrqlAlertCondition.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">baseline_direction</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">critical</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expected_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_overlap</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nrql</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">open_violation_on_group_overlap</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">runbook_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">terms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value_function</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">violation_time_limit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">violation_time_limit_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">warning</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.NrqlAlertCondition.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NrqlAlertCondition resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The New Relic account ID of the account you wish to create the condition. Defaults to the account ID set in your environment variable <code class="docutils literal notranslate"><span class="pre">NEW_RELIC_ACCOUNT_ID</span></code>.</p></li>
<li><p><strong>baseline_direction</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The baseline direction of a <em>baseline</em> NRQL alert condition. Valid values are: <code class="docutils literal notranslate"><span class="pre">lower_only</span></code>, <code class="docutils literal notranslate"><span class="pre">upper_and_lower</span></code>, <code class="docutils literal notranslate"><span class="pre">upper_only</span></code> (case insensitive).</p></li>
<li><p><strong>critical</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list containing the <code class="docutils literal notranslate"><span class="pre">critical</span></code> threshold values. See Terms below for details.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the NRQL alert condition.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable the alert condition. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>expected_groups</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of expected groups when using <code class="docutils literal notranslate"><span class="pre">outlier</span></code> detection.</p></li>
<li><p><strong>ignore_overlap</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <strong>DEPRECATED:</strong> Use <code class="docutils literal notranslate"><span class="pre">open_violation_on_group_overlap</span></code> instead, but use the inverse value of your boolean - e.g. if <code class="docutils literal notranslate"><span class="pre">ignore_overlap</span> <span class="pre">=</span> <span class="pre">false</span></code>, use <code class="docutils literal notranslate"><span class="pre">open_violation_on_group_overlap</span> <span class="pre">=</span> <span class="pre">true</span></code>. This argument sets whether to trigger a violation when groups overlap. If set to <code class="docutils literal notranslate"><span class="pre">true</span></code> overlapping groups will not trigger a violation. This argument is only applicable in <code class="docutils literal notranslate"><span class="pre">outlier</span></code> conditions.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of the condition.</p></li>
<li><p><strong>nrql</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A NRQL query. See NRQL below for details.</p></li>
<li><p><strong>open_violation_on_group_overlap</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to trigger a violation when groups overlap. Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want to trigger a violation when groups overlap. This argument is only applicable in <code class="docutils literal notranslate"><span class="pre">outlier</span></code> conditions.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the policy where this condition should be used.</p></li>
<li><p><strong>runbook_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Runbook URL to display in notifications.</p></li>
<li><p><strong>terms</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <strong>DEPRECATED</strong> Use <code class="docutils literal notranslate"><span class="pre">critical</span></code>, and <code class="docutils literal notranslate"><span class="pre">warning</span></code> instead.  A list of terms for this condition. See Terms below for details.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the condition. Valid values are <code class="docutils literal notranslate"><span class="pre">static</span></code>, <code class="docutils literal notranslate"><span class="pre">baseline</span></code>, or <code class="docutils literal notranslate"><span class="pre">outlier</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">static</span></code>.</p></li>
<li><p><strong>value_function</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Possible values are <code class="docutils literal notranslate"><span class="pre">single_value</span></code>, <code class="docutils literal notranslate"><span class="pre">sum</span></code> (case insensitive). Defaults to <code class="docutils literal notranslate"><span class="pre">single_value</span></code>.</p></li>
<li><p><strong>violation_time_limit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are <code class="docutils literal notranslate"><span class="pre">ONE_HOUR</span></code>, <code class="docutils literal notranslate"><span class="pre">TWO_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">FOUR_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">EIGHT_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">TWELVE_HOURS</span></code>, <code class="docutils literal notranslate"><span class="pre">TWENTY_FOUR_HOURS</span></code> (case insensitive).</p></li>
<li><p><strong>violation_time_limit_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <strong>DEPRECATED:</strong> Use <code class="docutils literal notranslate"><span class="pre">violation_time_limit</span></code> instead. Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are <code class="docutils literal notranslate"><span class="pre">3600</span></code>, <code class="docutils literal notranslate"><span class="pre">7200</span></code>, <code class="docutils literal notranslate"><span class="pre">14400</span></code>, <code class="docutils literal notranslate"><span class="pre">28800</span></code>, <code class="docutils literal notranslate"><span class="pre">43200</span></code>, and <code class="docutils literal notranslate"><span class="pre">86400</span></code>.</p></li>
<li><p><strong>warning</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list containing the <code class="docutils literal notranslate"><span class="pre">warning</span></code> threshold values. See Terms below for details.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>critical</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdOccurrences</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>nrql</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationOffset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sinceValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>terms</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdOccurrences</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>warning</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdOccurrences</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
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
<dt id="pulumi_newrelic.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_api_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cacert_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">infrastructure_api_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">insecure_skip_verify</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">insights_insert_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">insights_insert_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">insights_query_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nerdgraph_api_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">synthetics_api_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.Provider" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">get_account</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.get_account" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>account_id</strong> (<em>float</em>) – The account ID in New Relic.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The account name in New Relic.</p></li>
<li><p><strong>scope</strong> (<em>str</em>) – The scope of the account in New Relic.  Valid values are “global” and “in_region”.  Defaults to “in_region”.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_newrelic.get_alert_channel">
<code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">get_alert_channel</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.get_alert_channel" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a specific alert channel in New Relic that already exists.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foo_alert_channel</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">get_alert_channel</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;foo@example.com&quot;</span><span class="p">)</span>
<span class="c1"># Resource</span>
<span class="n">foo_alert_policy</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertPolicy</span><span class="p">(</span><span class="s2">&quot;fooAlertPolicy&quot;</span><span class="p">)</span>
<span class="c1"># Using the data source and resource together</span>
<span class="n">foo_alert_policy_channel</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertPolicyChannel</span><span class="p">(</span><span class="s2">&quot;fooAlertPolicyChannel&quot;</span><span class="p">,</span>
    <span class="n">policy_id</span><span class="o">=</span><span class="n">foo_alert_policy</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">channel_id</span><span class="o">=</span><span class="n">foo_alert_channel</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the alert channel in New Relic.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_newrelic.get_alert_policy">
<code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">get_alert_policy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">incident_preference</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.get_alert_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a specific alert policy in New Relic that already exists.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foo_alert_channel</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">get_alert_channel</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;foo@example.com&quot;</span><span class="p">)</span>
<span class="n">foo_alert_policy</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">get_alert_policy</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;foo policy&quot;</span><span class="p">)</span>
<span class="n">foo_alert_policy_channel</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertPolicyChannel</span><span class="p">(</span><span class="s2">&quot;fooAlertPolicyChannel&quot;</span><span class="p">,</span>
    <span class="n">policy_id</span><span class="o">=</span><span class="n">foo_alert_policy</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">channel_id</span><span class="o">=</span><span class="n">foo_alert_channel</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
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
<code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">get_application</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.get_application" title="Permalink to this definition">¶</a></dt>
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
    <span class="n">terms</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;duration&quot;</span><span class="p">:</span> <span class="mi">5</span><span class="p">,</span>
        <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;below&quot;</span><span class="p">,</span>
        <span class="s2">&quot;priority&quot;</span><span class="p">:</span> <span class="s2">&quot;critical&quot;</span><span class="p">,</span>
        <span class="s2">&quot;threshold&quot;</span><span class="p">:</span> <span class="s2">&quot;0.75&quot;</span><span class="p">,</span>
        <span class="s2">&quot;timeFunction&quot;</span><span class="p">:</span> <span class="s2">&quot;all&quot;</span><span class="p">,</span>
    <span class="p">}])</span>
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
<code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">get_entity</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.get_entity" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a specific entity in New Relic One that already exists.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">app</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">get_entity</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;my-app&quot;</span><span class="p">,</span>
    <span class="n">domain</span><span class="o">=</span><span class="s2">&quot;APM&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;APPLICATION&quot;</span><span class="p">,</span>
    <span class="n">tag</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;my-tag&quot;</span><span class="p">,</span>
        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;my-tag-value&quot;</span><span class="p">,</span>
    <span class="p">})</span>
<span class="n">foo_alert_policy</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertPolicy</span><span class="p">(</span><span class="s2">&quot;fooAlertPolicy&quot;</span><span class="p">)</span>
<span class="n">foo_alert_condition</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertCondition</span><span class="p">(</span><span class="s2">&quot;fooAlertCondition&quot;</span><span class="p">,</span>
    <span class="n">policy_id</span><span class="o">=</span><span class="n">foo_alert_policy</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;apm_app_metric&quot;</span><span class="p">,</span>
    <span class="n">entities</span><span class="o">=</span><span class="p">[</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;newrelic_application&quot;</span><span class="p">][</span><span class="s2">&quot;app&quot;</span><span class="p">][</span><span class="s2">&quot;application_id&quot;</span><span class="p">]],</span>
    <span class="n">metric</span><span class="o">=</span><span class="s2">&quot;apdex&quot;</span><span class="p">,</span>
    <span class="n">runbook_url</span><span class="o">=</span><span class="s2">&quot;https://www.example.com&quot;</span><span class="p">,</span>
    <span class="n">terms</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;duration&quot;</span><span class="p">:</span> <span class="mi">5</span><span class="p">,</span>
        <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;below&quot;</span><span class="p">,</span>
        <span class="s2">&quot;priority&quot;</span><span class="p">:</span> <span class="s2">&quot;critical&quot;</span><span class="p">,</span>
        <span class="s2">&quot;threshold&quot;</span><span class="p">:</span> <span class="s2">&quot;0.75&quot;</span><span class="p">,</span>
        <span class="s2">&quot;timeFunction&quot;</span><span class="p">:</span> <span class="s2">&quot;all&quot;</span><span class="p">,</span>
    <span class="p">}])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>domain</strong> (<em>str</em>) – The entity’s domain. Valid values are APM, BROWSER, INFRA, MOBILE, and SYNTH.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the entity in New Relic One.  The first entity matching this name for the given search parameters will be returned.</p></li>
<li><p><strong>type</strong> (<em>str</em>) – The entity’s type. Valid values are APPLICATION, DASHBOARD, HOST, MONITOR, and WORRKLOAD.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>tag</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_newrelic.get_key_transaction">
<code class="sig-prename descclassname">pulumi_newrelic.</code><code class="sig-name descname">get_key_transaction</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.get_key_transaction" title="Permalink to this definition">¶</a></dt>
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
    <span class="n">terms</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;duration&quot;</span><span class="p">:</span> <span class="mi">5</span><span class="p">,</span>
        <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;below&quot;</span><span class="p">,</span>
        <span class="s2">&quot;priority&quot;</span><span class="p">:</span> <span class="s2">&quot;critical&quot;</span><span class="p">,</span>
        <span class="s2">&quot;threshold&quot;</span><span class="p">:</span> <span class="s2">&quot;0.75&quot;</span><span class="p">,</span>
        <span class="s2">&quot;timeFunction&quot;</span><span class="p">:</span> <span class="s2">&quot;all&quot;</span><span class="p">,</span>
    <span class="p">}])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the key transaction in New Relic.</p>
</dd>
</dl>
</dd></dl>

</div>
