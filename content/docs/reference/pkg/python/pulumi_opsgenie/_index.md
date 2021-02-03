---
title: Package pulumi_opsgenie
title_tag: Package pulumi_opsgenie | Python SDK
linktitle: pulumi_opsgenie
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "opsgenie" >}}

<div class="section" id="pulumi-opsgenie">
<h1>Pulumi OpsGenie<a class="headerlink" href="#pulumi-opsgenie" title="Permalink to this headline"></a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-opsgenie">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-opsgenie/issues">pulumi/pulumi-opsgenie repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-opsgenie/issues">terraform-providers/terraform-provider-opsgenie repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_opsgenie"></span><dl class="py class">
<dt id="pulumi_opsgenie.AlertPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">AlertPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">actions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alias</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">continue_policy</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entity</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>AlertPolicyFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>AlertPolicyFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>AlertPolicyFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>AlertPolicyFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_original_actions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_original_details</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_original_responders</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_original_tags</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">responders</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>AlertPolicyResponderArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>AlertPolicyResponderArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>AlertPolicyResponderArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>AlertPolicyResponderArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_restrictions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>AlertPolicyTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>AlertPolicyTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>AlertPolicyTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>AlertPolicyTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.AlertPolicy" title="Permalink to this definition"></a></dt>
<dd><p>Manages a Alert Policy within Opsgenie.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_opsgenie</span> <span class="k">as</span> <span class="nn">opsgenie</span>

<span class="n">test_team</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">Team</span><span class="p">(</span><span class="s2">&quot;testTeam&quot;</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">&quot;This team deals with all the things&quot;</span><span class="p">)</span>
<span class="n">test_alert_policy</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">AlertPolicy</span><span class="p">(</span><span class="s2">&quot;testAlertPolicy&quot;</span><span class="p">,</span>
    <span class="n">team_id</span><span class="o">=</span><span class="n">test_team</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">policy_description</span><span class="o">=</span><span class="s2">&quot;This is sample policy&quot;</span><span class="p">,</span>
    <span class="n">message</span><span class="o">=</span><span class="s2">&quot;{{message}}&quot;</span><span class="p">,</span>
    <span class="n">filters</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">AlertPolicyFilterArgs</span><span class="p">()],</span>
    <span class="n">time_restrictions</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">AlertPolicyTimeRestrictionArgs</span><span class="p">(</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;weekday-and-time-of-day&quot;</span><span class="p">,</span>
        <span class="n">restrictions</span><span class="o">=</span><span class="p">[</span>
            <span class="n">opsgenie</span><span class="o">.</span><span class="n">AlertPolicyTimeRestrictionRestrictionArgs</span><span class="p">(</span>
                <span class="n">end_day</span><span class="o">=</span><span class="s2">&quot;monday&quot;</span><span class="p">,</span>
                <span class="n">end_hour</span><span class="o">=</span><span class="mi">7</span><span class="p">,</span>
                <span class="n">end_min</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
                <span class="n">start_day</span><span class="o">=</span><span class="s2">&quot;sunday&quot;</span><span class="p">,</span>
                <span class="n">start_hour</span><span class="o">=</span><span class="mi">21</span><span class="p">,</span>
                <span class="n">start_min</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">opsgenie</span><span class="o">.</span><span class="n">AlertPolicyTimeRestrictionRestrictionArgs</span><span class="p">(</span>
                <span class="n">end_day</span><span class="o">=</span><span class="s2">&quot;tuesday&quot;</span><span class="p">,</span>
                <span class="n">end_hour</span><span class="o">=</span><span class="mi">7</span><span class="p">,</span>
                <span class="n">end_min</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
                <span class="n">start_day</span><span class="o">=</span><span class="s2">&quot;monday&quot;</span><span class="p">,</span>
                <span class="n">start_hour</span><span class="o">=</span><span class="mi">22</span><span class="p">,</span>
                <span class="n">start_min</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">],</span>
    <span class="p">)])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Actions to add to the alerts original actions value as a list of strings. If ignore_original_actions field is set to true, this will replace the original actions.</p></li>
<li><p><strong>alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alias of the alert. You can use {{alias}} to refer to the original alias. Default value is {{alias}}</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If policy should be enabled. Default: true</p></li>
<li><p><strong>entity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Entity field of the alert. You can use {{entity}} to refer to the original entity. Default value is {{entity}}</p></li>
<li><p><strong>filters</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AlertPolicyFilterArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A alert filter which will be applied. This filter can be empty: filter {} - this means ‘match-all’. This is a block, structure is documented below.</p></li>
<li><p><strong>ignore_original_actions</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to true, policy will ignore the original actions of the alert. Default value is false</p></li>
<li><p><strong>ignore_original_details</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to true, policy will ignore the original details of the alert. Default value is false</p></li>
<li><p><strong>ignore_original_responders</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to true, policy will ignore the original responders of the alert. Default value is false</p></li>
<li><p><strong>ignore_original_tags</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to true, policy will ignore the original tags of the alert. Default value is false</p></li>
<li><p><strong>message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Message of the alerts</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the responder</p></li>
<li><p><strong>policy_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the policy. This can be max 512 characters.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Priority of the alert. Should be one of P1, P2, P3, P4, or P5</p></li>
<li><p><strong>responders</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AlertPolicyResponderArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Responders to add to the alerts original responders value as a list of teams, users or the reserved word none or all. If ignoreOriginalResponders field is set to true, this will replace the original responders. The possible values for responders are: user, team. This is a block, structure is documented below.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Source field of the alert. You can use {{source}} to refer to the original source. Default value is {{source}}</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Tags to add to the alerts original tags value as a list of strings. If ignoreOriginalResponders field is set to true, this will replace the original responders.</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of team that this policy belongs to.</p></li>
<li><p><strong>time_restrictions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AlertPolicyTimeRestrictionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Time restrictions specified in this field must be met for this policy to work. This is a block, structure is documented below.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_opsgenie.AlertPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">actions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alias</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">continue_policy</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entity</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>AlertPolicyFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>AlertPolicyFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>AlertPolicyFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>AlertPolicyFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_original_actions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_original_details</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_original_responders</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_original_tags</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">responders</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>AlertPolicyResponderArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>AlertPolicyResponderArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>AlertPolicyResponderArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>AlertPolicyResponderArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_restrictions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>AlertPolicyTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>AlertPolicyTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>AlertPolicyTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>AlertPolicyTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_opsgenie.AlertPolicy" title="pulumi_opsgenie.AlertPolicy">AlertPolicy</a><a class="headerlink" href="#pulumi_opsgenie.AlertPolicy.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing AlertPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Actions to add to the alerts original actions value as a list of strings. If ignore_original_actions field is set to true, this will replace the original actions.</p></li>
<li><p><strong>alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alias of the alert. You can use {{alias}} to refer to the original alias. Default value is {{alias}}</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If policy should be enabled. Default: true</p></li>
<li><p><strong>entity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Entity field of the alert. You can use {{entity}} to refer to the original entity. Default value is {{entity}}</p></li>
<li><p><strong>filters</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AlertPolicyFilterArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A alert filter which will be applied. This filter can be empty: filter {} - this means ‘match-all’. This is a block, structure is documented below.</p></li>
<li><p><strong>ignore_original_actions</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to true, policy will ignore the original actions of the alert. Default value is false</p></li>
<li><p><strong>ignore_original_details</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to true, policy will ignore the original details of the alert. Default value is false</p></li>
<li><p><strong>ignore_original_responders</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to true, policy will ignore the original responders of the alert. Default value is false</p></li>
<li><p><strong>ignore_original_tags</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to true, policy will ignore the original tags of the alert. Default value is false</p></li>
<li><p><strong>message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Message of the alerts</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the responder</p></li>
<li><p><strong>policy_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the policy. This can be max 512 characters.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Priority of the alert. Should be one of P1, P2, P3, P4, or P5</p></li>
<li><p><strong>responders</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AlertPolicyResponderArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Responders to add to the alerts original responders value as a list of teams, users or the reserved word none or all. If ignoreOriginalResponders field is set to true, this will replace the original responders. The possible values for responders are: user, team. This is a block, structure is documented below.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Source field of the alert. You can use {{source}} to refer to the original source. Default value is {{source}}</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Tags to add to the alerts original tags value as a list of strings. If ignoreOriginalResponders field is set to true, this will replace the original responders.</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of team that this policy belongs to.</p></li>
<li><p><strong>time_restrictions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AlertPolicyTimeRestrictionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Time restrictions specified in this field must be met for this policy to work. This is a block, structure is documented below.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.AlertPolicy.actions">
<em class="property">property </em><code class="sig-name descname">actions</code><a class="headerlink" href="#pulumi_opsgenie.AlertPolicy.actions" title="Permalink to this definition"></a></dt>
<dd><p>Actions to add to the alerts original actions value as a list of strings. If ignore_original_actions field is set to true, this will replace the original actions.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.AlertPolicy.alias">
<em class="property">property </em><code class="sig-name descname">alias</code><a class="headerlink" href="#pulumi_opsgenie.AlertPolicy.alias" title="Permalink to this definition"></a></dt>
<dd><p>Alias of the alert. You can use {{alias}} to refer to the original alias. Default value is {{alias}}</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.AlertPolicy.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_opsgenie.AlertPolicy.enabled" title="Permalink to this definition"></a></dt>
<dd><p>If policy should be enabled. Default: true</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.AlertPolicy.entity">
<em class="property">property </em><code class="sig-name descname">entity</code><a class="headerlink" href="#pulumi_opsgenie.AlertPolicy.entity" title="Permalink to this definition"></a></dt>
<dd><p>Entity field of the alert. You can use {{entity}} to refer to the original entity. Default value is {{entity}}</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.AlertPolicy.filters">
<em class="property">property </em><code class="sig-name descname">filters</code><a class="headerlink" href="#pulumi_opsgenie.AlertPolicy.filters" title="Permalink to this definition"></a></dt>
<dd><p>A alert filter which will be applied. This filter can be empty: filter {} - this means ‘match-all’. This is a block, structure is documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.AlertPolicy.ignore_original_actions">
<em class="property">property </em><code class="sig-name descname">ignore_original_actions</code><a class="headerlink" href="#pulumi_opsgenie.AlertPolicy.ignore_original_actions" title="Permalink to this definition"></a></dt>
<dd><p>If set to true, policy will ignore the original actions of the alert. Default value is false</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.AlertPolicy.ignore_original_details">
<em class="property">property </em><code class="sig-name descname">ignore_original_details</code><a class="headerlink" href="#pulumi_opsgenie.AlertPolicy.ignore_original_details" title="Permalink to this definition"></a></dt>
<dd><p>If set to true, policy will ignore the original details of the alert. Default value is false</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.AlertPolicy.ignore_original_responders">
<em class="property">property </em><code class="sig-name descname">ignore_original_responders</code><a class="headerlink" href="#pulumi_opsgenie.AlertPolicy.ignore_original_responders" title="Permalink to this definition"></a></dt>
<dd><p>If set to true, policy will ignore the original responders of the alert. Default value is false</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.AlertPolicy.ignore_original_tags">
<em class="property">property </em><code class="sig-name descname">ignore_original_tags</code><a class="headerlink" href="#pulumi_opsgenie.AlertPolicy.ignore_original_tags" title="Permalink to this definition"></a></dt>
<dd><p>If set to true, policy will ignore the original tags of the alert. Default value is false</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.AlertPolicy.message">
<em class="property">property </em><code class="sig-name descname">message</code><a class="headerlink" href="#pulumi_opsgenie.AlertPolicy.message" title="Permalink to this definition"></a></dt>
<dd><p>Message of the alerts</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.AlertPolicy.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_opsgenie.AlertPolicy.name" title="Permalink to this definition"></a></dt>
<dd><p>Name of the responder</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.AlertPolicy.policy_description">
<em class="property">property </em><code class="sig-name descname">policy_description</code><a class="headerlink" href="#pulumi_opsgenie.AlertPolicy.policy_description" title="Permalink to this definition"></a></dt>
<dd><p>Description of the policy. This can be max 512 characters.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.AlertPolicy.priority">
<em class="property">property </em><code class="sig-name descname">priority</code><a class="headerlink" href="#pulumi_opsgenie.AlertPolicy.priority" title="Permalink to this definition"></a></dt>
<dd><p>Priority of the alert. Should be one of P1, P2, P3, P4, or P5</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.AlertPolicy.responders">
<em class="property">property </em><code class="sig-name descname">responders</code><a class="headerlink" href="#pulumi_opsgenie.AlertPolicy.responders" title="Permalink to this definition"></a></dt>
<dd><p>Responders to add to the alerts original responders value as a list of teams, users or the reserved word none or all. If ignoreOriginalResponders field is set to true, this will replace the original responders. The possible values for responders are: user, team. This is a block, structure is documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.AlertPolicy.source">
<em class="property">property </em><code class="sig-name descname">source</code><a class="headerlink" href="#pulumi_opsgenie.AlertPolicy.source" title="Permalink to this definition"></a></dt>
<dd><p>Source field of the alert. You can use {{source}} to refer to the original source. Default value is {{source}}</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.AlertPolicy.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_opsgenie.AlertPolicy.tags" title="Permalink to this definition"></a></dt>
<dd><p>Tags to add to the alerts original tags value as a list of strings. If ignoreOriginalResponders field is set to true, this will replace the original responders.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.AlertPolicy.team_id">
<em class="property">property </em><code class="sig-name descname">team_id</code><a class="headerlink" href="#pulumi_opsgenie.AlertPolicy.team_id" title="Permalink to this definition"></a></dt>
<dd><p>Id of team that this policy belongs to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.AlertPolicy.time_restrictions">
<em class="property">property </em><code class="sig-name descname">time_restrictions</code><a class="headerlink" href="#pulumi_opsgenie.AlertPolicy.time_restrictions" title="Permalink to this definition"></a></dt>
<dd><p>Time restrictions specified in this field must be met for this policy to work. This is a block, structure is documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.AlertPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.AlertPolicy.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.AlertPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.AlertPolicy.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.ApiIntegration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">ApiIntegration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_write_access</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">headers</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_responders_from_payload</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">responders</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>ApiIntegrationResponderArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ApiIntegrationResponderArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>ApiIntegrationResponderArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ApiIntegrationResponderArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">suppress_notifications</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">webhook_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.ApiIntegration" title="Permalink to this definition"></a></dt>
<dd><p>Manages an API Integration within Opsgenie.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_opsgenie</span> <span class="k">as</span> <span class="nn">opsgenie</span>

<span class="n">example_api_integration_api_integration</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">ApiIntegration</span><span class="p">(</span><span class="s2">&quot;example-api-integrationApiIntegration&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;API&quot;</span><span class="p">,</span>
    <span class="n">responders</span><span class="o">=</span><span class="p">[</span>
        <span class="n">opsgenie</span><span class="o">.</span><span class="n">ApiIntegrationResponderArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;user&quot;</span><span class="p">,</span>
            <span class="nb">id</span><span class="o">=</span><span class="n">opsgenie_user</span><span class="p">[</span><span class="s2">&quot;user&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
        <span class="p">),</span>
        <span class="n">opsgenie</span><span class="o">.</span><span class="n">ApiIntegrationResponderArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;user&quot;</span><span class="p">,</span>
            <span class="nb">id</span><span class="o">=</span><span class="n">opsgenie_user</span><span class="p">[</span><span class="s2">&quot;fahri&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
        <span class="p">),</span>
    <span class="p">])</span>
<span class="n">example_api_integration_index_api_integration_api_integration</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">ApiIntegration</span><span class="p">(</span><span class="s2">&quot;example-api-integrationIndex/apiIntegrationApiIntegration&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;Prometheus&quot;</span><span class="p">,</span>
    <span class="n">responders</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">ApiIntegrationResponderArgs</span><span class="p">(</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;user&quot;</span><span class="p">,</span>
        <span class="nb">id</span><span class="o">=</span><span class="n">opsgenie_user</span><span class="p">[</span><span class="s2">&quot;user&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="p">)],</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">allow_write_access</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">ignore_responders_from_payload</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">suppress_notifications</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">owner_team_id</span><span class="o">=</span><span class="n">opsgenie_team</span><span class="p">[</span><span class="s2">&quot;team&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
<span class="n">test3</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">ApiIntegration</span><span class="p">(</span><span class="s2">&quot;test3&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;Webhook&quot;</span><span class="p">,</span>
    <span class="n">responders</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">ApiIntegrationResponderArgs</span><span class="p">(</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;user&quot;</span><span class="p">,</span>
        <span class="nb">id</span><span class="o">=</span><span class="n">opsgenie_user</span><span class="p">[</span><span class="s2">&quot;user&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="p">)],</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">allow_write_access</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">suppress_notifications</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">webhook_url</span><span class="o">=</span><span class="s2">&quot;https://api.example.com/v1&quot;</span><span class="p">,</span>
    <span class="n">headers</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;header1&quot;</span><span class="p">:</span> <span class="n">value1</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<p>API Integrations can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import opsgenie:index/apiIntegration:ApiIntegration defaultintegration 812be1a1-32c8-4666-a7fb-03ecc385106c<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_write_access</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This parameter is for configuring the write access of integration. If write access is restricted, the integration will not be authorized to write within any domain. Defaults to true.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This parameter is for specifying whether the integration will be enabled or not. Defaults to true</p></li>
