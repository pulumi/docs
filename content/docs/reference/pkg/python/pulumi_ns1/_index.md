---
title: Package pulumi_ns1
title_tag: Package pulumi_ns1 | Python SDK
linktitle: pulumi_ns1
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "ns1" >}}

<div class="section" id="pulumi-ns1">
<h1>Pulumi NS1<a class="headerlink" href="#pulumi-ns1" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-ns1">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-ns1/issues">pulumi/pulumi-ns1 repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-ns1/issues">terraform-providers/terraform-provider-ns1 repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_ns1"></span><dl class="py class">
<dt id="pulumi_ns1.APIKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">APIKey</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_account_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_apikeys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_payment_methods</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_teams</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_view_activity_log</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_view_invoices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_manage_datafeeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_manage_datasources</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_push_to_datafeeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dhcp_manage_dhcp</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dhcp_view_dhcp</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_manage_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_view_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_allow_by_default</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_allows</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_denies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_whitelist_strict</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_whitelists</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_manage_ipam</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_view_ipam</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_manage_jobs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_manage_lists</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_view_jobs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_manage_active_directory</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_manage_global2fa</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">teams</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.APIKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a APIKey resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] account_manage_account_settings: Whether the apikey can modify account settings.
:param pulumi.Input[bool] account_manage_apikeys: Whether the apikey can modify account apikeys.
:param pulumi.Input[bool] account_manage_payment_methods: Whether the apikey can modify account payment methods.
:param pulumi.Input[bool] account_manage_plan: Whether the apikey can modify the account plan.
:param pulumi.Input[bool] account_manage_teams: Whether the apikey can modify other teams in the account.
:param pulumi.Input[bool] account_manage_users: Whether the apikey can modify account users.
:param pulumi.Input[bool] account_view_activity_log: Whether the apikey can view activity logs.
:param pulumi.Input[bool] account_view_invoices: Whether the apikey can view invoices.
:param pulumi.Input[bool] data_manage_datafeeds: Whether the apikey can modify data feeds.
:param pulumi.Input[bool] data_manage_datasources: Whether the apikey can modify data sources.
:param pulumi.Input[bool] data_push_to_datafeeds: Whether the apikey can publish to data feeds.
:param pulumi.Input[bool] dhcp_manage_dhcp: Whether the apikey can manage DHCP.</p>
<blockquote>
<div><p>Only relevant for the DDI product.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dhcp_view_dhcp</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can view DHCP.
Only relevant for the DDI product.</p></li>
<li><p><strong>dns_manage_zones</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can modify the accounts zones.</p></li>
<li><p><strong>dns_view_zones</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can view the accounts zones.</p></li>
<li><p><strong>dns_zones_allow_by_default</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, enable the <code class="docutils literal notranslate"><span class="pre">dns_zones_allow</span></code> list, otherwise enable the <code class="docutils literal notranslate"><span class="pre">dns_zones_deny</span></code> list.</p></li>
<li><p><strong>dns_zones_allows</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of zones that the apikey may access.</p></li>
<li><p><strong>dns_zones_denies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of zones that the apikey may not access.</p></li>
<li><p><strong>ip_whitelist_strict</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Sets exclusivity on this IP whitelist.</p></li>
<li><p><strong>ip_whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The IP addresses to whitelist for this key.</p></li>
<li><p><strong>ipam_manage_ipam</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can manage IPAM.
Only relevant for the DDI product.</p></li>
<li><p><strong>ipam_view_ipam</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can view IPAM.
Only relevant for the DDI product.</p></li>
<li><p><strong>monitoring_manage_jobs</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can modify monitoring jobs.</p></li>
<li><p><strong>monitoring_manage_lists</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can modify notification lists.</p></li>
<li><p><strong>monitoring_view_jobs</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can view monitoring jobs.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The free form name of the apikey.</p></li>
<li><p><strong>security_manage_active_directory</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can manage global active directory.
Only relevant for the DDI product.</p></li>
<li><p><strong>security_manage_global2fa</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can manage global two factor authentication.</p></li>
<li><p><strong>teams</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The teams that the apikey belongs to.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.account_manage_account_settings">
<code class="sig-name descname">account_manage_account_settings</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.account_manage_account_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the apikey can modify account settings.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.account_manage_apikeys">
<code class="sig-name descname">account_manage_apikeys</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.account_manage_apikeys" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the apikey can modify account apikeys.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.account_manage_payment_methods">
<code class="sig-name descname">account_manage_payment_methods</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.account_manage_payment_methods" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the apikey can modify account payment methods.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.account_manage_plan">
<code class="sig-name descname">account_manage_plan</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.account_manage_plan" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the apikey can modify the account plan.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.account_manage_teams">
<code class="sig-name descname">account_manage_teams</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.account_manage_teams" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the apikey can modify other teams in the account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.account_manage_users">
<code class="sig-name descname">account_manage_users</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.account_manage_users" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the apikey can modify account users.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.account_view_activity_log">
<code class="sig-name descname">account_view_activity_log</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.account_view_activity_log" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the apikey can view activity logs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.account_view_invoices">
<code class="sig-name descname">account_view_invoices</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.account_view_invoices" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the apikey can view invoices.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.data_manage_datafeeds">
<code class="sig-name descname">data_manage_datafeeds</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.data_manage_datafeeds" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the apikey can modify data feeds.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.data_manage_datasources">
<code class="sig-name descname">data_manage_datasources</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.data_manage_datasources" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the apikey can modify data sources.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.data_push_to_datafeeds">
<code class="sig-name descname">data_push_to_datafeeds</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.data_push_to_datafeeds" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the apikey can publish to data feeds.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.dhcp_manage_dhcp">
<code class="sig-name descname">dhcp_manage_dhcp</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.dhcp_manage_dhcp" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the apikey can manage DHCP.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.dhcp_view_dhcp">
<code class="sig-name descname">dhcp_view_dhcp</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.dhcp_view_dhcp" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the apikey can view DHCP.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.dns_manage_zones">
<code class="sig-name descname">dns_manage_zones</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.dns_manage_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the apikey can modify the accounts zones.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.dns_view_zones">
<code class="sig-name descname">dns_view_zones</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.dns_view_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the apikey can view the accounts zones.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.dns_zones_allow_by_default">
<code class="sig-name descname">dns_zones_allow_by_default</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.dns_zones_allow_by_default" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, enable the <code class="docutils literal notranslate"><span class="pre">dns_zones_allow</span></code> list, otherwise enable the <code class="docutils literal notranslate"><span class="pre">dns_zones_deny</span></code> list.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.dns_zones_allows">
<code class="sig-name descname">dns_zones_allows</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.dns_zones_allows" title="Permalink to this definition">¶</a></dt>
<dd><p>List of zones that the apikey may access.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.dns_zones_denies">
<code class="sig-name descname">dns_zones_denies</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.dns_zones_denies" title="Permalink to this definition">¶</a></dt>
<dd><p>List of zones that the apikey may not access.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.ip_whitelist_strict">
<code class="sig-name descname">ip_whitelist_strict</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.ip_whitelist_strict" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets exclusivity on this IP whitelist.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.ip_whitelists">
<code class="sig-name descname">ip_whitelists</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.ip_whitelists" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP addresses to whitelist for this key.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.ipam_manage_ipam">
<code class="sig-name descname">ipam_manage_ipam</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.ipam_manage_ipam" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the apikey can manage IPAM.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.ipam_view_ipam">
<code class="sig-name descname">ipam_view_ipam</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.ipam_view_ipam" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the apikey can view IPAM.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.key">
<code class="sig-name descname">key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.key" title="Permalink to this definition">¶</a></dt>
<dd><p>The apikeys authentication token.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.monitoring_manage_jobs">
<code class="sig-name descname">monitoring_manage_jobs</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.monitoring_manage_jobs" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the apikey can modify monitoring jobs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.monitoring_manage_lists">
<code class="sig-name descname">monitoring_manage_lists</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.monitoring_manage_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the apikey can modify notification lists.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.monitoring_view_jobs">
<code class="sig-name descname">monitoring_view_jobs</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.monitoring_view_jobs" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the apikey can view monitoring jobs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The free form name of the apikey.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.security_manage_active_directory">
<code class="sig-name descname">security_manage_active_directory</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.security_manage_active_directory" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the apikey can manage global active directory.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.security_manage_global2fa">
<code class="sig-name descname">security_manage_global2fa</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.security_manage_global2fa" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the apikey can manage global two factor authentication.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.APIKey.teams">
<code class="sig-name descname">teams</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.APIKey.teams" title="Permalink to this definition">¶</a></dt>
<dd><p>The teams that the apikey belongs to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_account_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_apikeys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_payment_methods</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_teams</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_view_activity_log</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_view_invoices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_manage_datafeeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_manage_datasources</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_push_to_datafeeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dhcp_manage_dhcp</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dhcp_view_dhcp</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_manage_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_view_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_allow_by_default</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_allows</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_denies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_whitelist_strict</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_whitelists</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_manage_ipam</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_view_ipam</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_manage_jobs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_manage_lists</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_view_jobs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_manage_active_directory</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_manage_global2fa</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">teams</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.APIKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing APIKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_manage_account_settings</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can modify account settings.</p></li>
<li><p><strong>account_manage_apikeys</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can modify account apikeys.</p></li>
<li><p><strong>account_manage_payment_methods</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can modify account payment methods.</p></li>
<li><p><strong>account_manage_plan</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can modify the account plan.</p></li>
<li><p><strong>account_manage_teams</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can modify other teams in the account.</p></li>
<li><p><strong>account_manage_users</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can modify account users.</p></li>
<li><p><strong>account_view_activity_log</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can view activity logs.</p></li>
<li><p><strong>account_view_invoices</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can view invoices.</p></li>
<li><p><strong>data_manage_datafeeds</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can modify data feeds.</p></li>
<li><p><strong>data_manage_datasources</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can modify data sources.</p></li>
<li><p><strong>data_push_to_datafeeds</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can publish to data feeds.</p></li>
<li><p><strong>dhcp_manage_dhcp</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can manage DHCP.
Only relevant for the DDI product.</p></li>
<li><p><strong>dhcp_view_dhcp</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can view DHCP.
Only relevant for the DDI product.</p></li>
<li><p><strong>dns_manage_zones</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can modify the accounts zones.</p></li>
<li><p><strong>dns_view_zones</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can view the accounts zones.</p></li>
<li><p><strong>dns_zones_allow_by_default</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, enable the <code class="docutils literal notranslate"><span class="pre">dns_zones_allow</span></code> list, otherwise enable the <code class="docutils literal notranslate"><span class="pre">dns_zones_deny</span></code> list.</p></li>
<li><p><strong>dns_zones_allows</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of zones that the apikey may access.</p></li>
<li><p><strong>dns_zones_denies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of zones that the apikey may not access.</p></li>
<li><p><strong>ip_whitelist_strict</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Sets exclusivity on this IP whitelist.</p></li>
<li><p><strong>ip_whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The IP addresses to whitelist for this key.</p></li>
<li><p><strong>ipam_manage_ipam</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can manage IPAM.
Only relevant for the DDI product.</p></li>
<li><p><strong>ipam_view_ipam</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can view IPAM.
Only relevant for the DDI product.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The apikeys authentication token.</p></li>
<li><p><strong>monitoring_manage_jobs</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can modify monitoring jobs.</p></li>
<li><p><strong>monitoring_manage_lists</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can modify notification lists.</p></li>
<li><p><strong>monitoring_view_jobs</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can view monitoring jobs.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The free form name of the apikey.</p></li>
<li><p><strong>security_manage_active_directory</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can manage global active directory.
Only relevant for the DDI product.</p></li>
<li><p><strong>security_manage_global2fa</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the apikey can manage global two factor authentication.</p></li>
<li><p><strong>teams</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The teams that the apikey belongs to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.APIKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.APIKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_ns1.APIKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.APIKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_ns1.AwaitableGetDNSSecResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">AwaitableGetDNSSecResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">delegation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.AwaitableGetDNSSecResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_ns1.AwaitableGetZoneResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">AwaitableGetZoneResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">additional_primaries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dnssec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostmaster</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">link</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">networks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nx_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondaries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.AwaitableGetZoneResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_ns1.DataFeed">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">DataFeed</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.DataFeed" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a NS1 Data Feed resource. This can be used to create, modify, and delete data feeds.</p>
<p><a class="reference external" href="https://ns1.com/api#data-feeds">Datafeed Api Doc</a></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The feeds configuration matching the specification in
<code class="docutils literal notranslate"><span class="pre">feed_config</span></code> from /data/sourcetypes.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The free form name of the data feed.</p></li>
<li><p><strong>source_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data source id that this feed is connected to.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_ns1.DataFeed.config">
<code class="sig-name descname">config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.DataFeed.config" title="Permalink to this definition">¶</a></dt>
<dd><p>The feeds configuration matching the specification in
<code class="docutils literal notranslate"><span class="pre">feed_config</span></code> from /data/sourcetypes.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.DataFeed.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.DataFeed.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The free form name of the data feed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.DataFeed.source_id">
<code class="sig-name descname">source_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.DataFeed.source_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The data source id that this feed is connected to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.DataFeed.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.DataFeed.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DataFeed resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The feeds configuration matching the specification in
<code class="docutils literal notranslate"><span class="pre">feed_config</span></code> from /data/sourcetypes.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The free form name of the data feed.</p></li>
<li><p><strong>source_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data source id that this feed is connected to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.DataFeed.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.DataFeed.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_ns1.DataFeed.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.DataFeed.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_ns1.DataSource">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">DataSource</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sourcetype</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.DataSource" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a NS1 Data Source resource. This can be used to create, modify, and delete data sources.</p>
<p><a class="reference external" href="https://ns1.com/api#data-sources">Datasource Api Doc</a></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The data source configuration, determined by its type,
matching the specification in <code class="docutils literal notranslate"><span class="pre">config</span></code> from /data/sourcetypes.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The free form name of the data source.</p></li>
<li><p><strong>sourcetype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data sources type, listed in API endpoint <a class="reference external" href="https://api.nsone.net/v1/data/sourcetypes">https://api.nsone.net/v1/data/sourcetypes</a>.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_ns1.DataSource.config">
<code class="sig-name descname">config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.DataSource.config" title="Permalink to this definition">¶</a></dt>
<dd><p>The data source configuration, determined by its type,
matching the specification in <code class="docutils literal notranslate"><span class="pre">config</span></code> from /data/sourcetypes.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.DataSource.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.DataSource.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The free form name of the data source.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.DataSource.sourcetype">
<code class="sig-name descname">sourcetype</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.DataSource.sourcetype" title="Permalink to this definition">¶</a></dt>
<dd><p>The data sources type, listed in API endpoint <a class="reference external" href="https://api.nsone.net/v1/data/sourcetypes">https://api.nsone.net/v1/data/sourcetypes</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.DataSource.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sourcetype</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.DataSource.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DataSource resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The data source configuration, determined by its type,
matching the specification in <code class="docutils literal notranslate"><span class="pre">config</span></code> from /data/sourcetypes.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The free form name of the data source.</p></li>
<li><p><strong>sourcetype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data sources type, listed in API endpoint <a class="reference external" href="https://api.nsone.net/v1/data/sourcetypes">https://api.nsone.net/v1/data/sourcetypes</a>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.DataSource.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.DataSource.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_ns1.DataSource.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.DataSource.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_ns1.GetDNSSecResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">GetDNSSecResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">delegation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.GetDNSSecResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDNSSec.</p>
<dl class="py attribute">
<dt id="pulumi_ns1.GetDNSSecResult.delegation">
<code class="sig-name descname">delegation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.GetDNSSecResult.delegation" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) - Delegation field is documented
below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.GetDNSSecResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.GetDNSSecResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.GetDNSSecResult.keys">
<code class="sig-name descname">keys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.GetDNSSecResult.keys" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) - Keys field is documented below.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_ns1.GetZoneResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">GetZoneResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">additional_primaries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dnssec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostmaster</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">link</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">networks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nx_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondaries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.GetZoneResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getZone.</p>
<dl class="py attribute">
<dt id="pulumi_ns1.GetZoneResult.additional_primaries">
<code class="sig-name descname">additional_primaries</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.GetZoneResult.additional_primaries" title="Permalink to this definition">¶</a></dt>
<dd><p>List of additional IPv4 addresses for the primary
zone.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.GetZoneResult.dns_servers">
<code class="sig-name descname">dns_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.GetZoneResult.dns_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>Authoritative Name Servers.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.GetZoneResult.dnssec">
<code class="sig-name descname">dnssec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.GetZoneResult.dnssec" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not DNSSEC is enabled for the zone.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.GetZoneResult.expiry">
<code class="sig-name descname">expiry</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.GetZoneResult.expiry" title="Permalink to this definition">¶</a></dt>
<dd><p>The SOA Expiry.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.GetZoneResult.hostmaster">
<code class="sig-name descname">hostmaster</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.GetZoneResult.hostmaster" title="Permalink to this definition">¶</a></dt>
<dd><p>The SOA Hostmaster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.GetZoneResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.GetZoneResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.GetZoneResult.link">
<code class="sig-name descname">link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.GetZoneResult.link" title="Permalink to this definition">¶</a></dt>
<dd><p>The linked target zone.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.GetZoneResult.networks">
<code class="sig-name descname">networks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.GetZoneResult.networks" title="Permalink to this definition">¶</a></dt>
<dd><p>List of network IDs (<code class="docutils literal notranslate"><span class="pre">int</span></code>) for which the zone should be made
available. Default is network 0, the primary NSONE Global Network.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.GetZoneResult.nx_ttl">
<code class="sig-name descname">nx_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.GetZoneResult.nx_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The SOA NX TTL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.GetZoneResult.primary">
<code class="sig-name descname">primary</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.GetZoneResult.primary" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary zones’ IPv4 address.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.GetZoneResult.refresh">
<code class="sig-name descname">refresh</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.GetZoneResult.refresh" title="Permalink to this definition">¶</a></dt>
<dd><p>The SOA Refresh.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.GetZoneResult.retry">
<code class="sig-name descname">retry</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.GetZoneResult.retry" title="Permalink to this definition">¶</a></dt>
<dd><p>The SOA Retry.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.GetZoneResult.secondaries">
<code class="sig-name descname">secondaries</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.GetZoneResult.secondaries" title="Permalink to this definition">¶</a></dt>
<dd><p>List of secondary servers. Secondaries is
documented below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.GetZoneResult.ttl">
<code class="sig-name descname">ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.GetZoneResult.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The SOA TTL.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_ns1.MonitoringJob">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">MonitoringJob</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frequency</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">job_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_delay</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_failback</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_list</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_regional</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_repeat</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rapid_recheck</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">regions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.MonitoringJob" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a NS1 Monitoring Job resource. This can be used to create, modify, and delete monitoring jobs.</p>
<p><a class="reference external" href="https://ns1.com/api#monitoring-jobs">MonitoringJob Api Doc</a></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates if the job is active or temporarily disabled.</p></li>
<li><p><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A configuration dictionary with keys and values depending on the jobs’ type.</p></li>
<li><p><strong>frequency</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The frequency, in seconds, at which to run the monitoring job in each region.</p></li>
<li><p><strong>job_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of monitoring job to be run. See NS1 API
docs for supported values.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The free-form display name for the monitoring job.</p></li>
<li><p><strong>notes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Freeform notes to be included in any notifications about this job.</p></li>
<li><p><strong>notify_delay</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time in seconds after a failure to wait before sending a notification.</p></li>
<li><p><strong>notify_failback</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, a notification is sent when a job returns to an “up” state.</p></li>
<li><p><strong>notify_list</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the notification list to send notifications to.</p></li>
<li><p><strong>notify_regional</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, notifications are sent for any regional failure (and failback if desired), in addition to global state notifications.</p></li>
<li><p><strong>notify_repeat</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time in seconds between repeat notifications of a failed job.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy for determining the monitor’s global status
based on the status of the job in all regions. See NS1 API docs for supported values.</p></li>
<li><p><strong>rapid_recheck</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, on any apparent state change, the job is quickly re-run after one second to confirm the state change before notification.</p></li>
<li><p><strong>regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of region codes in which to run the monitoring
job. See NS1 API docs for supported values.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of rules for determining failure conditions. Job Rules are documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comparison</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The comparison to perform on the the output.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The output key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value to compare to.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_ns1.MonitoringJob.active">
<code class="sig-name descname">active</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.MonitoringJob.active" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates if the job is active or temporarily disabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.MonitoringJob.config">
<code class="sig-name descname">config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.MonitoringJob.config" title="Permalink to this definition">¶</a></dt>
<dd><p>A configuration dictionary with keys and values depending on the jobs’ type.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.MonitoringJob.frequency">
<code class="sig-name descname">frequency</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.MonitoringJob.frequency" title="Permalink to this definition">¶</a></dt>
<dd><p>The frequency, in seconds, at which to run the monitoring job in each region.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.MonitoringJob.job_type">
<code class="sig-name descname">job_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.MonitoringJob.job_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of monitoring job to be run. See NS1 API
docs for supported values.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.MonitoringJob.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.MonitoringJob.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The free-form display name for the monitoring job.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.MonitoringJob.notes">
<code class="sig-name descname">notes</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.MonitoringJob.notes" title="Permalink to this definition">¶</a></dt>
<dd><p>Freeform notes to be included in any notifications about this job.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.MonitoringJob.notify_delay">
<code class="sig-name descname">notify_delay</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.MonitoringJob.notify_delay" title="Permalink to this definition">¶</a></dt>
<dd><p>The time in seconds after a failure to wait before sending a notification.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.MonitoringJob.notify_failback">
<code class="sig-name descname">notify_failback</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.MonitoringJob.notify_failback" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, a notification is sent when a job returns to an “up” state.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.MonitoringJob.notify_list">
<code class="sig-name descname">notify_list</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.MonitoringJob.notify_list" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the notification list to send notifications to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.MonitoringJob.notify_regional">
<code class="sig-name descname">notify_regional</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.MonitoringJob.notify_regional" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, notifications are sent for any regional failure (and failback if desired), in addition to global state notifications.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.MonitoringJob.notify_repeat">
<code class="sig-name descname">notify_repeat</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.MonitoringJob.notify_repeat" title="Permalink to this definition">¶</a></dt>
<dd><p>The time in seconds between repeat notifications of a failed job.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.MonitoringJob.policy">
<code class="sig-name descname">policy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.MonitoringJob.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy for determining the monitor’s global status
based on the status of the job in all regions. See NS1 API docs for supported values.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.MonitoringJob.rapid_recheck">
<code class="sig-name descname">rapid_recheck</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.MonitoringJob.rapid_recheck" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, on any apparent state change, the job is quickly re-run after one second to confirm the state change before notification.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.MonitoringJob.regions">
<code class="sig-name descname">regions</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.MonitoringJob.regions" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of region codes in which to run the monitoring
job. See NS1 API docs for supported values.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.MonitoringJob.rules">
<code class="sig-name descname">rules</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.MonitoringJob.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of rules for determining failure conditions. Job Rules are documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comparison</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The comparison to perform on the the output.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The output key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value to compare to.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.MonitoringJob.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frequency</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">job_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_delay</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_failback</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_list</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_regional</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_repeat</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rapid_recheck</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">regions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.MonitoringJob.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MonitoringJob resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates if the job is active or temporarily disabled.</p></li>
<li><p><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A configuration dictionary with keys and values depending on the jobs’ type.</p></li>
<li><p><strong>frequency</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The frequency, in seconds, at which to run the monitoring job in each region.</p></li>
<li><p><strong>job_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of monitoring job to be run. See NS1 API
docs for supported values.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The free-form display name for the monitoring job.</p></li>
<li><p><strong>notes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Freeform notes to be included in any notifications about this job.</p></li>
<li><p><strong>notify_delay</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time in seconds after a failure to wait before sending a notification.</p></li>
<li><p><strong>notify_failback</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, a notification is sent when a job returns to an “up” state.</p></li>
<li><p><strong>notify_list</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the notification list to send notifications to.</p></li>
<li><p><strong>notify_regional</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, notifications are sent for any regional failure (and failback if desired), in addition to global state notifications.</p></li>
<li><p><strong>notify_repeat</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time in seconds between repeat notifications of a failed job.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy for determining the monitor’s global status
based on the status of the job in all regions. See NS1 API docs for supported values.</p></li>
<li><p><strong>rapid_recheck</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, on any apparent state change, the job is quickly re-run after one second to confirm the state change before notification.</p></li>
<li><p><strong>regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of region codes in which to run the monitoring
job. See NS1 API docs for supported values.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of rules for determining failure conditions. Job Rules are documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comparison</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The comparison to perform on the the output.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The output key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value to compare to.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.MonitoringJob.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.MonitoringJob.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_ns1.MonitoringJob.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.MonitoringJob.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_ns1.NotifyList">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">NotifyList</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifications</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.NotifyList" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a NS1 Notify List resource. This can be used to create, modify, and delete notify lists.</p>
<p><a class="reference external" href="https://ns1.com/api#notification-lists">NotifyList Api Doc</a></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The free-form display name for the notify list.</p></li>
<li><p><strong>notifications</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of notifiers. All notifiers in a notification list will receive notifications whenever an event is send to the list (e.g., when a monitoring job fails). Notifiers are documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>notifications</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration details for the given notifier type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of notifier. Available notifiers are indicated in /notifytypes endpoint.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_ns1.NotifyList.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.NotifyList.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The free-form display name for the notify list.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.NotifyList.notifications">
<code class="sig-name descname">notifications</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.NotifyList.notifications" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of notifiers. All notifiers in a notification list will receive notifications whenever an event is send to the list (e.g., when a monitoring job fails). Notifiers are documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">config</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Configuration details for the given notifier type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of notifier. Available notifiers are indicated in /notifytypes endpoint.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.NotifyList.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifications</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.NotifyList.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NotifyList resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The free-form display name for the notify list.</p></li>
<li><p><strong>notifications</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of notifiers. All notifiers in a notification list will receive notifications whenever an event is send to the list (e.g., when a monitoring job fails). Notifiers are documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>notifications</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration details for the given notifier type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of notifier. Available notifiers are indicated in /notifytypes endpoint.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.NotifyList.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.NotifyList.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_ns1.NotifyList.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.NotifyList.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_ns1.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">apikey</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_ddi</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_ssl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rate_limit_parallelism</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the ns1 package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>apikey</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ns1 API key, this is required</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_ns1.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_ns1.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_ns1.Record">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">Record</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">answers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">link</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">meta</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">regions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">short_answers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_client_subnet</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Record" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a NS1 Record resource. This can be used to create, modify, and delete records.</p>
<p><a class="reference external" href="https://ns1.com/api#records">Record Api Doc</a></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>answers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more NS1 answers for the records’ specified type.
Answers are documented below.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The records’ domain. Cannot have leading or trailing
dots - see the example above and <code class="docutils literal notranslate"><span class="pre">FQDN</span> <span class="pre">formatting</span></code> below.</p></li>
<li><p><strong>filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more NS1 filters for the record(order matters).
Filters are documented below.</p></li>
<li><p><strong>link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target record to link to. This means this record is a
‘linked’ record, and it inherits all properties from its target.</p></li>
<li><p><strong>regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more “regions” for the record. These are really
just groupings based on metadata, and are called “Answer Groups” in the NS1 UI,
but remain <code class="docutils literal notranslate"><span class="pre">regions</span></code> here for legacy reasons. Regions are
documented below. Please note the ordering requirement!</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The records’ time to live.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The records’ RR type.</p></li>
<li><p><strong>use_client_subnet</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EDNS client subnet data when
available(in filter chain).</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* ` meta` - (Optional) meta is supported at the `record` level. Meta
is documented below.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone the record belongs to. Cannot have leading or
trailing dots (“.”) - see the example above and <code class="docutils literal notranslate"><span class="pre">FQDN</span> <span class="pre">formatting</span></code> below.</p>
</dd>
</dl>
<p>The <strong>answers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">answer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Space delimited string of RDATA fields dependent on the record type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">meta</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region (Answer Group really) that this answer
belongs to. This should be one of the names specified in <code class="docutils literal notranslate"><span class="pre">regions</span></code>. Only a
single <code class="docutils literal notranslate"><span class="pre">region</span></code> per answer is currently supported. If you want an answer in
multiple regions, duplicating the answer (including metadata) is the correct
approach.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">meta</span></code> - (Optional) meta is supported at the <code class="docutils literal notranslate"><span class="pre">answer</span></code> level. Meta
is documented below.</p></li>
</ul>
</li>
</ul>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The filters’ configuration. Simple key/value pairs
determined by the filter type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Determines whether the filter is applied in the
filter chain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of filter.</p></li>
</ul>
<p>The <strong>regions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">meta</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the region (or Answer Group).</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_ns1.Record.answers">
<code class="sig-name descname">answers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Record.answers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more NS1 answers for the records’ specified type.
Answers are documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">answer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Space delimited string of RDATA fields dependent on the record type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">meta</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The region (Answer Group really) that this answer
belongs to. This should be one of the names specified in <code class="docutils literal notranslate"><span class="pre">regions</span></code>. Only a
single <code class="docutils literal notranslate"><span class="pre">region</span></code> per answer is currently supported. If you want an answer in
multiple regions, duplicating the answer (including metadata) is the correct
approach.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">meta</span></code> - (Optional) meta is supported at the <code class="docutils literal notranslate"><span class="pre">answer</span></code> level. Meta
is documented below.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Record.domain">
<code class="sig-name descname">domain</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Record.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The records’ domain. Cannot have leading or trailing
dots - see the example above and <code class="docutils literal notranslate"><span class="pre">FQDN</span> <span class="pre">formatting</span></code> below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Record.filters">
<code class="sig-name descname">filters</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Record.filters" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more NS1 filters for the record(order matters).
Filters are documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">config</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The filters’ configuration. Simple key/value pairs
determined by the filter type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Determines whether the filter is applied in the
filter chain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of filter.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Record.link">
<code class="sig-name descname">link</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Record.link" title="Permalink to this definition">¶</a></dt>
<dd><p>The target record to link to. This means this record is a
‘linked’ record, and it inherits all properties from its target.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Record.regions">
<code class="sig-name descname">regions</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Record.regions" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more “regions” for the record. These are really
just groupings based on metadata, and are called “Answer Groups” in the NS1 UI,
but remain <code class="docutils literal notranslate"><span class="pre">regions</span></code> here for legacy reasons. Regions are
documented below. Please note the ordering requirement!</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">meta</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the region (or Answer Group).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Record.ttl">
<code class="sig-name descname">ttl</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Record.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The records’ time to live.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Record.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Record.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The records’ RR type.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Record.use_client_subnet">
<code class="sig-name descname">use_client_subnet</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Record.use_client_subnet" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use EDNS client subnet data when
available(in filter chain).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">meta</span></code> - (Optional) meta is supported at the <code class="docutils literal notranslate"><span class="pre">record</span></code> level. Meta
is documented below.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Record.zone">
<code class="sig-name descname">zone</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Record.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone the record belongs to. Cannot have leading or
trailing dots (“.”) - see the example above and <code class="docutils literal notranslate"><span class="pre">FQDN</span> <span class="pre">formatting</span></code> below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Record.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">answers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">link</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">meta</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">regions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">short_answers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_client_subnet</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Record.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Record resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>answers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more NS1 answers for the records’ specified type.
Answers are documented below.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The records’ domain. Cannot have leading or trailing
dots - see the example above and <code class="docutils literal notranslate"><span class="pre">FQDN</span> <span class="pre">formatting</span></code> below.</p></li>
<li><p><strong>filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more NS1 filters for the record(order matters).
Filters are documented below.</p></li>
<li><p><strong>link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target record to link to. This means this record is a
‘linked’ record, and it inherits all properties from its target.</p></li>
<li><p><strong>regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more “regions” for the record. These are really
just groupings based on metadata, and are called “Answer Groups” in the NS1 UI,
but remain <code class="docutils literal notranslate"><span class="pre">regions</span></code> here for legacy reasons. Regions are
documented below. Please note the ordering requirement!</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The records’ time to live.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The records’ RR type.</p></li>
<li><p><strong>use_client_subnet</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use EDNS client subnet data when
available(in filter chain).</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* ` meta` - (Optional) meta is supported at the `record` level. Meta
is documented below.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone the record belongs to. Cannot have leading or
trailing dots (“.”) - see the example above and <code class="docutils literal notranslate"><span class="pre">FQDN</span> <span class="pre">formatting</span></code> below.</p>
</dd>
</dl>
<p>The <strong>answers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">answer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Space delimited string of RDATA fields dependent on the record type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">meta</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region (Answer Group really) that this answer
belongs to. This should be one of the names specified in <code class="docutils literal notranslate"><span class="pre">regions</span></code>. Only a
single <code class="docutils literal notranslate"><span class="pre">region</span></code> per answer is currently supported. If you want an answer in
multiple regions, duplicating the answer (including metadata) is the correct
approach.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">meta</span></code> - (Optional) meta is supported at the <code class="docutils literal notranslate"><span class="pre">answer</span></code> level. Meta
is documented below.</p></li>
</ul>
</li>
</ul>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The filters’ configuration. Simple key/value pairs
determined by the filter type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Determines whether the filter is applied in the
filter chain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of filter.</p></li>
</ul>
<p>The <strong>regions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">meta</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the region (or Answer Group).</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Record.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Record.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_ns1.Record.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Record.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_ns1.Team">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">Team</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_account_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_apikeys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_payment_methods</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_teams</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_view_activity_log</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_view_invoices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_manage_datafeeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_manage_datasources</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_push_to_datafeeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dhcp_manage_dhcp</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dhcp_view_dhcp</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_manage_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_view_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_allow_by_default</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_allows</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_denies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_whitelists</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_manage_ipam</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_view_ipam</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_manage_jobs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_manage_lists</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_view_jobs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_manage_active_directory</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_manage_global2fa</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Team" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a NS1 Team resource. This can be used to create, modify, and delete
teams. The credentials used must have the <code class="docutils literal notranslate"><span class="pre">manage_teams</span></code> permission set.</p>
<p><a class="reference external" href="https://ns1.com/api#team">Team Api Docs</a></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_manage_account_settings</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can modify account settings.</p></li>
<li><p><strong>account_manage_apikeys</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can modify account apikeys.</p></li>
<li><p><strong>account_manage_payment_methods</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can modify account payment methods.</p></li>
<li><p><strong>account_manage_plan</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can modify the account plan.</p></li>
<li><p><strong>account_manage_teams</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can modify other teams in the account.</p></li>
<li><p><strong>account_manage_users</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can modify account users.</p></li>
<li><p><strong>account_view_activity_log</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can view activity logs.</p></li>
<li><p><strong>account_view_invoices</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can view invoices.</p></li>
<li><p><strong>data_manage_datafeeds</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can modify data feeds.</p></li>
<li><p><strong>data_manage_datasources</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can modify data sources.</p></li>
<li><p><strong>data_push_to_datafeeds</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can publish to data feeds.</p></li>
<li><p><strong>dhcp_manage_dhcp</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can manage DHCP.
Only relevant for the DDI product.</p></li>
<li><p><strong>dhcp_view_dhcp</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can view DHCP.
Only relevant for the DDI product.</p></li>
<li><p><strong>dns_manage_zones</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can modify the accounts zones.</p></li>
<li><p><strong>dns_view_zones</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can view the accounts zones.</p></li>
<li><p><strong>dns_zones_allow_by_default</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, enable the <code class="docutils literal notranslate"><span class="pre">dns_zones_allow</span></code> list, otherwise enable the <code class="docutils literal notranslate"><span class="pre">dns_zones_deny</span></code> list.</p></li>
<li><p><strong>dns_zones_allows</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of zones that the team may access.</p></li>
<li><p><strong>dns_zones_denies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of zones that the team may not access.</p></li>
<li><p><strong>ip_whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The IP addresses to whitelist for this key.</p></li>
<li><p><strong>ipam_manage_ipam</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can manage IPAM.
Only relevant for the DDI product.</p></li>
<li><p><strong>ipam_view_ipam</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can view IPAM.
Only relevant for the DDI product.</p></li>
<li><p><strong>monitoring_manage_jobs</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can modify monitoring jobs.</p></li>
<li><p><strong>monitoring_manage_lists</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can modify notification lists.</p></li>
<li><p><strong>monitoring_view_jobs</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can view monitoring jobs.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The free form name of the team.</p></li>
<li><p><strong>security_manage_active_directory</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can manage global active directory.
Only relevant for the DDI product.</p></li>
<li><p><strong>security_manage_global2fa</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can manage global two factor authentication.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ip_whitelists</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The free form name of the team.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_ns1.Team.account_manage_account_settings">
<code class="sig-name descname">account_manage_account_settings</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.account_manage_account_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the team can modify account settings.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Team.account_manage_apikeys">
<code class="sig-name descname">account_manage_apikeys</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.account_manage_apikeys" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the team can modify account apikeys.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Team.account_manage_payment_methods">
<code class="sig-name descname">account_manage_payment_methods</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.account_manage_payment_methods" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the team can modify account payment methods.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Team.account_manage_plan">
<code class="sig-name descname">account_manage_plan</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.account_manage_plan" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the team can modify the account plan.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Team.account_manage_teams">
<code class="sig-name descname">account_manage_teams</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.account_manage_teams" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the team can modify other teams in the account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Team.account_manage_users">
<code class="sig-name descname">account_manage_users</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.account_manage_users" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the team can modify account users.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Team.account_view_activity_log">
<code class="sig-name descname">account_view_activity_log</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.account_view_activity_log" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the team can view activity logs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Team.account_view_invoices">
<code class="sig-name descname">account_view_invoices</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.account_view_invoices" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the team can view invoices.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Team.data_manage_datafeeds">
<code class="sig-name descname">data_manage_datafeeds</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.data_manage_datafeeds" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the team can modify data feeds.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Team.data_manage_datasources">
<code class="sig-name descname">data_manage_datasources</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.data_manage_datasources" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the team can modify data sources.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Team.data_push_to_datafeeds">
<code class="sig-name descname">data_push_to_datafeeds</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.data_push_to_datafeeds" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the team can publish to data feeds.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Team.dhcp_manage_dhcp">
<code class="sig-name descname">dhcp_manage_dhcp</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.dhcp_manage_dhcp" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the team can manage DHCP.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Team.dhcp_view_dhcp">
<code class="sig-name descname">dhcp_view_dhcp</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.dhcp_view_dhcp" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the team can view DHCP.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Team.dns_manage_zones">
<code class="sig-name descname">dns_manage_zones</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.dns_manage_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the team can modify the accounts zones.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Team.dns_view_zones">
<code class="sig-name descname">dns_view_zones</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.dns_view_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the team can view the accounts zones.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Team.dns_zones_allow_by_default">
<code class="sig-name descname">dns_zones_allow_by_default</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.dns_zones_allow_by_default" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, enable the <code class="docutils literal notranslate"><span class="pre">dns_zones_allow</span></code> list, otherwise enable the <code class="docutils literal notranslate"><span class="pre">dns_zones_deny</span></code> list.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Team.dns_zones_allows">
<code class="sig-name descname">dns_zones_allows</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.dns_zones_allows" title="Permalink to this definition">¶</a></dt>
<dd><p>List of zones that the team may access.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Team.dns_zones_denies">
<code class="sig-name descname">dns_zones_denies</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.dns_zones_denies" title="Permalink to this definition">¶</a></dt>
<dd><p>List of zones that the team may not access.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Team.ip_whitelists">
<code class="sig-name descname">ip_whitelists</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.ip_whitelists" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP addresses to whitelist for this key.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The free form name of the team.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Team.ipam_manage_ipam">
<code class="sig-name descname">ipam_manage_ipam</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.ipam_manage_ipam" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the team can manage IPAM.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Team.ipam_view_ipam">
<code class="sig-name descname">ipam_view_ipam</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.ipam_view_ipam" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the team can view IPAM.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Team.monitoring_manage_jobs">
<code class="sig-name descname">monitoring_manage_jobs</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.monitoring_manage_jobs" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the team can modify monitoring jobs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Team.monitoring_manage_lists">
<code class="sig-name descname">monitoring_manage_lists</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.monitoring_manage_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the team can modify notification lists.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Team.monitoring_view_jobs">
<code class="sig-name descname">monitoring_view_jobs</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.monitoring_view_jobs" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the team can view monitoring jobs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Team.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The free form name of the team.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Team.security_manage_active_directory">
<code class="sig-name descname">security_manage_active_directory</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.security_manage_active_directory" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the team can manage global active directory.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Team.security_manage_global2fa">
<code class="sig-name descname">security_manage_global2fa</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Team.security_manage_global2fa" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the team can manage global two factor authentication.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_account_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_apikeys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_payment_methods</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_teams</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_view_activity_log</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_view_invoices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_manage_datafeeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_manage_datasources</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_push_to_datafeeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dhcp_manage_dhcp</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dhcp_view_dhcp</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_manage_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_view_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_allow_by_default</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_allows</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_denies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_whitelists</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_manage_ipam</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_view_ipam</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_manage_jobs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_manage_lists</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_view_jobs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_manage_active_directory</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_manage_global2fa</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Team.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Team resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_manage_account_settings</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can modify account settings.</p></li>
<li><p><strong>account_manage_apikeys</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can modify account apikeys.</p></li>
<li><p><strong>account_manage_payment_methods</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can modify account payment methods.</p></li>
<li><p><strong>account_manage_plan</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can modify the account plan.</p></li>
<li><p><strong>account_manage_teams</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can modify other teams in the account.</p></li>
<li><p><strong>account_manage_users</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can modify account users.</p></li>
<li><p><strong>account_view_activity_log</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can view activity logs.</p></li>
<li><p><strong>account_view_invoices</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can view invoices.</p></li>
<li><p><strong>data_manage_datafeeds</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can modify data feeds.</p></li>
<li><p><strong>data_manage_datasources</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can modify data sources.</p></li>
<li><p><strong>data_push_to_datafeeds</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can publish to data feeds.</p></li>
<li><p><strong>dhcp_manage_dhcp</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can manage DHCP.
Only relevant for the DDI product.</p></li>
<li><p><strong>dhcp_view_dhcp</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can view DHCP.
Only relevant for the DDI product.</p></li>
<li><p><strong>dns_manage_zones</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can modify the accounts zones.</p></li>
<li><p><strong>dns_view_zones</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can view the accounts zones.</p></li>
<li><p><strong>dns_zones_allow_by_default</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, enable the <code class="docutils literal notranslate"><span class="pre">dns_zones_allow</span></code> list, otherwise enable the <code class="docutils literal notranslate"><span class="pre">dns_zones_deny</span></code> list.</p></li>
<li><p><strong>dns_zones_allows</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of zones that the team may access.</p></li>
<li><p><strong>dns_zones_denies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of zones that the team may not access.</p></li>
<li><p><strong>ip_whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The IP addresses to whitelist for this key.</p></li>
<li><p><strong>ipam_manage_ipam</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can manage IPAM.
Only relevant for the DDI product.</p></li>
<li><p><strong>ipam_view_ipam</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can view IPAM.
Only relevant for the DDI product.</p></li>
<li><p><strong>monitoring_manage_jobs</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can modify monitoring jobs.</p></li>
<li><p><strong>monitoring_manage_lists</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can modify notification lists.</p></li>
<li><p><strong>monitoring_view_jobs</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can view monitoring jobs.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The free form name of the team.</p></li>
<li><p><strong>security_manage_active_directory</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can manage global active directory.
Only relevant for the DDI product.</p></li>
<li><p><strong>security_manage_global2fa</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the team can manage global two factor authentication.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ip_whitelists</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The free form name of the team.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Team.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Team.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_ns1.Team.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Team.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_ns1.User">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_account_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_apikeys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_payment_methods</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_teams</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_view_activity_log</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_view_invoices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_manage_datafeeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_manage_datasources</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_push_to_datafeeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dhcp_manage_dhcp</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dhcp_view_dhcp</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_manage_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_view_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_allow_by_default</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_allows</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_denies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_whitelist_strict</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_whitelists</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_manage_ipam</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_view_ipam</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_manage_jobs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_manage_lists</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_view_jobs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_manage_active_directory</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_manage_global2fa</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">teams</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a User resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] account_manage_account_settings: Whether the user can modify account settings.
:param pulumi.Input[bool] account_manage_apikeys: Whether the user can modify account apikeys.
:param pulumi.Input[bool] account_manage_payment_methods: Whether the user can modify account payment methods.
:param pulumi.Input[bool] account_manage_plan: Whether the user can modify the account plan.
:param pulumi.Input[bool] account_manage_teams: Whether the user can modify other teams in the account.
:param pulumi.Input[bool] account_manage_users: Whether the user can modify account users.
:param pulumi.Input[bool] account_view_activity_log: Whether the user can view activity logs.
:param pulumi.Input[bool] account_view_invoices: Whether the user can view invoices.
:param pulumi.Input[bool] data_manage_datafeeds: Whether the user can modify data feeds.
:param pulumi.Input[bool] data_manage_datasources: Whether the user can modify data sources.
:param pulumi.Input[bool] data_push_to_datafeeds: Whether the user can publish to data feeds.
:param pulumi.Input[bool] dhcp_manage_dhcp: Whether the user can manage DHCP.</p>
<blockquote>
<div><p>Only relevant for the DDI product.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dhcp_view_dhcp</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can view DHCP.
Only relevant for the DDI product.</p></li>
<li><p><strong>dns_manage_zones</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can modify the accounts zones.</p></li>
<li><p><strong>dns_view_zones</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can view the accounts zones.</p></li>
<li><p><strong>dns_zones_allow_by_default</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, enable the <code class="docutils literal notranslate"><span class="pre">dns_zones_allow</span></code> list, otherwise enable the <code class="docutils literal notranslate"><span class="pre">dns_zones_deny</span></code> list.</p></li>
<li><p><strong>dns_zones_allows</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of zones that the user may access.</p></li>
<li><p><strong>dns_zones_denies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of zones that the user may not access.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address of the user.</p></li>
<li><p><strong>ip_whitelist_strict</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Sets exclusivity on this IP whitelist.</p></li>
<li><p><strong>ip_whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The IP addresses to whitelist for this key.</p></li>
<li><p><strong>ipam_manage_ipam</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can manage IPAM.
Only relevant for the DDI product.</p></li>
<li><p><strong>monitoring_manage_jobs</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can modify monitoring jobs.</p></li>
<li><p><strong>monitoring_manage_lists</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can modify notification lists.</p></li>
<li><p><strong>monitoring_view_jobs</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can view monitoring jobs.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The free form name of the user.</p></li>
<li><p><strong>notify</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Whether or not to notify the user of specified events. Only <code class="docutils literal notranslate"><span class="pre">billing</span></code> is available currently.</p></li>
<li><p><strong>security_manage_active_directory</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can manage global active directory.
Only relevant for the DDI product.</p></li>
<li><p><strong>security_manage_global2fa</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can manage global two factor authentication.</p></li>
<li><p><strong>teams</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The teams that the user belongs to.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The users login name.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_ns1.User.account_manage_account_settings">
<code class="sig-name descname">account_manage_account_settings</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.account_manage_account_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user can modify account settings.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.account_manage_apikeys">
<code class="sig-name descname">account_manage_apikeys</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.account_manage_apikeys" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user can modify account apikeys.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.account_manage_payment_methods">
<code class="sig-name descname">account_manage_payment_methods</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.account_manage_payment_methods" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user can modify account payment methods.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.account_manage_plan">
<code class="sig-name descname">account_manage_plan</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.account_manage_plan" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user can modify the account plan.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.account_manage_teams">
<code class="sig-name descname">account_manage_teams</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.account_manage_teams" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user can modify other teams in the account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.account_manage_users">
<code class="sig-name descname">account_manage_users</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.account_manage_users" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user can modify account users.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.account_view_activity_log">
<code class="sig-name descname">account_view_activity_log</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.account_view_activity_log" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user can view activity logs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.account_view_invoices">
<code class="sig-name descname">account_view_invoices</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.account_view_invoices" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user can view invoices.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.data_manage_datafeeds">
<code class="sig-name descname">data_manage_datafeeds</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.data_manage_datafeeds" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user can modify data feeds.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.data_manage_datasources">
<code class="sig-name descname">data_manage_datasources</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.data_manage_datasources" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user can modify data sources.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.data_push_to_datafeeds">
<code class="sig-name descname">data_push_to_datafeeds</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.data_push_to_datafeeds" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user can publish to data feeds.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.dhcp_manage_dhcp">
<code class="sig-name descname">dhcp_manage_dhcp</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.dhcp_manage_dhcp" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user can manage DHCP.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.dhcp_view_dhcp">
<code class="sig-name descname">dhcp_view_dhcp</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.dhcp_view_dhcp" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user can view DHCP.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.dns_manage_zones">
<code class="sig-name descname">dns_manage_zones</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.dns_manage_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user can modify the accounts zones.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.dns_view_zones">
<code class="sig-name descname">dns_view_zones</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.dns_view_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user can view the accounts zones.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.dns_zones_allow_by_default">
<code class="sig-name descname">dns_zones_allow_by_default</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.dns_zones_allow_by_default" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, enable the <code class="docutils literal notranslate"><span class="pre">dns_zones_allow</span></code> list, otherwise enable the <code class="docutils literal notranslate"><span class="pre">dns_zones_deny</span></code> list.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.dns_zones_allows">
<code class="sig-name descname">dns_zones_allows</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.dns_zones_allows" title="Permalink to this definition">¶</a></dt>
<dd><p>List of zones that the user may access.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.dns_zones_denies">
<code class="sig-name descname">dns_zones_denies</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.dns_zones_denies" title="Permalink to this definition">¶</a></dt>
<dd><p>List of zones that the user may not access.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.email">
<code class="sig-name descname">email</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address of the user.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.ip_whitelist_strict">
<code class="sig-name descname">ip_whitelist_strict</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.ip_whitelist_strict" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets exclusivity on this IP whitelist.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.ip_whitelists">
<code class="sig-name descname">ip_whitelists</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.ip_whitelists" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP addresses to whitelist for this key.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.ipam_manage_ipam">
<code class="sig-name descname">ipam_manage_ipam</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.ipam_manage_ipam" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user can manage IPAM.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.monitoring_manage_jobs">
<code class="sig-name descname">monitoring_manage_jobs</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.monitoring_manage_jobs" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user can modify monitoring jobs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.monitoring_manage_lists">
<code class="sig-name descname">monitoring_manage_lists</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.monitoring_manage_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user can modify notification lists.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.monitoring_view_jobs">
<code class="sig-name descname">monitoring_view_jobs</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.monitoring_view_jobs" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user can view monitoring jobs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The free form name of the user.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.notify">
<code class="sig-name descname">notify</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.notify" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not to notify the user of specified events. Only <code class="docutils literal notranslate"><span class="pre">billing</span></code> is available currently.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.security_manage_active_directory">
<code class="sig-name descname">security_manage_active_directory</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.security_manage_active_directory" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user can manage global active directory.
Only relevant for the DDI product.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.security_manage_global2fa">
<code class="sig-name descname">security_manage_global2fa</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.security_manage_global2fa" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user can manage global two factor authentication.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.teams">
<code class="sig-name descname">teams</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.teams" title="Permalink to this definition">¶</a></dt>
<dd><p>The teams that the user belongs to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.User.username">
<code class="sig-name descname">username</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.User.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The users login name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_account_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_apikeys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_payment_methods</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_teams</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_manage_users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_view_activity_log</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_view_invoices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_manage_datafeeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_manage_datasources</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_push_to_datafeeds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dhcp_manage_dhcp</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dhcp_view_dhcp</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_manage_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_view_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_allow_by_default</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_allows</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_zones_denies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_whitelist_strict</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_whitelists</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_manage_ipam</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_view_ipam</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_manage_jobs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_manage_lists</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_view_jobs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_manage_active_directory</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_manage_global2fa</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">teams</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_manage_account_settings</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can modify account settings.</p></li>
<li><p><strong>account_manage_apikeys</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can modify account apikeys.</p></li>
<li><p><strong>account_manage_payment_methods</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can modify account payment methods.</p></li>
<li><p><strong>account_manage_plan</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can modify the account plan.</p></li>
<li><p><strong>account_manage_teams</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can modify other teams in the account.</p></li>
<li><p><strong>account_manage_users</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can modify account users.</p></li>
<li><p><strong>account_view_activity_log</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can view activity logs.</p></li>
<li><p><strong>account_view_invoices</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can view invoices.</p></li>
<li><p><strong>data_manage_datafeeds</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can modify data feeds.</p></li>
<li><p><strong>data_manage_datasources</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can modify data sources.</p></li>
<li><p><strong>data_push_to_datafeeds</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can publish to data feeds.</p></li>
<li><p><strong>dhcp_manage_dhcp</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can manage DHCP.
Only relevant for the DDI product.</p></li>
<li><p><strong>dhcp_view_dhcp</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can view DHCP.
Only relevant for the DDI product.</p></li>
<li><p><strong>dns_manage_zones</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can modify the accounts zones.</p></li>
<li><p><strong>dns_view_zones</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can view the accounts zones.</p></li>
<li><p><strong>dns_zones_allow_by_default</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, enable the <code class="docutils literal notranslate"><span class="pre">dns_zones_allow</span></code> list, otherwise enable the <code class="docutils literal notranslate"><span class="pre">dns_zones_deny</span></code> list.</p></li>
<li><p><strong>dns_zones_allows</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of zones that the user may access.</p></li>
<li><p><strong>dns_zones_denies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of zones that the user may not access.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address of the user.</p></li>
<li><p><strong>ip_whitelist_strict</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Sets exclusivity on this IP whitelist.</p></li>
<li><p><strong>ip_whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The IP addresses to whitelist for this key.</p></li>
<li><p><strong>ipam_manage_ipam</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can manage IPAM.
Only relevant for the DDI product.</p></li>
<li><p><strong>monitoring_manage_jobs</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can modify monitoring jobs.</p></li>
<li><p><strong>monitoring_manage_lists</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can modify notification lists.</p></li>
<li><p><strong>monitoring_view_jobs</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can view monitoring jobs.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The free form name of the user.</p></li>
<li><p><strong>notify</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Whether or not to notify the user of specified events. Only <code class="docutils literal notranslate"><span class="pre">billing</span></code> is available currently.</p></li>
<li><p><strong>security_manage_active_directory</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can manage global active directory.
Only relevant for the DDI product.</p></li>
<li><p><strong>security_manage_global2fa</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user can manage global two factor authentication.</p></li>
<li><p><strong>teams</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The teams that the user belongs to.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The users login name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_ns1.User.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_ns1.Zone">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">Zone</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_primaries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">autogenerate_ns_record</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dnssec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">link</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">networks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nx_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondaries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Zone resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] additional_primaries: List of additional IPv4 addresses for the primary</p>
<blockquote>
<div><p>zone. Conflicts with <code class="docutils literal notranslate"><span class="pre">secondaries</span></code>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dnssec</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not DNSSEC is enabled for the zone.
Note that DNSSEC must be enabled on the account by support for this to be set
to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>expiry</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The SOA Expiry. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and
<code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code> (default must be accepted).</p></li>
<li><p><strong>link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target zone(domain name) to link to.</p></li>
<li><p><strong>networks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <ul>
<li><p>List of network IDs (<code class="docutils literal notranslate"><span class="pre">int</span></code>) for which the zone</p></li>
</ul>
<p>should be made available. Default is network 0, the primary NSONE Global
Network. Normally, you should not have to worry about this.</p>
</p></li>
<li><p><strong>nx_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The SOA NX TTL. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and
<code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code> (default must be accepted).</p></li>
<li><p><strong>primary</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The primary zones’ IPv4 address. This makes the zone a
secondary. Conflicts with <code class="docutils literal notranslate"><span class="pre">secondaries</span></code>.</p></li>
<li><p><strong>refresh</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The SOA Refresh. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and
<code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code> (default must be accepted).</p></li>
<li><p><strong>retry</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The SOA Retry. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and
<code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code> (default must be accepted).</p></li>
<li><p><strong>secondaries</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of secondary servers. This makes the zone a
primary. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and <code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code>.
Secondaries is documented below.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The SOA TTL.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain name of the zone.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>secondaries</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - IPv4 address of the secondary server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - - List of network IDs (<code class="docutils literal notranslate"><span class="pre">int</span></code>) for which the zone
should be made available. Default is network 0, the primary NSONE Global
Network. Normally, you should not have to worry about this.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notify</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether we send <code class="docutils literal notranslate"><span class="pre">NOTIFY</span></code> messages to the secondary host
when the zone changes. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Port of the the secondary server. Default <code class="docutils literal notranslate"><span class="pre">53</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_ns1.Zone.additional_primaries">
<code class="sig-name descname">additional_primaries</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Zone.additional_primaries" title="Permalink to this definition">¶</a></dt>
<dd><p>List of additional IPv4 addresses for the primary
zone. Conflicts with <code class="docutils literal notranslate"><span class="pre">secondaries</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Zone.dns_servers">
<code class="sig-name descname">dns_servers</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Zone.dns_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) Authoritative Name Servers.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Zone.dnssec">
<code class="sig-name descname">dnssec</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Zone.dnssec" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not DNSSEC is enabled for the zone.
Note that DNSSEC must be enabled on the account by support for this to be set
to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Zone.expiry">
<code class="sig-name descname">expiry</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Zone.expiry" title="Permalink to this definition">¶</a></dt>
<dd><p>The SOA Expiry. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and
<code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code> (default must be accepted).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Zone.hostmaster">
<code class="sig-name descname">hostmaster</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Zone.hostmaster" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The SOA Hostmaster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Zone.link">
<code class="sig-name descname">link</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Zone.link" title="Permalink to this definition">¶</a></dt>
<dd><p>The target zone(domain name) to link to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Zone.networks">
<code class="sig-name descname">networks</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Zone.networks" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li><p>List of network IDs (<code class="docutils literal notranslate"><span class="pre">int</span></code>) for which the zone
should be made available. Default is network 0, the primary NSONE Global
Network. Normally, you should not have to worry about this.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Zone.nx_ttl">
<code class="sig-name descname">nx_ttl</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Zone.nx_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The SOA NX TTL. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and
<code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code> (default must be accepted).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Zone.primary">
<code class="sig-name descname">primary</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Zone.primary" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary zones’ IPv4 address. This makes the zone a
secondary. Conflicts with <code class="docutils literal notranslate"><span class="pre">secondaries</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Zone.refresh">
<code class="sig-name descname">refresh</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Zone.refresh" title="Permalink to this definition">¶</a></dt>
<dd><p>The SOA Refresh. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and
<code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code> (default must be accepted).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Zone.retry">
<code class="sig-name descname">retry</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Zone.retry" title="Permalink to this definition">¶</a></dt>
<dd><p>The SOA Retry. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and
<code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code> (default must be accepted).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Zone.secondaries">
<code class="sig-name descname">secondaries</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Zone.secondaries" title="Permalink to this definition">¶</a></dt>
<dd><p>List of secondary servers. This makes the zone a
primary. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and <code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code>.
Secondaries is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - IPv4 address of the secondary server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networks</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - - List of network IDs (<code class="docutils literal notranslate"><span class="pre">int</span></code>) for which the zone
should be made available. Default is network 0, the primary NSONE Global
Network. Normally, you should not have to worry about this.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notify</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether we send <code class="docutils literal notranslate"><span class="pre">NOTIFY</span></code> messages to the secondary host
when the zone changes. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Port of the the secondary server. Default <code class="docutils literal notranslate"><span class="pre">53</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Zone.ttl">
<code class="sig-name descname">ttl</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Zone.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The SOA TTL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_ns1.Zone.zone">
<code class="sig-name descname">zone</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_ns1.Zone.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain name of the zone.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Zone.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_primaries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">autogenerate_ns_record</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dnssec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostmaster</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">link</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">networks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nx_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondaries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Zone.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Zone resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_primaries</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of additional IPv4 addresses for the primary
zone. Conflicts with <code class="docutils literal notranslate"><span class="pre">secondaries</span></code>.</p></li>
<li><p><strong>dns_servers</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) Authoritative Name Servers.</p></li>
<li><p><strong>dnssec</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not DNSSEC is enabled for the zone.
Note that DNSSEC must be enabled on the account by support for this to be set
to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>expiry</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The SOA Expiry. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and
<code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code> (default must be accepted).</p></li>
<li><p><strong>hostmaster</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The SOA Hostmaster.</p></li>
<li><p><strong>link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target zone(domain name) to link to.</p></li>
<li><p><strong>networks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <ul>
<li><p>List of network IDs (<code class="docutils literal notranslate"><span class="pre">int</span></code>) for which the zone</p></li>
</ul>
<p>should be made available. Default is network 0, the primary NSONE Global
Network. Normally, you should not have to worry about this.</p>
</p></li>
<li><p><strong>nx_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The SOA NX TTL. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and
<code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code> (default must be accepted).</p></li>
<li><p><strong>primary</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The primary zones’ IPv4 address. This makes the zone a
secondary. Conflicts with <code class="docutils literal notranslate"><span class="pre">secondaries</span></code>.</p></li>
<li><p><strong>refresh</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The SOA Refresh. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and
<code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code> (default must be accepted).</p></li>
<li><p><strong>retry</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The SOA Retry. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and
<code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code> (default must be accepted).</p></li>
<li><p><strong>secondaries</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of secondary servers. This makes the zone a
primary. Conflicts with <code class="docutils literal notranslate"><span class="pre">primary</span></code> and <code class="docutils literal notranslate"><span class="pre">additional_primaries</span></code>.
Secondaries is documented below.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The SOA TTL.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain name of the zone.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>secondaries</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - IPv4 address of the secondary server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - - List of network IDs (<code class="docutils literal notranslate"><span class="pre">int</span></code>) for which the zone
should be made available. Default is network 0, the primary NSONE Global
Network. Normally, you should not have to worry about this.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notify</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether we send <code class="docutils literal notranslate"><span class="pre">NOTIFY</span></code> messages to the secondary host
when the zone changes. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Port of the the secondary server. Default <code class="docutils literal notranslate"><span class="pre">53</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_ns1.Zone.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Zone.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_ns1.Zone.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.Zone.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_ns1.get_dns_sec">
<code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">get_dns_sec</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.get_dns_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides DNSSEC details about a NS1 Zone.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>zone</strong> (<em>str</em>) – The name of the zone to get DNSSEC details for.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_ns1.get_zone">
<code class="sig-prename descclassname">pulumi_ns1.</code><code class="sig-name descname">get_zone</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">additional_primaries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_ns1.get_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about a NS1 Zone. Use this if you would simply like to read
information from NS1 into your configurations. For read/write operations, you
should use a resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>additional_primaries</strong> (<em>list</em>) – List of additional IPv4 addresses for the primary
zone.</p></li>
<li><p><strong>zone</strong> (<em>str</em>) – The domain name of the zone.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
