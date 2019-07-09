---
---

<div class="section" id="budgets">
<h1>budgets<a class="headerlink" href="#budgets" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.budgets"></span><dl class="class">
<dt id="pulumi_aws.budgets.Budget">
<em class="property">class </em><code class="descclassname">pulumi_aws.budgets.</code><code class="descname">Budget</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>account_id=None</em>, <em>budget_type=None</em>, <em>cost_filters=None</em>, <em>cost_types=None</em>, <em>limit_amount=None</em>, <em>limit_unit=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>notifications=None</em>, <em>time_period_end=None</em>, <em>time_period_start=None</em>, <em>time_unit=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.budgets.Budget" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a budgets budget resource. Budgets use the cost visualisation provided by Cost Explorer to show you the status of your budgets, to provide forecasts of your estimated costs, and to track your AWS usage, including your free tier usage.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the target account for budget. Will use current user’s account_id by default if omitted.</li>
<li><strong>budget_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether this budget tracks monetary cost or usage.</li>
<li><strong>cost_filters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of CostFilters key/value pairs to apply to the budget.</li>
<li><strong>cost_types</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Object containing CostTypes The types of cost included in a budget, such as tax and subscriptions..</li>
<li><strong>limit_amount</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The amount of cost or usage being measured for a budget.</li>
<li><strong>limit_unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unit of measurement used for the budget forecast, actual spend, or budget threshold, such as dollars or GB. See <a class="reference external" href="http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/data-type-spend.html">Spend</a> documentation.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a budget. Unique within accounts.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The prefix of the name of a budget. Unique within accounts.</li>
<li><strong>notifications</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Object containing Budget Notifications. Can be used multiple times to define more than one budget notification</li>
<li><strong>time_period_end</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The end of the time period covered by the budget. There are no restrictions on the end date. Format: <code class="docutils literal notranslate"><span class="pre">2017-01-01_12:00</span></code>.</li>
<li><strong>time_period_start</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The start of the time period covered by the budget. The start date must come before the end date. Format: <code class="docutils literal notranslate"><span class="pre">2017-01-01_12:00</span></code>.</li>
<li><strong>time_unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The length of time until a budget resets the actual and forecasted spend. Valid values: <code class="docutils literal notranslate"><span class="pre">MONTHLY</span></code>, <code class="docutils literal notranslate"><span class="pre">QUARTERLY</span></code>, <code class="docutils literal notranslate"><span class="pre">ANNUALLY</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/budgets_budget.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/budgets_budget.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.budgets.Budget.account_id">
<code class="descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.budgets.Budget.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the target account for budget. Will use current user’s account_id by default if omitted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.budgets.Budget.budget_type">
<code class="descname">budget_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.budgets.Budget.budget_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this budget tracks monetary cost or usage.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.budgets.Budget.cost_filters">
<code class="descname">cost_filters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.budgets.Budget.cost_filters" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of CostFilters key/value pairs to apply to the budget.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.budgets.Budget.cost_types">
<code class="descname">cost_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.budgets.Budget.cost_types" title="Permalink to this definition">¶</a></dt>
<dd><p>Object containing CostTypes The types of cost included in a budget, such as tax and subscriptions..</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.budgets.Budget.limit_amount">
<code class="descname">limit_amount</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.budgets.Budget.limit_amount" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of cost or usage being measured for a budget.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.budgets.Budget.limit_unit">
<code class="descname">limit_unit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.budgets.Budget.limit_unit" title="Permalink to this definition">¶</a></dt>
<dd><p>The unit of measurement used for the budget forecast, actual spend, or budget threshold, such as dollars or GB. See <a class="reference external" href="http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/data-type-spend.html">Spend</a> documentation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.budgets.Budget.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.budgets.Budget.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a budget. Unique within accounts.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.budgets.Budget.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.budgets.Budget.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The prefix of the name of a budget. Unique within accounts.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.budgets.Budget.notifications">
<code class="descname">notifications</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.budgets.Budget.notifications" title="Permalink to this definition">¶</a></dt>
<dd><p>Object containing Budget Notifications. Can be used multiple times to define more than one budget notification</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.budgets.Budget.time_period_end">
<code class="descname">time_period_end</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.budgets.Budget.time_period_end" title="Permalink to this definition">¶</a></dt>
<dd><p>The end of the time period covered by the budget. There are no restrictions on the end date. Format: <code class="docutils literal notranslate"><span class="pre">2017-01-01_12:00</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.budgets.Budget.time_period_start">
<code class="descname">time_period_start</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.budgets.Budget.time_period_start" title="Permalink to this definition">¶</a></dt>
<dd><p>The start of the time period covered by the budget. The start date must come before the end date. Format: <code class="docutils literal notranslate"><span class="pre">2017-01-01_12:00</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.budgets.Budget.time_unit">
<code class="descname">time_unit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.budgets.Budget.time_unit" title="Permalink to this definition">¶</a></dt>
<dd><p>The length of time until a budget resets the actual and forecasted spend. Valid values: <code class="docutils literal notranslate"><span class="pre">MONTHLY</span></code>, <code class="docutils literal notranslate"><span class="pre">QUARTERLY</span></code>, <code class="docutils literal notranslate"><span class="pre">ANNUALLY</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.budgets.Budget.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.budgets.Budget.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.budgets.Budget.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.budgets.Budget.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

</div>