<li><p><strong>ignore_responders_from_payload</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If enabled, the integration will ignore recipients sent in request payloads. Defaults to false.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the integration. Name must be unique for each integration.</p></li>
<li><p><strong>owner_team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Owner team id of the integration.</p></li>
<li><p><strong>responders</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ApiIntegrationResponderArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – User, schedule, teams or escalation names to calculate which users will receive the notifications of the alert.</p></li>
<li><p><strong>suppress_notifications</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If enabled, notifications that come from alerts will be suppressed. Defaults to false.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the integration (API, Marid, Prometheus, etc). The full list of options can be found <a class="reference external" href="https://docs.opsgenie.com/docs/integration-types-to-use-with-api">here</a>.</p></li>
<li><p><strong>webhook_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – It is required if type is <code class="docutils literal notranslate"><span class="pre">Webhook</span></code>. This is the url Opsgenie will be sending request to.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_opsgenie.ApiIntegration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_write_access</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">headers</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_responders_from_payload</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">responders</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>ApiIntegrationResponderArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ApiIntegrationResponderArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>ApiIntegrationResponderArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ApiIntegrationResponderArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">suppress_notifications</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">webhook_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_opsgenie.ApiIntegration" title="pulumi_opsgenie.ApiIntegration">ApiIntegration</a><a class="headerlink" href="#pulumi_opsgenie.ApiIntegration.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing ApiIntegration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_write_access</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This parameter is for configuring the write access of integration. If write access is restricted, the integration will not be authorized to write within any domain. Defaults to true.</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) API key of the created integration</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – This parameter is for specifying whether the integration will be enabled or not. Defaults to true</p></li>
<li><p><strong>ignore_responders_from_payload</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If enabled, the integration will ignore recipients sent in request payloads. Defaults to false.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the integration. Name must be unique for each integration.</p></li>
<li><p><strong>owner_team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Owner team id of the integration.</p></li>
<li><p><strong>responders</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ApiIntegrationResponderArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – User, schedule, teams or escalation names to calculate which users will receive the notifications of the alert.</p></li>
<li><p><strong>suppress_notifications</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If enabled, notifications that come from alerts will be suppressed. Defaults to false.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Type of the integration (API, Marid, Prometheus, etc). The full list of options can be found <a class="reference external" href="https://docs.opsgenie.com/docs/integration-types-to-use-with-api">here</a>.</p>
</p></li>
<li><p><strong>webhook_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – It is required if type is <code class="docutils literal notranslate"><span class="pre">Webhook</span></code>. This is the url Opsgenie will be sending request to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.ApiIntegration.allow_write_access">
<em class="property">property </em><code class="sig-name descname">allow_write_access</code><a class="headerlink" href="#pulumi_opsgenie.ApiIntegration.allow_write_access" title="Permalink to this definition"></a></dt>
<dd><p>This parameter is for configuring the write access of integration. If write access is restricted, the integration will not be authorized to write within any domain. Defaults to true.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.ApiIntegration.api_key">
<em class="property">property </em><code class="sig-name descname">api_key</code><a class="headerlink" href="#pulumi_opsgenie.ApiIntegration.api_key" title="Permalink to this definition"></a></dt>
<dd><p>(Computed) API key of the created integration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.ApiIntegration.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_opsgenie.ApiIntegration.enabled" title="Permalink to this definition"></a></dt>
<dd><p>This parameter is for specifying whether the integration will be enabled or not. Defaults to true</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.ApiIntegration.ignore_responders_from_payload">
<em class="property">property </em><code class="sig-name descname">ignore_responders_from_payload</code><a class="headerlink" href="#pulumi_opsgenie.ApiIntegration.ignore_responders_from_payload" title="Permalink to this definition"></a></dt>
<dd><p>If enabled, the integration will ignore recipients sent in request payloads. Defaults to false.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.ApiIntegration.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_opsgenie.ApiIntegration.name" title="Permalink to this definition"></a></dt>
<dd><p>Name of the integration. Name must be unique for each integration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.ApiIntegration.owner_team_id">
<em class="property">property </em><code class="sig-name descname">owner_team_id</code><a class="headerlink" href="#pulumi_opsgenie.ApiIntegration.owner_team_id" title="Permalink to this definition"></a></dt>
<dd><p>Owner team id of the integration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.ApiIntegration.responders">
<em class="property">property </em><code class="sig-name descname">responders</code><a class="headerlink" href="#pulumi_opsgenie.ApiIntegration.responders" title="Permalink to this definition"></a></dt>
<dd><p>User, schedule, teams or escalation names to calculate which users will receive the notifications of the alert.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.ApiIntegration.suppress_notifications">
<em class="property">property </em><code class="sig-name descname">suppress_notifications</code><a class="headerlink" href="#pulumi_opsgenie.ApiIntegration.suppress_notifications" title="Permalink to this definition"></a></dt>
<dd><p>If enabled, notifications that come from alerts will be suppressed. Defaults to false.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.ApiIntegration.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_opsgenie.ApiIntegration.type" title="Permalink to this definition"></a></dt>
<dd><p>Type of the integration (API, Marid, Prometheus, etc). The full list of options can be found <a class="reference external" href="https://docs.opsgenie.com/docs/integration-types-to-use-with-api">here</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.ApiIntegration.webhook_url">
<em class="property">property </em><code class="sig-name descname">webhook_url</code><a class="headerlink" href="#pulumi_opsgenie.ApiIntegration.webhook_url" title="Permalink to this definition"></a></dt>
<dd><p>It is required if type is <code class="docutils literal notranslate"><span class="pre">Webhook</span></code>. This is the url Opsgenie will be sending request to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.ApiIntegration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.ApiIntegration.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.ApiIntegration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.ApiIntegration.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.AwaitableGetEscalationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">AwaitableGetEscalationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_team_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repeats</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.AwaitableGetEscalationResult" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_opsgenie.AwaitableGetHeartbeatResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">AwaitableGetHeartbeatResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">alert_message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interval</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interval_unit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_team_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.AwaitableGetHeartbeatResult" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_opsgenie.AwaitableGetScheduleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">AwaitableGetScheduleResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_team_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timezone</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.AwaitableGetScheduleResult" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_opsgenie.AwaitableGetServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">AwaitableGetServiceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.AwaitableGetServiceResult" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_opsgenie.AwaitableGetTeamResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">AwaitableGetTeamResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.AwaitableGetTeamResult" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_opsgenie.AwaitableGetUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">AwaitableGetUserResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">full_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locale</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timezone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.AwaitableGetUserResult" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_opsgenie.CustomRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">CustomRole</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disallowed_rights</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extended_role</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">granted_rights</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.CustomRole" title="Permalink to this definition"></a></dt>
<dd><p>Manages custom user roles within Opsgenie.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_opsgenie</span> <span class="k">as</span> <span class="nn">opsgenie</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">CustomRole</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">disallowed_rights</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;profile-edit&quot;</span><span class="p">,</span>
        <span class="s2">&quot;contacts-edit&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">extended_role</span><span class="o">=</span><span class="s2">&quot;user&quot;</span><span class="p">,</span>
    <span class="n">granted_rights</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;alert-delete&quot;</span><span class="p">],</span>
    <span class="n">role_name</span><span class="o">=</span><span class="s2">&quot;genierole&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>disallowed_rights</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The rights this role cannot have. For allowed values please refer <a class="reference external" href="https://docs.opsgenie.com/docs/custom-user-role-api#section-user-right-prerequisites">User Right Prerequisites</a></p></li>
<li><p><strong>extended_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role from which this role has been derived. Allowed Values: “user”, “observer”, “stakeholder”.</p></li>
<li><p><strong>granted_rights</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – <p>The rights granted to this role. For allowed values please refer <a class="reference external" href="https://docs.opsgenie.com/docs/custom-user-role-api#section-user-right-prerequisites">User Right Prerequisites</a></p>
</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the custom role.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_opsgenie.CustomRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disallowed_rights</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extended_role</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">granted_rights</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_opsgenie.CustomRole" title="pulumi_opsgenie.CustomRole">CustomRole</a><a class="headerlink" href="#pulumi_opsgenie.CustomRole.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing CustomRole resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>disallowed_rights</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – <p>The rights this role cannot have. For allowed values please refer <a class="reference external" href="https://docs.opsgenie.com/docs/custom-user-role-api#section-user-right-prerequisites">User Right Prerequisites</a></p>
</p></li>
<li><p><strong>extended_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role from which this role has been derived. Allowed Values: “user”, “observer”, “stakeholder”.</p></li>
<li><p><strong>granted_rights</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – <p>The rights granted to this role. For allowed values please refer <a class="reference external" href="https://docs.opsgenie.com/docs/custom-user-role-api#section-user-right-prerequisites">User Right Prerequisites</a></p>
</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the custom role.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.CustomRole.disallowed_rights">
<em class="property">property </em><code class="sig-name descname">disallowed_rights</code><a class="headerlink" href="#pulumi_opsgenie.CustomRole.disallowed_rights" title="Permalink to this definition"></a></dt>
<dd><p>The rights this role cannot have. For allowed values please refer <a class="reference external" href="https://docs.opsgenie.com/docs/custom-user-role-api#section-user-right-prerequisites">User Right Prerequisites</a></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.CustomRole.extended_role">
<em class="property">property </em><code class="sig-name descname">extended_role</code><a class="headerlink" href="#pulumi_opsgenie.CustomRole.extended_role" title="Permalink to this definition"></a></dt>
<dd><p>The role from which this role has been derived. Allowed Values: “user”, “observer”, “stakeholder”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.CustomRole.granted_rights">
<em class="property">property </em><code class="sig-name descname">granted_rights</code><a class="headerlink" href="#pulumi_opsgenie.CustomRole.granted_rights" title="Permalink to this definition"></a></dt>
<dd><p>The rights granted to this role. For allowed values please refer <a class="reference external" href="https://docs.opsgenie.com/docs/custom-user-role-api#section-user-right-prerequisites">User Right Prerequisites</a></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.CustomRole.role_name">
<em class="property">property </em><code class="sig-name descname">role_name</code><a class="headerlink" href="#pulumi_opsgenie.CustomRole.role_name" title="Permalink to this definition"></a></dt>
<dd><p>Name of the custom role.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.CustomRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.CustomRole.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.CustomRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.CustomRole.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.EmailIntegration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">EmailIntegration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_responders_from_payload</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">responders</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>EmailIntegrationResponderArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>EmailIntegrationResponderArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>EmailIntegrationResponderArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>EmailIntegrationResponderArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">suppress_notifications</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.EmailIntegration" title="Permalink to this definition"></a></dt>
<dd><p>Manages an Email Integration within Opsgenie.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_opsgenie</span> <span class="k">as</span> <span class="nn">opsgenie</span>

<span class="n">test_email_integration</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">EmailIntegration</span><span class="p">(</span><span class="s2">&quot;testEmailIntegration&quot;</span><span class="p">,</span> <span class="n">email_username</span><span class="o">=</span><span class="s2">&quot;fahri&quot;</span><span class="p">)</span>
<span class="n">test_index_email_integration_email_integration</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">EmailIntegration</span><span class="p">(</span><span class="s2">&quot;testIndex/emailIntegrationEmailIntegration&quot;</span><span class="p">,</span>
    <span class="n">responders</span><span class="o">=</span><span class="p">[</span>
        <span class="n">opsgenie</span><span class="o">.</span><span class="n">EmailIntegrationResponderArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;user&quot;</span><span class="p">,</span>
            <span class="nb">id</span><span class="o">=</span><span class="n">opsgenie_user</span><span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
        <span class="p">),</span>
        <span class="n">opsgenie</span><span class="o">.</span><span class="n">EmailIntegrationResponderArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;schedule&quot;</span><span class="p">,</span>
            <span class="nb">id</span><span class="o">=</span><span class="n">opsgenie_schedule</span><span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
        <span class="p">),</span>
        <span class="n">opsgenie</span><span class="o">.</span><span class="n">EmailIntegrationResponderArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;escalation&quot;</span><span class="p">,</span>
            <span class="nb">id</span><span class="o">=</span><span class="n">opsgenie_escalation</span><span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
        <span class="p">),</span>
        <span class="n">opsgenie</span><span class="o">.</span><span class="n">EmailIntegrationResponderArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;team&quot;</span><span class="p">,</span>
            <span class="nb">id</span><span class="o">=</span><span class="n">opsgenie_team</span><span class="p">[</span><span class="s2">&quot;test2&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="n">email_username</span><span class="o">=</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">ignore_responders_from_payload</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">suppress_notifications</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">test_opsgenie_index_email_integration_email_integration</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">EmailIntegration</span><span class="p">(</span><span class="s2">&quot;testOpsgenieIndex/emailIntegrationEmailIntegration&quot;</span><span class="p">,</span>
    <span class="n">responders</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">EmailIntegrationResponderArgs</span><span class="p">(</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;user&quot;</span><span class="p">,</span>
        <span class="nb">id</span><span class="o">=</span><span class="n">opsgenie_user</span><span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="p">)],</span>
    <span class="n">email_username</span><span class="o">=</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">ignore_responders_from_payload</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">suppress_notifications</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">owner_team_id</span><span class="o">=</span><span class="n">opsgenie_team_genies</span><span class="p">[</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<p>Email Integrations can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import opsgenie:index/emailIntegration:EmailIntegration <span class="nb">test</span> 812be1a1-32c8-4666-a7fb-03ecc385106c<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>email_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username part of the email address. It must be unique for each integration.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A Member block as documented below.</p></li>
<li><p><strong>ignore_responders_from_payload</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If enabled, the integration will ignore recipients sent in request payloads. Defaults to false.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the integration. Name must be unique for each integration.</p></li>
<li><p><strong>owner_team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Owner team id of the integration.</p></li>
<li><p><strong>suppress_notifications</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If enabled, notifications that come from alerts will be suppressed. Defaults to false.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_opsgenie.EmailIntegration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_responders_from_payload</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">responders</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>EmailIntegrationResponderArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>EmailIntegrationResponderArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>EmailIntegrationResponderArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>EmailIntegrationResponderArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">suppress_notifications</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_opsgenie.EmailIntegration" title="pulumi_opsgenie.EmailIntegration">EmailIntegration</a><a class="headerlink" href="#pulumi_opsgenie.EmailIntegration.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing EmailIntegration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>email_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username part of the email address. It must be unique for each integration.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A Member block as documented below.</p></li>
<li><p><strong>ignore_responders_from_payload</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If enabled, the integration will ignore recipients sent in request payloads. Defaults to false.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the integration. Name must be unique for each integration.</p></li>
<li><p><strong>owner_team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Owner team id of the integration.</p></li>
<li><p><strong>suppress_notifications</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If enabled, notifications that come from alerts will be suppressed. Defaults to false.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.EmailIntegration.email_username">
<em class="property">property </em><code class="sig-name descname">email_username</code><a class="headerlink" href="#pulumi_opsgenie.EmailIntegration.email_username" title="Permalink to this definition"></a></dt>
<dd><p>The username part of the email address. It must be unique for each integration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.EmailIntegration.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_opsgenie.EmailIntegration.enabled" title="Permalink to this definition"></a></dt>
<dd><p>A Member block as documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.EmailIntegration.ignore_responders_from_payload">
<em class="property">property </em><code class="sig-name descname">ignore_responders_from_payload</code><a class="headerlink" href="#pulumi_opsgenie.EmailIntegration.ignore_responders_from_payload" title="Permalink to this definition"></a></dt>
<dd><p>If enabled, the integration will ignore recipients sent in request payloads. Defaults to false.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.EmailIntegration.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_opsgenie.EmailIntegration.name" title="Permalink to this definition"></a></dt>
<dd><p>Name of the integration. Name must be unique for each integration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.EmailIntegration.owner_team_id">
<em class="property">property </em><code class="sig-name descname">owner_team_id</code><a class="headerlink" href="#pulumi_opsgenie.EmailIntegration.owner_team_id" title="Permalink to this definition"></a></dt>
<dd><p>Owner team id of the integration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.EmailIntegration.suppress_notifications">
<em class="property">property </em><code class="sig-name descname">suppress_notifications</code><a class="headerlink" href="#pulumi_opsgenie.EmailIntegration.suppress_notifications" title="Permalink to this definition"></a></dt>
<dd><p>If enabled, notifications that come from alerts will be suppressed. Defaults to false.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.EmailIntegration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.EmailIntegration.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.EmailIntegration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.EmailIntegration.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.Escalation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">Escalation</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repeats</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>EscalationRepeatArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>EscalationRepeatArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>EscalationRepeatArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>EscalationRepeatArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>EscalationRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>EscalationRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>EscalationRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>EscalationRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.Escalation" title="Permalink to this definition"></a></dt>
<dd><p>Manages an Escalation within Opsgenie.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_opsgenie</span> <span class="k">as</span> <span class="nn">opsgenie</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">Escalation</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">owner_team_id</span><span class="o">=</span><span class="n">opsgenie_team</span><span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">repeats</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">EscalationRepeatArgs</span><span class="p">(</span>
        <span class="n">close_alert_after_all</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="n">count</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
        <span class="n">reset_recipient_states</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">wait_interval</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">rules</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">EscalationRuleArgs</span><span class="p">(</span>
        <span class="n">condition</span><span class="o">=</span><span class="s2">&quot;if-not-acked&quot;</span><span class="p">,</span>
        <span class="n">delay</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
        <span class="n">notify_type</span><span class="o">=</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
        <span class="n">recipients</span><span class="o">=</span><span class="p">[</span>
            <span class="n">opsgenie</span><span class="o">.</span><span class="n">EscalationRuleRecipientArgs</span><span class="p">(</span>
                <span class="nb">id</span><span class="o">=</span><span class="n">opsgenie_user</span><span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
                <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;user&quot;</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">opsgenie</span><span class="o">.</span><span class="n">EscalationRuleRecipientArgs</span><span class="p">(</span>
                <span class="nb">id</span><span class="o">=</span><span class="n">opsgenie_team</span><span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
                <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;team&quot;</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">opsgenie</span><span class="o">.</span><span class="n">EscalationRuleRecipientArgs</span><span class="p">(</span>
                <span class="nb">id</span><span class="o">=</span><span class="n">opsgenie_schedule</span><span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
                <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;schedule&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">],</span>
    <span class="p">)])</span>
