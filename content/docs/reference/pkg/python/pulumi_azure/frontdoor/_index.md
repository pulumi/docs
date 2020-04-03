---
title: Module frontdoor
title_tag: Module frontdoor | Package pulumi_azure | Python SDK
linktitle: frontdoor
notitle: true
---

<div class="section" id="frontdoor">
<h1>frontdoor<a class="headerlink" href="#frontdoor" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.frontdoor"></span><dl class="class">
<dt id="pulumi_azure.frontdoor.FirewallPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.frontdoor.</code><code class="sig-name descname">FirewallPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">custom_block_response_body=None</em>, <em class="sig-param">custom_block_response_status_code=None</em>, <em class="sig-param">custom_rules=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">managed_rules=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">redirect_url=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.frontdoor.FirewallPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Front Door Web Application Firewall Policy instance.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/frontdoor_firewall_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/frontdoor_firewall_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>custom_block_response_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If a <code class="docutils literal notranslate"><span class="pre">custom_rule</span></code> block’s action type is <code class="docutils literal notranslate"><span class="pre">block</span></code>, this is the response body. The body must be specified in base64 encoding.</p></li>
<li><p><strong>custom_block_response_status_code</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If a <code class="docutils literal notranslate"><span class="pre">custom_rule</span></code> block’s action type is <code class="docutils literal notranslate"><span class="pre">block</span></code>, this is the response status code. Possible values are <code class="docutils literal notranslate"><span class="pre">200</span></code>, <code class="docutils literal notranslate"><span class="pre">403</span></code>, <code class="docutils literal notranslate"><span class="pre">405</span></code>, <code class="docutils literal notranslate"><span class="pre">406</span></code>, or <code class="docutils literal notranslate"><span class="pre">429</span></code>.</p></li>
<li><p><strong>custom_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">custom_rule</span></code> blocks as defined below.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is the policy a enabled state or disabled state. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>managed_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">managed_rule</span></code> blocks as defined below.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The firewall policy mode. Possible values are <code class="docutils literal notranslate"><span class="pre">Detection</span></code>, <code class="docutils literal notranslate"><span class="pre">Prevention</span></code> and defaults to <code class="docutils literal notranslate"><span class="pre">Prevention</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy. Changing this forces a new resource to be created.</p></li>
<li><p><strong>redirect_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If action type is redirect, this field represents redirect URL for the client.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the Web Application Firewall Policy.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>custom_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The action to perform when the rule is matched. Possible values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code>, <code class="docutils literal notranslate"><span class="pre">Block</span></code>, <code class="docutils literal notranslate"><span class="pre">Log</span></code>, or <code class="docutils literal notranslate"><span class="pre">Redirect</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the rule is enabled or disabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matchConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">match_condition</span></code> block defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Up to <code class="docutils literal notranslate"><span class="pre">100</span></code> possible values to match.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matchVariable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The request variable to compare with. Possible values are <code class="docutils literal notranslate"><span class="pre">Cookies</span></code>, <code class="docutils literal notranslate"><span class="pre">PostArgs</span></code>, <code class="docutils literal notranslate"><span class="pre">QueryString</span></code>, <code class="docutils literal notranslate"><span class="pre">RemoteAddr</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestBody</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestHeader</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestMethod</span></code>, or <code class="docutils literal notranslate"><span class="pre">RequestUri</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negationCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the result of the condition be negated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Comparison type to use for matching with the variable value. Possible values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GeoMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">IPMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code> or <code class="docutils literal notranslate"><span class="pre">RegEx</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Match against a specific key if the <code class="docutils literal notranslate"><span class="pre">match_variable</span></code> is <code class="docutils literal notranslate"><span class="pre">QueryString</span></code>, <code class="docutils literal notranslate"><span class="pre">PostArgs</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestHeader</span></code> or <code class="docutils literal notranslate"><span class="pre">Cookies</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Up to <code class="docutils literal notranslate"><span class="pre">5</span></code> transforms to apply. Possible values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code>, <code class="docutils literal notranslate"><span class="pre">RemoveNulls</span></code>, <code class="docutils literal notranslate"><span class="pre">Trim</span></code>, <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>, <code class="docutils literal notranslate"><span class="pre">URLDecode</span></code> or<code class="docutils literal notranslate"><span class="pre">URLEncode</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Gets name of the resource that is unique within a policy. This name can be used to access the resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The priority of the rule. Rules with a lower value will be evaluated before rules with a higher value. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rateLimitDurationInMinutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The rate limit duration in minutes. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rateLimitThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The rate limit threshold. Defaults to <code class="docutils literal notranslate"><span class="pre">10</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of rule. Possible values are <code class="docutils literal notranslate"><span class="pre">MatchRule</span></code> or <code class="docutils literal notranslate"><span class="pre">RateLimitRule</span></code>.</p></li>
</ul>
<p>The <strong>managed_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">exclusions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">exclusion</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchVariable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The variable type to be excluded. Possible values are <code class="docutils literal notranslate"><span class="pre">QueryStringArgNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestBodyPostArgNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestCookieNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestHeaderNames</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Comparison operator to apply to the selector when specifying which elements in the collection this exclusion applies to. Possible values are: <code class="docutils literal notranslate"><span class="pre">Equals</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">StartsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">EqualsAny</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Selector for the value in the <code class="docutils literal notranslate"><span class="pre">match_variable</span></code> attribute this exclusion applies to.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrides</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">override</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">exclusions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">exclusion</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchVariable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The variable type to be excluded. Possible values are <code class="docutils literal notranslate"><span class="pre">QueryStringArgNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestBodyPostArgNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestCookieNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestHeaderNames</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Comparison operator to apply to the selector when specifying which elements in the collection this exclusion applies to. Possible values are: <code class="docutils literal notranslate"><span class="pre">Equals</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">StartsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">EqualsAny</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Selector for the value in the <code class="docutils literal notranslate"><span class="pre">match_variable</span></code> attribute this exclusion applies to.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleGroupName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The managed rule group to override.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">rule</span></code> blocks as defined below. If none are specified, all of the rules in the group will be disabled.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The action to be applied when the rule matches. Possible values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code>, <code class="docutils literal notranslate"><span class="pre">Block</span></code>, <code class="docutils literal notranslate"><span class="pre">Log</span></code>, or <code class="docutils literal notranslate"><span class="pre">Redirect</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the managed rule override enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">exclusions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">exclusion</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchVariable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The variable type to be excluded. Possible values are <code class="docutils literal notranslate"><span class="pre">QueryStringArgNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestBodyPostArgNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestCookieNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestHeaderNames</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Comparison operator to apply to the selector when specifying which elements in the collection this exclusion applies to. Possible values are: <code class="docutils literal notranslate"><span class="pre">Equals</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">StartsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">EqualsAny</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Selector for the value in the <code class="docutils literal notranslate"><span class="pre">match_variable</span></code> attribute this exclusion applies to.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">rule_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Identifier for the managed rule.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the managed rule to use with this resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version on the managed rule to use with this resource.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.frontdoor.FirewallPolicy.custom_block_response_body">
<code class="sig-name descname">custom_block_response_body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.frontdoor.FirewallPolicy.custom_block_response_body" title="Permalink to this definition">¶</a></dt>
<dd><p>If a <code class="docutils literal notranslate"><span class="pre">custom_rule</span></code> block’s action type is <code class="docutils literal notranslate"><span class="pre">block</span></code>, this is the response body. The body must be specified in base64 encoding.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.frontdoor.FirewallPolicy.custom_block_response_status_code">
<code class="sig-name descname">custom_block_response_status_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.frontdoor.FirewallPolicy.custom_block_response_status_code" title="Permalink to this definition">¶</a></dt>
<dd><p>If a <code class="docutils literal notranslate"><span class="pre">custom_rule</span></code> block’s action type is <code class="docutils literal notranslate"><span class="pre">block</span></code>, this is the response status code. Possible values are <code class="docutils literal notranslate"><span class="pre">200</span></code>, <code class="docutils literal notranslate"><span class="pre">403</span></code>, <code class="docutils literal notranslate"><span class="pre">405</span></code>, <code class="docutils literal notranslate"><span class="pre">406</span></code>, or <code class="docutils literal notranslate"><span class="pre">429</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.frontdoor.FirewallPolicy.custom_rules">
<code class="sig-name descname">custom_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.frontdoor.FirewallPolicy.custom_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">custom_rule</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The action to perform when the rule is matched. Possible values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code>, <code class="docutils literal notranslate"><span class="pre">Block</span></code>, <code class="docutils literal notranslate"><span class="pre">Log</span></code>, or <code class="docutils literal notranslate"><span class="pre">Redirect</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is the rule is enabled or disabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matchConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">match_condition</span></code> block defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Up to <code class="docutils literal notranslate"><span class="pre">100</span></code> possible values to match.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matchVariable</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The request variable to compare with. Possible values are <code class="docutils literal notranslate"><span class="pre">Cookies</span></code>, <code class="docutils literal notranslate"><span class="pre">PostArgs</span></code>, <code class="docutils literal notranslate"><span class="pre">QueryString</span></code>, <code class="docutils literal notranslate"><span class="pre">RemoteAddr</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestBody</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestHeader</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestMethod</span></code>, or <code class="docutils literal notranslate"><span class="pre">RequestUri</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negationCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should the result of the condition be negated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Comparison type to use for matching with the variable value. Possible values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GeoMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">IPMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code> or <code class="docutils literal notranslate"><span class="pre">RegEx</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Match against a specific key if the <code class="docutils literal notranslate"><span class="pre">match_variable</span></code> is <code class="docutils literal notranslate"><span class="pre">QueryString</span></code>, <code class="docutils literal notranslate"><span class="pre">PostArgs</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestHeader</span></code> or <code class="docutils literal notranslate"><span class="pre">Cookies</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Up to <code class="docutils literal notranslate"><span class="pre">5</span></code> transforms to apply. Possible values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code>, <code class="docutils literal notranslate"><span class="pre">RemoveNulls</span></code>, <code class="docutils literal notranslate"><span class="pre">Trim</span></code>, <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>, <code class="docutils literal notranslate"><span class="pre">URLDecode</span></code> or<code class="docutils literal notranslate"><span class="pre">URLEncode</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Gets name of the resource that is unique within a policy. This name can be used to access the resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The priority of the rule. Rules with a lower value will be evaluated before rules with a higher value. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rateLimitDurationInMinutes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The rate limit duration in minutes. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rateLimitThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The rate limit threshold. Defaults to <code class="docutils literal notranslate"><span class="pre">10</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of rule. Possible values are <code class="docutils literal notranslate"><span class="pre">MatchRule</span></code> or <code class="docutils literal notranslate"><span class="pre">RateLimitRule</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.frontdoor.FirewallPolicy.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.frontdoor.FirewallPolicy.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is the policy a enabled state or disabled state. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.frontdoor.FirewallPolicy.frontend_endpoint_ids">
<code class="sig-name descname">frontend_endpoint_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.frontdoor.FirewallPolicy.frontend_endpoint_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>the Frontend Endpoints associated with this Front Door Web Application Firewall policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.frontdoor.FirewallPolicy.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.frontdoor.FirewallPolicy.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.frontdoor.FirewallPolicy.managed_rules">
<code class="sig-name descname">managed_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.frontdoor.FirewallPolicy.managed_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">managed_rule</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">exclusions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">exclusion</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchVariable</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The variable type to be excluded. Possible values are <code class="docutils literal notranslate"><span class="pre">QueryStringArgNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestBodyPostArgNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestCookieNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestHeaderNames</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Comparison operator to apply to the selector when specifying which elements in the collection this exclusion applies to. Possible values are: <code class="docutils literal notranslate"><span class="pre">Equals</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">StartsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">EqualsAny</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Selector for the value in the <code class="docutils literal notranslate"><span class="pre">match_variable</span></code> attribute this exclusion applies to.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrides</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">override</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">exclusions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">exclusion</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchVariable</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The variable type to be excluded. Possible values are <code class="docutils literal notranslate"><span class="pre">QueryStringArgNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestBodyPostArgNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestCookieNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestHeaderNames</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Comparison operator to apply to the selector when specifying which elements in the collection this exclusion applies to. Possible values are: <code class="docutils literal notranslate"><span class="pre">Equals</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">StartsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">EqualsAny</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Selector for the value in the <code class="docutils literal notranslate"><span class="pre">match_variable</span></code> attribute this exclusion applies to.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleGroupName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The managed rule group to override.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rules</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">rule</span></code> blocks as defined below. If none are specified, all of the rules in the group will be disabled.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The action to be applied when the rule matches. Possible values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code>, <code class="docutils literal notranslate"><span class="pre">Block</span></code>, <code class="docutils literal notranslate"><span class="pre">Log</span></code>, or <code class="docutils literal notranslate"><span class="pre">Redirect</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is the managed rule override enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">exclusions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">exclusion</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchVariable</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The variable type to be excluded. Possible values are <code class="docutils literal notranslate"><span class="pre">QueryStringArgNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestBodyPostArgNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestCookieNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestHeaderNames</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Comparison operator to apply to the selector when specifying which elements in the collection this exclusion applies to. Possible values are: <code class="docutils literal notranslate"><span class="pre">Equals</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">StartsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">EqualsAny</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Selector for the value in the <code class="docutils literal notranslate"><span class="pre">match_variable</span></code> attribute this exclusion applies to.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">rule_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Identifier for the managed rule.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the managed rule to use with this resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The version on the managed rule to use with this resource.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.frontdoor.FirewallPolicy.mode">
<code class="sig-name descname">mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.frontdoor.FirewallPolicy.mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The firewall policy mode. Possible values are <code class="docutils literal notranslate"><span class="pre">Detection</span></code>, <code class="docutils literal notranslate"><span class="pre">Prevention</span></code> and defaults to <code class="docutils literal notranslate"><span class="pre">Prevention</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.frontdoor.FirewallPolicy.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.frontdoor.FirewallPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.frontdoor.FirewallPolicy.redirect_url">
<code class="sig-name descname">redirect_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.frontdoor.FirewallPolicy.redirect_url" title="Permalink to this definition">¶</a></dt>
<dd><p>If action type is redirect, this field represents redirect URL for the client.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.frontdoor.FirewallPolicy.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.frontdoor.FirewallPolicy.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.frontdoor.FirewallPolicy.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.frontdoor.FirewallPolicy.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the Web Application Firewall Policy.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.frontdoor.FirewallPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">custom_block_response_body=None</em>, <em class="sig-param">custom_block_response_status_code=None</em>, <em class="sig-param">custom_rules=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">frontend_endpoint_ids=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">managed_rules=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">redirect_url=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.frontdoor.FirewallPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FirewallPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>custom_block_response_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If a <code class="docutils literal notranslate"><span class="pre">custom_rule</span></code> block’s action type is <code class="docutils literal notranslate"><span class="pre">block</span></code>, this is the response body. The body must be specified in base64 encoding.</p></li>
<li><p><strong>custom_block_response_status_code</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If a <code class="docutils literal notranslate"><span class="pre">custom_rule</span></code> block’s action type is <code class="docutils literal notranslate"><span class="pre">block</span></code>, this is the response status code. Possible values are <code class="docutils literal notranslate"><span class="pre">200</span></code>, <code class="docutils literal notranslate"><span class="pre">403</span></code>, <code class="docutils literal notranslate"><span class="pre">405</span></code>, <code class="docutils literal notranslate"><span class="pre">406</span></code>, or <code class="docutils literal notranslate"><span class="pre">429</span></code>.</p></li>
<li><p><strong>custom_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">custom_rule</span></code> blocks as defined below.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is the policy a enabled state or disabled state. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>frontend_endpoint_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – the Frontend Endpoints associated with this Front Door Web Application Firewall policy.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource location.</p></li>
<li><p><strong>managed_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">managed_rule</span></code> blocks as defined below.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The firewall policy mode. Possible values are <code class="docutils literal notranslate"><span class="pre">Detection</span></code>, <code class="docutils literal notranslate"><span class="pre">Prevention</span></code> and defaults to <code class="docutils literal notranslate"><span class="pre">Prevention</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy. Changing this forces a new resource to be created.</p></li>
<li><p><strong>redirect_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If action type is redirect, this field represents redirect URL for the client.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the Web Application Firewall Policy.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>custom_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The action to perform when the rule is matched. Possible values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code>, <code class="docutils literal notranslate"><span class="pre">Block</span></code>, <code class="docutils literal notranslate"><span class="pre">Log</span></code>, or <code class="docutils literal notranslate"><span class="pre">Redirect</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the rule is enabled or disabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matchConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">match_condition</span></code> block defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Up to <code class="docutils literal notranslate"><span class="pre">100</span></code> possible values to match.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matchVariable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The request variable to compare with. Possible values are <code class="docutils literal notranslate"><span class="pre">Cookies</span></code>, <code class="docutils literal notranslate"><span class="pre">PostArgs</span></code>, <code class="docutils literal notranslate"><span class="pre">QueryString</span></code>, <code class="docutils literal notranslate"><span class="pre">RemoteAddr</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestBody</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestHeader</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestMethod</span></code>, or <code class="docutils literal notranslate"><span class="pre">RequestUri</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negationCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the result of the condition be negated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Comparison type to use for matching with the variable value. Possible values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GeoMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">IPMatch</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code> or <code class="docutils literal notranslate"><span class="pre">RegEx</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Match against a specific key if the <code class="docutils literal notranslate"><span class="pre">match_variable</span></code> is <code class="docutils literal notranslate"><span class="pre">QueryString</span></code>, <code class="docutils literal notranslate"><span class="pre">PostArgs</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestHeader</span></code> or <code class="docutils literal notranslate"><span class="pre">Cookies</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Up to <code class="docutils literal notranslate"><span class="pre">5</span></code> transforms to apply. Possible values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code>, <code class="docutils literal notranslate"><span class="pre">RemoveNulls</span></code>, <code class="docutils literal notranslate"><span class="pre">Trim</span></code>, <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>, <code class="docutils literal notranslate"><span class="pre">URLDecode</span></code> or<code class="docutils literal notranslate"><span class="pre">URLEncode</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Gets name of the resource that is unique within a policy. This name can be used to access the resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The priority of the rule. Rules with a lower value will be evaluated before rules with a higher value. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rateLimitDurationInMinutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The rate limit duration in minutes. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rateLimitThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The rate limit threshold. Defaults to <code class="docutils literal notranslate"><span class="pre">10</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of rule. Possible values are <code class="docutils literal notranslate"><span class="pre">MatchRule</span></code> or <code class="docutils literal notranslate"><span class="pre">RateLimitRule</span></code>.</p></li>
</ul>
<p>The <strong>managed_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">exclusions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">exclusion</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchVariable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The variable type to be excluded. Possible values are <code class="docutils literal notranslate"><span class="pre">QueryStringArgNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestBodyPostArgNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestCookieNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestHeaderNames</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Comparison operator to apply to the selector when specifying which elements in the collection this exclusion applies to. Possible values are: <code class="docutils literal notranslate"><span class="pre">Equals</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">StartsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">EqualsAny</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Selector for the value in the <code class="docutils literal notranslate"><span class="pre">match_variable</span></code> attribute this exclusion applies to.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrides</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">override</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">exclusions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">exclusion</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchVariable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The variable type to be excluded. Possible values are <code class="docutils literal notranslate"><span class="pre">QueryStringArgNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestBodyPostArgNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestCookieNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestHeaderNames</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Comparison operator to apply to the selector when specifying which elements in the collection this exclusion applies to. Possible values are: <code class="docutils literal notranslate"><span class="pre">Equals</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">StartsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">EqualsAny</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Selector for the value in the <code class="docutils literal notranslate"><span class="pre">match_variable</span></code> attribute this exclusion applies to.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleGroupName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The managed rule group to override.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">rule</span></code> blocks as defined below. If none are specified, all of the rules in the group will be disabled.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The action to be applied when the rule matches. Possible values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code>, <code class="docutils literal notranslate"><span class="pre">Block</span></code>, <code class="docutils literal notranslate"><span class="pre">Log</span></code>, or <code class="docutils literal notranslate"><span class="pre">Redirect</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the managed rule override enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">exclusions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">exclusion</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchVariable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The variable type to be excluded. Possible values are <code class="docutils literal notranslate"><span class="pre">QueryStringArgNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestBodyPostArgNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestCookieNames</span></code>, <code class="docutils literal notranslate"><span class="pre">RequestHeaderNames</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Comparison operator to apply to the selector when specifying which elements in the collection this exclusion applies to. Possible values are: <code class="docutils literal notranslate"><span class="pre">Equals</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">StartsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">EqualsAny</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Selector for the value in the <code class="docutils literal notranslate"><span class="pre">match_variable</span></code> attribute this exclusion applies to.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">rule_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Identifier for the managed rule.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the managed rule to use with this resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version on the managed rule to use with this resource.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.frontdoor.FirewallPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.frontdoor.FirewallPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_azure.frontdoor.FirewallPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.frontdoor.FirewallPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_azure.frontdoor.Frontdoor">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.frontdoor.</code><code class="sig-name descname">Frontdoor</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend_pool_health_probes=None</em>, <em class="sig-param">backend_pool_load_balancings=None</em>, <em class="sig-param">backend_pools=None</em>, <em class="sig-param">enforce_backend_pools_certificate_name_check=None</em>, <em class="sig-param">friendly_name=None</em>, <em class="sig-param">frontend_endpoints=None</em>, <em class="sig-param">load_balancer_enabled=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">routing_rules=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.frontdoor.Frontdoor" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Front Door instance.</p>
<p>Azure Front Door Service is Microsoft’s highly available and scalable web application acceleration platform and global HTTP(s) load balancer. It provides built-in DDoS protection and application layer security and caching. Front Door enables you to build applications that maximize and automate high-availability and performance for your end-users. Use Front Door with Azure services including Web/Mobile Apps, Cloud Services and Virtual Machines – or combine it with on-premises services for hybrid deployments and smooth cloud migration.</p>
<p>Below are some of the key scenarios that Azure Front Door Service addresses:</p>
<ul class="simple">
<li><p>Use Front Door to improve application scale and availability with instant multi-region failover</p></li>
<li><p>Use Front Door to improve application performance with SSL offload and routing requests to the fastest available application backend.</p></li>
<li><p>Use Front Door for application layer security and DDoS protection for your application.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/frontdoor.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/frontdoor.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend_pool_health_probes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">backend_pool_health_probe</span></code> block as defined below.</p></li>
<li><p><strong>backend_pool_load_balancings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">backend_pool_load_balancing</span></code> block as defined below.</p></li>
<li><p><strong>backend_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">backend_pool</span></code> block as defined below.</p></li>
<li><p><strong>enforce_backend_pools_certificate_name_check</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enforce certificate name check on <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code> requests to all backend pools, this setting will have no effect on <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> requests. Permitted values are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>friendly_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name for the Front Door service.</p></li>
<li><p><strong>frontend_endpoints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">frontend_endpoint</span></code> block as defined below.</p></li>
<li><p><strong>load_balancer_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Front Door Load Balancer be Enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Front Door service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which the Front Door service should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>routing_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">routing_rule</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>backend_pool_health_probes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this health probe enabled? Dafaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the FrontDoor.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval_in_seconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of seconds between each Health Probe. Defaults to <code class="docutils literal notranslate"><span class="pre">120</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Health Probe.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to use for the Health Probe. Default is <code class="docutils literal notranslate"><span class="pre">/</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">probeMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies HTTP method the health probe uses when querying the backend pool instances. Possible values include: <code class="docutils literal notranslate"><span class="pre">Get</span></code> and <code class="docutils literal notranslate"><span class="pre">Head</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Get</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Protocol scheme to use for the Health Probe. Defaults to <code class="docutils literal notranslate"><span class="pre">Http</span></code>.</p></li>
</ul>
<p>The <strong>backend_pool_load_balancings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">additionalLatencyMilliseconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The additional latency in milliseconds for probes to fall into the lowest latency bucket. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the FrontDoor.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Load Balancer.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sampleSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of samples to consider for load balancing decisions. Defaults to <code class="docutils literal notranslate"><span class="pre">4</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">successfulSamplesRequired</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of samples within the sample period that must succeed. Defaults to <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
</ul>
<p>The <strong>backend_pools</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">backends</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">backend</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Location of the backend (IP address or FQDN)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies if the backend is enabled or not. Valid options are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value to use as the host header sent to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The HTTP TCP port number. Possible values are between <code class="docutils literal notranslate"><span class="pre">1</span></code> - <code class="docutils literal notranslate"><span class="pre">65535</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpsPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The HTTPS TCP port number. Possible values are between <code class="docutils literal notranslate"><span class="pre">1</span></code> - <code class="docutils literal notranslate"><span class="pre">65535</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Priority to use for load balancing. Higher priorities will not be used for load balancing if any lower priority backend is healthy. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Weight of this endpoint for load balancing purposes. Defaults to <code class="docutils literal notranslate"><span class="pre">50</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthProbeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the <code class="docutils literal notranslate"><span class="pre">backend_pool_health_probe</span></code> block whithin this resource to use for this <code class="docutils literal notranslate"><span class="pre">Backend</span> <span class="pre">Pool</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the FrontDoor.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancingName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the <code class="docutils literal notranslate"><span class="pre">backend_pool_load_balancing</span></code> block within this resource to use for this <code class="docutils literal notranslate"><span class="pre">Backend</span> <span class="pre">Pool</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Backend Pool.</p></li>
</ul>
<p>The <strong>frontend_endpoints</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customHttpsConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">custom_https_configuration</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">azureKeyVaultCertificateSecretName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Key Vault secret representing the full certificate PFX.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azureKeyVaultCertificateSecretVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of the Key Vault secret representing the full certificate PFX.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azureKeyVaultCertificateVaultId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Key Vault containing the SSL certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateSource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Certificate source to encrypted <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code> traffic with. Allowed values are <code class="docutils literal notranslate"><span class="pre">FrontDoor</span></code> or <code class="docutils literal notranslate"><span class="pre">AzureKeyVault</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">FrontDoor</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum_tls_version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Minimum client TLS version supported.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provisioningState</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Provisioning state of the Front Door.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provisioningSubstate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Provisioning substate of the Front Door</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">customHttpsProvisioningEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the HTTPS protocol be enabled for a custom domain associated with the Front Door?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the host name of the <code class="docutils literal notranslate"><span class="pre">frontend_endpoint</span></code>. Must be a domain name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the FrontDoor.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the <code class="docutils literal notranslate"><span class="pre">frontend_endpoint</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionAffinityEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to allow session affinity on this host. Valid options are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code> Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionAffinityTtlSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The TTL to use in seconds for session affinity, if applicable. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webApplicationFirewallPolicyLinkId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Defines the Web Application Firewall policy <code class="docutils literal notranslate"><span class="pre">ID</span></code> for each host.</p></li>
</ul>
<p>The <strong>routing_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">acceptedProtocols</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Protocol schemes to match for the Backend Routing Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">Http</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - <code class="docutils literal notranslate"><span class="pre">Enable</span></code> or <code class="docutils literal notranslate"><span class="pre">Disable</span></code> use of this Backend Routing Rule. Permitted values are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forwardingConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">forwarding_configuration</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">backendPoolName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Backend Pool to forward the incoming traffic to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether to Enable caching or not. Valid options are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheQueryParameterStripDirective</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Defines cache behavior in releation to query string parameters. Valid options are <code class="docutils literal notranslate"><span class="pre">StripAll</span></code> or <code class="docutils literal notranslate"><span class="pre">StripNone</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">StripAll</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheUseDynamicCompression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use dynamic compression when caching. Valid options are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customForwardingPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Path to use when constructing the request to forward to the backend. This functions as a URL Rewrite. Default behavior preserves the URL path.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forwardingProtocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Protocol to use when redirecting. Valid options are <code class="docutils literal notranslate"><span class="pre">HttpOnly</span></code>, <code class="docutils literal notranslate"><span class="pre">HttpsOnly</span></code>, or <code class="docutils literal notranslate"><span class="pre">MatchRequest</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">HttpsOnly</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">frontend_endpoints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The names of the <code class="docutils literal notranslate"><span class="pre">frontend_endpoint</span></code> blocks whithin this resource to associate with this <code class="docutils literal notranslate"><span class="pre">routing_rule</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the FrontDoor.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Routing Rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">patternsToMatches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The route patterns for the Backend Routing Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">/*</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">redirect_configuration</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">customFragment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The destination fragment in the portion of URL after ‘#’. Set this to add a fragment to the redirect URL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customHost</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Set this to change the URL for the redirection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to retain as per the incoming request, or update in the URL for the redirection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customQueryString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Replace any existing query string from the incoming request URL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectProtocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Protocol to use when redirecting. Valid options are <code class="docutils literal notranslate"><span class="pre">HttpOnly</span></code>, <code class="docutils literal notranslate"><span class="pre">HttpsOnly</span></code>, or <code class="docutils literal notranslate"><span class="pre">MatchRequest</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">MatchRequest</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Status code for the redirect. Valida options are <code class="docutils literal notranslate"><span class="pre">Moved</span></code>, <code class="docutils literal notranslate"><span class="pre">Found</span></code>, <code class="docutils literal notranslate"><span class="pre">TemporaryRedirect</span></code>, <code class="docutils literal notranslate"><span class="pre">PermanentRedirect</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Found</span></code></p></li>
</ul>
</li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.frontdoor.Frontdoor.backend_pool_health_probes">
<code class="sig-name descname">backend_pool_health_probes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.frontdoor.Frontdoor.backend_pool_health_probes" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">backend_pool_health_probe</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this health probe enabled? Dafaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the FrontDoor.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval_in_seconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of seconds between each Health Probe. Defaults to <code class="docutils literal notranslate"><span class="pre">120</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the Health Probe.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to use for the Health Probe. Default is <code class="docutils literal notranslate"><span class="pre">/</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">probeMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies HTTP method the health probe uses when querying the backend pool instances. Possible values include: <code class="docutils literal notranslate"><span class="pre">Get</span></code> and <code class="docutils literal notranslate"><span class="pre">Head</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Get</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Protocol scheme to use for the Health Probe. Defaults to <code class="docutils literal notranslate"><span class="pre">Http</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.frontdoor.Frontdoor.backend_pool_load_balancings">
<code class="sig-name descname">backend_pool_load_balancings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.frontdoor.Frontdoor.backend_pool_load_balancings" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">backend_pool_load_balancing</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">additionalLatencyMilliseconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The additional latency in milliseconds for probes to fall into the lowest latency bucket. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the FrontDoor.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the Load Balancer.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sampleSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of samples to consider for load balancing decisions. Defaults to <code class="docutils literal notranslate"><span class="pre">4</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">successfulSamplesRequired</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of samples within the sample period that must succeed. Defaults to <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.frontdoor.Frontdoor.backend_pools">
<code class="sig-name descname">backend_pools</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.frontdoor.Frontdoor.backend_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">backend_pool</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">backends</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A <code class="docutils literal notranslate"><span class="pre">backend</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Location of the backend (IP address or FQDN)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies if the backend is enabled or not. Valid options are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value to use as the host header sent to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpPort</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The HTTP TCP port number. Possible values are between <code class="docutils literal notranslate"><span class="pre">1</span></code> - <code class="docutils literal notranslate"><span class="pre">65535</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpsPort</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The HTTPS TCP port number. Possible values are between <code class="docutils literal notranslate"><span class="pre">1</span></code> - <code class="docutils literal notranslate"><span class="pre">65535</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Priority to use for load balancing. Higher priorities will not be used for load balancing if any lower priority backend is healthy. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Weight of this endpoint for load balancing purposes. Defaults to <code class="docutils literal notranslate"><span class="pre">50</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthProbeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the <code class="docutils literal notranslate"><span class="pre">backend_pool_health_probe</span></code> block whithin this resource to use for this <code class="docutils literal notranslate"><span class="pre">Backend</span> <span class="pre">Pool</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the FrontDoor.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancingName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the <code class="docutils literal notranslate"><span class="pre">backend_pool_load_balancing</span></code> block within this resource to use for this <code class="docutils literal notranslate"><span class="pre">Backend</span> <span class="pre">Pool</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the Backend Pool.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.frontdoor.Frontdoor.cname">
<code class="sig-name descname">cname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.frontdoor.Frontdoor.cname" title="Permalink to this definition">¶</a></dt>
<dd><p>The host that each frontendEndpoint must CNAME to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.frontdoor.Frontdoor.enforce_backend_pools_certificate_name_check">
<code class="sig-name descname">enforce_backend_pools_certificate_name_check</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.frontdoor.Frontdoor.enforce_backend_pools_certificate_name_check" title="Permalink to this definition">¶</a></dt>
<dd><p>Enforce certificate name check on <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code> requests to all backend pools, this setting will have no effect on <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> requests. Permitted values are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.frontdoor.Frontdoor.friendly_name">
<code class="sig-name descname">friendly_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.frontdoor.Frontdoor.friendly_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly name for the Front Door service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.frontdoor.Frontdoor.frontend_endpoints">
<code class="sig-name descname">frontend_endpoints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.frontdoor.Frontdoor.frontend_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">frontend_endpoint</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customHttpsConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">custom_https_configuration</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">azureKeyVaultCertificateSecretName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Key Vault secret representing the full certificate PFX.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azureKeyVaultCertificateSecretVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The version of the Key Vault secret representing the full certificate PFX.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azureKeyVaultCertificateVaultId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Key Vault containing the SSL certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateSource</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Certificate source to encrypted <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code> traffic with. Allowed values are <code class="docutils literal notranslate"><span class="pre">FrontDoor</span></code> or <code class="docutils literal notranslate"><span class="pre">AzureKeyVault</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">FrontDoor</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum_tls_version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Minimum client TLS version supported.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provisioningState</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Provisioning state of the Front Door.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provisioningSubstate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Provisioning substate of the Front Door</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">customHttpsProvisioningEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should the HTTPS protocol be enabled for a custom domain associated with the Front Door?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the host name of the <code class="docutils literal notranslate"><span class="pre">frontend_endpoint</span></code>. Must be a domain name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the FrontDoor.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the <code class="docutils literal notranslate"><span class="pre">frontend_endpoint</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionAffinityEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to allow session affinity on this host. Valid options are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code> Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionAffinityTtlSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The TTL to use in seconds for session affinity, if applicable. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webApplicationFirewallPolicyLinkId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Defines the Web Application Firewall policy <code class="docutils literal notranslate"><span class="pre">ID</span></code> for each host.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.frontdoor.Frontdoor.load_balancer_enabled">
<code class="sig-name descname">load_balancer_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.frontdoor.Frontdoor.load_balancer_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the Front Door Load Balancer be Enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.frontdoor.Frontdoor.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.frontdoor.Frontdoor.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Front Door service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.frontdoor.Frontdoor.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.frontdoor.Frontdoor.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group in which the Front Door service should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.frontdoor.Frontdoor.routing_rules">
<code class="sig-name descname">routing_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.frontdoor.Frontdoor.routing_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">routing_rule</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">acceptedProtocols</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Protocol schemes to match for the Backend Routing Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">Http</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - <code class="docutils literal notranslate"><span class="pre">Enable</span></code> or <code class="docutils literal notranslate"><span class="pre">Disable</span></code> use of this Backend Routing Rule. Permitted values are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forwardingConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">forwarding_configuration</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">backendPoolName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the Backend Pool to forward the incoming traffic to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether to Enable caching or not. Valid options are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheQueryParameterStripDirective</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Defines cache behavior in releation to query string parameters. Valid options are <code class="docutils literal notranslate"><span class="pre">StripAll</span></code> or <code class="docutils literal notranslate"><span class="pre">StripNone</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">StripAll</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheUseDynamicCompression</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to use dynamic compression when caching. Valid options are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customForwardingPath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Path to use when constructing the request to forward to the backend. This functions as a URL Rewrite. Default behavior preserves the URL path.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forwardingProtocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Protocol to use when redirecting. Valid options are <code class="docutils literal notranslate"><span class="pre">HttpOnly</span></code>, <code class="docutils literal notranslate"><span class="pre">HttpsOnly</span></code>, or <code class="docutils literal notranslate"><span class="pre">MatchRequest</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">HttpsOnly</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">frontend_endpoints</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The names of the <code class="docutils literal notranslate"><span class="pre">frontend_endpoint</span></code> blocks whithin this resource to associate with this <code class="docutils literal notranslate"><span class="pre">routing_rule</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the FrontDoor.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the Routing Rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">patternsToMatches</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The route patterns for the Backend Routing Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">/*</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">redirect_configuration</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">customFragment</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The destination fragment in the portion of URL after ‘#’. Set this to add a fragment to the redirect URL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customHost</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Set this to change the URL for the redirection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customPath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path to retain as per the incoming request, or update in the URL for the redirection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customQueryString</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Replace any existing query string from the incoming request URL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectProtocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Protocol to use when redirecting. Valid options are <code class="docutils literal notranslate"><span class="pre">HttpOnly</span></code>, <code class="docutils literal notranslate"><span class="pre">HttpsOnly</span></code>, or <code class="docutils literal notranslate"><span class="pre">MatchRequest</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">MatchRequest</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Status code for the redirect. Valida options are <code class="docutils literal notranslate"><span class="pre">Moved</span></code>, <code class="docutils literal notranslate"><span class="pre">Found</span></code>, <code class="docutils literal notranslate"><span class="pre">TemporaryRedirect</span></code>, <code class="docutils literal notranslate"><span class="pre">PermanentRedirect</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Found</span></code></p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.frontdoor.Frontdoor.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.frontdoor.Frontdoor.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.frontdoor.Frontdoor.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend_pool_health_probes=None</em>, <em class="sig-param">backend_pool_load_balancings=None</em>, <em class="sig-param">backend_pools=None</em>, <em class="sig-param">cname=None</em>, <em class="sig-param">enforce_backend_pools_certificate_name_check=None</em>, <em class="sig-param">friendly_name=None</em>, <em class="sig-param">frontend_endpoints=None</em>, <em class="sig-param">load_balancer_enabled=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">routing_rules=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.frontdoor.Frontdoor.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Frontdoor resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend_pool_health_probes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">backend_pool_health_probe</span></code> block as defined below.</p></li>
<li><p><strong>backend_pool_load_balancings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">backend_pool_load_balancing</span></code> block as defined below.</p></li>
<li><p><strong>backend_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">backend_pool</span></code> block as defined below.</p></li>
<li><p><strong>cname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The host that each frontendEndpoint must CNAME to.</p></li>
<li><p><strong>enforce_backend_pools_certificate_name_check</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enforce certificate name check on <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code> requests to all backend pools, this setting will have no effect on <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> requests. Permitted values are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>friendly_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name for the Front Door service.</p></li>
<li><p><strong>frontend_endpoints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">frontend_endpoint</span></code> block as defined below.</p></li>
<li><p><strong>load_balancer_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Front Door Load Balancer be Enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Front Door service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which the Front Door service should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>routing_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">routing_rule</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>backend_pool_health_probes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this health probe enabled? Dafaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the FrontDoor.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval_in_seconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of seconds between each Health Probe. Defaults to <code class="docutils literal notranslate"><span class="pre">120</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Health Probe.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to use for the Health Probe. Default is <code class="docutils literal notranslate"><span class="pre">/</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">probeMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies HTTP method the health probe uses when querying the backend pool instances. Possible values include: <code class="docutils literal notranslate"><span class="pre">Get</span></code> and <code class="docutils literal notranslate"><span class="pre">Head</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Get</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Protocol scheme to use for the Health Probe. Defaults to <code class="docutils literal notranslate"><span class="pre">Http</span></code>.</p></li>
</ul>
<p>The <strong>backend_pool_load_balancings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">additionalLatencyMilliseconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The additional latency in milliseconds for probes to fall into the lowest latency bucket. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the FrontDoor.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Load Balancer.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sampleSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of samples to consider for load balancing decisions. Defaults to <code class="docutils literal notranslate"><span class="pre">4</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">successfulSamplesRequired</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of samples within the sample period that must succeed. Defaults to <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
</ul>
<p>The <strong>backend_pools</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">backends</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">backend</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Location of the backend (IP address or FQDN)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies if the backend is enabled or not. Valid options are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value to use as the host header sent to the backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The HTTP TCP port number. Possible values are between <code class="docutils literal notranslate"><span class="pre">1</span></code> - <code class="docutils literal notranslate"><span class="pre">65535</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpsPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The HTTPS TCP port number. Possible values are between <code class="docutils literal notranslate"><span class="pre">1</span></code> - <code class="docutils literal notranslate"><span class="pre">65535</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Priority to use for load balancing. Higher priorities will not be used for load balancing if any lower priority backend is healthy. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Weight of this endpoint for load balancing purposes. Defaults to <code class="docutils literal notranslate"><span class="pre">50</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthProbeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the <code class="docutils literal notranslate"><span class="pre">backend_pool_health_probe</span></code> block whithin this resource to use for this <code class="docutils literal notranslate"><span class="pre">Backend</span> <span class="pre">Pool</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the FrontDoor.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancingName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the <code class="docutils literal notranslate"><span class="pre">backend_pool_load_balancing</span></code> block within this resource to use for this <code class="docutils literal notranslate"><span class="pre">Backend</span> <span class="pre">Pool</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Backend Pool.</p></li>
</ul>
<p>The <strong>frontend_endpoints</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customHttpsConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">custom_https_configuration</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">azureKeyVaultCertificateSecretName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Key Vault secret representing the full certificate PFX.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azureKeyVaultCertificateSecretVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of the Key Vault secret representing the full certificate PFX.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">azureKeyVaultCertificateVaultId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Key Vault containing the SSL certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateSource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Certificate source to encrypted <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code> traffic with. Allowed values are <code class="docutils literal notranslate"><span class="pre">FrontDoor</span></code> or <code class="docutils literal notranslate"><span class="pre">AzureKeyVault</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">FrontDoor</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum_tls_version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Minimum client TLS version supported.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provisioningState</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Provisioning state of the Front Door.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provisioningSubstate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Provisioning substate of the Front Door</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">customHttpsProvisioningEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the HTTPS protocol be enabled for a custom domain associated with the Front Door?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the host name of the <code class="docutils literal notranslate"><span class="pre">frontend_endpoint</span></code>. Must be a domain name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the FrontDoor.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the <code class="docutils literal notranslate"><span class="pre">frontend_endpoint</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionAffinityEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to allow session affinity on this host. Valid options are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code> Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionAffinityTtlSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The TTL to use in seconds for session affinity, if applicable. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webApplicationFirewallPolicyLinkId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Defines the Web Application Firewall policy <code class="docutils literal notranslate"><span class="pre">ID</span></code> for each host.</p></li>
</ul>
<p>The <strong>routing_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">acceptedProtocols</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Protocol schemes to match for the Backend Routing Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">Http</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - <code class="docutils literal notranslate"><span class="pre">Enable</span></code> or <code class="docutils literal notranslate"><span class="pre">Disable</span></code> use of this Backend Routing Rule. Permitted values are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forwardingConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">forwarding_configuration</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">backendPoolName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Backend Pool to forward the incoming traffic to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether to Enable caching or not. Valid options are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheQueryParameterStripDirective</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Defines cache behavior in releation to query string parameters. Valid options are <code class="docutils literal notranslate"><span class="pre">StripAll</span></code> or <code class="docutils literal notranslate"><span class="pre">StripNone</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">StripAll</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheUseDynamicCompression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use dynamic compression when caching. Valid options are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customForwardingPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Path to use when constructing the request to forward to the backend. This functions as a URL Rewrite. Default behavior preserves the URL path.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forwardingProtocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Protocol to use when redirecting. Valid options are <code class="docutils literal notranslate"><span class="pre">HttpOnly</span></code>, <code class="docutils literal notranslate"><span class="pre">HttpsOnly</span></code>, or <code class="docutils literal notranslate"><span class="pre">MatchRequest</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">HttpsOnly</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">frontend_endpoints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The names of the <code class="docutils literal notranslate"><span class="pre">frontend_endpoint</span></code> blocks whithin this resource to associate with this <code class="docutils literal notranslate"><span class="pre">routing_rule</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the FrontDoor.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Routing Rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">patternsToMatches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The route patterns for the Backend Routing Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">/*</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">redirect_configuration</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">customFragment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The destination fragment in the portion of URL after ‘#’. Set this to add a fragment to the redirect URL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customHost</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Set this to change the URL for the redirection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to retain as per the incoming request, or update in the URL for the redirection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customQueryString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Replace any existing query string from the incoming request URL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectProtocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Protocol to use when redirecting. Valid options are <code class="docutils literal notranslate"><span class="pre">HttpOnly</span></code>, <code class="docutils literal notranslate"><span class="pre">HttpsOnly</span></code>, or <code class="docutils literal notranslate"><span class="pre">MatchRequest</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">MatchRequest</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Status code for the redirect. Valida options are <code class="docutils literal notranslate"><span class="pre">Moved</span></code>, <code class="docutils literal notranslate"><span class="pre">Found</span></code>, <code class="docutils literal notranslate"><span class="pre">TemporaryRedirect</span></code>, <code class="docutils literal notranslate"><span class="pre">PermanentRedirect</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Found</span></code></p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.frontdoor.Frontdoor.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.frontdoor.Frontdoor.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_azure.frontdoor.Frontdoor.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.frontdoor.Frontdoor.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
