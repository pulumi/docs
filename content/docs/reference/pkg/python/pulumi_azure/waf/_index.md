---
title: Module waf
title_tag: Module waf | Package pulumi_azure | Python SDK
linktitle: waf
notitle: true
---

<div class="section" id="waf">
<h1>waf<a class="headerlink" href="#waf" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.waf"></span><dl class="py class">
<dt id="pulumi_azure.waf.Policy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.waf.</code><code class="sig-name descname">Policy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">managed_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.waf.Policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Azure Web Application Firewall Policy instance.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;West US 2&quot;</span><span class="p">)</span>
<span class="n">example_policy</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">waf</span><span class="o">.</span><span class="n">Policy</span><span class="p">(</span><span class="s2">&quot;examplePolicy&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">custom_rules</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;Rule1&quot;</span><span class="p">,</span>
            <span class="s2">&quot;priority&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
            <span class="s2">&quot;ruleType&quot;</span><span class="p">:</span> <span class="s2">&quot;MatchRule&quot;</span><span class="p">,</span>
            <span class="s2">&quot;match_conditions&quot;</span><span class="p">:</span> <span class="p">[{</span>
                <span class="s2">&quot;match_variables&quot;</span><span class="p">:</span> <span class="p">[{</span>
                    <span class="s2">&quot;variableName&quot;</span><span class="p">:</span> <span class="s2">&quot;RemoteAddr&quot;</span><span class="p">,</span>
                <span class="p">}],</span>
                <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;IPMatch&quot;</span><span class="p">,</span>
                <span class="s2">&quot;negationCondition&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
                <span class="s2">&quot;matchValues&quot;</span><span class="p">:</span> <span class="p">[</span>
                    <span class="s2">&quot;192.168.1.0/24&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;10.0.0.0/24&quot;</span><span class="p">,</span>
                <span class="p">],</span>
            <span class="p">}],</span>
            <span class="s2">&quot;action&quot;</span><span class="p">:</span> <span class="s2">&quot;Block&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;Rule2&quot;</span><span class="p">,</span>
            <span class="s2">&quot;priority&quot;</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span>
            <span class="s2">&quot;ruleType&quot;</span><span class="p">:</span> <span class="s2">&quot;MatchRule&quot;</span><span class="p">,</span>
            <span class="s2">&quot;match_conditions&quot;</span><span class="p">:</span> <span class="p">[</span>
                <span class="p">{</span>
                    <span class="s2">&quot;match_variables&quot;</span><span class="p">:</span> <span class="p">[{</span>
                        <span class="s2">&quot;variableName&quot;</span><span class="p">:</span> <span class="s2">&quot;RemoteAddr&quot;</span><span class="p">,</span>
                    <span class="p">}],</span>
                    <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;IPMatch&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;negationCondition&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
                    <span class="s2">&quot;matchValues&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;192.168.1.0/24&quot;</span><span class="p">],</span>
                <span class="p">},</span>
                <span class="p">{</span>
                    <span class="s2">&quot;match_variables&quot;</span><span class="p">:</span> <span class="p">[{</span>
                        <span class="s2">&quot;variableName&quot;</span><span class="p">:</span> <span class="s2">&quot;RequestHeaders&quot;</span><span class="p">,</span>
                        <span class="s2">&quot;selector&quot;</span><span class="p">:</span> <span class="s2">&quot;UserAgent&quot;</span><span class="p">,</span>
                    <span class="p">}],</span>
                    <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;Contains&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;negationCondition&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
                    <span class="s2">&quot;matchValues&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;Windows&quot;</span><span class="p">],</span>
                <span class="p">},</span>
            <span class="p">],</span>
            <span class="s2">&quot;action&quot;</span><span class="p">:</span> <span class="s2">&quot;Block&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">],</span>
    <span class="n">policy_settings</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;enabled&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;mode&quot;</span><span class="p">:</span> <span class="s2">&quot;Prevention&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">managed_rules</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;exclusion&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="p">{</span>
                <span class="s2">&quot;matchVariable&quot;</span><span class="p">:</span> <span class="s2">&quot;RequestHeaderNames&quot;</span><span class="p">,</span>
                <span class="s2">&quot;selector&quot;</span><span class="p">:</span> <span class="s2">&quot;x-company-secret-header&quot;</span><span class="p">,</span>
                <span class="s2">&quot;selectorMatchOperator&quot;</span><span class="p">:</span> <span class="s2">&quot;Equals&quot;</span><span class="p">,</span>
            <span class="p">},</span>
            <span class="p">{</span>
                <span class="s2">&quot;matchVariable&quot;</span><span class="p">:</span> <span class="s2">&quot;RequestCookieNames&quot;</span><span class="p">,</span>
                <span class="s2">&quot;selector&quot;</span><span class="p">:</span> <span class="s2">&quot;too-tasty&quot;</span><span class="p">,</span>
                <span class="s2">&quot;selectorMatchOperator&quot;</span><span class="p">:</span> <span class="s2">&quot;EndsWith&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">],</span>
        <span class="s2">&quot;managed_rule_set&quot;</span><span class="p">:</span> <span class="p">[{</span>
            <span class="s2">&quot;ruleSetType&quot;</span><span class="p">:</span> <span class="s2">&quot;OWASP&quot;</span><span class="p">,</span>
            <span class="s2">&quot;ruleSetVersion&quot;</span><span class="p">:</span> <span class="s2">&quot;3.1&quot;</span><span class="p">,</span>
            <span class="s2">&quot;rule_group_override&quot;</span><span class="p">:</span> <span class="p">[{</span>
                <span class="s2">&quot;ruleGroupName&quot;</span><span class="p">:</span> <span class="s2">&quot;REQUEST-920-PROTOCOL-ENFORCEMENT&quot;</span><span class="p">,</span>
                <span class="s2">&quot;disabledRules&quot;</span><span class="p">:</span> <span class="p">[</span>
                    <span class="s2">&quot;920300&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;920440&quot;</span><span class="p">,</span>
                <span class="p">],</span>
            <span class="p">}],</span>
        <span class="p">}],</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>custom_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">custom_rules</span></code> blocks as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource location. Changing this forces a new resource to be created.</p></li>
<li><p><strong>managed_rules</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">managed_rules</span></code> blocks as defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy. Changing this forces a new resource to be created.</p></li>
<li><p><strong>policy_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">policy_settings</span></code> block as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the Web Application Firewall Policy.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>custom_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of action.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matchConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">match_conditions</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of match values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matchVariables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">match_variables</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Describes field of the matchVariable collection</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">variableName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Match Variable</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">negationCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Describes if this is negate condition or not</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Describes operator to be matched.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Gets name of the resource that is unique within a policy. This name can be used to access the resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Describes priority of the rule. Rules with a lower value will be evaluated before rules with a higher value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Describes the type of rule.</p></li>
</ul>
<p>The <strong>managed_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">exclusions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">exclusion</span></code> block defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchVariable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Describes field of the matchVariable collection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selectorMatchOperator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Describes operator to be matched. Possible values: <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equals</span></code>, <code class="docutils literal notranslate"><span class="pre">EqualsAny</span></code>, <code class="docutils literal notranslate"><span class="pre">StartsWith</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedRuleSets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">managed_rule_set</span></code> block defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleGroupOverrides</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">rule_group_override</span></code> block defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabledRules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more Rule ID’s</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleGroupName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Rule Group</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The rule set type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The rule set version.</p></li>
</ul>
</li>
</ul>
<p>The <strong>policy_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Describes if the policy is in enabled state or disabled state Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Describes if it is in detection mode  or prevention mode at the policy level Defaults to <code class="docutils literal notranslate"><span class="pre">Prevention</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.waf.Policy.custom_rules">
<code class="sig-name descname">custom_rules</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.waf.Policy.custom_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">custom_rules</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Type of action.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matchConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">match_conditions</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of match values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matchVariables</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">match_variables</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Describes field of the matchVariable collection</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">variableName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Match Variable</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">negationCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Describes if this is negate condition or not</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Describes operator to be matched.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Gets name of the resource that is unique within a policy. This name can be used to access the resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Describes priority of the rule. Rules with a lower value will be evaluated before rules with a higher value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Describes the type of rule.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.waf.Policy.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.waf.Policy.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource location. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.waf.Policy.managed_rules">
<code class="sig-name descname">managed_rules</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.waf.Policy.managed_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">managed_rules</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">exclusions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">exclusion</span></code> block defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchVariable</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Describes field of the matchVariable collection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selectorMatchOperator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Describes operator to be matched. Possible values: <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equals</span></code>, <code class="docutils literal notranslate"><span class="pre">EqualsAny</span></code>, <code class="docutils literal notranslate"><span class="pre">StartsWith</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedRuleSets</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">managed_rule_set</span></code> block defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleGroupOverrides</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">rule_group_override</span></code> block defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabledRules</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more Rule ID’s</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleGroupName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Rule Group</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The rule set type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The rule set version.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.waf.Policy.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.waf.Policy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.waf.Policy.policy_settings">
<code class="sig-name descname">policy_settings</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.waf.Policy.policy_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">policy_settings</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Describes if the policy is in enabled state or disabled state Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Describes if it is in detection mode  or prevention mode at the policy level Defaults to <code class="docutils literal notranslate"><span class="pre">Prevention</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.waf.Policy.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.waf.Policy.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.waf.Policy.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.waf.Policy.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the Web Application Firewall Policy.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.waf.Policy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">managed_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.waf.Policy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Policy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>custom_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">custom_rules</span></code> blocks as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource location. Changing this forces a new resource to be created.</p></li>
<li><p><strong>managed_rules</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">managed_rules</span></code> blocks as defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy. Changing this forces a new resource to be created.</p></li>
<li><p><strong>policy_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">policy_settings</span></code> block as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the Web Application Firewall Policy.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>custom_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of action.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matchConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">match_conditions</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of match values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matchVariables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">match_variables</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Describes field of the matchVariable collection</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">variableName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Match Variable</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">negationCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Describes if this is negate condition or not</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Describes operator to be matched.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Gets name of the resource that is unique within a policy. This name can be used to access the resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Describes priority of the rule. Rules with a lower value will be evaluated before rules with a higher value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Describes the type of rule.</p></li>
</ul>
<p>The <strong>managed_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">exclusions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">exclusion</span></code> block defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchVariable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Describes field of the matchVariable collection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selectorMatchOperator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Describes operator to be matched. Possible values: <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equals</span></code>, <code class="docutils literal notranslate"><span class="pre">EqualsAny</span></code>, <code class="docutils literal notranslate"><span class="pre">StartsWith</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedRuleSets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">managed_rule_set</span></code> block defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleGroupOverrides</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">rule_group_override</span></code> block defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabledRules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more Rule ID’s</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleGroupName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Rule Group</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The rule set type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The rule set version.</p></li>
</ul>
</li>
</ul>
<p>The <strong>policy_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Describes if the policy is in enabled state or disabled state Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Describes if it is in detection mode  or prevention mode at the policy level Defaults to <code class="docutils literal notranslate"><span class="pre">Prevention</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.waf.Policy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.waf.Policy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.waf.Policy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.waf.Policy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