</pre></div>
</div>
<p>Escalations can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import opsgenie:index/escalation:Escalation <span class="nb">test</span> 812be1a1-32c8-4666-a7fb-03ecc385106c<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the escalation.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the escalation.</p></li>
<li><p><strong>owner_team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Owner team id of the escalation.</p></li>
<li><p><strong>repeats</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'EscalationRepeatArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Repeat preferences of the escalation including repeat interval, count, reverting acknowledge and seen states back and closing an alert automatically as soon as repeats are completed</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'EscalationRuleArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – List of the escalation rules.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_opsgenie.Escalation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repeats</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>EscalationRepeatArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>EscalationRepeatArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>EscalationRepeatArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>EscalationRepeatArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>EscalationRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>EscalationRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>EscalationRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>EscalationRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_opsgenie.Escalation" title="pulumi_opsgenie.Escalation">Escalation</a><a class="headerlink" href="#pulumi_opsgenie.Escalation.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Escalation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the escalation.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the escalation.</p></li>
<li><p><strong>owner_team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Owner team id of the escalation.</p></li>
<li><p><strong>repeats</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'EscalationRepeatArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Repeat preferences of the escalation including repeat interval, count, reverting acknowledge and seen states back and closing an alert automatically as soon as repeats are completed</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'EscalationRuleArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – List of the escalation rules.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Escalation.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_opsgenie.Escalation.description" title="Permalink to this definition"></a></dt>
<dd><p>Description of the escalation.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Escalation.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_opsgenie.Escalation.name" title="Permalink to this definition"></a></dt>
<dd><p>Name of the escalation.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Escalation.owner_team_id">
<em class="property">property </em><code class="sig-name descname">owner_team_id</code><a class="headerlink" href="#pulumi_opsgenie.Escalation.owner_team_id" title="Permalink to this definition"></a></dt>
<dd><p>Owner team id of the escalation.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Escalation.repeats">
<em class="property">property </em><code class="sig-name descname">repeats</code><a class="headerlink" href="#pulumi_opsgenie.Escalation.repeats" title="Permalink to this definition"></a></dt>
<dd><p>Repeat preferences of the escalation including repeat interval, count, reverting acknowledge and seen states back and closing an alert automatically as soon as repeats are completed</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Escalation.rules">
<em class="property">property </em><code class="sig-name descname">rules</code><a class="headerlink" href="#pulumi_opsgenie.Escalation.rules" title="Permalink to this definition"></a></dt>
<dd><p>List of the escalation rules.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Escalation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.Escalation.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.Escalation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.Escalation.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.GetEscalationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">GetEscalationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_team_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repeats</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.GetEscalationResult" title="Permalink to this definition"></a></dt>
<dd><p>A collection of values returned by getEscalation.</p>
<dl class="py method">
<dt id="pulumi_opsgenie.GetEscalationResult.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_opsgenie.GetEscalationResult.description" title="Permalink to this definition"></a></dt>
<dd><p>Escalation Description</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.GetEscalationResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_opsgenie.GetEscalationResult.id" title="Permalink to this definition"></a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.GetEscalationResult.owner_team_id">
<em class="property">property </em><code class="sig-name descname">owner_team_id</code><a class="headerlink" href="#pulumi_opsgenie.GetEscalationResult.owner_team_id" title="Permalink to this definition"></a></dt>
<dd><p>If owner team exist the id of the team is exported</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.GetEscalationResult.repeats">
<em class="property">property </em><code class="sig-name descname">repeats</code><a class="headerlink" href="#pulumi_opsgenie.GetEscalationResult.repeats" title="Permalink to this definition"></a></dt>
<dd><p>Escalation repeat preferences</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.GetEscalationResult.rules">
<em class="property">property </em><code class="sig-name descname">rules</code><a class="headerlink" href="#pulumi_opsgenie.GetEscalationResult.rules" title="Permalink to this definition"></a></dt>
<dd><p>Escalation rules</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_opsgenie.GetHeartbeatResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">GetHeartbeatResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">alert_message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interval</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interval_unit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_team_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.GetHeartbeatResult" title="Permalink to this definition"></a></dt>
<dd><p>A collection of values returned by getHeartbeat.</p>
<dl class="py method">
<dt id="pulumi_opsgenie.GetHeartbeatResult.alert_message">
<em class="property">property </em><code class="sig-name descname">alert_message</code><a class="headerlink" href="#pulumi_opsgenie.GetHeartbeatResult.alert_message" title="Permalink to this definition"></a></dt>
<dd><p>Specifies the alert message for heartbeat expiration alert. If this is not provided, default alert message is “HeartbeatName is expired”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.GetHeartbeatResult.alert_priority">
<em class="property">property </em><code class="sig-name descname">alert_priority</code><a class="headerlink" href="#pulumi_opsgenie.GetHeartbeatResult.alert_priority" title="Permalink to this definition"></a></dt>
<dd><p>Specifies the alert priority for heartbeat expiration alert. If this is not provided, default priority is P3.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.GetHeartbeatResult.alert_tags">
<em class="property">property </em><code class="sig-name descname">alert_tags</code><a class="headerlink" href="#pulumi_opsgenie.GetHeartbeatResult.alert_tags" title="Permalink to this definition"></a></dt>
<dd><p>Specifies the alert tags for heartbeat expiration alert.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.GetHeartbeatResult.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_opsgenie.GetHeartbeatResult.description" title="Permalink to this definition"></a></dt>
<dd><p>An optional description of the heartbeat</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.GetHeartbeatResult.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_opsgenie.GetHeartbeatResult.enabled" title="Permalink to this definition"></a></dt>
<dd><p>Enable/disable heartbeat monitoring.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.GetHeartbeatResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_opsgenie.GetHeartbeatResult.id" title="Permalink to this definition"></a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.GetHeartbeatResult.interval">
<em class="property">property </em><code class="sig-name descname">interval</code><a class="headerlink" href="#pulumi_opsgenie.GetHeartbeatResult.interval" title="Permalink to this definition"></a></dt>
<dd><p>Specifies how often a heartbeat message should be expected.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.GetHeartbeatResult.interval_unit">
<em class="property">property </em><code class="sig-name descname">interval_unit</code><a class="headerlink" href="#pulumi_opsgenie.GetHeartbeatResult.interval_unit" title="Permalink to this definition"></a></dt>
<dd><p>Interval specified as minutes, hours or days.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.GetHeartbeatResult.owner_team_id">
<em class="property">property </em><code class="sig-name descname">owner_team_id</code><a class="headerlink" href="#pulumi_opsgenie.GetHeartbeatResult.owner_team_id" title="Permalink to this definition"></a></dt>
<dd><p>Owner team of the heartbeat.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_opsgenie.GetScheduleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">GetScheduleResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_team_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timezone</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.GetScheduleResult" title="Permalink to this definition"></a></dt>
<dd><p>A collection of values returned by getSchedule.</p>
<dl class="py method">
<dt id="pulumi_opsgenie.GetScheduleResult.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_opsgenie.GetScheduleResult.description" title="Permalink to this definition"></a></dt>
<dd><p>Timezone of schedule. Please look at <a class="reference external" href="https://docs.opsgenie.com/docs/supported-timezone-ids">Supported Timezone Ids</a> for available timezones - Defaults to “America/New_York”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.GetScheduleResult.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_opsgenie.GetScheduleResult.enabled" title="Permalink to this definition"></a></dt>
<dd><p>Enable/disable state of schedule</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.GetScheduleResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_opsgenie.GetScheduleResult.id" title="Permalink to this definition"></a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.GetScheduleResult.owner_team_id">
<em class="property">property </em><code class="sig-name descname">owner_team_id</code><a class="headerlink" href="#pulumi_opsgenie.GetScheduleResult.owner_team_id" title="Permalink to this definition"></a></dt>
<dd><p>Owner team id of the schedule.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.GetScheduleResult.timezone">
<em class="property">property </em><code class="sig-name descname">timezone</code><a class="headerlink" href="#pulumi_opsgenie.GetScheduleResult.timezone" title="Permalink to this definition"></a></dt>
<dd><p>The description of schedule.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_opsgenie.GetServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">GetServiceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.GetServiceResult" title="Permalink to this definition"></a></dt>
<dd><p>A collection of values returned by getService.</p>
<dl class="py method">
<dt id="pulumi_opsgenie.GetServiceResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_opsgenie.GetServiceResult.id" title="Permalink to this definition"></a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_opsgenie.GetTeamResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">GetTeamResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.GetTeamResult" title="Permalink to this definition"></a></dt>
<dd><p>A collection of values returned by getTeam.</p>
<dl class="py method">
<dt id="pulumi_opsgenie.GetTeamResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_opsgenie.GetTeamResult.id" title="Permalink to this definition"></a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_opsgenie.GetUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">GetUserResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">full_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locale</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timezone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.GetUserResult" title="Permalink to this definition"></a></dt>
<dd><p>A collection of values returned by getUser.</p>
<dl class="py method">
<dt id="pulumi_opsgenie.GetUserResult.full_name">
<em class="property">property </em><code class="sig-name descname">full_name</code><a class="headerlink" href="#pulumi_opsgenie.GetUserResult.full_name" title="Permalink to this definition"></a></dt>
<dd><p>The Full Name of the User.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.GetUserResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_opsgenie.GetUserResult.id" title="Permalink to this definition"></a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.GetUserResult.locale">
<em class="property">property </em><code class="sig-name descname">locale</code><a class="headerlink" href="#pulumi_opsgenie.GetUserResult.locale" title="Permalink to this definition"></a></dt>
<dd><p>Location information for the user. Please look at <a class="reference external" href="https://docs.opsgenie.com/docs/supported-locales">Supported Locale Ids</a> for available locales.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.GetUserResult.role">
<em class="property">property </em><code class="sig-name descname">role</code><a class="headerlink" href="#pulumi_opsgenie.GetUserResult.role" title="Permalink to this definition"></a></dt>
<dd><p>The Role assigned to the User. Either a built-in such as ‘Owner’, ‘Admin’ or ‘User’ - or the name of a custom role.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.GetUserResult.timezone">
<em class="property">property </em><code class="sig-name descname">timezone</code><a class="headerlink" href="#pulumi_opsgenie.GetUserResult.timezone" title="Permalink to this definition"></a></dt>
<dd><p>Timezone information of the user. Please look at <a class="reference external" href="https://docs.opsgenie.com/docs/supported-timezone-ids">Supported Timezone Ids</a> for available timezones.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_opsgenie.Heartbeat">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">Heartbeat</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_message</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_priority</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_tags</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interval</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interval_unit</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.Heartbeat" title="Permalink to this definition"></a></dt>
<dd><p>Manages heartbeat within Opsgenie.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_opsgenie</span> <span class="k">as</span> <span class="nn">opsgenie</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">Heartbeat</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">alert_message</span><span class="o">=</span><span class="s2">&quot;Test&quot;</span><span class="p">,</span>
    <span class="n">alert_priority</span><span class="o">=</span><span class="s2">&quot;P3&quot;</span><span class="p">,</span>
    <span class="n">alert_tags</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;test&quot;</span><span class="p">,</span>
        <span class="s2">&quot;fahri&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;test opsgenie heartbeat terraform&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">interval</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
    <span class="n">interval_unit</span><span class="o">=</span><span class="s2">&quot;minutes&quot;</span><span class="p">,</span>
    <span class="n">owner_team_id</span><span class="o">=</span><span class="n">opsgenie_team</span><span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<p>Heartbeat Integrations can be imported using the <code class="docutils literal notranslate"><span class="pre">name</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import opsgenie:index/heartbeat:Heartbeat <span class="nb">test</span> geniehearbeat-%s<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alert_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the alert message for heartbeat expiration alert. If this is not provided, default alert message is “HeartbeatName is expired”.</p></li>
<li><p><strong>alert_priority</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the alert priority for heartbeat expiration alert. If this is not provided, default priority is P3.</p></li>
<li><p><strong>alert_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Specifies the alert tags for heartbeat expiration alert.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional description of the heartbeat</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable heartbeat monitoring.</p></li>
<li><p><strong>interval</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specifies how often a heartbeat message should be expected.</p></li>
<li><p><strong>interval_unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Interval specified as minutes, hours or days.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the heartbeat</p></li>
<li><p><strong>owner_team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Owner team of the heartbeat.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_opsgenie.Heartbeat.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_message</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_priority</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_tags</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interval</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interval_unit</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_opsgenie.Heartbeat" title="pulumi_opsgenie.Heartbeat">Heartbeat</a><a class="headerlink" href="#pulumi_opsgenie.Heartbeat.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Heartbeat resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alert_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the alert message for heartbeat expiration alert. If this is not provided, default alert message is “HeartbeatName is expired”.</p></li>
<li><p><strong>alert_priority</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the alert priority for heartbeat expiration alert. If this is not provided, default priority is P3.</p></li>
<li><p><strong>alert_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Specifies the alert tags for heartbeat expiration alert.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional description of the heartbeat</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable heartbeat monitoring.</p></li>
<li><p><strong>interval</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specifies how often a heartbeat message should be expected.</p></li>
<li><p><strong>interval_unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Interval specified as minutes, hours or days.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the heartbeat</p></li>
<li><p><strong>owner_team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Owner team of the heartbeat.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Heartbeat.alert_message">
<em class="property">property </em><code class="sig-name descname">alert_message</code><a class="headerlink" href="#pulumi_opsgenie.Heartbeat.alert_message" title="Permalink to this definition"></a></dt>
<dd><p>Specifies the alert message for heartbeat expiration alert. If this is not provided, default alert message is “HeartbeatName is expired”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Heartbeat.alert_priority">
<em class="property">property </em><code class="sig-name descname">alert_priority</code><a class="headerlink" href="#pulumi_opsgenie.Heartbeat.alert_priority" title="Permalink to this definition"></a></dt>
<dd><p>Specifies the alert priority for heartbeat expiration alert. If this is not provided, default priority is P3.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Heartbeat.alert_tags">
<em class="property">property </em><code class="sig-name descname">alert_tags</code><a class="headerlink" href="#pulumi_opsgenie.Heartbeat.alert_tags" title="Permalink to this definition"></a></dt>
<dd><p>Specifies the alert tags for heartbeat expiration alert.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Heartbeat.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_opsgenie.Heartbeat.description" title="Permalink to this definition"></a></dt>
<dd><p>An optional description of the heartbeat</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Heartbeat.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_opsgenie.Heartbeat.enabled" title="Permalink to this definition"></a></dt>
<dd><p>Enable/disable heartbeat monitoring.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Heartbeat.interval">
<em class="property">property </em><code class="sig-name descname">interval</code><a class="headerlink" href="#pulumi_opsgenie.Heartbeat.interval" title="Permalink to this definition"></a></dt>
<dd><p>Specifies how often a heartbeat message should be expected.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Heartbeat.interval_unit">
<em class="property">property </em><code class="sig-name descname">interval_unit</code><a class="headerlink" href="#pulumi_opsgenie.Heartbeat.interval_unit" title="Permalink to this definition"></a></dt>
<dd><p>Interval specified as minutes, hours or days.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Heartbeat.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_opsgenie.Heartbeat.name" title="Permalink to this definition"></a></dt>
<dd><p>Name of the heartbeat</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Heartbeat.owner_team_id">
<em class="property">property </em><code class="sig-name descname">owner_team_id</code><a class="headerlink" href="#pulumi_opsgenie.Heartbeat.owner_team_id" title="Permalink to this definition"></a></dt>
<dd><p>Owner team of the heartbeat.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Heartbeat.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.Heartbeat.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.Heartbeat.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.Heartbeat.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.IncidentTemplate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">IncidentTemplate</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">details</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">impacted_services</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stakeholder_properties</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>IncidentTemplateStakeholderPropertyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>IncidentTemplateStakeholderPropertyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>IncidentTemplateStakeholderPropertyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>IncidentTemplateStakeholderPropertyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.IncidentTemplate" title="Permalink to this definition"></a></dt>
<dd><p>Manages an Incident Template within Opsgenie.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_opsgenie</span> <span class="k">as</span> <span class="nn">opsgenie</span>

<span class="n">test_team</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">Team</span><span class="p">(</span><span class="s2">&quot;testTeam&quot;</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">&quot;This team deals with all the things&quot;</span><span class="p">)</span>
<span class="n">test_service</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">Service</span><span class="p">(</span><span class="s2">&quot;testService&quot;</span><span class="p">,</span> <span class="n">team_id</span><span class="o">=</span><span class="n">test_team</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">test_incident_template</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">IncidentTemplate</span><span class="p">(</span><span class="s2">&quot;testIncidentTemplate&quot;</span><span class="p">,</span>
    <span class="n">message</span><span class="o">=</span><span class="s2">&quot;Incident Message&quot;</span><span class="p">,</span>
    <span class="n">priority</span><span class="o">=</span><span class="s2">&quot;P2&quot;</span><span class="p">,</span>
    <span class="n">stakeholder_properties</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">IncidentTemplateStakeholderPropertyArgs</span><span class="p">(</span>
        <span class="n">enable</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">message</span><span class="o">=</span><span class="s2">&quot;Stakeholder Message&quot;</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Stakeholder Description&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;tag1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;tag2&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Incident Description&quot;</span><span class="p">,</span>
    <span class="n">details</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;key1&quot;</span><span class="p">:</span> <span class="s2">&quot;value1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;key2&quot;</span><span class="p">:</span> <span class="s2">&quot;value2&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">impacted_services</span><span class="o">=</span><span class="p">[</span><span class="n">test_service</span><span class="o">.</span><span class="n">id</span><span class="p">])</span>
</pre></div>
</div>
<p>Service can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import opsgenie:index/incidentTemplate:IncidentTemplate <span class="nb">test</span> 812be1a1-32c8-4666-a7fb-03ecc385106c<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description that is generally used to provide a detailed information about the alert. This field must not be longer than 15000 characters.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>details</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Map of key-value pairs to use as custom properties of the incident template. This field must not be longer than 8000 characters.</p></li>
<li><p><strong>message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Message that is to be passed to audience that is generally used to provide a content information about the alert.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the incident template.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Priority level of the incident. Possible values are P1, P2, P3, P4 and P5.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Tags of the incident template.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_opsgenie.IncidentTemplate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">details</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">impacted_services</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stakeholder_properties</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>IncidentTemplateStakeholderPropertyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>IncidentTemplateStakeholderPropertyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>IncidentTemplateStakeholderPropertyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>IncidentTemplateStakeholderPropertyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_opsgenie.IncidentTemplate" title="pulumi_opsgenie.IncidentTemplate">IncidentTemplate</a><a class="headerlink" href="#pulumi_opsgenie.IncidentTemplate.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing IncidentTemplate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description that is generally used to provide a detailed information about the alert. This field must not be longer than 15000 characters.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>details</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Map of key-value pairs to use as custom properties of the incident template. This field must not be longer than 8000 characters.</p></li>
<li><p><strong>message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Message that is to be passed to audience that is generally used to provide a content information about the alert.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the incident template.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Priority level of the incident. Possible values are P1, P2, P3, P4 and P5.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Tags of the incident template.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.IncidentTemplate.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_opsgenie.IncidentTemplate.description" title="Permalink to this definition"></a></dt>
<dd><p>Description that is generally used to provide a detailed information about the alert. This field must not be longer than 15000 characters.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.IncidentTemplate.details">
<em class="property">property </em><code class="sig-name descname">details</code><a class="headerlink" href="#pulumi_opsgenie.IncidentTemplate.details" title="Permalink to this definition"></a></dt>
<dd><p>Map of key-value pairs to use as custom properties of the incident template. This field must not be longer than 8000 characters.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.IncidentTemplate.message">
<em class="property">property </em><code class="sig-name descname">message</code><a class="headerlink" href="#pulumi_opsgenie.IncidentTemplate.message" title="Permalink to this definition"></a></dt>
<dd><p>Message that is to be passed to audience that is generally used to provide a content information about the alert.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.IncidentTemplate.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_opsgenie.IncidentTemplate.name" title="Permalink to this definition"></a></dt>
<dd><p>Name of the incident template.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.IncidentTemplate.priority">
<em class="property">property </em><code class="sig-name descname">priority</code><a class="headerlink" href="#pulumi_opsgenie.IncidentTemplate.priority" title="Permalink to this definition"></a></dt>
<dd><p>Priority level of the incident. Possible values are P1, P2, P3, P4 and P5.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.IncidentTemplate.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_opsgenie.IncidentTemplate.tags" title="Permalink to this definition"></a></dt>
<dd><p>Tags of the incident template.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.IncidentTemplate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.IncidentTemplate.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.IncidentTemplate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.IncidentTemplate.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.IntegrationAction">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">IntegrationAction</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acknowledges</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>IntegrationActionAcknowledgeArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>IntegrationActionAcknowledgeArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>IntegrationActionAcknowledgeArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>IntegrationActionAcknowledgeArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">add_notes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>IntegrationActionAddNoteArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>IntegrationActionAddNoteArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>IntegrationActionAddNoteArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>IntegrationActionAddNoteArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">closes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>IntegrationActionCloseArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>IntegrationActionCloseArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>IntegrationActionCloseArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>IntegrationActionCloseArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creates</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>IntegrationActionCreateArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>IntegrationActionCreateArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>IntegrationActionCreateArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>IntegrationActionCreateArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignores</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>IntegrationActionIgnoreArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>IntegrationActionIgnoreArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>IntegrationActionIgnoreArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>IntegrationActionIgnoreArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.IntegrationAction" title="Permalink to this definition"></a></dt>
<dd><p>Manages advanced actions for Integrations within Opsgenie. This applies for the following resources:</p>
<ul class="simple">
<li><p>ApiIntegration</p></li>
<li><p>EmailIntegration</p></li>
</ul>
<p>The actions that are supported are:</p>
<ul class="simple">
<li><p>create</p></li>
<li><p>close</p></li>
<li><p>acknowledge</p></li>
<li><p>add_note</p></li>
<li><p>ignore</p></li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_opsgenie</span> <span class="k">as</span> <span class="nn">opsgenie</span>

<span class="n">test_action</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">IntegrationAction</span><span class="p">(</span><span class="s2">&quot;testAction&quot;</span><span class="p">,</span>
    <span class="n">integration_id</span><span class="o">=</span><span class="n">opsgenie_api_integration</span><span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">creates</span><span class="o">=</span><span class="p">[</span>
        <span class="n">opsgenie</span><span class="o">.</span><span class="n">IntegrationActionCreateArgs</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;create action&quot;</span><span class="p">,</span>
            <span class="n">tags</span><span class="o">=</span><span class="p">[</span>
                <span class="s2">&quot;CRITICAL&quot;</span><span class="p">,</span>
                <span class="s2">&quot;SEV-0&quot;</span><span class="p">,</span>
            <span class="p">],</span>
            <span class="n">user</span><span class="o">=</span><span class="s2">&quot;Example-service&quot;</span><span class="p">,</span>
            <span class="n">note</span><span class="o">=</span><span class="s2">&quot;{{note}}&quot;</span><span class="p">,</span>
            <span class="n">alias</span><span class="o">=</span><span class="s2">&quot;{{alias}}&quot;</span><span class="p">,</span>
            <span class="n">source</span><span class="o">=</span><span class="s2">&quot;{{source}}&quot;</span><span class="p">,</span>
            <span class="n">message</span><span class="o">=</span><span class="s2">&quot;{{message}}&quot;</span><span class="p">,</span>
            <span class="n">description</span><span class="o">=</span><span class="s2">&quot;{{description}}&quot;</span><span class="p">,</span>
            <span class="n">entity</span><span class="o">=</span><span class="s2">&quot;{{entity}}&quot;</span><span class="p">,</span>
            <span class="n">alert_actions</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;Runbook ID#342&quot;</span><span class="p">],</span>
            <span class="n">filters</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">IntegrationActionCreateFilterArgs</span><span class="p">(</span>
                <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;match-all-conditions&quot;</span><span class="p">,</span>
                <span class="n">conditions</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">IntegrationActionCreateFilterConditionArgs</span><span class="p">(</span>
                    <span class="n">field</span><span class="o">=</span><span class="s2">&quot;priority&quot;</span><span class="p">,</span>
                    <span class="n">operation</span><span class="o">=</span><span class="s2">&quot;equals&quot;</span><span class="p">,</span>
                    <span class="n">expected_value</span><span class="o">=</span><span class="s2">&quot;P1&quot;</span><span class="p">,</span>
                <span class="p">)],</span>
            <span class="p">)],</span>
            <span class="n">responders</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">IntegrationActionCreateResponderArgs</span><span class="p">(</span>
                <span class="nb">id</span><span class="o">=</span><span class="n">opsgenie_team</span><span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
                <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;team&quot;</span><span class="p">,</span>
            <span class="p">)],</span>
        <span class="p">),</span>
        <span class="n">opsgenie</span><span class="o">.</span><span class="n">IntegrationActionCreateArgs</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Create medium priority alerts&quot;</span><span class="p">,</span>
            <span class="n">tags</span><span class="o">=</span><span class="p">[</span>
                <span class="s2">&quot;SEVERE&quot;</span><span class="p">,</span>
                <span class="s2">&quot;SEV-1&quot;</span><span class="p">,</span>
            <span class="p">],</span>
            <span class="n">priority</span><span class="o">=</span><span class="s2">&quot;P3&quot;</span><span class="p">,</span>
            <span class="n">filters</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">IntegrationActionCreateFilterArgs</span><span class="p">(</span>
                <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;match-all-conditions&quot;</span><span class="p">,</span>
                <span class="n">conditions</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">IntegrationActionCreateFilterConditionArgs</span><span class="p">(</span>
                    <span class="n">field</span><span class="o">=</span><span class="s2">&quot;priority&quot;</span><span class="p">,</span>
                    <span class="n">operation</span><span class="o">=</span><span class="s2">&quot;equals&quot;</span><span class="p">,</span>
                    <span class="n">expected_value</span><span class="o">=</span><span class="s2">&quot;P2&quot;</span><span class="p">,</span>
                <span class="p">)],</span>
            <span class="p">)],</span>
        <span class="p">),</span>
        <span class="n">opsgenie</span><span class="o">.</span><span class="n">IntegrationActionCreateArgs</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Create alert with priority from message&quot;</span><span class="p">,</span>
            <span class="n">custom_priority</span><span class="o">=</span><span class="s2">&quot;{{message.substringAfter(&quot;</span><span class="p">[</span><span class="n">custom</span><span class="p">]</span><span class="s2">&quot;)}}&quot;</span><span class="p">,</span>
            <span class="n">filters</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">IntegrationActionCreateFilterArgs</span><span class="p">(</span>
                <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;match-all-conditions&quot;</span><span class="p">,</span>
                <span class="n">conditions</span><span class="o">=</span><span class="p">[</span>
                    <span class="n">opsgenie</span><span class="o">.</span><span class="n">IntegrationActionCreateFilterConditionArgs</span><span class="p">(</span>
                        <span class="n">field</span><span class="o">=</span><span class="s2">&quot;tags&quot;</span><span class="p">,</span>
                        <span class="n">operation</span><span class="o">=</span><span class="s2">&quot;contains&quot;</span><span class="p">,</span>
                        <span class="n">expected_value</span><span class="o">=</span><span class="s2">&quot;P5&quot;</span><span class="p">,</span>
                    <span class="p">),</span>
                    <span class="n">opsgenie</span><span class="o">.</span><span class="n">IntegrationActionCreateFilterConditionArgs</span><span class="p">(</span>
                        <span class="n">field</span><span class="o">=</span><span class="s2">&quot;message&quot;</span><span class="p">,</span>
                        <span class="n">operation</span><span class="o">=</span><span class="s2">&quot;Starts With&quot;</span><span class="p">,</span>
                        <span class="n">expected_value</span><span class="o">=</span><span class="s2">&quot;[custom]&quot;</span><span class="p">,</span>
                    <span class="p">),</span>
                <span class="p">],</span>
            <span class="p">)],</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="n">closes</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">IntegrationActionCloseArgs</span><span class="p">(</span>
        <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Low priority alerts&quot;</span><span class="p">,</span>
        <span class="n">filters</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">IntegrationActionCloseFilterArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;match-any-condition&quot;</span><span class="p">,</span>
            <span class="n">conditions</span><span class="o">=</span><span class="p">[</span>
                <span class="n">opsgenie</span><span class="o">.</span><span class="n">IntegrationActionCloseFilterConditionArgs</span><span class="p">(</span>
                    <span class="n">field</span><span class="o">=</span><span class="s2">&quot;priority&quot;</span><span class="p">,</span>
                    <span class="n">operation</span><span class="o">=</span><span class="s2">&quot;equals&quot;</span><span class="p">,</span>
                    <span class="n">expected_value</span><span class="o">=</span><span class="s2">&quot;P5&quot;</span><span class="p">,</span>
                <span class="p">),</span>
                <span class="n">opsgenie</span><span class="o">.</span><span class="n">IntegrationActionCloseFilterConditionArgs</span><span class="p">(</span>
                    <span class="n">field</span><span class="o">=</span><span class="s2">&quot;message&quot;</span><span class="p">,</span>
                    <span class="n">operation</span><span class="o">=</span><span class="s2">&quot;contains&quot;</span><span class="p">,</span>
                    <span class="n">expected_value</span><span class="o">=</span><span class="s2">&quot;DEBUG&quot;</span><span class="p">,</span>
                <span class="p">),</span>
            <span class="p">],</span>
        <span class="p">)],</span>
    <span class="p">)],</span>
    <span class="n">acknowledges</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">IntegrationActionAcknowledgeArgs</span><span class="p">(</span>
        <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Auto-ack test alerts&quot;</span><span class="p">,</span>
        <span class="n">filters</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">IntegrationActionAcknowledgeFilterArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;match-all-conditions&quot;</span><span class="p">,</span>
            <span class="n">conditions</span><span class="o">=</span><span class="p">[</span>
                <span class="n">opsgenie</span><span class="o">.</span><span class="n">IntegrationActionAcknowledgeFilterConditionArgs</span><span class="p">(</span>
                    <span class="n">field</span><span class="o">=</span><span class="s2">&quot;message&quot;</span><span class="p">,</span>
                    <span class="n">operation</span><span class="o">=</span><span class="s2">&quot;contains&quot;</span><span class="p">,</span>
                    <span class="n">expected_value</span><span class="o">=</span><span class="s2">&quot;TEST&quot;</span><span class="p">,</span>
                <span class="p">),</span>
                <span class="n">opsgenie</span><span class="o">.</span><span class="n">IntegrationActionAcknowledgeFilterConditionArgs</span><span class="p">(</span>
                    <span class="n">field</span><span class="o">=</span><span class="s2">&quot;priority&quot;</span><span class="p">,</span>
                    <span class="n">operation</span><span class="o">=</span><span class="s2">&quot;equals&quot;</span><span class="p">,</span>
                    <span class="n">expected_value</span><span class="o">=</span><span class="s2">&quot;P5&quot;</span><span class="p">,</span>
                <span class="p">),</span>
            <span class="p">],</span>
        <span class="p">)],</span>
    <span class="p">)],</span>
    <span class="n">add_notes</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">IntegrationActionAddNoteArgs</span><span class="p">(</span>
        <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Add note to all alerts&quot;</span><span class="p">,</span>
        <span class="n">note</span><span class="o">=</span><span class="s2">&quot;Created from test integration&quot;</span><span class="p">,</span>
        <span class="n">filters</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">IntegrationActionAddNoteFilterArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;match-all&quot;</span><span class="p">,</span>
        <span class="p">)],</span>
    <span class="p">)],</span>
    <span class="n">ignores</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">IntegrationActionIgnoreArgs</span><span class="p">(</span>
        <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Ignore alerts with ignore tag&quot;</span><span class="p">,</span>
        <span class="n">filters</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">IntegrationActionIgnoreFilterArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;match-all-conditions&quot;</span><span class="p">,</span>
            <span class="n">conditions</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">IntegrationActionIgnoreFilterConditionArgs</span><span class="p">(</span>
                <span class="n">field</span><span class="o">=</span><span class="s2">&quot;tags&quot;</span><span class="p">,</span>
                <span class="n">operation</span><span class="o">=</span><span class="s2">&quot;contains&quot;</span><span class="p">,</span>
                <span class="n">expected_value</span><span class="o">=</span><span class="s2">&quot;ignore&quot;</span><span class="p">,</span>
            <span class="p">)],</span>
        <span class="p">)],</span>
    <span class="p">)])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>integration_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the parent integration resource to bind to.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_opsgenie.IntegrationAction.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acknowledges</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>IntegrationActionAcknowledgeArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>IntegrationActionAcknowledgeArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>IntegrationActionAcknowledgeArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>IntegrationActionAcknowledgeArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">add_notes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>IntegrationActionAddNoteArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>IntegrationActionAddNoteArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>IntegrationActionAddNoteArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>IntegrationActionAddNoteArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">closes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>IntegrationActionCloseArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>IntegrationActionCloseArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>IntegrationActionCloseArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>IntegrationActionCloseArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creates</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>IntegrationActionCreateArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>IntegrationActionCreateArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>IntegrationActionCreateArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>IntegrationActionCreateArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignores</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>IntegrationActionIgnoreArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>IntegrationActionIgnoreArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>IntegrationActionIgnoreArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>IntegrationActionIgnoreArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_opsgenie.IntegrationAction" title="pulumi_opsgenie.IntegrationAction">IntegrationAction</a><a class="headerlink" href="#pulumi_opsgenie.IntegrationAction.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing IntegrationAction resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>integration_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the parent integration resource to bind to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.IntegrationAction.integration_id">
<em class="property">property </em><code class="sig-name descname">integration_id</code><a class="headerlink" href="#pulumi_opsgenie.IntegrationAction.integration_id" title="Permalink to this definition"></a></dt>
<dd><p>ID of the parent integration resource to bind to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.IntegrationAction.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.IntegrationAction.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.IntegrationAction.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.IntegrationAction.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.Maintenance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">Maintenance</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>MaintenanceRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>MaintenanceRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>MaintenanceRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>MaintenanceRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">times</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>MaintenanceTimeArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>MaintenanceTimeArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>MaintenanceTimeArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>MaintenanceTimeArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.Maintenance" title="Permalink to this definition"></a></dt>
<dd><p>Manages a Maintenance within Opsgenie.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_opsgenie</span> <span class="k">as</span> <span class="nn">opsgenie</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">Maintenance</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;geniemaintenance-</span><span class="si">%s</span><span class="s2">&quot;</span><span class="p">,</span>
    <span class="n">rules</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">MaintenanceRuleArgs</span><span class="p">(</span>
        <span class="n">entities</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">MaintenanceRuleEntityArgs</span><span class="p">(</span>
            <span class="nb">id</span><span class="o">=</span><span class="n">opsgenie_email_integration</span><span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;integration&quot;</span><span class="p">,</span>
        <span class="p">)],</span>
        <span class="n">state</span><span class="o">=</span><span class="s2">&quot;enabled&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">times</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">MaintenanceTimeArgs</span><span class="p">(</span>
        <span class="n">end_date</span><span class="o">=</span><span class="s2">&quot;2019-06-</span><span class="si">%d</span><span class="s2">T17:50:00Z&quot;</span><span class="p">,</span>
        <span class="n">start_date</span><span class="o">=</span><span class="s2">&quot;2019-06-20T17:45:00Z&quot;</span><span class="p">,</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;schedule&quot;</span><span class="p">,</span>
    <span class="p">)])</span>
</pre></div>
</div>
<p>Maintenance policies can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import opsgenie:index/maintenance:Maintenance <span class="nb">test</span> 812be1a1-32c8-4666-a7fb-03ecc385106c<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description for the maintenance.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'MaintenanceRuleArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Rules of maintenance, which takes a list of rule objects and defines the maintenance rules over integrations and policies.</p></li>
<li><p><strong>times</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'MaintenanceTimeArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Time configuration of maintenance. It takes a time object which has type, startDate and endDate fields</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_opsgenie.Maintenance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>MaintenanceRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>MaintenanceRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>MaintenanceRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>MaintenanceRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">times</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>MaintenanceTimeArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>MaintenanceTimeArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>MaintenanceTimeArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>MaintenanceTimeArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_opsgenie.Maintenance" title="pulumi_opsgenie.Maintenance">Maintenance</a><a class="headerlink" href="#pulumi_opsgenie.Maintenance.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Maintenance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description for the maintenance.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'MaintenanceRuleArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Rules of maintenance, which takes a list of rule objects and defines the maintenance rules over integrations and policies.</p></li>
<li><p><strong>times</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'MaintenanceTimeArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Time configuration of maintenance. It takes a time object which has type, startDate and endDate fields</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Maintenance.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_opsgenie.Maintenance.description" title="Permalink to this definition"></a></dt>
<dd><p>Description for the maintenance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Maintenance.rules">
<em class="property">property </em><code class="sig-name descname">rules</code><a class="headerlink" href="#pulumi_opsgenie.Maintenance.rules" title="Permalink to this definition"></a></dt>
<dd><p>Rules of maintenance, which takes a list of rule objects and defines the maintenance rules over integrations and policies.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Maintenance.times">
<em class="property">property </em><code class="sig-name descname">times</code><a class="headerlink" href="#pulumi_opsgenie.Maintenance.times" title="Permalink to this definition"></a></dt>
<dd><p>Time configuration of maintenance. It takes a time object which has type, startDate and endDate fields</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Maintenance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.Maintenance.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.Maintenance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.Maintenance.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.NotificationPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">NotificationPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_close_actions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyAutoCloseActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyAutoCloseActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyAutoCloseActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyAutoCloseActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_restart_actions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyAutoRestartActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyAutoRestartActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyAutoRestartActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyAutoRestartActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">de_duplication_actions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyDeDuplicationActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyDeDuplicationActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyDeDuplicationActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyDeDuplicationActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delay_actions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyDelayActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyDelayActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyDelayActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyDelayActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">suppress</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_restrictions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.NotificationPolicy" title="Permalink to this definition"></a></dt>
<dd><p>Manages a Notification Policy within Opsgenie.</p>
<p>Notification policies can be imported using the <code class="docutils literal notranslate"><span class="pre">team</span> <span class="pre">id</span></code> and <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import opsgenie:index/notificationPolicy:NotificationPolicy <span class="nb">test</span> teamId/Id<span class="sb">`</span>

For this example- Team <span class="nv">Id</span> <span class="o">=</span> <span class="sb">``</span>c827c472-31f2-497b-9ec6-8ec855d7d94c<span class="sb">``</span>
</pre></div>
</div>
<ul class="simple">
<li><p>Notification Policy Id = <code class="docutils literal notranslate"><span class="pre">2d1a78d0-c13e-47d3-af0a-8b6d0cc2b7b1</span></code></p></li>
</ul>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import opsgenie:index/notificationPolicy:NotificationPolicy <span class="nb">test</span> c827c472-31f2-497b-9ec6-8ec855d7d94c/2d1a78d0-c13e-47d3-af0a-8b6d0cc2b7b1<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_close_actions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NotificationPolicyAutoCloseActionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Auto Restart Action of the policy. This is a block, structure is documented below.</p></li>
<li><p><strong>auto_restart_actions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NotificationPolicyAutoRestartActionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Auto Restart Action of the policy. This is a block, structure is documented below.</p></li>
<li><p><strong>de_duplication_actions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NotificationPolicyDeDuplicationActionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Deduplication Action of the policy. This is a block, structure is documented below.</p></li>
<li><p><strong>delay_actions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NotificationPolicyDelayActionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Delay notifications. This is a block, structure is documented below.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If policy should be enabled. Default: true</p></li>
<li><p><strong>filters</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NotificationPolicyFilterArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A notification filter which will be applied. This filter can be empty: filter {} - this means ‘match-all’. This is a block, structure is documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the notification policy</p></li>
<li><p><strong>policy_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the policy. This can be max 512 characters.</p></li>
<li><p><strong>suppress</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Suppress value of the policy. Values are: true, false. Default: false</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of team that this policy belons to.</p></li>
<li><p><strong>time_restrictions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NotificationPolicyTimeRestrictionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Time restrictions specified in this field must be met for this policy to work. This is a block, structure is documented below.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_opsgenie.NotificationPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_close_actions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyAutoCloseActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyAutoCloseActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyAutoCloseActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyAutoCloseActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_restart_actions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyAutoRestartActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyAutoRestartActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyAutoRestartActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyAutoRestartActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">de_duplication_actions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyDeDuplicationActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyDeDuplicationActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyDeDuplicationActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyDeDuplicationActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delay_actions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyDelayActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyDelayActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyDelayActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyDelayActionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">suppress</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_restrictions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationPolicyTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_opsgenie.NotificationPolicy" title="pulumi_opsgenie.NotificationPolicy">NotificationPolicy</a><a class="headerlink" href="#pulumi_opsgenie.NotificationPolicy.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing NotificationPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_close_actions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NotificationPolicyAutoCloseActionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Auto Restart Action of the policy. This is a block, structure is documented below.</p></li>
<li><p><strong>auto_restart_actions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NotificationPolicyAutoRestartActionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Auto Restart Action of the policy. This is a block, structure is documented below.</p></li>
<li><p><strong>de_duplication_actions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NotificationPolicyDeDuplicationActionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Deduplication Action of the policy. This is a block, structure is documented below.</p></li>
<li><p><strong>delay_actions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NotificationPolicyDelayActionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Delay notifications. This is a block, structure is documented below.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If policy should be enabled. Default: true</p></li>
<li><p><strong>filters</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NotificationPolicyFilterArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A notification filter which will be applied. This filter can be empty: filter {} - this means ‘match-all’. This is a block, structure is documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the notification policy</p></li>
<li><p><strong>policy_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the policy. This can be max 512 characters.</p></li>
<li><p><strong>suppress</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Suppress value of the policy. Values are: true, false. Default: false</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of team that this policy belons to.</p></li>
<li><p><strong>time_restrictions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NotificationPolicyTimeRestrictionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Time restrictions specified in this field must be met for this policy to work. This is a block, structure is documented below.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.NotificationPolicy.auto_close_actions">
<em class="property">property </em><code class="sig-name descname">auto_close_actions</code><a class="headerlink" href="#pulumi_opsgenie.NotificationPolicy.auto_close_actions" title="Permalink to this definition"></a></dt>
<dd><p>Auto Restart Action of the policy. This is a block, structure is documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.NotificationPolicy.auto_restart_actions">
<em class="property">property </em><code class="sig-name descname">auto_restart_actions</code><a class="headerlink" href="#pulumi_opsgenie.NotificationPolicy.auto_restart_actions" title="Permalink to this definition"></a></dt>
<dd><p>Auto Restart Action of the policy. This is a block, structure is documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.NotificationPolicy.de_duplication_actions">
<em class="property">property </em><code class="sig-name descname">de_duplication_actions</code><a class="headerlink" href="#pulumi_opsgenie.NotificationPolicy.de_duplication_actions" title="Permalink to this definition"></a></dt>
<dd><p>Deduplication Action of the policy. This is a block, structure is documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.NotificationPolicy.delay_actions">
<em class="property">property </em><code class="sig-name descname">delay_actions</code><a class="headerlink" href="#pulumi_opsgenie.NotificationPolicy.delay_actions" title="Permalink to this definition"></a></dt>
<dd><p>Delay notifications. This is a block, structure is documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.NotificationPolicy.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_opsgenie.NotificationPolicy.enabled" title="Permalink to this definition"></a></dt>
<dd><p>If policy should be enabled. Default: true</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.NotificationPolicy.filters">
<em class="property">property </em><code class="sig-name descname">filters</code><a class="headerlink" href="#pulumi_opsgenie.NotificationPolicy.filters" title="Permalink to this definition"></a></dt>
<dd><p>A notification filter which will be applied. This filter can be empty: filter {} - this means ‘match-all’. This is a block, structure is documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.NotificationPolicy.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_opsgenie.NotificationPolicy.name" title="Permalink to this definition"></a></dt>
<dd><p>Name of the notification policy</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.NotificationPolicy.policy_description">
<em class="property">property </em><code class="sig-name descname">policy_description</code><a class="headerlink" href="#pulumi_opsgenie.NotificationPolicy.policy_description" title="Permalink to this definition"></a></dt>
<dd><p>Description of the policy. This can be max 512 characters.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.NotificationPolicy.suppress">
<em class="property">property </em><code class="sig-name descname">suppress</code><a class="headerlink" href="#pulumi_opsgenie.NotificationPolicy.suppress" title="Permalink to this definition"></a></dt>
<dd><p>Suppress value of the policy. Values are: true, false. Default: false</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.NotificationPolicy.team_id">
<em class="property">property </em><code class="sig-name descname">team_id</code><a class="headerlink" href="#pulumi_opsgenie.NotificationPolicy.team_id" title="Permalink to this definition"></a></dt>
<dd><p>Id of team that this policy belons to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.NotificationPolicy.time_restrictions">
<em class="property">property </em><code class="sig-name descname">time_restrictions</code><a class="headerlink" href="#pulumi_opsgenie.NotificationPolicy.time_restrictions" title="Permalink to this definition"></a></dt>
<dd><p>Time restrictions specified in this field must be met for this policy to work. This is a block, structure is documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.NotificationPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.NotificationPolicy.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.NotificationPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.NotificationPolicy.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.NotificationRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">NotificationRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">criterias</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationRuleCriteriaArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationRuleCriteriaArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationRuleCriteriaArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationRuleCriteriaArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_times</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">order</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repeats</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationRuleRepeatArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationRuleRepeatArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationRuleRepeatArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationRuleRepeatArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schedules</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationRuleScheduleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationRuleScheduleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationRuleScheduleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationRuleScheduleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">steps</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationRuleStepArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationRuleStepArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationRuleStepArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationRuleStepArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_restrictions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationRuleTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationRuleTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationRuleTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationRuleTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.NotificationRule" title="Permalink to this definition"></a></dt>
<dd><p>Manages a Notification Rule within Opsgenie.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_opsgenie</span> <span class="k">as</span> <span class="nn">opsgenie</span>

<span class="n">test_user</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;testUser&quot;</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;Example user&quot;</span><span class="p">,</span>
    <span class="n">full_name</span><span class="o">=</span><span class="s2">&quot;Name Lastname&quot;</span><span class="p">,</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;User&quot;</span><span class="p">)</span>
<span class="n">test_notification_rule</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">NotificationRule</span><span class="p">(</span><span class="s2">&quot;testNotificationRule&quot;</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="n">test_user</span><span class="o">.</span><span class="n">username</span><span class="p">,</span>
    <span class="n">action_type</span><span class="o">=</span><span class="s2">&quot;schedule-end&quot;</span><span class="p">,</span>
    <span class="n">notification_times</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;just-before&quot;</span><span class="p">,</span>
        <span class="s2">&quot;15-minutes-ago&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">steps</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">NotificationRuleStepArgs</span><span class="p">(</span>
        <span class="n">contacts</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">NotificationRuleStepContactArgs</span><span class="p">(</span>
            <span class="n">method</span><span class="o">=</span><span class="s2">&quot;email&quot;</span><span class="p">,</span>
            <span class="n">to</span><span class="o">=</span><span class="s2">&quot;example@user.com&quot;</span><span class="p">,</span>
        <span class="p">)],</span>
    <span class="p">)])</span>
</pre></div>
</div>
<p>Notification policies can be imported using the <code class="docutils literal notranslate"><span class="pre">user</span> <span class="pre">id</span></code> and <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import opsgenie:index/notificationRule:NotificationRule <span class="nb">test</span> userId/Id<span class="sb">`</span>

For this example- User <span class="nv">Id</span> <span class="o">=</span> <span class="sb">``</span>c827c472-31f2-497b-9ec6-8ec855d7d94c<span class="sb">``</span>
</pre></div>
</div>
<ul class="simple">
<li><p>Notification Rule Id = <code class="docutils literal notranslate"><span class="pre">2d1a78d0-c13e-47d3-af0a-8b6d0cc2b7b1</span></code></p></li>
</ul>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import opsgenie:index/notificationRule:NotificationRule <span class="nb">test</span> c827c472-31f2-497b-9ec6-8ec855d7d94c/2d1a78d0-c13e-47d3-af0a-8b6d0cc2b7b1<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the action that notification rule will have. Allowed values: “create-alert”, “acknowledged-alert”, “closed-alert”, “assigned-alert”, “add-note”, “schedule-start”, “schedule-end”, “incoming-call-routing”</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defined if this step is enabled. Default: true</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the notification policy</p></li>
<li><p><strong>notification_times</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of Time Periods that notification for schedule start/end will be sent. Allowed values: “just-before”, “15-minutes-ago”, “1-hour-ago”, “1-day-ago”. If <code class="docutils literal notranslate"><span class="pre">action_type</span></code> is “schedule-start” or “schedule-end” then it is required.</p></li>
<li><p><strong>order</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Order of the condition in conditions list</p></li>
<li><p><strong>steps</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NotificationRuleStepArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Notification rule steps to take (eg. SMS or email message). This is a block, structure is documented below.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username of user to which this notification rule belongs to.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_opsgenie.NotificationRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">criterias</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationRuleCriteriaArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationRuleCriteriaArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationRuleCriteriaArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationRuleCriteriaArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_times</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">order</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repeats</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationRuleRepeatArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationRuleRepeatArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationRuleRepeatArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationRuleRepeatArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schedules</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationRuleScheduleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationRuleScheduleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationRuleScheduleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationRuleScheduleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">steps</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationRuleStepArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationRuleStepArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationRuleStepArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationRuleStepArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_restrictions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationRuleTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationRuleTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>NotificationRuleTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>NotificationRuleTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_opsgenie.NotificationRule" title="pulumi_opsgenie.NotificationRule">NotificationRule</a><a class="headerlink" href="#pulumi_opsgenie.NotificationRule.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing NotificationRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the action that notification rule will have. Allowed values: “create-alert”, “acknowledged-alert”, “closed-alert”, “assigned-alert”, “add-note”, “schedule-start”, “schedule-end”, “incoming-call-routing”</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defined if this step is enabled. Default: true</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the notification policy</p></li>
<li><p><strong>notification_times</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of Time Periods that notification for schedule start/end will be sent. Allowed values: “just-before”, “15-minutes-ago”, “1-hour-ago”, “1-day-ago”. If <code class="docutils literal notranslate"><span class="pre">action_type</span></code> is “schedule-start” or “schedule-end” then it is required.</p></li>
<li><p><strong>order</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Order of the condition in conditions list</p></li>
<li><p><strong>steps</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NotificationRuleStepArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Notification rule steps to take (eg. SMS or email message). This is a block, structure is documented below.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username of user to which this notification rule belongs to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.NotificationRule.action_type">
<em class="property">property </em><code class="sig-name descname">action_type</code><a class="headerlink" href="#pulumi_opsgenie.NotificationRule.action_type" title="Permalink to this definition"></a></dt>
<dd><p>Type of the action that notification rule will have. Allowed values: “create-alert”, “acknowledged-alert”, “closed-alert”, “assigned-alert”, “add-note”, “schedule-start”, “schedule-end”, “incoming-call-routing”</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.NotificationRule.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_opsgenie.NotificationRule.enabled" title="Permalink to this definition"></a></dt>
<dd><p>Defined if this step is enabled. Default: true</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.NotificationRule.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_opsgenie.NotificationRule.name" title="Permalink to this definition"></a></dt>
<dd><p>Name of the notification policy</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.NotificationRule.notification_times">
<em class="property">property </em><code class="sig-name descname">notification_times</code><a class="headerlink" href="#pulumi_opsgenie.NotificationRule.notification_times" title="Permalink to this definition"></a></dt>
<dd><p>List of Time Periods that notification for schedule start/end will be sent. Allowed values: “just-before”, “15-minutes-ago”, “1-hour-ago”, “1-day-ago”. If <code class="docutils literal notranslate"><span class="pre">action_type</span></code> is “schedule-start” or “schedule-end” then it is required.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.NotificationRule.order">
<em class="property">property </em><code class="sig-name descname">order</code><a class="headerlink" href="#pulumi_opsgenie.NotificationRule.order" title="Permalink to this definition"></a></dt>
<dd><p>Order of the condition in conditions list</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.NotificationRule.steps">
<em class="property">property </em><code class="sig-name descname">steps</code><a class="headerlink" href="#pulumi_opsgenie.NotificationRule.steps" title="Permalink to this definition"></a></dt>
<dd><p>Notification rule steps to take (eg. SMS or email message). This is a block, structure is documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.NotificationRule.username">
<em class="property">property </em><code class="sig-name descname">username</code><a class="headerlink" href="#pulumi_opsgenie.NotificationRule.username" title="Permalink to this definition"></a></dt>
<dd><p>Username of user to which this notification rule belongs to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.NotificationRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.NotificationRule.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.NotificationRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.NotificationRule.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.Provider" title="Permalink to this definition"></a></dt>
<dd><p>The provider type for the opsgenie package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_opsgenie.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.Provider.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.Provider.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.Schedule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">Schedule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timezone</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.Schedule" title="Permalink to this definition"></a></dt>
<dd><p>Manages a Schedule within Opsgenie.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_opsgenie</span> <span class="k">as</span> <span class="nn">opsgenie</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">Schedule</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;schedule test&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">owner_team_id</span><span class="o">=</span><span class="n">opsgenie_team</span><span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">timezone</span><span class="o">=</span><span class="s2">&quot;Europe/Rome&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Schedule can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import opsgenie:index/schedule:Schedule <span class="nb">test</span> 812be1a1-32c8-4666-a7fb-03ecc385106c<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of schedule.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable state of schedule</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the schedule.</p></li>
<li><p><strong>owner_team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Owner team id of the schedule.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Timezone of schedule. Please look at <a class="reference external" href="https://docs.opsgenie.com/docs/supported-timezone-ids">Supported Timezone Ids</a> for available timezones - Defaults to “America/New_York”.</p>
</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_opsgenie.Schedule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timezone</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_opsgenie.Schedule" title="pulumi_opsgenie.Schedule">Schedule</a><a class="headerlink" href="#pulumi_opsgenie.Schedule.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Schedule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of schedule.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable/disable state of schedule</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the schedule.</p></li>
<li><p><strong>owner_team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Owner team id of the schedule.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Timezone of schedule. Please look at <a class="reference external" href="https://docs.opsgenie.com/docs/supported-timezone-ids">Supported Timezone Ids</a> for available timezones - Defaults to “America/New_York”.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Schedule.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_opsgenie.Schedule.description" title="Permalink to this definition"></a></dt>
<dd><p>The description of schedule.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Schedule.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_opsgenie.Schedule.enabled" title="Permalink to this definition"></a></dt>
<dd><p>Enable/disable state of schedule</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Schedule.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_opsgenie.Schedule.name" title="Permalink to this definition"></a></dt>
<dd><p>Name of the schedule.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Schedule.owner_team_id">
<em class="property">property </em><code class="sig-name descname">owner_team_id</code><a class="headerlink" href="#pulumi_opsgenie.Schedule.owner_team_id" title="Permalink to this definition"></a></dt>
<dd><p>Owner team id of the schedule.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Schedule.timezone">
<em class="property">property </em><code class="sig-name descname">timezone</code><a class="headerlink" href="#pulumi_opsgenie.Schedule.timezone" title="Permalink to this definition"></a></dt>
<dd><p>Timezone of schedule. Please look at <a class="reference external" href="https://docs.opsgenie.com/docs/supported-timezone-ids">Supported Timezone Ids</a> for available timezones - Defaults to “America/New_York”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Schedule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.Schedule.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.Schedule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.Schedule.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.ScheduleRotation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">ScheduleRotation</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_date</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">length</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">participants</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>ScheduleRotationParticipantArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ScheduleRotationParticipantArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>ScheduleRotationParticipantArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ScheduleRotationParticipantArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schedule_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_date</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_restrictions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>ScheduleRotationTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ScheduleRotationTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>ScheduleRotationTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ScheduleRotationTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.ScheduleRotation" title="Permalink to this definition"></a></dt>
<dd><p>Manages a Schedule Rotation within Opsgenie.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_opsgenie</span> <span class="k">as</span> <span class="nn">opsgenie</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">ScheduleRotation</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">end_date</span><span class="o">=</span><span class="s2">&quot;2019-06-20T17:30:00Z&quot;</span><span class="p">,</span>
    <span class="n">length</span><span class="o">=</span><span class="mi">6</span><span class="p">,</span>
    <span class="n">participants</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">ScheduleRotationParticipantArgs</span><span class="p">(</span>
        <span class="nb">id</span><span class="o">=</span><span class="n">opsgenie_user</span><span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;user&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">schedule_id</span><span class="o">=</span><span class="n">opsgenie_schedule</span><span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">start_date</span><span class="o">=</span><span class="s2">&quot;2019-06-18T17:00:00Z&quot;</span><span class="p">,</span>
    <span class="n">time_restrictions</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">ScheduleRotationTimeRestrictionArgs</span><span class="p">(</span>
        <span class="n">restrictions</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">ScheduleRotationTimeRestrictionRestrictionArgs</span><span class="p">(</span>
            <span class="n">end_hour</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
            <span class="n">end_min</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
            <span class="n">start_hour</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
            <span class="n">start_min</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
        <span class="p">)],</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;time-of-day&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;hourly&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Schedule Rotations can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code> and <code class="docutils literal notranslate"><span class="pre">schedule_id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import opsgenie:index/scheduleRotation:ScheduleRotation * <span class="sb">`</span>opsgenie_schedule_rotation.test schedule_id/id<span class="sb">`</span>

For this example- Schedule <span class="nv">Id</span> <span class="o">=</span> <span class="sb">``</span>c827c472-31f2-497b-9ec6-8ec855d7d94c<span class="sb">``</span>
</pre></div>
</div>
<ul class="simple">
<li><p>Rotation Id = <code class="docutils literal notranslate"><span class="pre">2d1a78d0-c13e-47d3-af0a-8b6d0cc2b7b1</span></code></p></li>
</ul>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import opsgenie:index/scheduleRotation:ScheduleRotation <span class="nb">test</span> c827c472-31f2-497b-9ec6-8ec855d7d94c/2d1a78d0-c13e-47d3-af0a-8b6d0cc2b7b1<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>end_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This parameter takes a date format as (yyyy-MM-dd’T’HH:mm:ssZ) (e.g. 2019-06-11T08:00:00+02:00). Minutes may take 0 or 30 as value. Otherwise they will be converted to nearest 0 or 30 automatically</p></li>
<li><p><strong>length</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Length of the rotation with default value 1.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of rotation.</p></li>
<li><p><strong>participants</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ScheduleRotationParticipantArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – List of escalations, teams, users or the reserved word none which will be used in schedule. Each of them can be used multiple times and will be rotated in the order they given. “user,escalation,team,none”</p></li>
<li><p><strong>schedule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the schedule.</p></li>
<li><p><strong>start_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This parameter takes a date format as (yyyy-MM-dd’T’HH:mm:ssZ) (e.g. 2019-06-11T08:00:00+02:00). Minutes may take 0 or 30 as value. Otherwise they will be converted to nearest 0 or 30 automatically</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of rotation. May be one of daily, weekly and hourly.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_opsgenie.ScheduleRotation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_date</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">length</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">participants</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>ScheduleRotationParticipantArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ScheduleRotationParticipantArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>ScheduleRotationParticipantArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ScheduleRotationParticipantArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schedule_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_date</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_restrictions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>ScheduleRotationTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ScheduleRotationTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>ScheduleRotationTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ScheduleRotationTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_opsgenie.ScheduleRotation" title="pulumi_opsgenie.ScheduleRotation">ScheduleRotation</a><a class="headerlink" href="#pulumi_opsgenie.ScheduleRotation.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing ScheduleRotation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>end_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This parameter takes a date format as (yyyy-MM-dd’T’HH:mm:ssZ) (e.g. 2019-06-11T08:00:00+02:00). Minutes may take 0 or 30 as value. Otherwise they will be converted to nearest 0 or 30 automatically</p></li>
<li><p><strong>length</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Length of the rotation with default value 1.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of rotation.</p></li>
<li><p><strong>participants</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ScheduleRotationParticipantArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – List of escalations, teams, users or the reserved word none which will be used in schedule. Each of them can be used multiple times and will be rotated in the order they given. “user,escalation,team,none”</p></li>
<li><p><strong>schedule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the schedule.</p></li>
<li><p><strong>start_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This parameter takes a date format as (yyyy-MM-dd’T’HH:mm:ssZ) (e.g. 2019-06-11T08:00:00+02:00). Minutes may take 0 or 30 as value. Otherwise they will be converted to nearest 0 or 30 automatically</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of rotation. May be one of daily, weekly and hourly.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.ScheduleRotation.end_date">
<em class="property">property </em><code class="sig-name descname">end_date</code><a class="headerlink" href="#pulumi_opsgenie.ScheduleRotation.end_date" title="Permalink to this definition"></a></dt>
<dd><p>This parameter takes a date format as (yyyy-MM-dd’T’HH:mm:ssZ) (e.g. 2019-06-11T08:00:00+02:00). Minutes may take 0 or 30 as value. Otherwise they will be converted to nearest 0 or 30 automatically</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.ScheduleRotation.length">
<em class="property">property </em><code class="sig-name descname">length</code><a class="headerlink" href="#pulumi_opsgenie.ScheduleRotation.length" title="Permalink to this definition"></a></dt>
<dd><p>Length of the rotation with default value 1.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.ScheduleRotation.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_opsgenie.ScheduleRotation.name" title="Permalink to this definition"></a></dt>
<dd><p>Name of rotation.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.ScheduleRotation.participants">
<em class="property">property </em><code class="sig-name descname">participants</code><a class="headerlink" href="#pulumi_opsgenie.ScheduleRotation.participants" title="Permalink to this definition"></a></dt>
<dd><p>List of escalations, teams, users or the reserved word none which will be used in schedule. Each of them can be used multiple times and will be rotated in the order they given. “user,escalation,team,none”</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.ScheduleRotation.schedule_id">
<em class="property">property </em><code class="sig-name descname">schedule_id</code><a class="headerlink" href="#pulumi_opsgenie.ScheduleRotation.schedule_id" title="Permalink to this definition"></a></dt>
<dd><p>Identifier of the schedule.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.ScheduleRotation.start_date">
<em class="property">property </em><code class="sig-name descname">start_date</code><a class="headerlink" href="#pulumi_opsgenie.ScheduleRotation.start_date" title="Permalink to this definition"></a></dt>
<dd><p>This parameter takes a date format as (yyyy-MM-dd’T’HH:mm:ssZ) (e.g. 2019-06-11T08:00:00+02:00). Minutes may take 0 or 30 as value. Otherwise they will be converted to nearest 0 or 30 automatically</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.ScheduleRotation.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_opsgenie.ScheduleRotation.type" title="Permalink to this definition"></a></dt>
<dd><p>Type of rotation. May be one of daily, weekly and hourly.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.ScheduleRotation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.ScheduleRotation.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.ScheduleRotation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.ScheduleRotation.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.Service">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">Service</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.Service" title="Permalink to this definition"></a></dt>
<dd><p>Manages a Service within Opsgenie.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_opsgenie</span> <span class="k">as</span> <span class="nn">opsgenie</span>

<span class="n">payment</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">Team</span><span class="p">(</span><span class="s2">&quot;payment&quot;</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">&quot;This team deals with all the things&quot;</span><span class="p">)</span>
<span class="n">this</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">Service</span><span class="p">(</span><span class="s2">&quot;this&quot;</span><span class="p">,</span> <span class="n">team_id</span><span class="o">=</span><span class="s2">&quot;$opsgenie_team.payment.id&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Teams can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import opsgenie:index/service:Service this 812be1a1-32c8-4666-a7fb-03ecc385106c<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description field of the service that is generally used to provide a detailed information about the service.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the service. This field must not be longer than 100 characters.</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Team id of the service. This field must not be longer than 512 characters.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_opsgenie.Service.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_opsgenie.Service" title="pulumi_opsgenie.Service">Service</a><a class="headerlink" href="#pulumi_opsgenie.Service.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Service resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description field of the service that is generally used to provide a detailed information about the service.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the service. This field must not be longer than 100 characters.</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Team id of the service. This field must not be longer than 512 characters.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Service.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_opsgenie.Service.description" title="Permalink to this definition"></a></dt>
<dd><p>Description field of the service that is generally used to provide a detailed information about the service.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Service.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_opsgenie.Service.name" title="Permalink to this definition"></a></dt>
<dd><p>Name of the service. This field must not be longer than 100 characters.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Service.team_id">
<em class="property">property </em><code class="sig-name descname">team_id</code><a class="headerlink" href="#pulumi_opsgenie.Service.team_id" title="Permalink to this definition"></a></dt>
<dd><p>Team id of the service. This field must not be longer than 512 characters.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Service.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.Service.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.Service.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.Service.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.ServiceIncidentRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">ServiceIncidentRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">incident_rules</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>ServiceIncidentRuleIncidentRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ServiceIncidentRuleIncidentRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>ServiceIncidentRuleIncidentRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ServiceIncidentRuleIncidentRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.ServiceIncidentRule" title="Permalink to this definition"></a></dt>
<dd><p>Manages a Service Incident Rule within Opsgenie.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_opsgenie</span> <span class="k">as</span> <span class="nn">opsgenie</span>

<span class="n">test_team</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">Team</span><span class="p">(</span><span class="s2">&quot;testTeam&quot;</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">&quot;This team deals with all the things&quot;</span><span class="p">)</span>
<span class="n">test_service</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">Service</span><span class="p">(</span><span class="s2">&quot;testService&quot;</span><span class="p">,</span> <span class="n">team_id</span><span class="o">=</span><span class="n">test_team</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">test_service_incident_rule</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">ServiceIncidentRule</span><span class="p">(</span><span class="s2">&quot;testServiceIncidentRule&quot;</span><span class="p">,</span>
    <span class="n">service_id</span><span class="o">=</span><span class="n">test_service</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">incident_rules</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">ServiceIncidentRuleIncidentRuleArgs</span><span class="p">(</span>
        <span class="n">condition_match_type</span><span class="o">=</span><span class="s2">&quot;match-any-condition&quot;</span><span class="p">,</span>
        <span class="n">conditions</span><span class="o">=</span><span class="p">[</span>
            <span class="n">opsgenie</span><span class="o">.</span><span class="n">ServiceIncidentRuleIncidentRuleConditionArgs</span><span class="p">(</span>
                <span class="n">field</span><span class="o">=</span><span class="s2">&quot;message&quot;</span><span class="p">,</span>
                <span class="n">not_</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
                <span class="n">operation</span><span class="o">=</span><span class="s2">&quot;contains&quot;</span><span class="p">,</span>
                <span class="n">expected_value</span><span class="o">=</span><span class="s2">&quot;expected1&quot;</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">opsgenie</span><span class="o">.</span><span class="n">ServiceIncidentRuleIncidentRuleConditionArgs</span><span class="p">(</span>
                <span class="n">field</span><span class="o">=</span><span class="s2">&quot;message&quot;</span><span class="p">,</span>
                <span class="n">not_</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
                <span class="n">operation</span><span class="o">=</span><span class="s2">&quot;contains&quot;</span><span class="p">,</span>
                <span class="n">expected_value</span><span class="o">=</span><span class="s2">&quot;expected2&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">],</span>
        <span class="n">incident_properties</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">ServiceIncidentRuleIncidentRuleIncidentPropertyArgs</span><span class="p">(</span>
            <span class="n">message</span><span class="o">=</span><span class="s2">&quot;This is a test message&quot;</span><span class="p">,</span>
            <span class="n">priority</span><span class="o">=</span><span class="s2">&quot;P3&quot;</span><span class="p">,</span>
            <span class="n">stakeholder_properties</span><span class="o">=</span><span class="p">[{</span>
                <span class="s2">&quot;message&quot;</span><span class="p">:</span> <span class="s2">&quot;Message for stakeholders&quot;</span><span class="p">,</span>
                <span class="s2">&quot;enable&quot;</span><span class="p">:</span> <span class="s2">&quot;true&quot;</span><span class="p">,</span>
            <span class="p">}],</span>
        <span class="p">)],</span>
    <span class="p">)])</span>
</pre></div>
</div>
<p>Service Incident Rule can be imported using the <code class="docutils literal notranslate"><span class="pre">service_id/service_incident_rule_id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import opsgenie:index/serviceIncidentRule:ServiceIncidentRule this 812be1a1-32c8-4666-a7fb-03ecc385106c/b84ed86f-6ce3-4388-91ac-7638ac0a8052<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>incident_rules</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceIncidentRuleIncidentRuleArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – This is the rule configuration for this incident rule. This is a block, structure is documented below.</p></li>
<li><p><strong>service_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the service associated</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_opsgenie.ServiceIncidentRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">incident_rules</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>ServiceIncidentRuleIncidentRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ServiceIncidentRuleIncidentRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>ServiceIncidentRuleIncidentRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ServiceIncidentRuleIncidentRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_opsgenie.ServiceIncidentRule" title="pulumi_opsgenie.ServiceIncidentRule">ServiceIncidentRule</a><a class="headerlink" href="#pulumi_opsgenie.ServiceIncidentRule.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing ServiceIncidentRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>incident_rules</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceIncidentRuleIncidentRuleArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – This is the rule configuration for this incident rule. This is a block, structure is documented below.</p></li>
<li><p><strong>service_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the service associated</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.ServiceIncidentRule.incident_rules">
<em class="property">property </em><code class="sig-name descname">incident_rules</code><a class="headerlink" href="#pulumi_opsgenie.ServiceIncidentRule.incident_rules" title="Permalink to this definition"></a></dt>
<dd><p>This is the rule configuration for this incident rule. This is a block, structure is documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.ServiceIncidentRule.service_id">
<em class="property">property </em><code class="sig-name descname">service_id</code><a class="headerlink" href="#pulumi_opsgenie.ServiceIncidentRule.service_id" title="Permalink to this definition"></a></dt>
<dd><p>ID of the service associated</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.ServiceIncidentRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.ServiceIncidentRule.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.ServiceIncidentRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.ServiceIncidentRule.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.Team">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">Team</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_default_resources</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_members</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>TeamMemberArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TeamMemberArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>TeamMemberArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TeamMemberArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.Team" title="Permalink to this definition"></a></dt>
<dd><p>Manages a Team within Opsgenie.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_opsgenie</span> <span class="k">as</span> <span class="nn">opsgenie</span>

<span class="n">first</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;first&quot;</span><span class="p">,</span>
    <span class="n">full_name</span><span class="o">=</span><span class="s2">&quot;name &quot;</span><span class="p">,</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;User&quot;</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;user@domain.com&quot;</span><span class="p">)</span>
<span class="n">second</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;second&quot;</span><span class="p">,</span>
    <span class="n">full_name</span><span class="o">=</span><span class="s2">&quot;name &quot;</span><span class="p">,</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;User&quot;</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;test@domain.com&quot;</span><span class="p">)</span>
<span class="n">test</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">Team</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;This team deals with all the things&quot;</span><span class="p">,</span>
    <span class="n">members</span><span class="o">=</span><span class="p">[</span>
        <span class="n">opsgenie</span><span class="o">.</span><span class="n">TeamMemberArgs</span><span class="p">(</span>
            <span class="nb">id</span><span class="o">=</span><span class="n">first</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
            <span class="n">role</span><span class="o">=</span><span class="s2">&quot;admin&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">opsgenie</span><span class="o">.</span><span class="n">TeamMemberArgs</span><span class="p">(</span>
            <span class="nb">id</span><span class="o">=</span><span class="n">second</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
            <span class="n">role</span><span class="o">=</span><span class="s2">&quot;user&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">])</span>
<span class="n">self_service</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">Team</span><span class="p">(</span><span class="s2">&quot;self-service&quot;</span><span class="p">,</span>
    <span class="n">delete_default_resources</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Membership in this team is managed via OpsGenie web UI only&quot;</span><span class="p">,</span>
    <span class="n">ignore_members</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>
</div>
<p>Teams can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import opsgenie:index/team:Team team1 812be1a1-32c8-4666-a7fb-03ecc385106c<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>delete_default_resources</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to true to remove default escalation and schedule for newly created team. <strong>Be careful its also changes that team routing rule to None. That means you have to define routing rule as well</strong></p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for this team.</p></li>
<li><p><strong>ignore_members</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to true to ignore any configured member blocks and any team member added/updated/removed via OpsGenie web UI. Use this option e.g. to maintain membership via web UI only and use it only for new teams. Changing the value for existing teams might lead to strange behaviour. Defaults to false.</p></li>
<li><p><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TeamMemberArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A Member block as documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name associated with this team. Opsgenie defines that this must not be longer than 100 characters.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_opsgenie.Team.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_default_resources</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_members</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>TeamMemberArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TeamMemberArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>TeamMemberArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TeamMemberArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_opsgenie.Team" title="pulumi_opsgenie.Team">Team</a><a class="headerlink" href="#pulumi_opsgenie.Team.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Team resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>delete_default_resources</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to true to remove default escalation and schedule for newly created team. <strong>Be careful its also changes that team routing rule to None. That means you have to define routing rule as well</strong></p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for this team.</p></li>
<li><p><strong>ignore_members</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to true to ignore any configured member blocks and any team member added/updated/removed via OpsGenie web UI. Use this option e.g. to maintain membership via web UI only and use it only for new teams. Changing the value for existing teams might lead to strange behaviour. Defaults to false.</p></li>
<li><p><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TeamMemberArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A Member block as documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name associated with this team. Opsgenie defines that this must not be longer than 100 characters.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Team.delete_default_resources">
<em class="property">property </em><code class="sig-name descname">delete_default_resources</code><a class="headerlink" href="#pulumi_opsgenie.Team.delete_default_resources" title="Permalink to this definition"></a></dt>
<dd><p>Set to true to remove default escalation and schedule for newly created team. <strong>Be careful its also changes that team routing rule to None. That means you have to define routing rule as well</strong></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Team.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_opsgenie.Team.description" title="Permalink to this definition"></a></dt>
<dd><p>A description for this team.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Team.ignore_members">
<em class="property">property </em><code class="sig-name descname">ignore_members</code><a class="headerlink" href="#pulumi_opsgenie.Team.ignore_members" title="Permalink to this definition"></a></dt>
<dd><p>Set to true to ignore any configured member blocks and any team member added/updated/removed via OpsGenie web UI. Use this option e.g. to maintain membership via web UI only and use it only for new teams. Changing the value for existing teams might lead to strange behaviour. Defaults to false.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Team.members">
<em class="property">property </em><code class="sig-name descname">members</code><a class="headerlink" href="#pulumi_opsgenie.Team.members" title="Permalink to this definition"></a></dt>
<dd><p>A Member block as documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Team.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_opsgenie.Team.name" title="Permalink to this definition"></a></dt>
<dd><p>The name associated with this team. Opsgenie defines that this must not be longer than 100 characters.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.Team.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.Team.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.Team.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.Team.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.TeamRoutingRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">TeamRoutingRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">criterias</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>TeamRoutingRuleCriteriaArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TeamRoutingRuleCriteriaArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>TeamRoutingRuleCriteriaArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TeamRoutingRuleCriteriaArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifies</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>TeamRoutingRuleNotifyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TeamRoutingRuleNotifyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>TeamRoutingRuleNotifyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TeamRoutingRuleNotifyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">order</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_restrictions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>TeamRoutingRuleTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TeamRoutingRuleTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>TeamRoutingRuleTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TeamRoutingRuleTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timezone</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.TeamRoutingRule" title="Permalink to this definition"></a></dt>
<dd><p>Manages a Team Routing Rule within Opsgenie.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_opsgenie</span> <span class="k">as</span> <span class="nn">opsgenie</span>

<span class="n">test_schedule</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">Schedule</span><span class="p">(</span><span class="s2">&quot;testSchedule&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;schedule test&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">timezone</span><span class="o">=</span><span class="s2">&quot;Europe/Rome&quot;</span><span class="p">)</span>
<span class="n">test_team</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">Team</span><span class="p">(</span><span class="s2">&quot;testTeam&quot;</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">&quot;This team deals with all the things&quot;</span><span class="p">)</span>
<span class="n">test_team_routing_rule</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">TeamRoutingRule</span><span class="p">(</span><span class="s2">&quot;testTeamRoutingRule&quot;</span><span class="p">,</span>
    <span class="n">criterias</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">TeamRoutingRuleCriteriaArgs</span><span class="p">(</span>
        <span class="n">conditions</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">TeamRoutingRuleCriteriaConditionArgs</span><span class="p">(</span>
            <span class="n">expected_value</span><span class="o">=</span><span class="s2">&quot;expected1&quot;</span><span class="p">,</span>
            <span class="n">field</span><span class="o">=</span><span class="s2">&quot;message&quot;</span><span class="p">,</span>
            <span class="n">not_</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="n">operation</span><span class="o">=</span><span class="s2">&quot;contains&quot;</span><span class="p">,</span>
        <span class="p">)],</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;match-any-condition&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">notifies</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">TeamRoutingRuleNotifyArgs</span><span class="p">(</span>
        <span class="n">name</span><span class="o">=</span><span class="n">test_schedule</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;schedule&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">order</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="n">team_id</span><span class="o">=</span><span class="n">test_team</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">time_restrictions</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">TeamRoutingRuleTimeRestrictionArgs</span><span class="p">(</span>
        <span class="n">restrictions</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">TeamRoutingRuleTimeRestrictionRestrictionArgs</span><span class="p">(</span>
            <span class="n">end_day</span><span class="o">=</span><span class="s2">&quot;tuesday&quot;</span><span class="p">,</span>
            <span class="n">end_hour</span><span class="o">=</span><span class="mi">18</span><span class="p">,</span>
            <span class="n">end_min</span><span class="o">=</span><span class="mi">30</span><span class="p">,</span>
            <span class="n">start_day</span><span class="o">=</span><span class="s2">&quot;monday&quot;</span><span class="p">,</span>
            <span class="n">start_hour</span><span class="o">=</span><span class="mi">8</span><span class="p">,</span>
            <span class="n">start_min</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
        <span class="p">)],</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;weekday-and-time-of-day&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">timezone</span><span class="o">=</span><span class="s2">&quot;America/Los_Angeles&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Team Routing Rules can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import opsgenie:index/teamRoutingRule:TeamRoutingRule ruletest teamId/routingRuleId<span class="sb">`</span>

For this example- Team <span class="nv">Id</span> <span class="o">=</span> <span class="sb">``</span>c827c472-31f2-497b-9ec6-8ec855d7d94c<span class="sb">``</span>
</pre></div>
</div>
<ul class="simple">
<li><p>Routing Rule Id = <code class="docutils literal notranslate"><span class="pre">2d1a78d0-c13e-47d3-af0a-8b6d0cc2b7b1</span></code></p></li>
</ul>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import opsgenie:index/teamRoutingRule:TeamRoutingRule ruletest c827c472-31f2-497b-9ec6-8ec855d7d94c/2d1a78d0-c13e-47d3-af0a-8b6d0cc2b7b1<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>criterias</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TeamRoutingRuleCriteriaArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – You can refer Criteria for detailed information about criteria and its fields</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the team routing rule</p></li>
<li><p><strong>notifies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TeamRoutingRuleNotifyArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Target entity of schedule, escalation, or the reserved word none which will be notified in routing rule. The possible values for notify type : schedule, escalation, none</p></li>
<li><p><strong>order</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The order of the team routing rule within the rules. order value is actually the index of the team routing rule whose minimum value is 0 and whose maximum value is n-1 (number of team routing rules is n)</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of the team owning the routing rule</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Timezone of team routing rule. If timezone field is not given, account timezone is used as default.You can refer to Supported Locale IDs for available timezones</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_opsgenie.TeamRoutingRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">criterias</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>TeamRoutingRuleCriteriaArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TeamRoutingRuleCriteriaArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>TeamRoutingRuleCriteriaArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TeamRoutingRuleCriteriaArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifies</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>TeamRoutingRuleNotifyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TeamRoutingRuleNotifyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>TeamRoutingRuleNotifyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TeamRoutingRuleNotifyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">order</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_restrictions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>TeamRoutingRuleTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TeamRoutingRuleTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>TeamRoutingRuleTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TeamRoutingRuleTimeRestrictionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timezone</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_opsgenie.TeamRoutingRule" title="pulumi_opsgenie.TeamRoutingRule">TeamRoutingRule</a><a class="headerlink" href="#pulumi_opsgenie.TeamRoutingRule.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing TeamRoutingRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>criterias</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TeamRoutingRuleCriteriaArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – You can refer Criteria for detailed information about criteria and its fields</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the team routing rule</p></li>
<li><p><strong>notifies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TeamRoutingRuleNotifyArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Target entity of schedule, escalation, or the reserved word none which will be notified in routing rule. The possible values for notify type : schedule, escalation, none</p></li>
<li><p><strong>order</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The order of the team routing rule within the rules. order value is actually the index of the team routing rule whose minimum value is 0 and whose maximum value is n-1 (number of team routing rules is n)</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of the team owning the routing rule</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Timezone of team routing rule. If timezone field is not given, account timezone is used as default.You can refer to Supported Locale IDs for available timezones</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.TeamRoutingRule.criterias">
<em class="property">property </em><code class="sig-name descname">criterias</code><a class="headerlink" href="#pulumi_opsgenie.TeamRoutingRule.criterias" title="Permalink to this definition"></a></dt>
<dd><p>You can refer Criteria for detailed information about criteria and its fields</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.TeamRoutingRule.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_opsgenie.TeamRoutingRule.name" title="Permalink to this definition"></a></dt>
<dd><p>Name of the team routing rule</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.TeamRoutingRule.notifies">
<em class="property">property </em><code class="sig-name descname">notifies</code><a class="headerlink" href="#pulumi_opsgenie.TeamRoutingRule.notifies" title="Permalink to this definition"></a></dt>
<dd><p>Target entity of schedule, escalation, or the reserved word none which will be notified in routing rule. The possible values for notify type : schedule, escalation, none</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.TeamRoutingRule.order">
<em class="property">property </em><code class="sig-name descname">order</code><a class="headerlink" href="#pulumi_opsgenie.TeamRoutingRule.order" title="Permalink to this definition"></a></dt>
<dd><p>The order of the team routing rule within the rules. order value is actually the index of the team routing rule whose minimum value is 0 and whose maximum value is n-1 (number of team routing rules is n)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.TeamRoutingRule.team_id">
<em class="property">property </em><code class="sig-name descname">team_id</code><a class="headerlink" href="#pulumi_opsgenie.TeamRoutingRule.team_id" title="Permalink to this definition"></a></dt>
<dd><p>Id of the team owning the routing rule</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.TeamRoutingRule.timezone">
<em class="property">property </em><code class="sig-name descname">timezone</code><a class="headerlink" href="#pulumi_opsgenie.TeamRoutingRule.timezone" title="Permalink to this definition"></a></dt>
<dd><p>Timezone of team routing rule. If timezone field is not given, account timezone is used as default.You can refer to Supported Locale IDs for available timezones</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.TeamRoutingRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.TeamRoutingRule.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.TeamRoutingRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.TeamRoutingRule.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.User">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">full_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locale</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skype_username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timezone</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_addresses</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>UserUserAddressArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>UserUserAddressArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>UserUserAddressArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>UserUserAddressArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_details</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.User" title="Permalink to this definition"></a></dt>
<dd><p>Manages a User within Opsgenie.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_opsgenie</span> <span class="k">as</span> <span class="nn">opsgenie</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">full_name</span><span class="o">=</span><span class="s2">&quot;Test User&quot;</span><span class="p">,</span>
    <span class="n">locale</span><span class="o">=</span><span class="s2">&quot;en_US&quot;</span><span class="p">,</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;User&quot;</span><span class="p">,</span>
    <span class="n">skype_username</span><span class="o">=</span><span class="s2">&quot;skypename&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;sre&quot;</span><span class="p">,</span>
        <span class="s2">&quot;opsgenie&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">timezone</span><span class="o">=</span><span class="s2">&quot;America/New_York&quot;</span><span class="p">,</span>
    <span class="n">user_addresses</span><span class="o">=</span><span class="p">[</span><span class="n">opsgenie</span><span class="o">.</span><span class="n">UserUserAddressArgs</span><span class="p">(</span>
        <span class="n">city</span><span class="o">=</span><span class="s2">&quot;City&quot;</span><span class="p">,</span>
        <span class="n">country</span><span class="o">=</span><span class="s2">&quot;Country&quot;</span><span class="p">,</span>
        <span class="n">line</span><span class="o">=</span><span class="s2">&quot;Line&quot;</span><span class="p">,</span>
        <span class="n">state</span><span class="o">=</span><span class="s2">&quot;State&quot;</span><span class="p">,</span>
        <span class="n">zipcode</span><span class="o">=</span><span class="s2">&quot;998877&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">user_details</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;key1&quot;</span><span class="p">:</span> <span class="s2">&quot;val1,val2&quot;</span><span class="p">,</span>
        <span class="s2">&quot;key2&quot;</span><span class="p">:</span> <span class="s2">&quot;val3,val4&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;user@domain.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Users can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import opsgenie:index/user:User user da4faf16-5546-41e4-8330-4d0002b74048s<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>full_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Full Name of the User.</p></li>
<li><p><strong>locale</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Location information for the user. Please look at <a class="reference external" href="https://docs.opsgenie.com/docs/supported-locales">Supported Locale Ids</a> for available locales.</p>
</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Role assigned to the User. Either a built-in such as ‘Admin’ or ‘User’ - or the name of a custom role.</p></li>
<li><p><strong>skype_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Skype username of the user.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags to be associated with the user.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Timezone information of the user. Please look at <a class="reference external" href="https://docs.opsgenie.com/docs/supported-timezone-ids">Supported Timezone Ids</a> for available timezones.</p>
</p></li>
<li><p><strong>user_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'UserUserAddressArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Address of the user.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>user_details</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Details about the user in form of key and list. of values.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address associated with this user. Opsgenie defines that this must not be longer than 100 characters and must contain lowercase characters only.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_opsgenie.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">full_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locale</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skype_username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timezone</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_addresses</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>UserUserAddressArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>UserUserAddressArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>UserUserAddressArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>UserUserAddressArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_details</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_opsgenie.User" title="pulumi_opsgenie.User">User</a><a class="headerlink" href="#pulumi_opsgenie.User.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>full_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Full Name of the User.</p></li>
<li><p><strong>locale</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Location information for the user. Please look at <a class="reference external" href="https://docs.opsgenie.com/docs/supported-locales">Supported Locale Ids</a> for available locales.</p>
</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Role assigned to the User. Either a built-in such as ‘Admin’ or ‘User’ - or the name of a custom role.</p></li>
<li><p><strong>skype_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Skype username of the user.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags to be associated with the user.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Timezone information of the user. Please look at <a class="reference external" href="https://docs.opsgenie.com/docs/supported-timezone-ids">Supported Timezone Ids</a> for available timezones.</p>
</p></li>
<li><p><strong>user_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'UserUserAddressArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Address of the user.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>user_details</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Details about the user in form of key and list. of values.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address associated with this user. Opsgenie defines that this must not be longer than 100 characters and must contain lowercase characters only.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.User.full_name">
<em class="property">property </em><code class="sig-name descname">full_name</code><a class="headerlink" href="#pulumi_opsgenie.User.full_name" title="Permalink to this definition"></a></dt>
<dd><p>The Full Name of the User.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.User.locale">
<em class="property">property </em><code class="sig-name descname">locale</code><a class="headerlink" href="#pulumi_opsgenie.User.locale" title="Permalink to this definition"></a></dt>
<dd><p>Location information for the user. Please look at <a class="reference external" href="https://docs.opsgenie.com/docs/supported-locales">Supported Locale Ids</a> for available locales.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.User.role">
<em class="property">property </em><code class="sig-name descname">role</code><a class="headerlink" href="#pulumi_opsgenie.User.role" title="Permalink to this definition"></a></dt>
<dd><p>The Role assigned to the User. Either a built-in such as ‘Admin’ or ‘User’ - or the name of a custom role.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.User.skype_username">
<em class="property">property </em><code class="sig-name descname">skype_username</code><a class="headerlink" href="#pulumi_opsgenie.User.skype_username" title="Permalink to this definition"></a></dt>
<dd><p>Skype username of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.User.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_opsgenie.User.tags" title="Permalink to this definition"></a></dt>
<dd><p>A list of tags to be associated with the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.User.timezone">
<em class="property">property </em><code class="sig-name descname">timezone</code><a class="headerlink" href="#pulumi_opsgenie.User.timezone" title="Permalink to this definition"></a></dt>
<dd><p>Timezone information of the user. Please look at <a class="reference external" href="https://docs.opsgenie.com/docs/supported-timezone-ids">Supported Timezone Ids</a> for available timezones.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.User.user_addresses">
<em class="property">property </em><code class="sig-name descname">user_addresses</code><a class="headerlink" href="#pulumi_opsgenie.User.user_addresses" title="Permalink to this definition"></a></dt>
<dd><p>Address of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.User.user_details">
<em class="property">property </em><code class="sig-name descname">user_details</code><a class="headerlink" href="#pulumi_opsgenie.User.user_details" title="Permalink to this definition"></a></dt>
<dd><p>Details about the user in form of key and list. of values.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.User.username">
<em class="property">property </em><code class="sig-name descname">username</code><a class="headerlink" href="#pulumi_opsgenie.User.username" title="Permalink to this definition"></a></dt>
<dd><p>The email address associated with this user. Opsgenie defines that this must not be longer than 100 characters and must contain lowercase characters only.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.User.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.User.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.User.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.UserContact">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">UserContact</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">method</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">to</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.UserContact" title="Permalink to this definition"></a></dt>
<dd><p>Manages a User Contact.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_opsgenie</span> <span class="k">as</span> <span class="nn">opsgenie</span>

<span class="n">sms</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">UserContact</span><span class="p">(</span><span class="s2">&quot;sms&quot;</span><span class="p">,</span>
    <span class="n">method</span><span class="o">=</span><span class="s2">&quot;sms&quot;</span><span class="p">,</span>
    <span class="n">to</span><span class="o">=</span><span class="s2">&quot;39-123&quot;</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="n">opsgenie_user</span><span class="p">[</span><span class="s2">&quot;exampleuser&quot;</span><span class="p">][</span><span class="s2">&quot;username&quot;</span><span class="p">])</span>
<span class="n">email</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">UserContact</span><span class="p">(</span><span class="s2">&quot;email&quot;</span><span class="p">,</span>
    <span class="n">method</span><span class="o">=</span><span class="s2">&quot;email&quot;</span><span class="p">,</span>
    <span class="n">to</span><span class="o">=</span><span class="s2">&quot;fahri@opsgenie.com&quot;</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="n">opsgenie_user</span><span class="p">[</span><span class="s2">&quot;exampleuser&quot;</span><span class="p">][</span><span class="s2">&quot;username&quot;</span><span class="p">])</span>
<span class="n">voice</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">UserContact</span><span class="p">(</span><span class="s2">&quot;voice&quot;</span><span class="p">,</span>
    <span class="n">method</span><span class="o">=</span><span class="s2">&quot;voice&quot;</span><span class="p">,</span>
    <span class="n">to</span><span class="o">=</span><span class="s2">&quot;39-123&quot;</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="n">opsgenie_user</span><span class="p">[</span><span class="s2">&quot;exampleuser&quot;</span><span class="p">][</span><span class="s2">&quot;username&quot;</span><span class="p">])</span>
</pre></div>
</div>
<p>Users can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import opsgenie:index/userContact:UserContact testcontact username/contactId<span class="sb">`</span>

For this example- <span class="nv">Username</span> <span class="o">=</span> <span class="sb">``</span>genie@awesometeam.com<span class="sb">``</span>
</pre></div>
</div>
<ul class="simple">
<li><p>Contact Id = <code class="docutils literal notranslate"><span class="pre">2d1a78d0-c13e-47d3-af0a-8b6d0cc2b7b1</span></code></p></li>
</ul>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import opsgenie:index/userContact:UserContact testcontact genie@awesometeam.com/2d1a78d0-c13e-47d3-af0a-8b6d0cc2b7b1<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable contact of the user in OpsGenie. Default value is true.</p></li>
<li><p><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This parameter is the contact method of user and should be one of email, sms or voice. Please note that adding mobile is not supported from API.</p></li>
<li><p><strong>to</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – to field is the address of given method.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username for contact.(reference)</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_opsgenie.UserContact.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">method</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">to</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_opsgenie.UserContact" title="pulumi_opsgenie.UserContact">UserContact</a><a class="headerlink" href="#pulumi_opsgenie.UserContact.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing UserContact resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable contact of the user in OpsGenie. Default value is true.</p></li>
<li><p><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This parameter is the contact method of user and should be one of email, sms or voice. Please note that adding mobile is not supported from API.</p></li>
<li><p><strong>to</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – to field is the address of given method.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username for contact.(reference)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.UserContact.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_opsgenie.UserContact.enabled" title="Permalink to this definition"></a></dt>
<dd><p>Enable contact of the user in OpsGenie. Default value is true.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.UserContact.method">
<em class="property">property </em><code class="sig-name descname">method</code><a class="headerlink" href="#pulumi_opsgenie.UserContact.method" title="Permalink to this definition"></a></dt>
<dd><p>This parameter is the contact method of user and should be one of email, sms or voice. Please note that adding mobile is not supported from API.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.UserContact.to">
<em class="property">property </em><code class="sig-name descname">to</code><a class="headerlink" href="#pulumi_opsgenie.UserContact.to" title="Permalink to this definition"></a></dt>
<dd><p>to field is the address of given method.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.UserContact.username">
<em class="property">property </em><code class="sig-name descname">username</code><a class="headerlink" href="#pulumi_opsgenie.UserContact.username" title="Permalink to this definition"></a></dt>
<dd><p>The username for contact.(reference)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_opsgenie.UserContact.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.UserContact.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.UserContact.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_opsgenie.UserContact.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_opsgenie.get_escalation">
<code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">get_escalation</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repeats</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>pulumi_opsgenie._inputs.GetEscalationRepeatArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>pulumi_opsgenie._inputs.GetEscalationRuleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_opsgenie.get_escalation.AwaitableGetEscalationResult<a class="headerlink" href="#pulumi_opsgenie.get_escalation" title="Permalink to this definition"></a></dt>
<dd><p>Manages an Escalation within Opsgenie.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_opsgenie</span> <span class="k">as</span> <span class="nn">opsgenie</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">get_escalation</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;existing-escalation&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description</strong> (<em>str</em>) – Escalation Description</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Name of the escalation.</p></li>
<li><p><strong>owner_team_id</strong> (<em>str</em>) – If owner team exist the id of the team is exported</p></li>
<li><p><strong>repeats</strong> (<em>Sequence</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GetEscalationRepeatArgs'</em><em>]</em><em>]</em>) – Escalation repeat preferences</p></li>
<li><p><strong>rules</strong> (<em>Sequence</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GetEscalationRuleArgs'</em><em>]</em><em>]</em>) – Escalation rules</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_opsgenie.get_heartbeat">
<code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">get_heartbeat</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">alert_message</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_priority</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_tags</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interval</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interval_unit</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_opsgenie.get_heartbeat.AwaitableGetHeartbeatResult<a class="headerlink" href="#pulumi_opsgenie.get_heartbeat" title="Permalink to this definition"></a></dt>
<dd><p>Manages existing heartbeat within Opsgenie.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_opsgenie</span> <span class="k">as</span> <span class="nn">opsgenie</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">get_heartbeat</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;genieheartbeat-existing&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>alert_message</strong> (<em>str</em>) – Specifies the alert message for heartbeat expiration alert. If this is not provided, default alert message is “HeartbeatName is expired”.</p></li>
<li><p><strong>alert_priority</strong> (<em>str</em>) – Specifies the alert priority for heartbeat expiration alert. If this is not provided, default priority is P3.</p></li>
<li><p><strong>alert_tags</strong> (<em>Sequence</em><em>[</em><em>str</em><em>]</em>) – Specifies the alert tags for heartbeat expiration alert.</p></li>
<li><p><strong>description</strong> (<em>str</em>) – An optional description of the heartbeat</p></li>
<li><p><strong>enabled</strong> (<em>bool</em>) – Enable/disable heartbeat monitoring.</p></li>
<li><p><strong>interval</strong> (<em>int</em>) – Specifies how often a heartbeat message should be expected.</p></li>
<li><p><strong>interval_unit</strong> (<em>str</em>) – Interval specified as minutes, hours or days.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Name of the heartbeat</p></li>
<li><p><strong>owner_team_id</strong> (<em>str</em>) – Owner team of the heartbeat.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_opsgenie.get_schedule">
<code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">get_schedule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timezone</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_opsgenie.get_schedule.AwaitableGetScheduleResult<a class="headerlink" href="#pulumi_opsgenie.get_schedule" title="Permalink to this definition"></a></dt>
<dd><p>Manages a Schedule within Opsgenie.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_opsgenie</span> <span class="k">as</span> <span class="nn">opsgenie</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">get_schedule</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;sre-team schedule&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description</strong> (<em>str</em>) – <p>Timezone of schedule. Please look at <a class="reference external" href="https://docs.opsgenie.com/docs/supported-timezone-ids">Supported Timezone Ids</a> for available timezones - Defaults to “America/New_York”.</p>
</p></li>
<li><p><strong>enabled</strong> (<em>bool</em>) – Enable/disable state of schedule</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Name of the schedule.</p></li>
<li><p><strong>owner_team_id</strong> (<em>str</em>) – Owner team id of the schedule.</p></li>
<li><p><strong>timezone</strong> (<em>str</em>) – The description of schedule.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_opsgenie.get_service">
<code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">get_service</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_opsgenie.get_service.AwaitableGetServiceResult<a class="headerlink" href="#pulumi_opsgenie.get_service" title="Permalink to this definition"></a></dt>
<dd><p>Manages existing Service within Opsgenie.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_opsgenie</span> <span class="k">as</span> <span class="nn">opsgenie</span>

<span class="n">this</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">get_service</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Payment&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description</strong> (<em>str</em>) – Description field of the service that is generally used to provide a detailed information about the service.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Name of the service. This field must not be longer than 100 characters.</p></li>
<li><p><strong>team_id</strong> (<em>str</em>) – Team id of the service.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_opsgenie.get_team">
<code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">get_team</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>pulumi_opsgenie._inputs.GetTeamMemberArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_opsgenie.get_team.AwaitableGetTeamResult<a class="headerlink" href="#pulumi_opsgenie.get_team" title="Permalink to this definition"></a></dt>
<dd><p>Manages existing Team within Opsgenie.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_opsgenie</span> <span class="k">as</span> <span class="nn">opsgenie</span>

<span class="n">sre_team</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">get_team</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;sre-team&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description</strong> (<em>str</em>) – A description for this team.</p></li>
<li><p><strong>members</strong> (<em>Sequence</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GetTeamMemberArgs'</em><em>]</em><em>]</em>) – A Member block as documented below.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name associated with this team. Opsgenie defines that this must not be longer than 100 characters.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_opsgenie.get_user">
<code class="sig-prename descclassname">pulumi_opsgenie.</code><code class="sig-name descname">get_user</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">full_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locale</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timezone</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_opsgenie.get_user.AwaitableGetUserResult<a class="headerlink" href="#pulumi_opsgenie.get_user" title="Permalink to this definition"></a></dt>
<dd><p>Manages existing User within Opsgenie.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_opsgenie</span> <span class="k">as</span> <span class="nn">opsgenie</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">opsgenie</span><span class="o">.</span><span class="n">get_user</span><span class="p">(</span><span class="n">username</span><span class="o">=</span><span class="s2">&quot;user@domain.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>full_name</strong> (<em>str</em>) – The Full Name of the User.</p></li>
<li><p><strong>locale</strong> (<em>str</em>) – <p>Location information for the user. Please look at <a class="reference external" href="https://docs.opsgenie.com/docs/supported-locales">Supported Locale Ids</a> for available locales.</p>
</p></li>
<li><p><strong>role</strong> (<em>str</em>) – The Role assigned to the User. Either a built-in such as ‘Owner’, ‘Admin’ or ‘User’ - or the name of a custom role.</p></li>
<li><p><strong>timezone</strong> (<em>str</em>) – <p>Timezone information of the user. Please look at <a class="reference external" href="https://docs.opsgenie.com/docs/supported-timezone-ids">Supported Timezone Ids</a> for available timezones.</p>
</p></li>
<li><p><strong>username</strong> (<em>str</em>) – The email address associated with this user. Opsgenie defines that this must not be longer than 100 characters.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
